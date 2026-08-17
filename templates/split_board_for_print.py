#!/usr/bin/env python3
"""Split a rift board down its printed seam into two US Letter pages to tape
together.

build_rift_board.py composes every board in a base 1536x1024 space with
SEAM = W // 2, then scales by cfg["scale"], so the true seam of a finished board
is always at exactly half its pixel width. Do NOT try to detect the dashed line
in the artwork: it is drawn at 80 alpha and the light token path reads brighter
than it does, which finds a seam ~48px off true.

Output, next to the source image:
  <name>_page1_left.png / _page2_right.png   the raw halves
  <name>_print.pdf                            2 pages, Letter portrait, ready to print

Printing and taping:
  1. Print the PDF at 100% / "actual size". Do NOT use "fit to page", which
     rescales the two sheets differently and leaves the halves mismatched.
  2. Each page carries a solid CUT LINE down its inner edge with scissor marks.
     Trim both sheets on that line.
  3. Butt the cut edges together and tape on the back. The path crosses the seam
     through a deliberate gap, so nothing important lands on the join.

Usage:
  python templates/split_board_for_print.py assets/session_08/underroot_board.png
"""
import os
import sys

from PIL import Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas

MARGIN = 0.14 * inch      # keeps clear of typical unprintable edges
CUT_INSET = 0.10 * inch   # how far the cut line sits outside the artwork


def split(src):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    seam = w // 2
    left = im.crop((0, 0, seam, h))
    right = im.crop((seam, 0, w, h))

    base = os.path.splitext(src)[0]
    lp, rp = base + "_page1_left.png", base + "_page2_right.png"
    left.save(lp)
    right.save(rp)
    print("seam at x=%d | halves %dx%d" % (seam, *left.size))
    return left, right, lp, rp, base


def page(c, half, cut_side):
    """Draw one half centred on a Letter portrait page.

    cut_side is 'right' for the left-hand sheet and 'left' for the right-hand
    sheet: that is the edge the DM trims and tapes.
    """
    pw, ph = letter
    avail_w, avail_h = pw - 2 * MARGIN, ph - 2 * MARGIN
    iw, ih = half.size
    scale = min(avail_w / iw, avail_h / ih)
    dw, dh = iw * scale, ih * scale
    x, y = (pw - dw) / 2, (ph - dh) / 2

    c.drawImage(ImageReader(half), x, y, dw, dh)

    # cut line just outside the artwork on the joining edge
    cx = x + dw + CUT_INSET if cut_side == "right" else x - CUT_INSET
    c.setDash(6, 4)
    c.setLineWidth(0.7)
    c.setStrokeColorRGB(0.45, 0.45, 0.45)
    c.line(cx, y - 6, cx, y + dh + 6)
    c.setDash()

    # scissor marks so it is obvious which edge to trim
    c.setFont("Helvetica", 9)
    c.setFillColorRGB(0.35, 0.35, 0.35)
    for yy in (y + dh + 12, y - 16):
        c.drawCentredString(cx, yy, "cut")
    c.showPage()


def build_pdf(left, right, base):
    out = base + "_print.pdf"
    c = canvas.Canvas(out, pagesize=letter)
    page(c, left, "right")
    page(c, right, "left")
    c.save()
    print("wrote", out)
    return out


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else os.path.join(
        "assets", "session_08", "underroot_board.png")
    left, right, lp, rp, base = split(src)
    build_pdf(left, right, base)
    print("wrote", lp)
    print("wrote", rp)
