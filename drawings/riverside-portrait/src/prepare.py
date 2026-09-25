"""Step 1: analyse the photo and cache everything the drawing steps need.

usage: python3 prepare.py PHOTO.jpg        (run inside the build directory)

Writes (to the current directory):
  photo_srgb.png   photo converted from its ICC profile (Display P3) to sRGB
  person_mask.npy  figure silhouette (GrabCut)
  bounds.npy       per-column boundaries: skyline, foot of the hills, bank, gravel, water, grass
  sky_coef.npy     smooth polynomial model of the cloud-free sky
  cloud_alpha.npy  cloud opacity map (how far each sky pixel is pushed towards white)

The rectangle / sample boxes below are tuned for this one photo (1932 x 2576).
"""
import io
import sys
import os

import cv2
import numpy as np
from PIL import Image, ImageCms

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scipy_free import gauss1d_nan  # noqa: E402

src_path = sys.argv[1]

# ---------------------------------------------------------------- colour: P3 -> sRGB
pim = Image.open(src_path)
raw = np.asarray(pim.convert('RGB'))[..., ::-1].copy()          # BGR, un-managed values
if 'icc_profile' in pim.info:
    prof = ImageCms.ImageCmsProfile(io.BytesIO(pim.info['icc_profile']))
    srgb = ImageCms.profileToProfile(pim.convert('RGB'), prof, ImageCms.createProfile('sRGB'),
                                     renderingIntent=0, outputMode='RGB')
else:
    srgb = pim.convert('RGB')
srgb.save('photo_srgb.png')
img = np.asarray(srgb)[..., ::-1].copy()                         # BGR sRGB
H, W = img.shape[:2]
print('photo', W, H)

# ---------------------------------------------------------------- figure silhouette
x0, y0, x1, y1 = 1060, 1180, 1600, H
sub = raw[y0:y1, x0:x1].copy()
mask = np.zeros(sub.shape[:2], np.uint8)
rect = (1120 - x0, 1200 - y0, 1540 - 1120, H - 1200 - 1)
bgd, fgd = np.zeros((1, 65), np.float64), np.zeros((1, 65), np.float64)
cv2.grabCut(sub, mask, rect, bgd, fgd, 8, cv2.GC_INIT_WITH_RECT)
m = np.where((mask == 1) | (mask == 3), 255, 0).astype(np.uint8)
full = np.zeros((H, W), np.uint8)
full[y0:y1, x0:x1] = m
n, lab_cc, st, _ = cv2.connectedComponentsWithStats(full)
big = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA])
full = (lab_cc == big).astype(np.uint8) * 255
cnts, _ = cv2.findContours(full, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
person_u8 = np.zeros_like(full)
cv2.drawContours(person_u8, cnts, -1, 255, -1)
np.save('person_mask.npy', person_u8)
person = person_u8 > 0
print('person bbox', np.where(person.any(0))[0][[0, -1]], np.where(person.any(1))[0][[0, -1]])

# ---------------------------------------------------------------- landscape boundaries
pdil = cv2.dilate(person.astype(np.uint8), np.ones((25, 25), np.uint8)) > 0
lab = cv2.cvtColor(cv2.GaussianBlur(img, (0, 0), 3), cv2.COLOR_BGR2LAB).astype(np.float32)
L, Bc = lab[..., 0], lab[..., 2]
# skyline: first row (from 1080 down) that stays darker / yellower than the horizon sky for 6 px
Y0, Y1 = 1080, 1275
skyL = np.median(L[1050:1090], axis=0)
skyB = np.median(Bc[1050:1090], axis=0)
skyline = np.zeros(W)
for x in range(W):
    land = ((skyL[x] - L[Y0:Y1, x]) > 14) | ((Bc[Y0:Y1, x] - skyB[x]) > 10)
    run = np.convolve(land.astype(int), np.ones(6, int), 'valid') == 6
    skyline[x] = Y0 + (np.argmax(run) if run.any() else (Y1 - Y0))

# below the plain: monotone column-wise segmentation into
# lit field -> shaded bank -> gravel -> water -> grass, by dynamic programming
classes = {
    'plain': [(0, 1000, 1338, 1382), (1720, 1932, 1296, 1330)],
    'bank': [(0, 900, 1420, 1520), (950, 1100, 1400, 1470)],
    'gravel': [(0, 1000, 1600, 1700), (1550, 1932, 1450, 1600), (1720, 1932, 1370, 1420)],
    'water': [(0, 1000, 1800, 2400), (1550, 1932, 1700, 2300)],
    'grass': [(0, 1000, 2525, 2576), (1600, 1932, 2480, 2576)],
}
names = list(classes)
models = []
for nme in names:
    pts = np.concatenate([lab[b0:b1, a0:a1].reshape(-1, 3) for (a0, a1, b0, b1) in classes[nme]])
    models.append((pts.mean(0), np.linalg.inv(np.cov(pts.T) + np.eye(3) * 4)))
Ys, Ye = 1300, H
C = len(names)
cost = np.zeros((C, Ye - Ys, W), np.float32)
for k, (mu, ic) in enumerate(models):
    d = lab[Ys:Ye] - mu
    cost[k] = np.minimum(np.einsum('...i,ij,...j->...', d, ic, d), 60.0)
cost[:, pdil[Ys:Ye]] = 0.0                     # the figure hides the scene: no evidence there
acc = np.full((C, W), 1e9, np.float32)
acc[0] = cost[0, 0]
back = np.zeros((Ye - Ys, C, W), np.int8)
for y in range(1, Ye - Ys):
    new = np.empty_like(acc)
    best = acc[0].copy()
    bidx = np.zeros(W, np.int8)
    for k in range(C):
        if k > 0:
            better = acc[k] < best
            best = np.where(better, acc[k], best)
            bidx = np.where(better, k, bidx).astype(np.int8)
        sw = np.where(bidx == k, best, best + 2.0)
        use_stay = acc[k] <= sw
        new[k] = np.where(use_stay, acc[k], sw) + cost[k, y]
        back[y, k] = np.where(use_stay, k, bidx)
    acc = new
lab_map = np.zeros((Ye - Ys, W), np.int8)
k = np.full(W, C - 1, np.int8)
for y in range(Ye - Ys - 1, -1, -1):
    lab_map[y] = k
    k = back[y, k, np.arange(W)]
raw_b = {names[k]: np.argmax(lab_map >= k, axis=0).astype(float) + Ys for k in range(1, C)}
raw_b['sky'] = skyline

# clean up: interpolate across the figure, drop spikes, smooth
pdil2 = cv2.dilate(person.astype(np.uint8), np.ones((31, 31), np.uint8)) > 0
xs = np.arange(W)
occl = {'sky': None, 'bank': (1320, 1460), 'gravel': (1380, 1620), 'water': (1600, 1800), 'grass': (2280, 2576)}
bounds = {}
for name, sig in [('sky', 1.5), ('bank', 5), ('gravel', 6), ('water', 6), ('grass', 18)]:
    yv = raw_b[name].astype(float).copy()
    if occl[name] is not None:
        yv[pdil2[occl[name][0]:occl[name][1]].any(axis=0)] = np.nan
    good = ~np.isnan(yv)
    yv = np.interp(xs, xs[good], yv[good])
    if name != 'sky':
        pad = np.pad(yv, 15, mode='edge')
        yv = np.array([np.median(pad[i:i + 31]) for i in range(W)])
    bounds[name] = gauss1d_nan(yv, sig)
bounds['plain'] = np.interp(xs, [0, 700, 1300, 1932], [1266, 1263, 1259, 1254])   # foot of the hills
np.save('bounds.npy', bounds, allow_pickle=True)

# ---------------------------------------------------------------- sky model + clouds
RGBf = img[..., ::-1].astype(np.float32)


def design(X, Y, deg=4):
    return np.stack([(X ** i) * (Y ** j) for i in range(deg + 1) for j in range(deg + 1 - i)], -1)


small = cv2.resize(RGBf, (W // 8, H // 8), interpolation=cv2.INTER_AREA)
hs, ws = small.shape[:2]
gy, gx = np.mgrid[0:hs, 0:ws]
valid = (gy * 8 + 4) < (np.interp(gx * 8 + 4, xs, skyline) - 20)
D = design(((gx * 8 + 4) / W)[valid], ((gy * 8 + 4) / H)[valid])
V = small[valid]
keep = np.ones(len(V), bool)
for _ in range(6):                                  # iteratively drop bright (cloud) samples
    coef, *_ = np.linalg.lstsq(D[keep], V[keep], rcond=None)
    res = (V - D @ coef).mean(1)
    keep = res < max(np.percentile(res[keep], 60), 1.5)
np.save('sky_coef.npy', coef)
Hs = 1250
yy, xx = np.mgrid[0:Hs, 0:W]
S = design(xx / W, yy / H) @ coef
alpha = ((RGBf[:Hs] - S) / np.maximum(255 - S, 1)).mean(-1)
alpha = np.where(yy < (skyline[None, :] - 3), alpha, 0)
np.save('cloud_alpha.npy', np.clip(alpha, 0, 1).astype(np.float32))
print('prepare done')
