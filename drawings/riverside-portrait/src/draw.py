"""Step 3: compose the whole illustration as one SVG.

Inputs (from prepare.py / person.py, read from the current directory):
  photo_srgb.png, person_mask.npy, bounds.npy, sky_coef.npy, cloud_alpha.npy, person_layer.svg.txt
Output: drawing.svg

Layers, back to front: sky gradient, cirrus clouds, hills, hay field (bales, fence), shaded bank,
gravel bar (stipple), river (ripple strokes), foreground grass, figure, paper grain.
Flat tones come from k-means per region; texture strokes come from the photo's own high-pass detail,
each stroke filled with the photo's colour at that spot.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cv2, numpy as np
from vec import mask_to_path, soft_threshold_mask
from scipy_free import gauss1d_nan
from tex import highpass, highpass_x, blob_paths, stipple

rng = np.random.default_rng(20240925)
img = cv2.imread('photo_srgb.png')                      # BGR uint8
H, W = img.shape[:2]
RGB = img[..., ::-1].astype(np.float32)
person = np.load('person_mask.npy') > 0
person_core = cv2.erode(person.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0
B = np.load('bounds.npy', allow_pickle=True).item()
Yc = np.arange(H)[:, None]
OV = 4  # overlap (px) each region extends under the next one


def hexc(c):
    c = np.clip(np.round(np.asarray(c, float)), 0, 255).astype(int)
    return '#%02x%02x%02x' % tuple(c)


def between(top, bot):
    return (Yc >= top[None, :]) & (Yc < bot[None, :])


def adjust(rgb, sat=1.0, gain=1.0, lift=0.0):
    rgb = np.asarray(rgb, float)
    g = rgb.mean(-1, keepdims=True)
    rgb = g + (rgb - g) * sat
    return np.clip(rgb * gain + lift, 0, 255)


def region_blur(region, sigma):
    """Blur the photo inside region, ignoring the person (normalized convolution)."""
    valid = (region & ~person).astype(np.float32)
    num = cv2.GaussianBlur(RGB * valid[..., None], (0, 0), sigma)
    den = cv2.GaussianBlur(valid, (0, 0), sigma)[..., None]
    return num / np.maximum(den, 1e-4)


# ------------------------------------------------------------------ posterize
def posterize(region, K, pre_sigma, smooth_sigma, eps=0.8, min_area=30, seed=1,
              sat=1.0, gain=1.0, pad=16, bilateral=False):
    """Stacked-tone vectorization of one region. Returns list of (path, rgb)."""
    ys, _ = np.where(region)
    y0, y1 = max(ys.min() - 2, 0), min(ys.max() + 3, H)
    reg = region[y0:y1]
    base = img[y0:y1]
    if bilateral:
        base = cv2.bilateralFilter(base, 9, 30, 9)
        base = cv2.bilateralFilter(base, 9, 30, 9)
    if pre_sigma > 0:
        base = cv2.GaussianBlur(base, (0, 0), pre_sigma)
    lab = cv2.cvtColor(base, cv2.COLOR_BGR2LAB).astype(np.float32)
    valid = reg & ~person[y0:y1]
    pts = lab[valid]
    sample = pts if len(pts) < 250000 else pts[rng.choice(len(pts), 250000, replace=False)]
    cv2.setRNGSeed(seed)
    _, _, centers = cv2.kmeans(sample, K, None,
                               (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 60, 0.3),
                               3, cv2.KMEANS_PP_CENTERS)
    centers = centers[np.argsort(centers[:, 0])]
    idx = np.full(reg.shape, -1, np.int32)
    flat = lab.reshape(-1, 3)
    li = np.empty(flat.shape[0], np.int32)
    for s in range(0, flat.shape[0], 400000):
        d = ((flat[s:s + 400000, None, :] - centers[None]) ** 2).sum(-1)
        li[s:s + 400000] = d.argmin(1)
    li = li.reshape(reg.shape)
    idx[valid] = li[valid]
    hole = reg & ~valid
    if hole.any():
        srcm = np.where(valid, 0, 1).astype(np.uint8)
        _, nl = cv2.distanceTransformWithLabels(srcm, cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
        zc = np.argwhere(srcm == 0)
        nn = zc[nl[hole] - 1]
        idx[hole] = idx[nn[:, 0], nn[:, 1]]
    cols = cv2.cvtColor(centers.reshape(1, -1, 3).astype(np.uint8), cv2.COLOR_LAB2RGB).reshape(-1, 3)
    out = []
    idxp = np.pad(idx, ((0, 0), (pad, pad)), mode='edge')
    regp = np.pad(reg, ((0, 0), (pad, pad)), mode='edge')
    for t in range(K):
        if t == 0:
            lm = regp.astype(np.uint8)
        else:
            lm = soft_threshold_mask(regp & (idxp >= t), smooth_sigma)
        d = mask_to_path(lm, smooth_sigma=1.0, eps=eps, min_area=min_area, offset=(-pad, y0))
        if d:
            out.append((d, adjust(cols[t], sat=sat, gain=gain)))
    return out


def paths_svg(items, op=None):
    o = '' if op is None else f' fill-opacity="{op}"'
    return ''.join(f'<path d="{d}" fill="{hexc(c)}"{o}/>' for d, c in items)


def circles_grouped(dots, K=20, seed=5):
    if not dots:
        return ''
    cols = np.array([c for _, _, _, c in dots], np.float32)
    cv2.setRNGSeed(seed)
    _, lbl, cent = cv2.kmeans(cols, min(K, len(cols)), None,
                              (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.5), 2, cv2.KMEANS_PP_CENTERS)
    lbl = lbl.ravel()
    out = []
    for k in range(len(cent)):
        idx = np.where(lbl == k)[0]
        body = ''.join(f'<circle cx="{dots[i][0]}" cy="{dots[i][1]}" r="{dots[i][2]:.1f}"/>' for i in idx)
        out.append(f'<g fill="{hexc(cent[k])}">{body}</g>')
    return ''.join(out)


svg, defs = [], []


def band_polygon(top, bot, step=6):
    xs_ = list(range(0, W, step)) + [W - 1]
    pts = [f'-12,{top[0]:.1f}'] + [f'{x},{top[x]:.1f}' for x in xs_] + [f'{W + 12},{top[-1]:.1f}', f'{W + 12},{bot[-1]:.1f}']
    pts += [f'{x},{bot[x]:.1f}' for x in reversed(xs_)] + [f'-12,{bot[0]:.1f}']
    return ' '.join(pts)


def soft_base(name, reg, top, bot, blur, **kw):
    """Posterized tones blurred into soft gradients, clipped to the band between top and bot."""
    items = posterize(reg, **kw)
    defs.append(f'<clipPath id="clip_{name}"><polygon points="{band_polygon(top, bot)}"/></clipPath>')
    defs.append(f'<filter id="blur_{name}" x="-2%" y="-10%" width="104%" height="120%"><feGaussianBlur stdDeviation="{blur}"/></filter>')
    return (f'<path d="{items[0][0]}" fill="{hexc(items[0][1])}"/>'
            f'<g clip-path="url(#clip_{name})"><g filter="url(#blur_{name})">' + paths_svg(items[1:]) + '</g></g>')

# ------------------------------------------------------------------ sky
coef = np.load('sky_coef.npy')


def design(X, Y, deg=4):
    cols = []
    for i in range(deg + 1):
        for j in range(deg + 1 - i):
            cols.append((X ** i) * (Y ** j))
    return np.stack(cols, -1)


sky_bottom = int(B['sky'].max()) + 40
ys_s = np.linspace(0, sky_bottom, 14)
left = design(np.zeros_like(ys_s), ys_s / H) @ coef
right = design(np.ones_like(ys_s) * (W - 1) / W, ys_s / H) @ coef
xs_s = np.linspace(0, W - 1, 9)
yy = np.linspace(0, sky_bottom, 60)
mvals = []
for xv in xs_s:
    C = design(np.full_like(yy, xv / W), yy / H) @ coef
    L_ = design(np.zeros_like(yy), yy / H) @ coef
    R_ = design(np.full_like(yy, (W - 1) / W), yy / H) @ coef
    mvals.append(np.clip(((C - R_) * (L_ - R_)).sum() / ((L_ - R_) ** 2).sum(), 0, 1))
SKY_SAT = 1.06


def stops(ys_, cols_):
    return ''.join(f'<stop offset="{y / sky_bottom:.4f}" stop-color="{hexc(adjust(c, sat=SKY_SAT))}"/>'
                   for y, c in zip(ys_, cols_))


defs.append(f'<linearGradient id="skyR" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="{sky_bottom}">{stops(ys_s, right)}</linearGradient>')
defs.append(f'<linearGradient id="skyL" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="0" y2="{sky_bottom}">{stops(ys_s, left)}</linearGradient>')
defs.append('<linearGradient id="skyM" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="%d" y2="0">%s</linearGradient>' % (
    W, ''.join(f'<stop offset="{x / (W - 1):.4f}" stop-color="#000" stop-opacity="{m:.4f}"/>' for x, m in zip(xs_s, mvals))))
defs.append(f'<mask id="skyMask" style="mask-type:alpha"><rect width="{W}" height="{sky_bottom}" fill="url(#skyM)"/></mask>')
svg.append(f'<g id="sky"><rect width="{W}" height="{sky_bottom}" fill="url(#skyR)"/>'
           f'<rect width="{W}" height="{sky_bottom}" fill="url(#skyL)" mask="url(#skyMask)"/></g>')

# ------------------------------------------------------------------ clouds
alpha = cv2.GaussianBlur(np.load('cloud_alpha.npy'), (0, 0), 1.2)
thr = [0.045, 0.09, 0.15, 0.23, 0.32, 0.43, 0.56]
mids = [(thr[i] + (thr[i + 1] if i + 1 < len(thr) else 0.7)) / 2 for i in range(len(thr))]
ops, prev = [], 0.0
for mv in mids:
    ops.append(max(1 - (1 - mv) / (1 - prev), 0.02)); prev = mv
cloud = []
for t, o in zip(thr, ops):
    m = np.pad((alpha >= t).astype(np.uint8), ((0, 0), (16, 16)), mode='edge')
    d = mask_to_path(soft_threshold_mask(m, 1.3), smooth_sigma=1.2, eps=0.7, min_area=40, offset=(-16, 0))
    cloud.append(f'<path d="{d}" fill="#fdfbf6" fill-opacity="{o:.3f}"/>')
defs.append('<filter id="cloudSoft" x="-5%" y="-5%" width="110%" height="110%"><feGaussianBlur stdDeviation="1.1"/></filter>')
svg.append('<g id="clouds" filter="url(#cloudSoft)">' + ''.join(cloud) + '</g>')

# ------------------------------------------------------------------ hills
reg = between(B['sky'], B['plain'] + OV)
svg.append('<g id="hills">' + paths_svg(posterize(reg, K=7, pre_sigma=2.0, smooth_sigma=2.2, sat=1.08)) + '</g>')
print('hills done')

# ------------------------------------------------------------------ plain (field, bales, fence)
reg = between(B['plain'], B['bank'] + OV)
parts = [soft_base('plain', reg, B['plain'], B['bank'] + OV, 2.5, K=6, pre_sigma=2.5, smooth_sigma=2.5, sat=1.10, bilateral=True)]
inner = between(B['plain'] + 1, B['bank'] - 1) & ~person_core
base = region_blur(reg, 6)
hp6 = highpass(img, 6, 0.6)
dark = soft_threshold_mask(inner & (hp6 < -5), 0.7) > 0
lite = soft_threshold_mask(inner & (hp6 > 5), 0.7) > 0
parts.append(paths_svg(blob_paths(dark, RGB, K=10, smooth=0, min_area=4, boost_ref=base, boost=1.15)))
parts.append(paths_svg(blob_paths(lite, RGB, K=10, smooth=0, min_area=4, boost_ref=base, boost=1.1)))
hp2 = highpass(img, 2.0, 0.6)
streak = soft_threshold_mask(inner & (hp2 > 2.5) & ~dark, 0.6) > 0
parts.append(paths_svg(blob_paths(streak, RGB, K=10, smooth=0, min_area=4, boost_ref=base, boost=1.1), op=0.8))
svg.append('<g id="plain">' + ''.join(parts) + '</g>')
print('plain done')

# ------------------------------------------------------------------ shaded bank
reg = between(B['bank'], B['gravel'] + OV)
parts = [soft_base('bank', reg, B['bank'], B['gravel'] + OV, 5, K=4, pre_sigma=4.0, smooth_sigma=4.0, sat=1.05)]
inner = between(B['bank'] + 1, B['gravel'] - 1) & ~person_core
base = region_blur(reg, 8)
hpb = highpass_x(img, 2.5, 0.6, norm_sigma=18, sy=1.2)
bdark = soft_threshold_mask(inner & (hpb < -0.6), 0.6) > 0
blades = soft_threshold_mask(inner & (hpb > 0.45), 0.9) > 0
blades2 = soft_threshold_mask(inner & (hpb > 1.3), 0.5) > 0
parts.append(paths_svg(blob_paths(bdark, RGB, K=8, smooth=0, min_area=5, boost_ref=base, boost=1.2)))
parts.append(paths_svg(blob_paths(blades, RGB, K=10, smooth=0, min_area=6, boost_ref=base, boost=1.3, lift=1)))
parts.append(paths_svg(blob_paths(blades2, RGB, K=10, smooth=0, min_area=5, boost_ref=base, boost=1.4, lift=2)))
svg.append('<g id="bank">' + ''.join(parts) + '</g>')
print('bank done')

# ------------------------------------------------------------------ gravel bar (stipple)
reg = between(B['gravel'], B['water'] + OV)
parts = [soft_base('gravel', reg, B['gravel'], B['water'] + OV, 7, K=6, pre_sigma=6.0, smooth_sigma=5.0, sat=1.0)]
inner = between(B['gravel'] + 2, B['water'] - 2) & ~person_core
base = region_blur(reg, 5)
hpg = highpass(img, 2.5, 0.6, norm_sigma=12)
src = cv2.GaussianBlur(RGB, (0, 0), 0.8)
dk = stipple(inner, hpg, src, 0.45, win=3, rmin=0.9, rmax=1.9, ytop=B['gravel'], ybot=B['water'],
             prob=0.7, rng=rng, boost_ref=base, boost=1.15, sign=-1)
lt = stipple(inner, hpg, src, 0.45, win=3, rmin=0.8, rmax=1.8, ytop=B['gravel'], ybot=B['water'],
             prob=0.7, rng=rng, boost_ref=base, boost=1.2, sign=1)
parts.append(circles_grouped(dk))
parts.append(circles_grouped(lt))
svg.append('<g id="gravel">' + ''.join(parts) + '</g>')
print('gravel done', len(dk), len(lt))

# ------------------------------------------------------------------ river
reg = between(B['water'], np.full(W, H + 10.0))
inner = between(B['water'] + 3, np.full(W, H + 10.0)) & ~person_core
hpw = highpass(img, 5.0, 0.9, norm_sigma=25)
yy_ = np.arange(H)[:, None]
crest = soft_threshold_mask(inner & (hpw > 0.55), 1.0) > 0
crest2 = soft_threshold_mask(inner & (hpw > 1.35), 0.9) > 0
trough = soft_threshold_mask(inner & (hpw < -0.55), 1.0) > 0
trough2 = soft_threshold_mask(inner & (hpw < -1.35), 0.9) > 0
basew = region_blur(reg, 10)
# calibrated base gradient = mean of the untouched (mid-tone) pixels per band of rows
mid = reg & ~person & ~crest & ~trough
yt, yb = int(B['water'].min()), int(B['grass'].max()) + 60
sy, sc = [], []
for y in range(yt, yb, 20):
    sl = slice(max(y - 10, 0), min(y + 10, H))
    v = mid[sl]
    if v.sum() > 300:
        sy.append(y); sc.append(RGB[sl][v].mean(0))
sc = np.array(sc)
for ch in range(3):
    sc[:, ch] = gauss1d_nan(sc[:, ch], 1.5)
g = ''.join(f'<stop offset="{(y - yt) / (sy[-1] - yt):.4f}" stop-color="{hexc(adjust(c, sat=1.08))}"/>' for y, c in zip(sy, sc))
defs.append(f'<linearGradient id="waterG" gradientUnits="userSpaceOnUse" x1="0" y1="{yt}" x2="0" y2="{sy[-1]}">{g}</linearGradient>')
top = B['water']
top_pts = ' '.join(f'{x},{top[x]:.1f}' for x in range(0, W, 6)) + f' {W - 1},{top[-1]:.1f}'
parts = [f'<polygon points="-10,{top[0]:.1f} {top_pts} {W + 10},{top[-1]:.1f} {W + 10},{H} -10,{H}" fill="url(#waterG)"/>']
for m, bst in [(trough, 1.15), (crest, 1.15), (trough2, 1.2), (crest2, 1.2)]:
    parts.append(paths_svg([(d, adjust(c, sat=1.08)) for d, c in
                            blob_paths(m, RGB, K=14, smooth=0, min_area=8, boost_ref=basew, boost=bst)]))
svg.append('<g id="river">' + ''.join(parts) + '</g>')
print('river done')

# ------------------------------------------------------------------ foreground grass bank
labb = cv2.cvtColor(cv2.GaussianBlur(img, (0, 0), 0.8), cv2.COLOR_BGR2LAB)
zone = yy_ >= (B['grass'][None, :] - 170)
grass = zone & (labb[..., 2] > 123) & ~person
grass = cv2.morphologyEx(grass.astype(np.uint8), cv2.MORPH_OPEN, np.ones((2, 2), np.uint8))
n, lb, st, _ = cv2.connectedComponentsWithStats(grass, connectivity=8)
touch = np.unique(lb[H - 3:, :])
grass = np.isin(lb, touch[touch > 0])
# rows below which every pixel is grass ("solid" bank), per column; forced grass only below that line
isg = (labb[..., 2] > 123) | person
nong = ~isg & zone
last_non = np.where(nong.any(0), H - 1 - np.argmax(nong[::-1], axis=0), 0).astype(float)
solid = np.maximum(last_non + 1, B['grass'] - 60)
pad_ = np.pad(solid, 20, mode='edge')
solid = np.array([np.median(pad_[i:i + 41]) for i in range(W)])
grass |= yy_ >= (solid[None, :] + 4)
grass &= ~person_core
grass_s = soft_threshold_mask(grass, 0.8) > 0
ys_, xs_ = np.where(grass_s)
gy0 = ys_.min()
# base tones inside the grass silhouette
reg = grass_s | (person & (yy_ >= gy0))
parts = [paths_svg(posterize(reg, K=5, pre_sigma=1.5, smooth_sigma=1.6, sat=1.08, min_area=12, eps=0.6))]
inner = grass_s & ~person
baseg = region_blur(grass_s, 5)
hpf = highpass_x(img, 2.5, 0.6, norm_sigma=14, sy=1.0)
lit = soft_threshold_mask(inner & (hpf > 0.7), 0.6) > 0
shd = soft_threshold_mask(inner & (hpf < -0.8), 0.6) > 0
parts.append(paths_svg(blob_paths(shd, RGB, K=10, smooth=0, min_area=5, boost_ref=baseg, boost=1.15)))
parts.append(paths_svg(blob_paths(lit, RGB, K=12, smooth=0, min_area=5, boost_ref=baseg, boost=1.2)))
svg.append('<g id="foreground">' + ''.join(parts) + '</g>')
print('foreground done')

# ------------------------------------------------------------------ person
if os.path.exists('person_layer.svg.txt'):
    svg.append(open('person_layer.svg.txt').read())

# ------------------------------------------------------------------ finishing: fine paper grain
defs.append('<filter id="grain" x="0" y="0" width="100%" height="100%">'
            '<feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2" seed="7" result="n"/>'
            '<feColorMatrix type="matrix" values="0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0 0.5  0.9 0.9 0.9 0 -1.1"/>'
            '</filter>')
svg.append(f'<rect width="{W}" height="{H}" filter="url(#grain)" opacity="0.10" style="mix-blend-mode:overlay"/>')

out = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">'
       f'<defs>{"".join(defs)}</defs>' + ''.join(svg) + '</svg>')
open('drawing.svg', 'w').write(out)
print('svg bytes', len(out))
