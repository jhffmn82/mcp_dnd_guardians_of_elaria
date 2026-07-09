# ws_probe.py -- per-page whitespace + content probe for a rendered PDF.
# Usage: python templates/ws_probe.py <pdf> [minpct]
# For every page it prints: page number, trailing-whitespace %, blank flag,
# the topmost heading text, the bottommost text line, image count, and the
# largest image's width/height in inches. This lets a reader correlate a
# gappy page back to the block that ends it (and the block pushed off it).
import sys, fitz
TOP, BOT = 54.0, 727.0  # usable content band, points
PPI = 72.0


def probe(pdf, minpct=0.0):
    d = fitz.open(pdf)
    rows = []
    for i, page in enumerate(d):
        maxy = TOP
        imgs = []
        for img in page.get_images(full=True):
            for r in page.get_image_rects(img[0]):
                maxy = max(maxy, r.y1)
                imgs.append((round((r.x1 - r.x0) / PPI, 2), round((r.y1 - r.y0) / PPI, 2), round(r.y1, 1)))
        blocks = [b for b in page.get_text("blocks") if b[4].strip() and b[1] < BOT - 8]
        for b in blocks:
            maxy = max(maxy, b[3])
        txt = page.get_text().strip()
        pct = (BOT - min(maxy, BOT)) / (BOT - TOP) * 100
        blank = len(txt) < 15
        blocks.sort(key=lambda b: b[1])
        top = blocks[0][4].strip().splitlines()[0][:60] if blocks else "(no text)"
        bot = blocks[-1][4].strip().splitlines()[-1][:60] if blocks else "(no text)"
        biggest = max(imgs, key=lambda t: t[0] * t[1]) if imgs else None
        rows.append((i + 1, pct, blank, len(imgs), biggest, top, bot))
    d.close()
    print(f"== {pdf} :: {len(rows)} pages ==")
    for pno, pct, blank, ni, big, top, bot in rows:
        if not blank and pct < minpct:
            continue
        tag = "BLANK" if blank else f"{pct:4.0f}%"
        bigs = f"img {ni}x biggest={big[0]}x{big[1]}in(bot y{big[2]})" if big else "no-img"
        line = f"  p{pno:>3} ws={tag}  {bigs}\n        top: {top}\n        bot: {bot}"
        print(line.encode("ascii", "replace").decode())


if __name__ == "__main__":
    probe(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else 0.0)
