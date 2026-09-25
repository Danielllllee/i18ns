"""Step 2: vectorize the figure as stacked tone layers.

Head, hoodie and trousers each get their own k-means palette (so the warm skin tones are not merged with
the cream trousers); a narrow band around the zone borders may use any palette, so the seams follow real
colour edges. Layers are ordered dark -> light and each layer contains every lighter one, so there are no
gaps between neighbouring shapes. Output: person_layer.svg.txt (an SVG fragment used by draw.py).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import cv2, numpy as np
from vec import mask_to_path, soft_threshold_mask

img = cv2.imread('photo_srgb.png')
H, W = img.shape[:2]
full = np.load('person_mask.npy') > 0
ys, xs = np.where(full)
x0, y0, x1, y1 = xs.min() - 10, ys.min() - 10, xs.max() + 11, H
sub = img[y0:y1, x0:x1]
RGBsub = sub[..., ::-1].astype(np.float32)
M = full[y0:y1, x0:x1]
# smooth silhouette a little (fine at head, coarser on body)
yy = np.arange(y0, y1)[:, None] * np.ones((1, x1 - x0))
w_fine = np.clip((1480 - yy) / 40.0, 0, 1)


def smooth(mask, s_fine, s_coarse):
    m = mask.astype(np.float32)
    f = w_fine * cv2.GaussianBlur(m, (0, 0), s_fine) + (1 - w_fine) * cv2.GaussianBlur(m, (0, 0), s_coarse)
    return f >= 0.5


Ms = smooth(M, 0.8, 1.8) & (np.arange(y0, y1)[:, None] < H)
sm = cv2.bilateralFilter(sub, 7, 30, 5)
sm = cv2.bilateralFilter(sm, 7, 30, 5)
lab = cv2.cvtColor(sm, cv2.COLOR_BGR2LAB).astype(np.float32)

# zones: head (0), hoodie (1), pants+tee hem (2); transition bands use the union palette
head_poly = np.array([(1120, 1200), (1470, 1200), (1470, 1415), (1405, 1424), (1385, 1430),
                      (1332, 1446), (1302, 1458), (1287, 1478), (1250, 1482), (1120, 1482)], np.int32)
pants_poly = np.array([(1100, 2000), (1180, 1992), (1238, 2005), (1262, 2038), (1300, 2030), (1312, 1990),
                       (1360, 1985), (1440, 1995), (1530, 2000), (1530, 2600), (1100, 2600)], np.int32)
zmap = np.ones(M.shape, np.uint8)
tmp = np.zeros(M.shape, np.uint8); cv2.fillPoly(tmp, [head_poly - np.array([x0, y0])], 1); zmap[tmp > 0] = 0
tmp = np.zeros(M.shape, np.uint8); cv2.fillPoly(tmp, [pants_poly - np.array([x0, y0])], 1); zmap[tmp > 0] = 2
BAND = 14
band = np.zeros(M.shape, bool)
for z in range(3):
    zm = (zmap == z).astype(np.uint8)
    din = cv2.distanceTransform(zm, cv2.DIST_L2, 5)
    band |= (zm > 0) & (din < BAND)
# only keep band pixels that are actually near another zone
near_other = np.zeros(M.shape, bool)
for z in range(3):
    zm = (zmap == z).astype(np.uint8)
    dout = cv2.distanceTransform(1 - zm, cv2.DIST_L2, 5)
    near_other |= (zm == 0) & (dout < BAND)
band &= near_other


def km(points, K, seed):
    cv2.setRNGSeed(seed)
    _, _, c = cv2.kmeans(points, K, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 80, 0.2),
                         5, cv2.KMEANS_PP_CENTERS)
    return c


Ks = [9, 10, 8]
cents = [km(lab[M & (zmap == z)], Ks[z], 11 + z) for z in range(3)]
C = np.concatenate(cents)
zone_of = np.concatenate([[z] * Ks[z] for z in range(3)])
offs = np.cumsum([0] + Ks[:-1])


def nearest(pts, cc):
    out = np.empty(len(pts), int)
    for s0 in range(0, len(pts), 300000):
        d = ((pts[s0:s0 + 300000, None, :] - cc[None]) ** 2).sum(-1)
        out[s0:s0 + 300000] = d.argmin(1)
    return out


lab_flat = lab.reshape(-1, 3)
lbl = np.zeros(M.shape, int)
for z in range(3):
    zi = nearest(lab_flat, cents[z]).reshape(M.shape) + offs[z]
    lbl = np.where(zmap == z, zi, lbl)
lbl = np.where(band, nearest(lab_flat, C).reshape(M.shape), lbl)
order = np.argsort(C[:, 0])
rank = np.empty(len(C), int); rank[order] = np.arange(len(C))
R = rank[lbl]
R[~Ms] = -1
holes = Ms & ~M
if holes.any():
    srcm = np.where(M, 0, 1).astype(np.uint8)
    _, nl = cv2.distanceTransformWithLabels(srcm, cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
    zc = np.argwhere(srcm == 0)
    nn = zc[nl[holes] - 1]
    R[holes] = rank[lbl[nn[:, 0], nn[:, 1]]]
cols = cv2.cvtColor(C[order].reshape(1, -1, 3).astype(np.uint8), cv2.COLOR_LAB2RGB).reshape(-1, 3).astype(float)
# spatial smoothing strength per zone (soft weights)
wz = [cv2.GaussianBlur((zmap == z).astype(np.float32), (0, 0), 12) for z in range(3)]
SIG = [0.9, 3.0, 4.2]


def smooth_zone(mask):
    m = mask.astype(np.float32)
    f = sum(wz[z] * cv2.GaussianBlur(m, (0, 0), SIG[z]) for z in range(3))
    return f >= 0.5


ZMEAN = [RGBsub[M & (zmap == z)].mean(0) for z in range(3)]


def grade(c, zone):
    c = np.asarray(c, float)
    # slight tone compression on clothing: flat cel tones read as more contrasty than soft photo shading
    k = [1.0, 0.88, 0.88][zone]
    c = ZMEAN[zone] + (c - ZMEAN[zone]) * k
    g = c.mean()
    sat = [1.05, 1.02, 1.02][zone]
    c = g + (c - g) * sat
    return np.clip(c, 0, 255)


def hexc(c):
    c = np.clip(np.round(c), 0, 255).astype(int)
    return '#%02x%02x%02x' % tuple(c)


# extend labels ~14 px outside the silhouette (nearest inside label) so smoothing does not pull the
# tone layers away from the outline; the whole figure is clipped to the silhouette instead.
inner_ok = M & (R >= 0)
srcm = np.where(inner_ok, 0, 1).astype(np.uint8)
dist, nl = cv2.distanceTransformWithLabels(srcm, cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
zc = np.argwhere(srcm == 0)
ext = (~inner_ok) & (dist < 14)
Rx = R.copy()
nn = zc[nl[ext] - 1]
Rx[ext] = R[nn[:, 0], nn[:, 1]]
sil_d = mask_to_path(Ms.astype(np.uint8), smooth_sigma=0.9, eps=0.5, min_area=12, offset=(x0, y0))
paths = []
for t in range(len(C)):
    layer = cv2.dilate(Ms.astype(np.uint8), np.ones((5, 5), np.uint8)) > 0 if t == 0 else smooth_zone(Rx >= t)
    d = mask_to_path(layer.astype(np.uint8), smooth_sigma=0.9, eps=0.5, min_area=12, offset=(x0, y0))
    if d:
        zone = zone_of[order[t]]
        paths.append(f'<path d="{d}" fill="{hexc(grade(cols[t], zone))}"/>')

# ---- details ----
# blue zipper on the pants: find saturated blue pixels
hsv = cv2.cvtColor(sub, cv2.COLOR_BGR2HSV)
blue = (hsv[..., 0] > 100) & (hsv[..., 0] < 125) & (hsv[..., 1] > 110) & (hsv[..., 2] > 60) & M
blue &= (np.arange(y0, y1)[:, None] > 2050)
blue = cv2.morphologyEx(blue.astype(np.uint8), cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))
n, lb, st, _ = cv2.connectedComponentsWithStats(blue)
zip_d = ''
for i in range(1, n):
    if st[i, cv2.CC_STAT_AREA] > 60:
        m = (lb == i).astype(np.uint8)
        m = soft_threshold_mask(cv2.dilate(m, np.ones((2, 2), np.uint8)), 1.0)
        zip_d += mask_to_path(m, smooth_sigma=1.0, eps=0.5, min_area=30, offset=(x0, y0))
if zip_d:
    paths.append(f'<path d="{zip_d}" fill="#2457c5"/>')
# cap logo: small bright mark on the dark cap
Lf = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)[..., 0]
logo = np.zeros(img.shape[:2], np.uint8)
lx0, ly0, lx1, ly1 = 1244, 1276, 1272, 1300
logo[ly0:ly1, lx0:lx1] = (Lf[ly0:ly1, lx0:lx1] > 140).astype(np.uint8)
logo = cv2.dilate(logo, np.ones((2, 2), np.uint8))
d = mask_to_path(soft_threshold_mask(logo, 0.6), smooth_sigma=0.5, eps=0.3, min_area=3)
if d:
    paths.append(f'<path d="{d}" fill="#efe9df"/>')
np.save('person_box.npy', np.array([x0, y0, x1, y1]))
open('person_layer.svg.txt', 'w').write(
    f'<clipPath id="personClip"><path d="{sil_d}"/></clipPath>'
    '<g id="person" clip-path="url(#personClip)">' + ''.join(paths) + '</g>')
print('person layers', len(paths), 'palette', [(int(zone_of[order[i]]), hexc(grade(c, zone_of[order[i]]))) for i, c in enumerate(cols)])
