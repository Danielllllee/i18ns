#!/usr/bin/env python3
"""Hand-composed SVG rendition of Leonardo da Vinci's Mona Lisa, drawn from memory.

Shapes, landmarks and colours are placed by hand. Loops and seeded randomness
are used only for texture: hair strands, sleeve pleats, rock and terrain dabs.
Units are millimetres of the original 53 x 77 cm poplar panel.

Usage: python3 generate.py [output.svg]
"""
import math
import random
import sys

W, H = 530, 770

# ---------------------------------------------------------------- geometry helpers


def n(v):
    s = f"{v:.1f}"
    if s.endswith(".0"):
        s = s[:-2]
    return "0" if s in ("-0", "-0.0") else s


def pt(p):
    return f"{n(p[0])},{n(p[1])}"


def smooth(pts, closed=True, t=1.0):
    k = len(pts)
    d = [f"M{pt(pts[0])}"]
    for i in range(k if closed else k - 1):
        if closed:
            p0, p1, p2, p3 = pts[(i - 1) % k], pts[i], pts[(i + 1) % k], pts[(i + 2) % k]
        else:
            p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 6, p1[1] + (p2[1] - p0[1]) * t / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 6, p2[1] - (p3[1] - p1[1]) * t / 6)
        d.append(f"C{pt(c1)} {pt(c2)} {pt(p2)}")
    if closed:
        d.append("Z")
    return "".join(d)


def poly(pts, closed=True):
    return "M" + " L".join(pt(p) for p in pts) + ("Z" if closed else "")


def catmull(pts, per=12):
    k = len(pts)
    out = []
    for i in range(k - 1):
        p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k - 1)]
        for s in range(per):
            u = s / per
            u2, u3 = u * u, u * u * u
            out.append(tuple(0.5 * ((2 * p1[j]) + (-p0[j] + p2[j]) * u
                                    + (2 * p0[j] - 5 * p1[j] + 4 * p2[j] - p3[j]) * u2
                                    + (-p0[j] + 3 * p1[j] - 3 * p2[j] + p3[j]) * u3) for j in (0, 1)))
    out.append(pts[-1])
    return out


def resample(pts, m):
    seg = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    total = sum(seg) or 1.0
    out, i, acc = [], 0, 0.0
    for j in range(m):
        s = total * j / (m - 1)
        while i < len(seg) - 1 and acc + seg[i] < s:
            acc += seg[i]
            i += 1
        L = seg[i] or 1.0
        u = min(max((s - acc) / L, 0.0), 1.0)
        a, b = pts[i], pts[i + 1]
        out.append((a[0] + (b[0] - a[0]) * u, a[1] + (b[1] - a[1]) * u))
    return out


def guide(pts, m):
    return resample(catmull(pts, 16), m)


def normals(c):
    out = []
    for i in range(len(c)):
        a, b = c[max(i - 1, 0)], c[min(i + 1, len(c) - 1)]
        dx, dy = b[0] - a[0], b[1] - a[1]
        L = math.hypot(dx, dy) or 1.0
        out.append((-dy / L, dx / L))
    return out


def ribbon(center, w0, w1, per=10):
    c = catmull(center, per)
    nm = normals(c)
    left, right = [], []
    for i, p in enumerate(c):
        w = w0 + (w1 - w0) * i / (len(c) - 1)
        left.append((p[0] + nm[i][0] * w / 2, p[1] + nm[i][1] * w / 2))
        right.append((p[0] - nm[i][0] * w / 2, p[1] - nm[i][1] * w / 2))
    return poly(left + right[::-1])


def finger_pts(center, w0, w1, tipk=0.62):
    """Closed outline of a tapered finger, slightly fuller at the two joints, with a rounded tip."""
    c = catmull(center, 8)
    nm = normals(c)
    left, right = [], []
    for i, p in enumerate(c):
        t = i / (len(c) - 1)
        w = w0 + (w1 - w0) * (t ** 0.8)
        w += 0.7 * (math.exp(-((t - 0.46) / 0.07) ** 2) + 0.8 * math.exp(-((t - 0.74) / 0.06) ** 2))
        left.append((p[0] + nm[i][0] * w / 2, p[1] + nm[i][1] * w / 2))
        right.append((p[0] - nm[i][0] * w / 2, p[1] - nm[i][1] * w / 2))
    tip = c[-1]
    tx, ty = tip[0] - c[-2][0], tip[1] - c[-2][1]
    L = math.hypot(tx, ty) or 1.0
    tx, ty = tx / L, ty / L
    nx, ny = nm[-1]
    cap = []
    for k in range(1, 8):
        a = math.pi * k / 8
        cap.append((tip[0] + nx * math.cos(a) * w1 / 2 + tx * math.sin(a) * w1 * tipk,
                    tip[1] + ny * math.cos(a) * w1 / 2 + ty * math.sin(a) * w1 * tipk))
    return left + cap + right[::-1]


def offset_line(center, off, per=10):
    c = catmull(center, per)
    nm = normals(c)
    return [(p[0] + nm[i][0] * off, p[1] + nm[i][1] * off) for i, p in enumerate(c)]


def cn(v, prec=1):
    """Compact number: given decimals, no leading zero, no trailing .0"""
    s = f"{v:.{prec}f}"
    if s.endswith(".0"):
        s = s[:-2]
    if s.startswith("0."):
        s = s[1:]
    elif s.startswith("-0."):
        s = "-" + s[2:]
    return "0" if s in ("-0", "") else s


def smooth_rel(pts, t=1.0, prec=0):
    """Open Catmull-Rom curve written with compact relative cubic commands (for texture strokes)."""
    k = len(pts)
    out = [f"M{cn(pts[0][0], prec)} {cn(pts[0][1], prec)}c"]
    cur = (float(cn(pts[0][0], prec)), float(cn(pts[0][1], prec)))
    segs = []
    for i in range(k - 1):
        p0, p1, p2, p3 = pts[max(i - 1, 0)], pts[i], pts[i + 1], pts[min(i + 2, k - 1)]
        c1 = (p1[0] + (p2[0] - p0[0]) * t / 6 - cur[0], p1[1] + (p2[1] - p0[1]) * t / 6 - cur[1])
        c2 = (p2[0] - (p3[0] - p1[0]) * t / 6 - cur[0], p2[1] - (p3[1] - p1[1]) * t / 6 - cur[1])
        e = (p2[0] - cur[0], p2[1] - cur[1])
        nums = [cn(c1[0], prec), cn(c1[1], prec), cn(c2[0], prec), cn(c2[1], prec), cn(e[0], prec), cn(e[1], prec)]
        # rounding drift: advance the pen by the rounded end point
        cur = (cur[0] + float(nums[4]), cur[1] + float(nums[5]))
        segs.append(" ".join(nums).replace(" -", "-"))
    out.append(" ".join(segs).replace(" -", "-"))
    return "".join(out)


def fractal(keys, rough, depth, rng):
    pts = list(keys)
    for _ in range(depth):
        new = [pts[0]]
        for a, b in zip(pts, pts[1:]):
            m = ((a[0] + b[0]) / 2 + rng.uniform(-0.12, 0.12) * (b[0] - a[0]),
                 (a[1] + b[1]) / 2 + rng.uniform(-1, 1) * rough * math.dist(a, b))
            new += [m, b]
        pts = new
    return pts


# ---------------------------------------------------------------- svg helpers

FILTERS = {}
DEFS = []
BODY = []


def blur(sd):
    key = f"{sd:.2f}".rstrip("0").rstrip(".").replace(".", "_")
    fid = f"b{key}"
    if fid not in FILTERS:
        FILTERS[fid] = (f'<filter id="{fid}" filterUnits="userSpaceOnUse" x="-80" y="-80" width="690" '
                        f'height="930" color-interpolation-filters="sRGB"><feGaussianBlur stdDeviation="{sd:g}"/>'
                        f'</filter>')
    return fid


def attrs(fill="none", op=None, sd=None, stroke=None, sw=None, extra=""):
    a = [f'fill="{fill}"']
    if stroke:
        a.append(f'stroke="{stroke}" stroke-width="{sw if sw is not None else 1:g}" stroke-linecap="round"')
    if op is not None and op < 0.999:
        a.append(f'opacity="{op:.2f}"')
    if sd:
        a.append(f'filter="url(#{blur(sd)})"')
    if extra:
        a.append(extra)
    return " ".join(a)


def P(d, fill="none", op=None, sd=None, stroke=None, sw=None, extra=""):
    return f'<path d="{d}" {attrs(fill, op, sd, stroke, sw, extra)}/>'


def E(cx, cy, rx, ry, fill, op=None, sd=None, rot=0):
    tr = f' transform="rotate({rot:g} {n(cx)} {n(cy)})"' if rot else ""
    return f'<ellipse cx="{n(cx)}" cy="{n(cy)}" rx="{n(rx)}" ry="{n(ry)}"{tr} {attrs(fill, op, sd)}/>'


def G(items, extra=""):
    return f"<g {extra}>" + "".join(items) + "</g>"


def SG(strokes, sd=None, extra=""):
    """Group of strokes sharing a blur: strokes = [(d, color, width, opacity)]."""
    f = f' filter="url(#{blur(sd)})"' if sd else ""
    body = "".join(f'<path d="{d}" stroke="{c}" stroke-width="{w:.2g}" opacity="{o:.2f}"/>' for d, c, w, o in strokes)
    return f'<g fill="none" stroke-linecap="round"{f} {extra}>{body}</g>'


def _stops(stops):
    out = []
    for st in stops:
        o, c = st[0], st[1]
        a = st[2] if len(st) > 2 else None
        out.append(f'<stop offset="{o:g}" stop-color="{c}"' + (f' stop-opacity="{a:g}"' if a is not None else "") + "/>")
    return "".join(out)


def lin(gid, x1, y1, x2, y2, stops):
    DEFS.append(f'<linearGradient id="{gid}" gradientUnits="userSpaceOnUse" x1="{n(x1)}" y1="{n(y1)}" x2="{n(x2)}" '
                f'y2="{n(y2)}">{_stops(stops)}</linearGradient>')
    return f"url(#{gid})"


def rad(gid, cx, cy, r, stops, fx=None, fy=None):
    f = f' fx="{n(fx)}" fy="{n(fy)}"' if fx is not None else ""
    DEFS.append(f'<radialGradient id="{gid}" gradientUnits="userSpaceOnUse" cx="{n(cx)}" cy="{n(cy)}" r="{n(r)}"{f}>'
                f'{_stops(stops)}</radialGradient>')
    return f"url(#{gid})"


def clip(cid, d):
    DEFS.append(f'<clipPath id="{cid}"><path d="{d}"/></clipPath>')
    return f'clip-path="url(#{cid})"'


def softmask(mid, d, sd):
    DEFS.append(f'<mask id="{mid}" maskUnits="userSpaceOnUse" x="-10" y="-10" width="{W + 20}" height="{H + 20}">'
                f'<path d="{d}" fill="#fff" filter="url(#{blur(sd)})"/></mask>')
    return f'mask="url(#{mid})"'


def add(*items):
    BODY.extend(items)


# ================================================================ landmarks

EYE_L = (227, 215)      # sitter's right eye (viewer's left, far side of the turned head)
EYE_R = (289, 214)      # sitter's left eye

FACE = [(258, 131), (286, 133), (309, 142), (326, 160), (336, 186), (340, 215), (341, 246), (336, 274),
        (325, 298), (306, 318), (281, 331), (256, 337), (234, 330), (216, 314), (204, 293), (196, 268),
        (193, 241), (194, 210), (198, 182), (210, 157), (231, 139)]

NECK = [(222, 292), (302, 292), (309, 330), (317, 358), (332, 382), (350, 404), (364, 428), (306, 442),
        (258, 447), (210, 442), (160, 433), (168, 408), (184, 386), (200, 360), (213, 332)]

NECKLINE = [(160, 432), (210, 441), (258, 447), (306, 442), (364, 428)]

HAIR_L_IN = [(258, 135), (240, 138), (222, 147), (209, 163), (200, 187), (195, 214), (193, 244), (196, 276),
             (204, 306), (205, 336), (197, 368), (183, 400), (165, 430), (146, 452)]
HAIR_L_OUT = [(258, 87), (231, 90), (207, 101), (189, 122), (177, 155), (169, 197), (164, 243), (161, 290),
              (156, 335), (146, 375), (132, 408), (114, 436), (96, 458), (82, 472)]
HAIR_R_IN = [(258, 135), (278, 137), (297, 145), (313, 159), (324, 183), (331, 212), (335, 245), (334, 276),
             (326, 304), (320, 334), (325, 366), (336, 398), (352, 428), (368, 450)]
HAIR_R_OUT = [(258, 87), (287, 90), (312, 102), (332, 125), (344, 161), (350, 205), (354, 252), (358, 300),
              (365, 345), (375, 386), (389, 420), (406, 448), (422, 468)]

SHOULDER = [(-6, 562), (20, 546), (55, 517), (95, 489), (135, 461), (172, 435), (205, 414), (320, 404),
            (364, 417), (414, 437), (464, 455), (504, 469), (536, 481), (536, 776), (-6, 776)]

PARAPET_Y = 456


# ================================================================ background

def dabs(rng, n_, xr, yr, cols, size=(2, 6), ops=(0.15, 0.4)):
    out = []
    for _ in range(n_):
        x, y = rng.uniform(*xr), rng.uniform(*yr)
        rx = rng.uniform(*size)
        out.append(E(x, y, rx, rx * rng.uniform(0.35, 0.7), rng.choice(cols), rng.uniform(*ops) * 0.6))
    return out


def sky():
    g = lin("gSky", 0, 0, 0, 470, [(0, "#5f7a6e"), (0.15, "#738c7e"), (0.32, "#90a48e"), (0.47, "#abb798"),
                                     (0.6, "#bfc29e"), (1, "#c6c39c")])
    add(f'<rect x="-6" y="-6" width="{W + 12}" height="480" fill="{g}"/>')
    rng = random.Random(5)
    haze = [E(265, 30, 330, 50, "#4e685d", 0.3, 26), E(120, 232, 170, 26, "#cbc9a6", 0.35, 16),
            E(440, 192, 150, 24, "#c9c7a6", 0.3, 16)]
    for _ in range(14):
        x, y = rng.uniform(-20, 550), rng.uniform(40, 170)
        haze.append(E(x, y, rng.uniform(40, 110), rng.uniform(6, 14), rng.choice(["#a9b79e", "#bcc4a6", "#6f877a"]),
                      rng.uniform(0.12, 0.28), 10))
    add(*haze)


def crag(x0, x1, top, base, rng, mid, lit, shade, op=0.75, rough=0.22):
    """Jagged rock outcrop: fractal crest, lit on the left flank, shadowed on the right."""
    w, h = x1 - x0, base - top
    crest = fractal([(x0, base - h * 0.25), (x0 + w * 0.18, top + h * 0.3), (x0 + w * 0.42, top),
                     (x0 + w * 0.62, top + h * 0.12), (x0 + w * 0.82, top + h * 0.4), (x1, base - h * 0.2)],
                    rough, 3, rng)
    body = poly(crest + [(x1, base), (x0, base)])
    out = [P(body, mid, op, 0.9)]
    cid = f"cCrag{len(DEFS)}"
    c = clip(cid, body)
    peak = min(crest, key=lambda q: q[1])
    out.append(G([P(poly([(x0 - 2, base), (x0 - 2, top - 2), (peak[0], top - 2), (peak[0] - w * 0.1, base)]), lit, 0.25,
                    2.6),
                  P(poly([(peak[0] + w * 0.12, top - 2), (x1 + 2, top - 2), (x1 + 2, base), (peak[0] + w * 0.2, base)]),
                    shade, 0.3, 2.6)], c))
    st = []
    for _ in range(int(w / 14)):
        xx = rng.uniform(x0 + 2, x1 - 2)
        st.append((poly([(xx, top + h * rng.uniform(0.15, 0.4)), (xx + rng.uniform(-2, 2), base - rng.uniform(2, 8))],
                        False), rng.choice([shade, lit]), rng.uniform(0.6, 1.2), rng.uniform(0.08, 0.18)))
    out.append(SG(st, 0.7, c))
    return out


def landscape():
    rng = random.Random(7)
    # far mountains: blue-green, softened by the air, paling towards their feet
    gfl = lin("gFarL", 0, 165, 0, 270, [(0, "#7a918a"), (0.55, "#8fa396"), (1, "#aeb9a4")])
    ridge = fractal([(-6, 190), (8, 173), (22, 163), (34, 167), (44, 153), (56, 157), (64, 146), (76, 152),
                     (92, 167), (110, 173), (126, 169), (146, 181), (170, 191), (205, 205)], 0.17, 3, rng)
    add(P(poly(ridge + [(205, 248), (-6, 248)]), gfl, 1, 0.8))
    ridge2 = fractal([(-6, 213), (12, 203), (26, 207), (38, 199), (52, 213), (70, 225), (96, 233), (130, 238),
                      (205, 242)], 0.15, 3, rng)
    add(P(poly(ridge2 + [(205, 250), (-6, 250)]), "#7c9086", 0.8, 0.8))
    gfr = lin("gFarR", 0, 115, 0, 224, [(0, "#748b81"), (0.6, "#899e92"), (1, "#a8b4a1")])
    ridgeR = fractal([(338, 206), (350, 183), (358, 161), (366, 145), (374, 141), (382, 153), (389, 159),
                      (396, 141), (404, 125), (412, 121), (419, 131), (425, 153), (434, 167), (444, 157),
                      (454, 139), (464, 129), (474, 137), (482, 157), (494, 173), (506, 163), (518, 147),
                      (536, 141)], 0.19, 3, rng)
    add(P(poly(ridgeR + [(536, 226), (338, 226)]), gfr, 1, 0.8))
    fac = []
    for (x, y) in [(374, 141), (412, 121), (464, 129), (518, 147), (22, 163), (44, 153), (64, 146), (396, 141),
                   (454, 139), (360, 160), (488, 165), (110, 172)]:
        h = rng.uniform(30, 52)
        fac.append(P(smooth([(x, y + 2), (x - 6, y + h * 0.5), (x - 12, y + h), (x - 2, y + h + 2)]), "#adbcaa", 0.34,
                     1.8))
        fac.append(P(smooth([(x + 1, y + 2), (x + 8, y + h * 0.5), (x + 14, y + h + 2), (x + 3, y + h + 4)]), "#5a716b",
                     0.34, 1.8))
        for _ in range(3):
            xx = x + rng.uniform(-10, 10)
            fac.append(P(poly([(xx, y + rng.uniform(8, 16)), (xx + rng.uniform(-2, 2), y + rng.uniform(26, 44))], False),
                         stroke=rng.choice(["#a6b5a4", "#5e756e"]), sw=1.2, op=0.3, sd=0.9))
    add(*fac)
    # haze lying on the lakes
    add(E(110, 238, 120, 12, "#c8cbb0", 0.5, 7), E(440, 212, 120, 10, "#c8cbb0", 0.45, 7))

    # lakes; the left one sits visibly lower than the right one
    add(P(smooth([(-6, 242), (60, 238), (130, 241), (206, 244), (206, 278), (120, 280), (-6, 276)]),
          lin("gLakeL", 0, 238, 0, 278, [(0, "#b9bea4"), (0.6, "#aab29a"), (1, "#9aa28a")])))
    add(P(smooth([(-6, 244), (40, 242), (90, 244), (140, 246), (206, 248), (206, 252), (120, 251), (-6, 249)]),
          "#8e9c8c", 0.4, 1.2))
    add(P(smooth([(20, 258), (34, 253), (52, 254), (60, 260), (30, 262)]), "#7e8a76", 0.45, 1.2))
    add(P(smooth([(120, 262), (140, 257), (160, 259), (170, 265), (130, 266)]), "#7a8672", 0.4, 1.2))
    add(P(poly([(-6, 272), (206, 274), (206, 282), (-6, 280)]), "#7e8268", 0.5, 2))
    add(P(smooth([(338, 220), (420, 216), (536, 214), (536, 254), (440, 256), (338, 257)]),
          lin("gLakeR", 0, 214, 0, 254, [(0, "#c6caaf"), (1, "#adb59d")])))
    st = []
    for lo, hi_, x0, x1 in [(244, 272, -5, 180), (220, 252, 345, 510)]:
        for _ in range(16):
            y, x = rng.uniform(lo, hi_), rng.uniform(x0, x1)
            st.append((poly([(x, y), (x + rng.uniform(15, 50), y)], False), rng.choice(["#d6d8bc", "#93a08c"]), 0.7,
                       rng.uniform(0.2, 0.4)))
    add(SG(st, 0.6))
    add(P(smooth([(372, 239), (382, 227), (392, 225), (400, 233), (404, 247), (376, 248)]), "#7a8e82", 0.7, 1))
    add(P(smooth([(486, 237), (496, 225), (508, 223), (520, 231), (526, 245), (488, 247)]), "#73867a", 0.7, 1))

    # middle ground, left: olive hills going down to warm browns, with rocky outcrops
    add(P(smooth([(-6, 270), (18, 272), (42, 280), (66, 277), (92, 285), (118, 292), (150, 302), (176, 318),
                  (206, 334), (206, 470), (-6, 470)]),
          lin("gMidL", 0, 270, 0, 466, [(0, "#88886a"), (0.3, "#767046"), (0.65, "#5f5431"), (1, "#433922")])))
    for (x0, x1, top, base) in [(-8, 64, 276, 334), (40, 146, 300, 346), (122, 208, 316, 368), (-8, 84, 362, 398),
                                (100, 208, 374, 410), (-8, 116, 414, 448)]:
        add(*crag(x0, x1, top, base, rng, "#5c5838", "#8e8a62", "#36321f", 0.55, 0.1))
    add(G(dabs(rng, 150, (-5, 205), (280, 460), ["#4c4426", "#6c7656", "#8a7e52", "#3c3620"], (2, 6),
               (0.12, 0.3)), f'filter="url(#{blur(1.2)})"'))
    road = [(150, 458), (132, 448), (112, 441), (104, 432), (118, 423), (140, 414), (148, 405), (132, 397),
            (106, 391), (86, 385), (84, 377), (99, 371), (116, 365), (118, 357), (101, 351), (80, 347),
            (64, 342), (59, 335)]
    add(P(ribbon(road, 5.5, 1.6), "#3e3622", 0.3, 1.6))
    add(P(ribbon(road, 4.2, 1.1), "#8c7c52", 0.5, 1))
    add(P(ribbon(road[2:-3], 1.4, 0.5), "#a89868", 0.3, 0.8))
    add(G(dabs(rng, 14, (60, 150), (340, 455), ["#5e5532", "#4c4426"], (3, 6), (0.3, 0.5)),
          f'filter="url(#{blur(1.2)})"'))

    # middle ground, right
    add(P(smooth([(338, 254), (400, 252), (460, 252), (536, 252), (536, 470), (338, 470)]),
          lin("gMidR", 0, 252, 0, 466, [(0, "#898d6e"), (0.25, "#77744c"), (0.6, "#635733"), (1, "#433922")])))
    for (x0, x1, top, base) in [(336, 414, 254, 304), (440, 538, 256, 296), (336, 404, 304, 346),
                                (472, 538, 298, 356), (336, 396, 352, 400), (484, 538, 362, 410)]:
        add(*crag(x0, x1, top, base, rng, "#5e5c3c", "#929070", "#383420", 0.55, 0.1))
    add(G(dabs(rng, 170, (340, 535), (256, 460), ["#4c4426", "#6c7656", "#8a7e52", "#3c3620"], (2, 6),
               (0.12, 0.3)), f'filter="url(#{blur(1.2)})"'))
    river = [(452, 254), (470, 266), (480, 284), (466, 300), (442, 312), (432, 326), (446, 342), (468, 354),
             (470, 370), (452, 386), (442, 400), (438, 414), (430, 432), (422, 450), (418, 462)]
    add(P(ribbon(river, 3, 11), "#3e3a24", 0.35, 1.6))
    add(P(ribbon(river, 2, 8.5), "#999b7b", 0.48, 1.1))
    add(P(ribbon(river[1:-2], 1, 3), "#b2b294", 0.24, 0.9))
    add(P(smooth([(397, 403), (438, 399), (481, 396), (482, 410), (440, 413), (397, 417)], t=0.4), "#6c5a3a", 0.85,
          0.7))
    add(P(smooth([(397, 402), (438, 398.5), (481, 395.5)], closed=False), stroke="#9c865a", sw=1.2, op=0.6, sd=0.6))
    for i in range(5):
        x = 402 + i * 15.6
        yb = 416 - (x - 397) * 0.07
        add(P(f"M{n(x)},{n(yb)} L{n(x)},{n(yb - 5)} Q{n(x + 5.5)},{n(yb - 10.5)} {n(x + 11)},{n(yb - 5.5)} "
              f"L{n(x + 11)},{n(yb - 0.8)}Z", "#2e281a", 0.55, 0.7))
    add(P(poly([(-6, 436), (206, 442), (206, 466), (-6, 466)]), "#3a3120", 0.5, 5))
    add(P(poly([(338, 440), (536, 436), (536, 466), (338, 466)]), "#3a3120", 0.5, 5))


def parapet():
    gp = lin("gPar", 0, PARAPET_Y, 0, 600, [(0, "#3a2f1c"), (0.12, "#272013"), (1, "#15100a")])
    add(P(poly([(-6, PARAPET_Y), (536, PARAPET_Y), (536, 776), (-6, 776)]), gp))
    add(P(poly([(-6, PARAPET_Y), (536, PARAPET_Y)], False), stroke="#5e5034", sw=1.4, op=0.6, sd=0.6))
    # bases of the loggia columns, barely visible at both edges
    for x0, x1 in [(-6, 7), (523, 536)]:
        add(P(poly([(x0, 408), (x1, 408), (x1, PARAPET_Y), (x0, PARAPET_Y)]), "#3a3020", 0.6, 0.8))
        add(P(poly([(x0, 438), (x1, 438), (x1, 443), (x0, 443)]), "#6a5a3a", 0.45, 0.6))


# ================================================================ texture generators

def strands(inner, outer, count, rng, colors, wave_start=0.45, amp=(2.0, 6.0), wl=(14, 24), widths=(0.5, 1.6),
            ops=(0.25, 0.6), m=70, curl=0.0, u_range=(0.0, 1.0), end=(0.8, 1.0), start=(0.0, 0.08)):
    A, B = guide(inner, m), guide(outer, m)
    out = []
    for _ in range(count):
        u = rng.uniform(*u_range)
        phase = rng.uniform(0, 2 * math.pi)
        a, L = rng.uniform(*amp), rng.uniform(*wl)
        i0, i1 = int(m * rng.uniform(*start)), int(m * rng.uniform(*end))
        base = [(A[i][0] * (1 - u) + B[i][0] * u, A[i][1] * (1 - u) + B[i][1] * u) for i in range(m)]
        nm = normals(base)
        pts, s = [], 0.0
        for i in range(i0, i1):
            if i > i0:
                s += math.dist(base[i], base[i - 1])
            t = i / (m - 1)
            ramp = max(0.0, (t - wave_start) / (1 - wave_start)) ** 1.3
            ang = 2 * math.pi * s / L + phase
            off, along = a * ramp * math.sin(ang), curl * a * ramp * math.cos(ang)
            tx, ty = nm[i][1], -nm[i][0]
            pts.append((base[i][0] + nm[i][0] * off + tx * along, base[i][1] + nm[i][1] * off + ty * along))
        if len(pts) >= 4:
            out.append((smooth_rel(pts[::3] + [pts[-1]]), rng.choice(colors), rng.uniform(*widths),
                        rng.uniform(*ops)))
    return out


def folds(A_pts, B_pts, count, rng, light, dark, amp=1.5, wl=(20, 40), sw=(0.6, 1.4), ops=(0.3, 0.6), gap=1.3,
          m=50, span=((0, 0.25), (0.7, 1.0))):
    A, B = guide(A_pts, m), guide(B_pts, m)
    darks, lights = [], []
    for k in range(count):
        u = (k + rng.uniform(-0.4, 0.4)) / max(count - 1, 1)
        phase, a, L = rng.uniform(0, 6.3), rng.uniform(0.3, 1) * amp, rng.uniform(*wl)
        base = [(A[i][0] * (1 - u) + B[i][0] * u, A[i][1] * (1 - u) + B[i][1] * u) for i in range(m)]
        nm = normals(base)
        s, line = 0.0, []
        for i in range(m):
            if i:
                s += math.dist(base[i], base[i - 1])
            off = a * math.sin(2 * math.pi * s / L + phase)
            line.append((base[i][0] + nm[i][0] * off, base[i][1] + nm[i][1] * off))
        i0, i1 = int(m * rng.uniform(*span[0])), int(m * rng.uniform(*span[1]))
        seg = line[i0:i1]
        if len(seg) < 4:
            continue
        w, o = rng.uniform(*sw), rng.uniform(*ops)
        darks.append((smooth_rel(seg[::3] + [seg[-1]]), dark, w, o))
        sh = [(p[0] - nm[i0 + j][0] * gap, p[1] - nm[i0 + j][1] * gap) for j, p in enumerate(seg)]
        lights.append((smooth_rel(sh[::3] + [sh[-1]]), light, w * 0.75, o * 0.85))
    return darks, lights


# ================================================================ figure

def dress():
    add(P(smooth(SHOULDER, t=0.6), lin("gDress", 150, 450, 420, 700,
                                       [(0, "#272114"), (0.5, "#1d1810"), (1, "#15110a")])))
    add(E(236, 530, 60, 70, "#382f1e", 0.5, 18), E(305, 600, 50, 40, "#0d0a06", 0.5, 16))
    rng = random.Random(11)
    st = []
    for _ in range(24):
        x = rng.uniform(200, 380)
        st.append((smooth([(x, 470 + rng.uniform(0, 30)), (x + rng.uniform(-8, 8), 560),
                           (x + rng.uniform(-12, 12), 640)], closed=False), rng.choice(["#3a311f", "#0b0905"]),
                   rng.uniform(1.5, 4), rng.uniform(0.2, 0.4)))
    add(SG(st, 2.4))


RSLEEVE = [(150, 462), (122, 474), (92, 490), (56, 513), (24, 542), (-6, 568), (-6, 708), (30, 709), (70, 703),
           (112, 692), (150, 679), (176, 670), (192, 662), (196, 646), (193, 630), (186, 614), (178, 590),
           (172, 560), (167, 530), (163, 498)]
LSLEEVE_UP = [(362, 490), (420, 518), (470, 546), (536, 580), (536, 636), (490, 638), (440, 644), (410, 640),
              (398, 608), (386, 566), (373, 525)]
LFOREARM = [(536, 616), (482, 624), (422, 632), (362, 640), (302, 649), (244, 660), (198, 672), (190, 690),
            (192, 712), (202, 734), (236, 762), (300, 778), (536, 778)]


def sleeve_texture(region_d, cid, A, B, count, rng, light, dark, amp, wl, cross=60, xr=None, yr=None):
    darks, lights = folds(A, B, count, rng, light, dark, amp=amp, wl=wl, sw=(0.5, 1.0), ops=(0.1, 0.24))
    c = clip(cid, region_d)
    out = [SG(darks, 0.6, c), SG(lights, 0.65, c)]
    bd, bl = folds(A, B, max(9, count // 4), rng, light, dark, amp=amp * 3, wl=(60, 120), sw=(5, 11),
                   ops=(0.3, 0.5), gap=5)
    out += [SG(bd, 3, c), SG(bl, 3.4, c)]
    if cross:
        st = []
        for _ in range(cross):
            x, y = rng.uniform(*xr), rng.uniform(*yr)
            ang, L = rng.uniform(0, math.pi), rng.uniform(3, 7)
            st.append((poly([(x, y), (x + math.cos(ang) * L, y + math.sin(ang) * L)], False),
                       rng.choice([dark, light]), rng.uniform(0.5, 1.0), rng.uniform(0.1, 0.2)))
        out.append(SG(st, 0.6, c))
    return out


def sleeves_back():
    rng = random.Random(23)
    d = smooth(LSLEEVE_UP, t=0.5)
    add(P(d, lin("gLUp", 380, 520, 520, 640, [(0, "#33250f"), (0.5, "#5a431e"), (1, "#3e2d14")])))
    add(*sleeve_texture(d, "cLUp", [(378, 500), (393, 556), (410, 606), (428, 648)],
                        [(500, 556), (520, 598), (536, 628), (545, 650)], 40, rng, "#a8843f", "#24190a", 1.0,
                        (40, 80), 12, (370, 536), (490, 645)))
    add(G([E(390, 560, 18, 60, "#160f06", 0.5, 10), E(480, 600, 40, 25, "#9a763a", 0.3, 12)], clip("cLUp2", d)))
    d = smooth(LFOREARM, t=0.5)
    add(P(d, lin("gLFore", 0, 616, 0, 770, [(0, "#8a6a32"), (0.22, "#6e5226"), (0.55, "#523c1c"),
                                            (1, "#2c200e")])))
    add(*sleeve_texture(d, "cLFore", [(545, 622), (480, 630), (420, 638), (360, 646), (300, 655), (244, 666),
                                      (196, 678)],
                        [(545, 790), (470, 792), (400, 790), (330, 784), (270, 770), (225, 748), (198, 724)],
                        72, rng, "#b08a44", "#2a1d0b", 1.2, (40, 90), 24, (200, 535), (640, 770)))
    add(G([E(330, 652, 130, 9, "#cfa85e", 0.35, 6), E(420, 748, 160, 30, "#1c1309", 0.55, 14),
           E(212, 720, 25, 40, "#20160a", 0.45, 10), E(360, 690, 90, 20, "#a07a3a", 0.2, 12)], clip("cLFore3", d)))


def mantle():
    rng = random.Random(31)
    M = [(330, 436), (352, 424), (384, 428), (420, 440), (462, 458), (500, 471), (536, 482), (536, 590),
         (500, 570), (466, 552), (432, 534), (400, 516), (374, 498), (352, 480), (336, 460)]
    d = smooth(M, t=0.5)
    add(P(d, lin("gMantle", 340, 430, 520, 590, [(0, "#382d19"), (0.5, "#2c2314"), (1, "#20190e")]), 0.96))
    st = []
    for k in range(16):
        x0 = 346 + k * 12 + rng.uniform(-4, 4)
        st.append((smooth([(x0, 428 + k * 3), (x0 + 20, 466 + k * 2), (x0 + 30, 518 + k)], closed=False),
                   rng.choice(["#64512c", "#54431f", "#100c06"]), rng.uniform(1.5, 4.5), rng.uniform(0.25, 0.5)))
    add(SG(st, 2, clip("cMantle", d)))
    add(P(smooth(M[7:] + [M[0]], closed=False, t=0.5), stroke="#77603a", sw=1.4, op=0.45, sd=0.8))


def guarnello():
    """The sheer veil worn over the dress, seen where it crosses the shoulders."""
    rng = random.Random(71)
    d = smooth([(100, 470), (150, 450), (190, 440), (172, 470), (150, 500), (118, 520), (80, 534), (60, 520)], t=0.6)
    add(P(d, "#8a7a58", 0.1, 4))
    st = []
    for _ in range(14):
        x0, y0 = rng.uniform(96, 186), rng.uniform(450, 470)
        st.append((smooth([(x0, y0), (x0 - 18, y0 + 26), (x0 - 40, y0 + 52)], closed=False), "#9a8a64",
                   rng.uniform(0.6, 1.4), rng.uniform(0.08, 0.16)))
    add(SG(st, 1.2, clip("cGuar", d)))
    d2 = smooth([(350, 446), (382, 440), (420, 452), (400, 470), (370, 478), (350, 470)], t=0.6)
    add(P(d2, "#7a6c4c", 0.08, 4))


def skin_neck():
    d = smooth(NECK, t=0.6)
    add(P(d, lin("gNeck", 196, 0, 356, 0, [(0, "#cda86e"), (0.45, "#b98f58"), (0.8, "#8c683c"), (1, "#6a4e2c")])))
    add(G([
        E(230, 418, 66, 24, "#ead6a2", 0.55, 14),
        E(306, 428, 40, 16, "#d0b282", 0.35, 12),
        P(smooth([(210, 306), (236, 334), (262, 348), (292, 334), (318, 306)], closed=False),
          stroke="#3f3018", sw=34, op=0.66, sd=8),
        E(320, 356, 22, 54, "#3f3018", 0.58, 10),
        E(350, 410, 22, 30, "#4f3c1e", 0.52, 10),
        E(198, 380, 12, 34, "#705a32", 0.42, 8),
        E(264, 396, 10, 6, "#7a5e36", 0.35, 4),
        E(244, 374, 20, 20, "#d2b27e", 0.28, 10),
        E(266, 372, 40, 16, "#7a5e36", 0.18, 10),
        P(smooth([(206, 404), (230, 400), (252, 401)], closed=False), stroke="#8a6c40", sw=2.2, op=0.18, sd=2.4),
        P(smooth([(276, 401), (300, 399), (326, 403)], closed=False), stroke="#705a32", sw=2.2, op=0.2, sd=2.4),
    ], softmask("mNeck", d, 0.8)))


def embroidery():
    rng = random.Random(41)
    c = guide(NECKLINE, 120)
    nm = normals(c)
    sgn = 1 if nm[60][1] > 0 else -1          # make the band hang below the neckline
    top = [(p[0] - sgn * nm[i][0] * 0.4, p[1] - sgn * nm[i][1] * 0.4) for i, p in enumerate(c)]
    bot = [(p[0] + sgn * nm[i][0] * 7.5, p[1] + sgn * nm[i][1] * 7.5) for i, p in enumerate(c)]
    st = []
    for k in range(80):
        i = int(k / 79 * 119)
        x, y = bot[i]
        dx = (x - 260) * 0.12
        L = rng.uniform(26, 56)
        st.append((smooth([(x, y), (x + dx * 0.5 + rng.uniform(-1, 1), y + L * 0.5),
                           (x + dx + rng.uniform(-2, 2), y + L)], closed=False),
                   rng.choice(["#463a22", "#0a0805", "#352c1d"]), rng.uniform(0.6, 1.5), rng.uniform(0.3, 0.6)))
    add(SG(st, 0.7))
    add(P(poly(top + bot[::-1]), "#1b150c", 0.95, 0.4))
    mid = [((a[0] + b[0]) / 2, (a[1] + b[1]) / 2) for a, b in zip(top, bot)]
    s_acc, l1, l2, rings = 0.0, [], [], []
    for i, p in enumerate(mid):
        if i:
            s_acc += math.dist(mid[i], mid[i - 1])
        off = 2.4 * math.sin(2 * math.pi * s_acc / 8.0)
        l1.append((p[0] + nm[i][0] * off, p[1] + nm[i][1] * off))
        l2.append((p[0] - nm[i][0] * off, p[1] - nm[i][1] * off))
        if i % 4 == 2:
            rings.append(f'<circle cx="{n(p[0])}" cy="{n(p[1])}" r="1.1"/>')
    add(SG([(smooth(l1, closed=False), "#a3834a", 0.7, 0.85), (smooth(l2, closed=False), "#86693a", 0.7, 0.85)],
           0.25))
    add(f'<g fill="none" stroke="#ad8c4e" stroke-width="0.5" opacity="0.65">{"".join(rings)}</g>')
    add(P(smooth(top, closed=False), stroke="#65502e", sw=0.6, op=0.6, sd=0.3))


# ---------------------------------------------------------------- face

def eye(cx, cy, w, h, idx, ir, side):
    """Heavy-lidded almond eye; side=+1 for the near (viewer's right) eye."""
    items = []
    inner_right = side < 0
    lc = (cx - w / 2, cy + (1.0 if inner_right else 0.4))
    rc = (cx + w / 2, cy + (0.4 if inner_right else 1.0))
    top = [lc, (cx - w * 0.26, cy - h * 0.40), (cx + w * 0.05, cy - h * 0.52), (cx + w * 0.31, cy - h * 0.36), rc]
    bot = [rc, (cx + w * 0.26, cy + h * 0.36), (cx - w * 0.02, cy + h * 0.45), (cx - w * 0.30, cy + h * 0.35), lc]
    od = smooth(top + bot[1:-1], t=0.85)
    # the socket: one broad, soft shadow that merges brow, lid and the hollow under the eye
    items.append(E(cx + side * 1.5, cy - 2, w * 0.95, h * 1.85, "#4f3b20", 0.55, 8))
    items.append(E(cx + side * 1.0, cy - 2, w * 0.66, h * 1.05, "#3e2c16", 0.35, 4.5))
    if side > 0:
        items.append(E(cx - w * 0.48, cy - 2, 7, 12, "#3e2a14", 0.5, 4))
    else:
        items.append(E(cx + w * 0.48, cy - 1, 5, 9, "#4a3519", 0.32, 4))
    # heavy upper lid catching a little light, with a soft fold above it
    crease = [(lc[0] + 3, lc[1] - h * 0.66), (cx - w * 0.14, cy - h * 1.05), (cx + w * 0.2, cy - h * 1.0),
              (rc[0] - 2, rc[1] - h * 0.6)]
    items.append(P(smooth(crease, closed=False), stroke="#4a3418", sw=3.2, op=0.32, sd=2.2))
    items.append(P(smooth([(cx - w * 0.24, cy - h * 0.72), (cx + w * 0.03, cy - h * 0.82), (cx + w * 0.26, cy - h * 0.7)],
                          closed=False), stroke="#d8bc88", sw=3.4, op=0.26, sd=2))
    gw = rad(f"gWhite{side}", cx + idx * 0.6, cy + 0.5, w * 0.55, [(0, "#9a8968"), (0.55, "#7e6e4e"), (1, "#4a3d26")])
    items.append(P(od, gw, 0.95, 0.6))
    c = clip(f"cEye{side}", od)
    iy = cy - h * 0.14
    gi = rad(f"gIris{side}", cx + idx, iy, ir, [(0, "#0c0704"), (0.4, "#150d06"), (0.8, "#2e1e0e"), (1, "#1a1108")])
    items.append(G([
        E(cx + idx, iy, ir, ir, gi, 0.95, 0.8),
        E(cx + idx, iy, ir * 0.45, ir * 0.45, "#070402", 0.75, 0.6),
        P(smooth(top, closed=False, t=0.85), stroke="#1e130a", sw=h * 0.8, op=0.6, sd=1.6),
        E(cx + idx - ir * 0.38, iy - ir * 0.15, 1.0, 0.75, "#ded0ac", 0.32, 0.45),
    ], c))
    items.append(P(smooth(top, closed=False, t=0.85), stroke="#1e130a", sw=1.6, op=0.7, sd=0.8))
    items.append(P(smooth(bot, closed=False, t=0.85), stroke="#4a3519", sw=1.0, op=0.38, sd=0.8))
    items.append(P(smooth([(p[0], p[1] + 1.8) for p in bot[1:-1]], closed=False), stroke="#cdb07c", sw=1.5, op=0.26,
                   sd=1))
    inner = rc if inner_right else lc
    items.append(E(inner[0] + (-1.6 if inner_right else 1.6), inner[1], 1.8, 1.3, "#86584a", 0.32, 0.9))
    bag = [(cx - w * 0.4, cy + h * 0.62 + 3), (cx, cy + h * 0.8 + 4.5), (cx + w * 0.4, cy + h * 0.62 + 3)]
    items.append(P(smooth(bag, closed=False), stroke="#5e472a", sw=3.2, op=0.34, sd=2.4))
    items.append(P(smooth([(p[0], p[1] + 4.2) for p in bag], closed=False), stroke="#dcc396", sw=3.4, op=0.24, sd=2.8))
    return items


def face():
    d = smooth(FACE, t=0.9)
    g = rad("gFace", 228, 198, 162, [(0, "#ebcd95"), (0.28, "#ddb77c"), (0.55, "#c69b60"), (0.8, "#9a7444"),
                                       (1, "#6e5030")])
    items = [P(d, g)]
    sh, sh2 = "#3f3018", "#55401f"          # olive-brown shadows under the old varnish
    items += [
        E(357, 236, 56, 126, sh, 0.72, 18),
        E(335, 172, 18, 34, sh2, 0.45, 10),
        E(327, 290, 30, 44, sh, 0.55, 12),
        E(297, 326, 36, 16, sh2, 0.4, 9),
        E(317, 232, 14, 42, "#6a5230", 0.28, 10),
        E(196, 240, 10, 76, "#705430", 0.45, 6),
        E(206, 294, 11, 22, "#705430", 0.36, 6),
        E(258, 140, 60, 10, "#86683c", 0.25, 6),
        E(242, 166, 50, 26, "#f2dcac", 0.55, 13),
        E(219, 252, 21, 27, "#ecd2a0", 0.5, 10),
        E(253, 198, 9, 15, "#ecd2a0", 0.4, 5),
        E(297, 252, 17, 17, "#d2b27e", 0.24, 9),
        E(305, 280, 22, 16, "#705430", 0.3, 9),
        E(209, 172, 16, 24, "#86683c", 0.4, 7),
        E(226, 185, 20, 6, "#6a5230", 0.16, 4),
        E(290, 184, 22, 6, "#6a5230", 0.18, 4),
    ]
    items += eye(EYE_L[0], EYE_L[1], 34, 15, 3.4, 7.2, -1)
    items += eye(EYE_R[0], EYE_R[1], 39, 16, 3.0, 7.8, 1)
    nx, ny = -2.5, 2.5

    def N(x, y):
        return (x + nx, y + ny)
    items += [
        P(smooth([N(254, 203), N(254.5, 226), N(255.5, 246), N(256, 254)], closed=False), stroke="#f0daa8", sw=4.4,
          op=0.45, sd=2.2),
        P(smooth([N(262, 203), N(268, 225), N(275, 247), N(280, 262), N(270, 266), N(264, 245), N(260.5, 222)]),
          "#5e4522", 0.58, 4),
        P(smooth([N(260.5, 208), N(262.5, 228), N(266, 246), N(269, 258)], closed=False), stroke="#6a4c26", sw=2.2,
          op=0.36, sd=1.4),
        P(smooth([N(247, 228), N(245, 246), N(243, 258)], closed=False), stroke="#86683c", sw=2, op=0.22, sd=2.2),
        E(*N(256, 255.5), 4.6, 3.6, "#f0daa8", 0.42, 1.8),
        E(*N(246, 262), 4.6, 3.4, "#7a5e36", 0.38, 1.6),
        E(*N(270.5, 261), 5.6, 4.2, "#4e3a1c", 0.52, 1.6),
        E(*N(258, 268.5), 12, 3.8, "#3f2c14", 0.55, 2.3),
        E(*N(250.5, 265.6), 2.8, 1.4, "#2e1e0c", 0.55, 1),
        E(*N(265.5, 265.4), 3.1, 1.5, "#2e1e0c", 0.62, 1),
        P(f"M{252.5 + nx:g},{271 + ny:g} L{253 + nx:g},{282 + ny:g}", stroke="#6a4c26", sw=1.3, op=0.18, sd=1.1),
        P(f"M{259.5 + nx:g},{271 + ny:g} L{259 + nx:g},{282 + ny:g}", stroke="#6a4c26", sw=1.3, op=0.22, sd=1.1),
        E(256 + nx, 277 + ny, 3, 5, "#e2c896", 0.2, 1.6),
        P(smooth([N(278, 267), N(284, 276), N(289, 286)], closed=False), stroke="#5e4522", sw=4, op=0.3, sd=3.4),
        P(smooth([N(241, 268), N(236, 276), N(232, 285)], closed=False), stroke="#7a5e36", sw=3, op=0.18, sd=3.4),
    ]
    my, mx = 292.5, -2

    def M(x, y):
        return (x + mx, my + y)
    items += [
        E(257, my - 4, 26, 5, "#7a5e36", 0.2, 3),
        E(*M(240, -12), 9, 7, "#ecd2a0", 0.3, 4), E(*M(278, -13), 9, 7, "#dcc08c", 0.22, 4),
        P(smooth([M(234, -1.2), M(245, -4.8), M(252.5, -5.6), M(258, -4.6), M(263.5, -5.6), M(272, -5),
                  M(283, -2.4), M(272, -0.2), M(258, 0.9), M(245, 0.1)]), "#8e6040", 0.45, 1.4),
        P(smooth([M(238, 1.7), M(258, 3.1), M(280, 1.1), M(272, 7.6), M(258, 9.8), M(244, 7.4)]), "#b0805a", 0.36, 1.8),
        E(*M(256.5, 5.5), 8, 2, "#dfc08e", 0.34, 1.6),
        P(f"M{233 + mx:g},{my - 1.3:g} C{243 + mx:g},{my + 0.7:g} {250.5 + mx:g},{my + 1.8:g} {258 + mx:g},{my + 1.8:g} "
          f"C{265.5 + mx:g},{my + 1.8:g} {273 + mx:g},{my + 0.6:g} {284 + mx:g},{my - 2.4:g}", stroke="#3a220e",
          sw=1.8, op=0.62, sd=0.95),
        # corners of the mouth: dark, turning upward and melting into the cheeks
        P(smooth([M(236, 0), M(232.5, -2), M(230, -5.5), M(229.5, -9)], closed=False), stroke="#3f2c14", sw=3.4,
          op=0.24, sd=2.6),
        P(smooth([M(281, -1), M(285, -3.2), M(288, -6.6), M(289, -10)], closed=False), stroke="#3f2c14", sw=3.6,
          op=0.28, sd=2.6),
        E(*M(233, -1.6), 3.4, 2.8, "#36250f", 0.4, 1.5),
        E(*M(284.5, -2.6), 3.6, 2.8, "#36250f", 0.45, 1.5),
        E(*M(227.5, -6), 7.5, 9, "#705430", 0.26, 4.6),
        E(*M(291.5, -7), 8.5, 10, "#634a28", 0.32, 4.6),
        E(*M(258, 13.6), 13, 3.8, "#5a4422", 0.4, 2.6),
        E(253, 322, 15, 9, "#e2c896", 0.42, 5),
        E(279, 326, 15, 9, "#5a4422", 0.36, 6),
    ]
    add(G(items, softmask("mFace", d, 1.2)))


def ringlet(cx, cy, r, turns, rot):
    pts = []
    steps = int(turns * 14)
    for i in range(steps + 1):
        t = i / steps
        a = rot + t * turns * 2 * math.pi
        rr = r * (1 - 0.55 * t)
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a) * 1.35))
    return smooth(pts, closed=False)


def hair():
    rng = random.Random(53)
    bl = [(86, 478), (100, 484), (122, 480)]
    br = [(420, 478), (404, 480), (386, 472)]
    dl = smooth(HAIR_L_OUT + bl + HAIR_L_IN[::-1], t=0.7)
    dr = smooth(HAIR_R_OUT + br + HAIR_R_IN[::-1], t=0.7)
    add(P(dl, "#170f07", 1, 1.3), P(dr, "#170f07", 1, 1.3))
    cl, cr = clip("cHairL", dl), clip("cHairR", dr)
    dark = ["#22170c", "#281b0d", "#2e2010", "#342412"]
    glint = ["#53391c", "#5e4320", "#4a3318", "#6a4c26"]
    # strands combed from the parting: smooth on the crown, rippling and loosening towards the shoulders
    for gi, go, cc in ((HAIR_L_IN, HAIR_L_OUT, cl), (HAIR_R_IN, HAIR_R_OUT, cr)):
        # smooth crown under the veil, then rippling locks down the sides
        add(SG(strands(gi, go, 60, rng, dark, wave_start=0.5, amp=(0.5, 1.5), wl=(14, 20), widths=(0.4, 0.9),
                       ops=(0.12, 0.28), start=(0.0, 0.04), end=(0.22, 0.34)), 0.5, cc))
        add(SG(strands(gi, go, 130, rng, dark, wave_start=0.1, amp=(1.2, 5.5), wl=(13, 21), curl=0.5,
                       widths=(0.4, 1.1), start=(0.16, 0.3)), 0.45, cc))
    add(SG(strands(HAIR_L_IN, HAIR_L_OUT, 40, rng, glint, wave_start=0.1, amp=(1.4, 5.5), wl=(13, 20), curl=0.6,
                   ops=(0.14, 0.32), widths=(0.4, 0.9), u_range=(0.0, 0.35), start=(0.25, 0.45), end=(0.6, 0.95)),
           0.45, cl))
    add(G([E(198, 260, 16, 70, "#4a3418", 0.3, 10), E(188, 360, 16, 40, "#3e2c14", 0.25, 10)], cl))
    add(SG(strands(HAIR_R_IN, HAIR_R_OUT, 16, rng, glint, wave_start=0.2, amp=(1.4, 5), wl=(13, 20), curl=0.6,
                   ops=(0.1, 0.24), widths=(0.4, 0.8), u_range=(0.4, 0.95), start=(0.4, 0.6), end=(0.75, 1.0)),
           0.45, cr))
    # a few corkscrew ringlets near the shoulders
    rl = []
    for (x, y, r, cl_) in [(176, 392, 4.5, "#5e4422"), (156, 418, 5, "#5e4422"), (134, 444, 5.5, "#53391c"),
                           (186, 352, 4, "#53391c"), (114, 462, 5, "#4a3318"),
                           (354, 380, 4.5, "#3e2c16"), (370, 412, 5, "#3e2c16"), (392, 446, 5, "#3a2814")]:
        for k in range(4):
            yy = y + k * r * 1.6
            rl.append((ringlet(x + rng.uniform(-1, 1), yy, r * (1 - 0.08 * k), 1.0, rng.uniform(0, 6.3)), cl_, 0.8,
                       0.4))
    add(SG(rl, 0.5, cl))
    add(G([E(222, 118, 14, 20, "#36250f", 0.3, 7), E(176, 300, 12, 56, "#34240f", 0.25, 9),
           E(258, 104, 72, 26, "#0c0804", 0.35, 10)], cl))
    add(G([E(258, 104, 72, 26, "#0c0804", 0.35, 10)], cr))
    add(G([E(352, 330, 14, 60, "#0a0603", 0.45, 9), E(330, 140, 14, 20, "#0e0904", 0.3, 7)], cr))
    add(SG([(smooth(HAIR_L_IN, closed=False), "#20140a", 3, 0.45), (smooth(HAIR_R_IN, closed=False), "#20140a", 3, 0.5)],
           1.6))
    wisps = []
    for side, pts_ in ((-1, HAIR_L_OUT), (1, HAIR_R_OUT)):
        g_ = guide(pts_, 60)
        for _ in range(22):
            i = rng.randrange(8, 58)
            x, y = g_[i]
            L = rng.uniform(8, 18)
            wisps.append((smooth([(x, y), (x + side * rng.uniform(1, 4), y + L * 0.5),
                                  (x + side * rng.uniform(0, 3), y + L)], closed=False), "#2a1d0f",
                          rng.uniform(0.3, 0.6), rng.uniform(0.25, 0.45)))
    add(SG(wisps, 0.35))


def veil():
    VL = [(258, 82), (228, 85), (201, 97), (181, 119), (168, 153), (160, 196), (155, 243), (152, 290), (147, 335),
          (137, 375), (122, 408), (104, 436), (88, 458), (80, 476), (96, 484)]
    VR = [(258, 82), (290, 85), (318, 98), (339, 122), (352, 159), (358, 205), (362, 252), (366, 300), (373, 345),
          (383, 386), (397, 420), (414, 448), (428, 470), (414, 482)]
    add(P(smooth(VL + HAIR_L_OUT[::-1][:-1], t=0.7), "#1a140b", 0.18, 2.2))
    add(P(smooth(VR + HAIR_R_OUT[::-1][:-1], t=0.7), "#1a140b", 0.18, 2.2))
    hem = [(206, 168), (220, 152), (240, 143), (258, 140.5), (278, 142), (298, 149), (315, 163)]
    add(P(smooth(hem, closed=False), stroke="#3a2a18", sw=2.4, op=0.3, sd=0.9))
    add(P(smooth([(p[0], p[1] + 2.2) for p in hem], closed=False), stroke="#efd6a2", sw=0.8, op=0.2, sd=0.6))


# ---------------------------------------------------------------- hands

def frame(origin, angle_deg, flip=False):
    a = math.radians(angle_deg)
    ux, uy = math.cos(a), math.sin(a)
    vx, vy = -uy, ux
    if flip:
        vx, vy = -vx, -vy
    return lambda p: (origin[0] + p[0] * ux + p[1] * vx, origin[1] + p[0] * uy + p[1] * vy)


def hand3(to, back, fingers, gid, cols, extra=()):
    """Hand built as back + overlapping tapered fingers; cols = (light, mid, dark, shade, hi)."""
    light, mid, dark, shade, hi = cols
    backc = [to(p) for p in back]
    fings = [([to(p) for p in c], w0, w1) for c, w0, w1 in fingers]
    a, b = to((40, -32)), to((70, 42))
    g = lin(gid, a[0], a[1], b[0], b[1], [(0, light), (0.5, mid), (1, dark)])
    sil = [P(smooth(backc, t=0.8), "#1a1107")] + [P(smooth(finger_pts(c, w0, w1), t=0.7), "#1a1107")
                                                   for c, w0, w1 in fings]
    items = [G(sil, f'opacity="0.5" filter="url(#{blur(3.2)})" transform="translate(2 4.5)"')]
    items.append(P(smooth(backc, t=0.8), g))
    for c, w0, w1 in fings:
        cc = catmull(c, 8)
        nm = normals(cc)
        sgn = 1 if nm[len(nm) // 2][1] > 0 else -1          # +1 when the normal points down the page
        fp = smooth(finger_pts(c, w0, w1), t=0.7)
        items.append(P(fp, g, 1, 0.3))
        items.append(P(smooth(offset_line(c, sgn * w0 * 0.34), closed=False), stroke=shade, sw=2.6, op=0.5, sd=1.4))
        items.append(P(smooth(offset_line(c, -sgn * w0 * 0.14)[2:-3], closed=False), stroke=hi, sw=2.2, op=0.4,
                       sd=1.5))
        for f in (0.46, 0.74):
            i = int(f * (len(cc) - 1))
            p, q = cc[i], nm[i]
            items.append(E(p[0] - sgn * q[0] * w0 * 0.12, p[1] - sgn * q[1] * w0 * 0.12, 2.6, 1.8, hi, 0.3, 1.1))
            items.append(P(poly([(p[0] - q[0] * w0 * 0.3, p[1] - q[1] * w0 * 0.3),
                                 (p[0] + q[0] * w0 * 0.3, p[1] + q[1] * w0 * 0.3)], False),
                           stroke=shade, sw=0.8, op=0.18, sd=0.9))
        tip, pre = cc[-1], cc[-6]
        nx, ny = nm[-1]
        items.append(E(tip[0] * 0.72 + pre[0] * 0.28 - sgn * nx * w1 * 0.1,
                       tip[1] * 0.72 + pre[1] * 0.28 - sgn * ny * w1 * 0.1, w1 * 0.3, w1 * 0.22, hi, 0.3, 1.0,
                       rot=math.degrees(math.atan2(tip[1] - pre[1], tip[0] - pre[0]))))
    items += list(extra)
    return G(items)


def armrest():
    # the rounded end of the chair's arm, gripped by the left hand
    add(P(poly([(-6, 700), (200, 700), (200, 778), (-6, 778)]), "#120d07", 0.95, 3))
    add(P(smooth([(112, 722), (150, 716), (204, 718), (204, 768), (150, 770), (114, 764), (100, 744)], t=0.6),
          "#2c2011", 0.95, 1.2))
    add(P(smooth([(104, 734), (118, 721), (150, 716), (200, 717)], closed=False), stroke="#6e5634", sw=1.6, op=0.55,
          sd=0.9))
    add(E(150, 752, 40, 10, "#0d0905", 0.5, 6))


def left_hand():
    """Sitter's left hand, its fingers curling over the end of the chair's arm."""
    to = frame((205, 691), 160, flip=True)
    back = [(-6, 0), (0, -17), (22, -20), (42, -24), (58, -26), (64, -14), (65, 0), (63, 14), (58, 24), (40, 22),
            (20, 19), (0, 16)]
    fingers = [([(54, -19), (70, -19), (83, -15), (90, -6), (93, 3)], 15, 11.5),
               ([(58, -5), (74, -3), (85, 3), (90, 12), (91, 21)], 15.5, 12),
               ([(56, 9), (70, 12), (79, 18), (83, 26), (84, 34)], 14.5, 11),
               ([(51, 21), (63, 25), (70, 31), (73, 38), (74, 44)], 12.5, 9.5)]
    cols = ("#d6ac72", "#b0824c", "#6e4826", "#4e3016", "#e4c28a")
    p = to((30, -4))
    extra = [E(p[0], p[1], 24, 10, "#e6c890", 0.4, 5, rot=-20)]
    add(hand3(to, back, fingers, "gLH", cols, extra))


def right_sleeve():
    """Sitter's right sleeve. The cuff() layer re-shows its wrist end over the hand via <use>."""
    rng = random.Random(61)
    d = smooth(RSLEEVE, t=0.5)
    out = [P(d, lin("gRS", 40, 520, 200, 650, [(0, "#3a2914"), (0.45, "#5e4520"), (0.75, "#76592c"),
                                                     (1, "#523b1b")]))]
    A1, B1 = [(148, 466), (100, 488), (60, 515), (24, 548), (-10, 586)], [(166, 502), (158, 546), (134, 588),
                                                                         (94, 620), (40, 646)]
    A2, B2 = [(-10, 606), (40, 620), (90, 626), (140, 625), (176, 624), (196, 628)], [(-10, 708), (40, 710),
                                                                                    (90, 702), (140, 690),
                                                                                    (176, 676), (196, 664)]
    for k, (A, B) in enumerate(((A1, B1), (A2, B2))):
        out += sleeve_texture(d, f"cRS{k}", A, B, 34, rng, "#a8843f", "#241809", 1.0, (40, 85), 8, (0, 195),
                              (470, 705))
    out.append(G([E(150, 476, 34, 22, "#140d05", 0.6, 10), E(30, 560, 40, 60, "#1e1509", 0.45, 16),
                  E(120, 632, 70, 11, "#c49c56", 0.32, 8), E(80, 704, 90, 14, "#1e1509", 0.5, 10),
                  E(186, 600, 14, 40, "#1e1509", 0.45, 8), E(70, 600, 50, 30, "#a07a3a", 0.18, 14)],
                 clip("cRSs", d)))
    add(G(out, 'id="rsleeve"'))


def right_hand():
    """Sitter's right hand lying over her left wrist, fingers towards the viewer's right."""
    to = frame((193, 644), 13)
    back = [(-8, 0), (-2, -19), (25, -22), (50, -27), (70, -30), (78, -18), (80, 0), (78, 18), (72, 31), (50, 28),
            (25, 23), (-2, 18)]
    fingers = [([(66, -22), (88, -23), (108, -23), (125, -20.5), (138, -15)], 15, 10.5),
               ([(70, -7), (95, -7), (118, -6), (136, -3), (149, 2.5)], 15.5, 11),
               ([(68, 8.5), (90, 9.5), (111, 11), (127, 14.5), (138, 19.5)], 14.5, 10),
               ([(63, 23), (80, 25), (96, 28), (108, 31.5), (118, 35.5)], 12.5, 8.8)]
    cols = ("#ecc68a", "#cc9c5e", "#8e6034", "#6a4422", "#f6dca8")

    def e(lp, rx, ry, col, op, sd):
        p = to(lp)
        return E(p[0], p[1], rx, ry, col, op, sd, rot=13)
    extra = [e((34, -6), 30, 13, "#f6dca8", 0.5, 6), e((42, 18), 32, 8, "#6e4826", 0.32, 5),
             e((2, 0), 6, 18, "#5e3c1c", 0.4, 4)]
    for v in (-14, -4, 6):
        a, b = to((14, v * 0.7)), to((66, v * 1.4))
        extra.append(P(poly([a, b], False), stroke="#f6dca8", sw=1.6, op=0.16, sd=1.4))
    add(hand3(to, back, fingers, "gRH", cols, extra))


# ---------------------------------------------------------------- finishing

def cuff():
    """The sleeve end laid over the right wrist, plus its lit rim."""
    add(G(['<use xlink:href="#rsleeve"/>'], clip("cWrist", poly([(168, 606), (199, 606), (201, 676), (168, 680)]))))
    add(P(smooth([(189, 618), (195, 633), (196.5, 648), (192.5, 662)], closed=False), stroke="#caa45c", sw=1.1,
          op=0.45, sd=0.7))
    add(P(smooth([(196, 620), (201, 636), (201, 652), (196, 664)], closed=False), stroke="#1e1408", sw=2.4, op=0.35,
          sd=1.6))


def finishing():
    def table(nv, at):
        vals = ["0"] * nv
        vals[at] = "1"
        return " ".join(vals)
    DEFS.append(
        '<filter id="crack" filterUnits="userSpaceOnUse" x="0" y="0" width="530" height="770" '
        'color-interpolation-filters="sRGB">'
        '<feTurbulence type="fractalNoise" baseFrequency="0.1" numOctaves="2" seed="8" result="n1"/>'
        '<feColorMatrix in="n1" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0" result="a1"/>'
        f'<feComponentTransfer in="a1" result="l1"><feFuncA type="table" tableValues="{table(121, 60)}"/>'
        '</feComponentTransfer>'
        '<feTurbulence type="fractalNoise" baseFrequency="0.16" numOctaves="1" seed="29" result="n2"/>'
        '<feColorMatrix in="n2" type="matrix" values="0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0" result="a2"/>'
        f'<feComponentTransfer in="a2" result="l2"><feFuncA type="table" tableValues="{table(121, 60)}"/>'
        '</feComponentTransfer>'
        '<feComposite in="l1" in2="l2" operator="arithmetic" k2="1" k3="0.6" result="lines"/>'
        '<feFlood flood-color="#1c1208"/><feComposite in2="lines" operator="in"/></filter>')
    DEFS.append(
        '<filter id="grain" filterUnits="userSpaceOnUse" x="0" y="0" width="530" height="770">'
        '<feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" seed="3"/>'
        '<feColorMatrix type="matrix" values="0 0 0 0 0.11 0 0 0 0 0.08 0 0 0 0 0.03 0 0 0 -2.2 1.25"/>'
        '</filter>')
    add(f'<rect width="{W}" height="{H}" filter="url(#grain)" opacity="0.06"/>')
    add(f'<rect width="{W}" height="{H}" filter="url(#crack)" opacity="0.09"/>')
    add(f'<rect width="{W}" height="{H}" fill="#7a6220" opacity="0.07"/>')
    v = rad("gVig", 265, 330, 520, [(0, "#000", 0), (0.55, "#000", 0), (1, "#140e05", 0.55)])
    add(f'<rect width="{W}" height="{H}" fill="{v}"/>')


def build():
    sky()
    landscape()
    parapet()
    dress()
    armrest()
    left_hand()
    sleeves_back()
    right_sleeve()
    mantle()
    guarnello()
    skin_neck()
    embroidery()
    face()
    hair()
    veil()
    right_hand()
    cuff()
    finishing()
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            '<title>Mona Lisa (after Leonardo da Vinci)</title>'
            "<desc>A hand-composed vector rendition of Leonardo da Vinci's Mona Lisa "
            "(c. 1503-1519, Musee du Louvre), drawn from memory.</desc>")
    defs = ("<defs>" + "".join(FILTERS.values()) + "".join(DEFS)
            + f'<clipPath id="panel"><rect width="{W}" height="{H}"/></clipPath></defs>')
    return head + defs + '<g clip-path="url(#panel)">' + "".join(BODY) + "</g></svg>"


if __name__ == "__main__":
    svg = build()
    out = sys.argv[1] if len(sys.argv) > 1 else "mona-lisa.svg"
    with open(out, "w") as fh:
        fh.write(svg)
    print(out, len(svg))
