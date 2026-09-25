import cv2, numpy as np
from vec import mask_to_path, soft_threshold_mask


def lstar(img_bgr, pre_sigma=0.0):
    L = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2LAB)[..., 0].astype(np.float32) * (100.0 / 255.0)
    if pre_sigma > 0:
        L = cv2.GaussianBlur(L, (0, 0), pre_sigma)
    return L


def highpass(img_bgr, hp_sigma, pre_sigma=0.7, norm_sigma=0.0):
    L = lstar(img_bgr, pre_sigma)
    hp = L - cv2.GaussianBlur(L, (0, 0), hp_sigma)
    if norm_sigma > 0:
        sd = np.sqrt(cv2.GaussianBlur(hp * hp, (0, 0), norm_sigma)) + 0.8
        hp = hp / sd
    return hp


def blob_paths(mask, src_rgb, K=16, smooth=0.8, min_area=5, eps=0.7, boost_ref=None, boost=1.0,
               lift=0.0, pad=16, seed=3):
    """Connected blobs of mask, each filled with its mean colour (quantised to K colours).
    Returns list of (path_d, rgb)."""
    m = mask.astype(np.uint8)
    n, lab = cv2.connectedComponents(m, connectivity=8)
    if n <= 1:
        return []
    cnt = np.bincount(lab.ravel(), minlength=n).astype(np.float64)
    means = np.stack([np.bincount(lab.ravel(), weights=src_rgb[..., c].ravel(), minlength=n) for c in range(3)], 1)
    means = means / np.maximum(cnt[:, None], 1)
    if boost_ref is not None:
        refm = np.stack([np.bincount(lab.ravel(), weights=boost_ref[..., c].ravel(), minlength=n) for c in range(3)], 1)
        refm = refm / np.maximum(cnt[:, None], 1)
        means = refm + (means - refm) * boost
    means = np.clip(means + lift, 0, 255)
    keep = np.arange(n) > 0
    keep &= cnt >= max(2, min_area // 2)
    ids = np.where(keep)[0]
    if len(ids) == 0:
        return []
    K = min(K, len(ids))
    data = means[ids].astype(np.float32)
    cv2.setRNGSeed(seed)
    _, lbl, cent = cv2.kmeans(data, K, None, (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 40, 0.5), 2,
                              cv2.KMEANS_PP_CENTERS)
    lbl = lbl.ravel()
    comp_color = np.full(n, -1, np.int32)
    comp_color[ids] = lbl
    colmap = comp_color[lab]
    out = []
    ys = np.where(mask.any(1))[0]
    y0, y1 = ys.min(), ys.max() + 1
    for k in range(K):
        mk = (colmap[y0:y1] == k)
        mk = np.pad(mk, ((0, 0), (pad, pad)), mode='constant')
        if smooth > 0:
            mk = soft_threshold_mask(mk, smooth)
        d = mask_to_path(mk, smooth_sigma=0.7, eps=eps, min_area=min_area, offset=(-pad, y0))
        if d:
            out.append((d, cent[k]))
    return out


def stipple(region, hp, src_rgb, thr, win=5, rmin=1.2, rmax=3.0, ytop=None, ybot=None, prob=1.0, rng=None,
            boost_ref=None, boost=1.0, sign=1):
    """Dots at local extrema of hp inside region. Returns list of (x, y, r, rgb)."""
    h = hp * sign
    k = np.ones((win, win), np.uint8)
    mx = cv2.dilate(h, k)
    peaks = (h >= mx) & (h > thr) & region
    ys, xs = np.nonzero(peaks)
    if rng is not None and prob < 1.0:
        sel = rng.random(len(xs)) < prob
        ys, xs = ys[sel], xs[sel]
    col = src_rgb[ys, xs].astype(np.float32)
    if boost_ref is not None:
        ref = boost_ref[ys, xs].astype(np.float32)
        col = ref + (col - ref) * boost
    if ytop is not None:
        t = np.clip((ys - ytop[xs]) / np.maximum(ybot[xs] - ytop[xs], 1), 0, 1)
    else:
        t = np.zeros(len(xs))
    strength = np.clip(h[ys, xs] / (thr * 3), 0.4, 1.0)
    r = (rmin + (rmax - rmin) * t) * (0.75 + 0.35 * strength)
    return list(zip(xs, ys, r, np.clip(col, 0, 255)))


def highpass_x(img_bgr, sx, pre_sigma=0.6, norm_sigma=0.0, sy=0.0):
    """High-pass against a horizontal-only blur: keeps vertical structures (grass blades)."""
    L = lstar(img_bgr, pre_sigma)
    k = int(3 * sx) * 2 + 1
    low = cv2.GaussianBlur(L, (k, 1), sx)
    hp = L - low
    if sy > 0:
        hp = cv2.GaussianBlur(hp, (1, int(3 * sy) * 2 + 1), sy)
    if norm_sigma > 0:
        sd = np.sqrt(cv2.GaussianBlur(hp * hp, (0, 0), norm_sigma)) + 0.8
        hp = hp / sd
    return hp
