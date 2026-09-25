import cv2, numpy as np

def smooth_closed(pts, sigma):
    """Gaussian-smooth a closed polyline (N,2)."""
    n = len(pts)
    if sigma <= 0 or n < 8:
        return pts.astype(float)
    r = int(3*sigma)+1
    k = np.exp(-0.5*(np.arange(-r, r+1)/sigma)**2); k /= k.sum()
    ext = np.concatenate([pts[-r:], pts, pts[:r]]).astype(float)
    out = np.stack([np.convolve(ext[:,i], k, mode='same') for i in range(2)], 1)
    return out[r:r+n]

def catmull_path(pts, closed=True, fmt='%.1f'):
    """Closed Catmull-Rom spline through pts -> SVG path data (cubic beziers)."""
    n = len(pts)
    if n < 3:
        return ''
    f = lambda p: (fmt % p[0]) + ',' + (fmt % p[1])
    d = ['M' + f(pts[0])]
    rng = range(n) if closed else range(n-1)
    for i in rng:
        p0 = pts[(i-1) % n] if (closed or i > 0) else pts[i]
        p1 = pts[i]; p2 = pts[(i+1) % n]
        p3 = pts[(i+2) % n] if (closed or i+2 < n) else pts[(i+1) % n]
        c1 = p1 + (p2-p0)/6.0; c2 = p2 - (p3-p1)/6.0
        d.append('C' + f(c1) + ' ' + f(c2) + ' ' + f(p2))
    if closed:
        d.append('Z')
    return ''.join(d)

def mask_to_path(mask, smooth_sigma=2.0, eps=0.7, min_area=12, offset=(0,0), scale=1.0):
    """Binary mask -> SVG path data using even-odd (outer contours + holes)."""
    m = (mask > 0).astype(np.uint8)
    cnts, hier = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    parts = []
    for c in cnts:
        if abs(cv2.contourArea(c)) < min_area:
            continue
        p = c[:,0,:].astype(float)
        p = smooth_closed(p, smooth_sigma)
        ap = cv2.approxPolyDP(p.astype(np.float32).reshape(-1,1,2), eps, True)[:,0,:].astype(float)
        if len(ap) < 3:
            continue
        ap = ap*scale + np.array(offset, float)
        parts.append(catmull_path(ap))
    return ''.join(parts)

def soft_threshold_mask(mask, sigma):
    """Morphologically smooth a binary mask by blurring and thresholding."""
    f = cv2.GaussianBlur((mask>0).astype(np.float32), (0,0), sigma) if sigma > 0 else (mask>0).astype(np.float32)
    return (f >= 0.5).astype(np.uint8)
