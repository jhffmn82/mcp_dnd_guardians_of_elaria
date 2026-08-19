# build_rift_board.py
# Generates a Mario-Party-style rift game board: a painterly plane backdrop
# dimmed to a board, overlaid with a winding token-path of colored spaces,
# illustrated cut-out location medallions, a title, and a legend. The board is
# sized to print across TWO US Letter sheets side by side (a vertical seam down
# the middle); the path crosses that seam only through a clean gap, and the
# generator SELF-CHECKS (no overlapping spaces, space-to-seam clearance, no
# location bumping the title) and refuses to render if a check fails.
#
# Resolution: all geometry is computed in a base 1536x1024 space, then drawn on
# a canvas scaled by cfg["scale"] (default 3 -> 4608x3072, ~270 dpi across two
# Letter sheets) so the path/circles/text stay crisp. The painterly backdrop is
# Lanczos-upscaled to match; its fine detail is still limited by the source art,
# so for the final print regenerate the backdrop at higher resolution first.
#
# Reskin for the Water/Fire/Air boards by copying the UNDERROOT config: swap the
# backdrop, the four location medallions (position + which region of the art to
# crop for each), and the winding waypoints. Everything else is shared.
#
# Build:  python templates/build_rift_board.py  ->  assets/session_08/underroot_board.png
import os, math
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
        return ImageFont.truetype(FONTS[0] if bold else FONTS[1], int(sz))
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
    GAP, HG, MIN = SR + 10, SR + 14, 2 * SR + 4
    slots = cfg["slots"]
    TITLE = (34, 30, 500, 120)

    # --- title clearance check (base coords) ---
    ttx, tty = cfg.get("title_pos", (34, 30))
    TBOX = (ttx, tty, ttx + 466, tty + 90)
    for s in slots:
        cx, cy = s["pos"]; r = s["r"]
        if cx - r < TBOX[2] and cy - r - 22 < TBOX[3] and cx + r > TBOX[0] and cy + r > TBOX[1]:
            raise SystemExit(f"location '{s['label']}' overlaps the title box; move it")

    # --- geometry in base space ---
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

    def subsplit(u, v):
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
        B1 = slotpos[b] - slots[b]["r"] - GAP
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

    md = min(abs(x - SEAM) for x, y in dots)
    mind = min(math.hypot(dots[i][0] - dots[j][0], dots[i][1] - dots[j][1])
               for i in range(len(dots)) for j in range(i + 1, len(dots)))
    if md - SR < 10:
        raise SystemExit(f"a space is only {md - SR:.0f}px from the cut; widen the seam gap")
    if mind < 2 * SR:
        raise SystemExit(f"two spaces overlap ({mind:.0f}px apart); loosen spacing")

    # --- space types: ~half events; a red just left of the cut; two wilds ---
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

    # --- label placement (base coords, collision-checked) ---
    LEG = (1284, 30, W - 28, 206); placed = []
    def _bc(bx, by, bx2, by2, cx, cy, rr):
        nx = max(bx, min(cx, bx2)); ny = max(by, min(cy, by2)); return (nx - cx) ** 2 + (ny - cy) ** 2 < rr * rr
    def _bb(a, b):
        return not (a[2] < b[0] or b[2] < a[0] or a[3] < b[1] or b[3] < a[1])
    mdraw = ImageDraw.Draw(Image.new("RGBA", (W, H)))
    labelbox = {}
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
        s = slots[j]
        tw = mdraw.textlength(s["label"], font=_font(23))
        labelbox[j] = place(s["pos"][0], s["pos"][1], s["r"], tw)

    # ===================== HIGH-RES DRAW =====================
    S = cfg.get("scale", 3)
    def q(v): return v * S
    HW, HH = W * S, H * S
    board = ImageEnhance.Brightness(plate.resize((HW, HH), Image.LANCZOS)).enhance(cfg.get("dim", 0.56))
    ov = Image.new("RGBA", (HW, HH), (0, 0, 0, 0)); d = ImageDraw.Draw(ov)

    for (x1, y1), (x2, y2) in zip(spine, spine[1:]):
        d.line([q(x1), q(y1), q(x2), q(y2)], fill=(236, 228, 203, 186), width=int(RIB * S))
    for x, y in spine[::4]:
        d.ellipse([q(x) - RIB * S / 2, q(y) - RIB * S / 2, q(x) + RIB * S / 2, q(y) + RIB * S / 2], fill=(236, 228, 203, 186))
    for yy in range(120, H - 40, 26):
        d.line([q(SEAM), q(yy), q(SEAM), q(yy + 13)], fill=(255, 255, 255, 80), width=int(2 * S))
    for (x, y), t in zip(dots, dtypes):
        cx, cy, rr = q(x), q(y), SR * S
        d.ellipse([cx - rr + 2 * S, cy - rr + 3 * S, cx + rr + 2 * S, cy + rr + 3 * S], fill=(0, 0, 0, 90))
        d.ellipse([cx - rr, cy - rr, cx + rr, cy + rr], fill=PALETTE[t], outline=(244, 238, 224, 245), width=int(4 * S))
        if t == "wild":
            f = _font(33 * S); w = d.textlength("!", font=f); d.text((cx - w / 2, cy - 20 * S), "!", font=f, fill=(248, 244, 235, 255))

    for j in order:
        s = slots[j]; cx, cy = s["pos"]; r = s["r"]; ring = tuple(s["ring"]) + (255,)
        sr = int(r * 1.25); sx, sy = s["src"]
        d.ellipse([q(cx) - r * S - 3 * S, q(cy) - r * S + 5 * S, q(cx) + r * S + 6 * S, q(cy) + r * S + 10 * S], fill=(0, 0, 0, 75))
        reg = plate.crop((max(0, sx - sr), max(0, sy - sr), min(W, sx + sr), min(H, sy + sr))).resize((int(2 * r * S), int(2 * r * S)), Image.LANCZOS)
        m = Image.new("L", reg.size, 0); ImageDraw.Draw(m).ellipse([0, 0, reg.size[0], reg.size[1]], fill=255)
        board.paste(reg, (int(q(cx) - r * S), int(q(cy) - r * S)), m)
        d.ellipse([q(cx) - r * S - 3 * S, q(cy) - r * S - 3 * S, q(cx) + r * S + 3 * S, q(cy) + r * S + 3 * S], outline=(12, 10, 16, 255), width=int(3 * S))
        d.ellipse([q(cx) - r * S, q(cy) - r * S, q(cx) + r * S, q(cy) + r * S], outline=ring, width=int(12 * S))
        if s["num"]:
            bx, by = q(cx), q(cy) - r * S
            d.ellipse([bx - 21 * S, by - 21 * S, bx + 21 * S, by + 21 * S], fill=ring, outline=(255, 255, 255, 255), width=int(3 * S))
            fn = _font(26 * S); w = d.textlength(s["num"], font=fn); d.text((bx - w / 2, by - 17 * S), s["num"], font=fn, fill=(20, 16, 10, 255))
        bx, by, bx2, by2 = labelbox[j]; f = _font(23 * S)
        d.rounded_rectangle([q(bx), q(by), q(bx2), q(by2)], radius=int(9 * S), fill=(16, 14, 22, 220))
        d.text((q(bx) + 12 * S, q(by) + 6 * S), s["label"], font=f, fill=(246, 240, 230, 255))

    tx, ty = cfg.get("title_pos", (34, 30))
    d.rounded_rectangle([q(tx), q(ty), q(tx + 466), q(ty + 90)], radius=int(12 * S), fill=(16, 14, 22, 210))
    d.text((q(tx + 18), q(ty + 12)), cfg["title"], font=_font(40 * S), fill=(246, 240, 230, 255))
    d.text((q(tx + 20), q(ty + 62)), cfg["subtitle"], font=_font(18 * S, False), fill=(212, 206, 226, 255))
    lx, ly = 1300, 44
    d.rounded_rectangle([q(lx - 16), q(ly - 14), q(W - 28), q(ly + 14 + 5 * 32)], radius=int(12 * S), fill=(16, 14, 22, 215))
    for i, (k, name) in enumerate([("trav", "Move"), ("enc", "Encounter"), ("boon", "Boon"), ("haz", "Hazard"), ("wild", "Wild !")]):
        yy = ly + i * 32
        d.ellipse([q(lx), q(yy), q(lx + 24), q(yy + 24)], fill=PALETTE[k], outline=(244, 238, 224, 235), width=int(2 * S))
        d.text((q(lx + 34), q(yy + 2)), name, font=_font(19 * S, False), fill=(242, 238, 230, 255))

    os.makedirs(os.path.dirname(cfg["out"]), exist_ok=True)
    Image.alpha_composite(board, ov).convert("RGB").save(cfg["out"], "PNG")
    print(f"built {cfg['out']} at {HW}x{HH} | {len(dots)} spaces, seam clearance {md - SR:.0f}px, min spacing {mind:.0f}px")


# --- Session 9: The Undersea (Water rift). Geometry inherited from the S8 board;
# the backdrop is the S8 board repainted as Unda, so the route and seam carry over. ---
UNDA = {
    "backdrop": "assets/world/s9_unda_board.png",
    "out": "assets/session_09/unda_board.png",
    "title": "The Undersea",
    "subtitle": "Water Rift  .  Session 9  .  reach the Guardian",
    "scale": 3,
    "space_r": 31, "loc_r": 112, "boss_r": 126, "ribbon_w": 92, "step": 68, "dim": 0.56,
    "wild_fracs": (0.25, 0.65),
    "title_pos": (34, 900),
    "waypoints": [
        (260, 214), (426, 154), (592, 160), (800, 168), (962, 205), (1124, 268),
        (1230, 360), (1265, 500), (1200, 630), (1060, 715), (900, 745), (720, 705),
        (640, 615), (668, 515), (800, 468), (940, 470),
    ],
    "slots": [
        {"pos": (260, 214), "r": 64,  "ring": (70, 120, 170),  "label": "The Rift Gate",       "num": None, "src": (150, 140)},
        {"pos": (592, 160), "r": 112, "ring": (214, 170, 72),  "label": "The Brightshoal",     "num": "1",  "src": (420, 200)},
        {"pos": (1265, 500), "r": 112, "ring": (214, 170, 72), "label": "The Kelp Cathedral",  "num": "2",  "src": (1180, 180)},
        {"pos": (1060, 715), "r": 112, "ring": (214, 170, 72), "label": "The Blackwater Seam", "num": "3",  "src": (1040, 700)},
        {"pos": (940, 470), "r": 126, "ring": (214, 66, 74),   "label": "The Guardian's Trench", "num": "4", "src": (870, 480)},
    ],
}

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    build_board(UNDA)
