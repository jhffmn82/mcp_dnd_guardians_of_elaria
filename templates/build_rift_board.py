# build_rift_board.py
# Generates a Mario-Party-style rift game board: a painterly plane backdrop
# dimmed to a board, overlaid with a winding token-path of colored spaces,
# illustrated cut-out location medallions, a title, and a legend. The board is
# sized to print across TWO US Letter sheets side by side (a vertical seam down
# the middle); the path crosses that seam only through a clean gap, and the
# generator SELF-CHECKS (no overlapping spaces, space-to-seam clearance, no
# location bumping the title) and refuses to render if a check fails.
#
# Reskin for the Water/Fire/Air boards by copying the UNDERROOT config: swap the
# backdrop, the four location medallions (position + which region of the art to
# crop for each), and the winding waypoints. Everything else is shared.
#
# Standards (locked with the Session 8 Underroot board, DM-approved 2026-07-10):
#   thick token-path (~92px); token-sized round spaces (r~31); cut-out location
#   circles ON TOP of the path (r~112, ~126 for the boss); muted jewel palette
#   (slate Move, garnet Encounter, moss Boon, ochre Hazard, amethyst Wild);
#   ~half the spaces are events; roughly even spacing with a clean gap on the
#   cut; labels auto-placed on an open side; legend top-right; no essence bar.
#
# Build:  python templates/build_rift_board.py  ->  assets/session_08/underroot_board.png
import os, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

PALETTE = {  # muted jewel/earth tones, not primaries
    "trav": (96, 132, 156, 255),   # slate blue  -> Move
    "enc":  (158, 58, 54, 255),    # garnet      -> Encounter
    "boon": (66, 128, 86, 255),    # moss        -> Boon
    "haz":  (190, 134, 64, 255),   # burnt ochre -> Hazard
    "wild": (122, 88, 162, 255),   # amethyst    -> Wild
}
FONTS = ("C:/Windows/Fonts/arialbd.ttf", "C:/Windows/Fonts/arial.ttf")


def _font(sz, bold=True):
    try:
        return ImageFont.truetype(FONTS[0] if bold else FONTS[1], sz)
    except Exception:
        return ImageFont.load_default()


def _catmull(pts, per=26):
    P = [pts[0]] + list(pts) + [pts[-1]]
    out = []
    for i in range(1, len(P) - 2):
        p0, p1, p2, p3 = P[i - 1], P[i], P[i + 1], P[i + 2]
        for k in range(per):
            t = k / per; t2 = t * t; t3 = t2 * t
            def c(a, b, cc, dd):
                return 0.5 * (2 * b + (-a + cc) * t + (2 * a - 5 * b + 4 * cc - dd) * t2 + (-a + 3 * b - 3 * cc + dd) * t3)
            out.append((c(p0[0], p1[0], p2[0], p3[0]), c(p0[1], p1[1], p2[1], p3[1])))
    out.append(pts[-1])
    return out


def build_board(cfg):
    plate = Image.open(cfg["backdrop"]).convert("RGBA")
    W, H = plate.size
    SEAM = W // 2
    SR, LR, BR = cfg["space_r"], cfg["loc_r"], cfg["boss_r"]
    RIB, STEP = cfg["ribbon_w"], cfg["step"]
    GAP, HG, MIN = SR + 10, SR + 14, 2 * SR + 4   # medallion gap, seam half-gap, min space spacing
    slots = cfg["slots"]
    TITLE = (34, 30, 500, 120)

    board = ImageEnhance.Brightness(plate).enhance(cfg.get("dim", 0.56))
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)

    # location circles/badges must not bump the title
    for s in slots:
        cx, cy = s["pos"]; r = s["r"]
        if cx - r < TITLE[2] and cy - r - 22 < TITLE[3] and cx + r > TITLE[0] and cy + r > TITLE[1]:
            raise SystemExit(f"location '{s['label']}' overlaps the title box; move it")

    spine = _catmull(cfg["waypoints"])
    cum = [0.0]
    for a, b in zip(spine, spine[1:]):
        cum.append(cum[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))

    def pt_at(ap):
        ap = max(0, min(cum[-1], ap))
        for i in range(1, len(cum)):
            if cum[i] >= ap:
                seg = cum[i] - cum[i - 1] or 1; t = (ap - cum[i - 1]) / seg
                return (spine[i - 1][0] + (spine[i][0] - spine[i - 1][0]) * t,
                        spine[i - 1][1] + (spine[i][1] - spine[i - 1][1]) * t)
        return spine[-1]

    crossings = []
    for i in range(1, len(spine)):
        a, b = spine[i - 1][0], spine[i][0]
        if (a - SEAM) * (b - SEAM) < 0 and a != b:
            crossings.append(cum[i - 1] + ((SEAM - a) / (b - a)) * (cum[i] - cum[i - 1]))

    slotpos = {j: cum[min(range(len(spine)), key=lambda k: (spine[k][0] - slots[j]["pos"][0]) ** 2 + (spine[k][1] - slots[j]["pos"][1]) ** 2)]
               for j in range(len(slots))}
    order = sorted(range(len(slots)), key=lambda j: slotpos[j])

    def subsplit(u, v):  # remove a clean zone around every seam crossing
        segs = [(u, v)]
        for C in crossings:
            fa, fb = C - HG, C + HG; ns = []
            for a, b in segs:
                if fb <= a or fa >= b:
                    ns.append((a, b))
                else:
                    if a < fa: ns.append((a, fa))
                    if fb < b: ns.append((fb, b))
            segs = ns
        return [(a, b) for a, b in segs if b - a > 10]

    dots = []
    for a, b in zip(order, order[1:]):
        A0 = slotpos[a] + slots[a]["r"] + GAP
        B1 = slotpos[b] - slots[b]["r"] + (-GAP)
        if B1 <= A0:
            continue
        for u, v in subsplit(A0, B1):
            L = v - u
            if L < MIN:
                dots.append(pt_at((u + v) / 2)); continue
            K = max(1, round(L / STEP))
            while K > 1 and L / K < MIN:
                K -= 1
            for i in range(K + 1):
                dots.append(pt_at(u + L * i / K))

    # --- self-checks ---
    md = min(abs(x - SEAM) for x, y in dots)
    mind = min(math.hypot(dots[i][0] - dots[j][0], dots[i][1] - dots[j][1])
               for i in range(len(dots)) for j in range(i + 1, len(dots)))
    if md - SR < 10:
        raise SystemExit(f"a space is only {md - SR:.0f}px from the cut; widen the seam gap")
    if mind < 2 * SR:
        raise SystemExit(f"two spaces overlap ({mind:.0f}px apart); loosen spacing")

    # --- space types: ~half events, mixed; a red just left of the cut; two wilds ---
    ecyc = ["enc", "boon", "haz", "enc", "boon", "enc", "haz", "enc", "boon", "haz", "enc", "boon"]
    dtypes = [(ecyc[(i // 2) % len(ecyc)] if i % 2 == 1 else "trav") for i in range(len(dots))]
    left_cut = [(abs(x - SEAM), idx) for idx, (x, y) in enumerate(dots) if x < SEAM and 150 < y < 430]
    if left_cut:
        dtypes[min(left_cut)[1]] = "enc"
    travs = [i for i, t in enumerate(dtypes) if t == "trav" and abs(dots[i][0] - SEAM) > 110]
    for frac in cfg.get("wild_fracs", (0.30, 0.72)):
        if not travs: break
        tgt = int(len(dots) * frac); best = min(travs, key=lambda i: abs(i - tgt))
        dtypes[best] = "wild"; travs.remove(best)

    # --- draw: ribbon, seam, spaces, medallions, title, legend ---
    for (x1, y1), (x2, y2) in zip(spine, spine[1:]):
        d.line([x1, y1, x2, y2], fill=(236, 228, 203, 186), width=RIB)
    for x, y in spine[::4]:
        d.ellipse([x - RIB // 2, y - RIB // 2, x + RIB // 2, y + RIB // 2], fill=(236, 228, 203, 186))
    for yy in range(120, H - 40, 26):
        d.line([SEAM, yy, SEAM, yy + 13], fill=(255, 255, 255, 80), width=2)
    for (x, y), t in zip(dots, dtypes):
        d.ellipse([x - SR + 2, y - SR + 3, x + SR + 2, y + SR + 3], fill=(0, 0, 0, 90))
        d.ellipse([x - SR, y - SR, x + SR, y + SR], fill=PALETTE[t], outline=(244, 238, 224, 245), width=4)
        if t == "wild":
            d.text((x - 6, y - 20), "!", font=_font(33), fill=(248, 244, 235, 255))

    LEG = (1284, 30, W - 28, 206); placed = []
    def _bc(bx, by, bx2, by2, cx, cy, rr):
        nx = max(bx, min(cx, bx2)); ny = max(by, min(cy, by2)); return (nx - cx) ** 2 + (ny - cy) ** 2 < rr * rr
    def _bb(a, b):
        return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])
    def place(cx, cy, r, tw, ph=34):
        for bx, by in [(cx - tw / 2 - 12, cy + r + 12), (cx - tw / 2 - 12, cy - r - 46),
                       (cx - r - 16 - (tw + 24), cy - ph / 2), (cx + r + 16, cy - ph / 2)]:
            box = (bx, by, bx + tw + 24, by + ph)
            if bx < 12 or box[2] > W - 12 or by < 126 or box[3] > H - 12: continue
            if bx < SEAM < box[2]: continue
            if _bb(box, TITLE) or _bb(box, LEG): continue
            if any(_bc(*box, dx, dy, SR + 4) for dx, dy in dots): continue
            if any(_bc(*box, s["pos"][0], s["pos"][1], s["r"] + 4) for s in slots): continue
            if any(_bb(box, pb) for pb in placed): continue
            placed.append(box); return box
        bx, by = cx - tw / 2 - 12, cy - r - 46; box = (bx, by, bx + tw + 24, by + ph); placed.append(box); return box

    for j in order:
        s = slots[j]; cx, cy = s["pos"]; r = s["r"]; ring = s["ring"] + (255,)
        sr = int(r * 1.25); sx, sy = s["src"]
        d.ellipse([cx - r - 3, cy - r + 5, cx + r + 6, cy + r + 10], fill=(0, 0, 0, 75))  # drop shadow
        reg = plate.crop((max(0, sx - sr), max(0, sy - sr), min(W, sx + sr), min(H, sy + sr))).resize((2 * r, 2 * r))
        m = Image.new("L", (2 * r, 2 * r), 0); ImageDraw.Draw(m).ellipse([0, 0, 2 * r, 2 * r], fill=255)
        board.paste(reg, (cx - r, cy - r), m)
        d.ellipse([cx - r - 3, cy - r - 3, cx + r + 3, cy + r + 3], outline=(12, 10, 16, 255), width=3)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=ring, width=12)
        if s["num"]:
            d.ellipse([cx - 21, cy - r - 21, cx + 21, cy - r + 21], fill=ring, outline=(255, 255, 255, 255), width=3)
            w = d.textlength(s["num"], font=_font(26)); d.text((cx - w / 2, cy - r - 17), s["num"], font=_font(26), fill=(20, 16, 10, 255))
        f = _font(23); tw = d.textlength(s["label"], font=f)
        bx, by, bx2, by2 = place(cx, cy, r, tw)
        d.rounded_rectangle([bx, by, bx2, by2], radius=9, fill=(16, 14, 22, 220))
        d.text((bx + 12, by + 6), s["label"], font=f, fill=(246, 240, 230, 255))

    d.rounded_rectangle([34, 30, 500, 120], radius=12, fill=(16, 14, 22, 210))
    d.text((52, 42), cfg["title"], font=_font(40), fill=(246, 240, 230, 255))
    d.text((54, 92), cfg["subtitle"], font=_font(18, False), fill=(212, 206, 226, 255))
    lx, ly = 1300, 44
    for i, (k, name) in enumerate([("trav", "Move"), ("enc", "Encounter"), ("boon", "Boon"), ("haz", "Hazard"), ("wild", "Wild")]):
        if i == 0:
            d.rounded_rectangle([lx - 16, ly - 14, W - 28, ly + 14 + 5 * 32], radius=12, fill=(16, 14, 22, 215))
        yy = ly + i * 32
        d.ellipse([lx, yy, lx + 24, yy + 24], fill=PALETTE[k], outline=(244, 238, 224, 235), width=2)
        d.text((lx + 34, yy + 2), name, font=_font(19, False), fill=(242, 238, 230, 255))

    os.makedirs(os.path.dirname(cfg["out"]), exist_ok=True)
    Image.alpha_composite(board, ov).convert("RGB").save(cfg["out"], "PNG")
    print(f"built {cfg['out']} | {len(dots)} spaces, seam clearance {md - SR:.0f}px, min spacing {mind:.0f}px")


# --- Session 8: The Underroot (Earth rift). Copy and edit this for other planes. ---
UNDERROOT = {
    "backdrop": "assets/world/s8_underroot_board.png",
    "out": "assets/session_08/underroot_board.png",
    "title": "The Underroot",
    "subtitle": "Earth Rift  .  Session 8  .  reach Groudon",
    "space_r": 31, "loc_r": 112, "boss_r": 126, "ribbon_w": 92, "step": 68, "dim": 0.56,
    "wild_fracs": (0.30, 0.72),
    "waypoints": [
        (636, 902), (540, 930), (448, 910), (360, 852), (316, 760),
        (300, 600), (250, 470), (320, 342), (440, 292),
        (560, 262), (700, 232), (842, 258), (980, 228), (1085, 286),
        (1185, 352), (1252, 478), (1188, 584), (1268, 672), (1315, 780), (1402, 858),
    ],
    "slots": [
        {"pos": (636, 902), "r": 64,  "ring": (70, 120, 170),  "label": "The Rift Gate",     "num": None, "src": (250, 600)},
        {"pos": (300, 600), "r": 112, "ring": (214, 170, 72),  "label": "Mosslight Landing", "num": "1",  "src": (300, 560)},
        {"pos": (560, 262), "r": 112, "ring": (214, 170, 72),  "label": "Chime Reef",        "num": "2",  "src": (520, 300)},
        {"pos": (1185, 352), "r": 112, "ring": (214, 170, 72), "label": "Glassed Gallery",   "num": "3",  "src": (1050, 360)},
        {"pos": (1402, 858), "r": 126, "ring": (214, 66, 74),  "label": "Groudon's Hollow",  "num": "4",  "src": (1370, 430)},
    ],
}

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    build_board(UNDERROOT)
