#!/usr/bin/env python3
"""Render campaign markdown drafts into one readable PDF.

The finished book is built with book_style's block system, which has no table
kind and expects hand-authored Python. Working drafts live as markdown, so this
renders them directly: headings, paragraphs, bullets, tables, read-aloud boxes,
DM notes and images, in the campaign's colours.

This is for REVIEW, not for the keepsake. When Session 8 is played and locked,
it gets hand-authored into a build_session_08.py like every other session.

Usage:
  python templates/render_draft_pdf.py OUT.pdf FILE.md [FILE.md ...]
"""
import html
import os
import re
import sys

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (Image, PageBreak, Paragraph, SimpleDocTemplate,
                                Spacer, Table, TableStyle)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INK = colors.HexColor("#2B2622")
GREY = colors.HexColor("#6F6046")
GOLD = colors.HexColor("#8A6D3B")
RULE = colors.HexColor("#D9C9A8")
READ_BG = colors.HexColor("#FBF4E4")
DM_BG = colors.HexColor("#EFE8F5")
DM_EDGE = colors.HexColor("#8B79A8")

_ss = getSampleStyleSheet()


def S(name, **kw):
    # callers may pass their own parent; only default it when they do not
    kw.setdefault("parent", _ss["Normal"])
    return ParagraphStyle(name, **kw)


H1 = S("h1", fontName="Times-Bold", fontSize=19, textColor=GOLD, leading=23,
       spaceBefore=16, spaceAfter=7)
H2 = S("h2", fontName="Times-Bold", fontSize=14, textColor=GOLD, leading=17,
       spaceBefore=13, spaceAfter=5)
H3 = S("h3", fontName="Times-Bold", fontSize=11.5, textColor=INK, leading=14,
       spaceBefore=10, spaceAfter=3)
BODY = S("body", fontName="Times-Roman", fontSize=10, textColor=INK, leading=13.4,
         spaceAfter=5)
BULLET = S("bullet", parent=BODY, leftIndent=14, bulletIndent=4, spaceAfter=3)
READ = S("read", fontName="Times-Italic", fontSize=10, textColor=INK, leading=13.6)
CELL = S("cell", fontName="Times-Roman", fontSize=8.6, textColor=INK, leading=11)
CELLH = S("cellh", fontName="Times-Bold", fontSize=8.6, textColor=colors.white, leading=11)
TITLE = S("title", fontName="Times-Bold", fontSize=26, textColor=GOLD, leading=30,
          alignment=TA_CENTER, spaceAfter=6)
SUB = S("sub", fontName="Times-Italic", fontSize=12, textColor=GREY, leading=15,
        alignment=TA_CENTER, spaceAfter=20)


def inline(t):
    """Markdown inline formatting to ReportLab markup."""
    t = html.escape(t)
    t = re.sub(r"\*\*\*(.+?)\*\*\*", r"<b><i>\1</i></b>", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t)
    t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<i>\1</i>", t)
    t = re.sub(r"`(.+?)`", r'<font face="Courier" size="8.5">\1</font>', t)
    return t


def boxed(paras, bg, edge):
    t = Table([[paras]], colWidths=[6.9 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), bg),
        ("BOX", (0, 0), (-1, -1), 0.9, edge),
        ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
        ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
    ]))
    return t


def table_block(rows):
    head, body = rows[0], rows[1:]
    data = [[Paragraph(inline(c), CELLH) for c in head]]
    data += [[Paragraph(inline(c), CELL) for c in r] for r in body]
    n = len(head)
    t = Table(data, colWidths=[6.9 * inch / n] * n, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), GOLD),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F7F1E4")]),
        ("GRID", (0, 0), (-1, -1), 0.4, RULE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
    ]))
    return t


def convert(md):
    """Markdown to a flowable list. Comments and image directives are dropped."""
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)
    out, i = [], 0
    lines = md.split("\n")
    while i < len(lines):
        ln = lines[i].rstrip()

        if not ln.strip():
            i += 1
            continue

        if ln.startswith("---") and set(ln.strip()) == {"-"}:
            out.append(Spacer(1, 8))
            i += 1
            continue

        # table
        if ln.lstrip().startswith("|") and i + 1 < len(lines) and re.match(
                r"^\s*\|[\s:|-]+\|\s*$", lines[i + 1]):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not re.match(r"^[\s:|-]+$", "".join(cells)):
                    rows.append(cells)
                i += 1
            out.append(table_block(rows))
            out.append(Spacer(1, 6))
            continue

        # blockquote run
        if ln.lstrip().startswith(">"):
            buf = []
            while i < len(lines) and (lines[i].lstrip().startswith(">") or not lines[i].strip()):
                if not lines[i].strip():
                    if i + 1 < len(lines) and lines[i + 1].lstrip().startswith(">"):
                        buf.append("")
                        i += 1
                        continue
                    break
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            text = "\n".join(buf)
            dm = bool(re.search(r"\*\*(DM|A note for the DM|DM note)", text))
            paras = []
            for chunk in [c for c in text.split("\n") if c.strip()]:
                paras.append(Paragraph(inline(chunk), READ))
                paras.append(Spacer(1, 3))
            out.append(boxed(paras[:-1] if paras else [], DM_BG if dm else READ_BG,
                             DM_EDGE if dm else GOLD))
            out.append(Spacer(1, 7))
            continue

        if ln.startswith("### "):
            out.append(Paragraph(inline(ln[4:]), H3)); i += 1; continue
        if ln.startswith("## "):
            out.append(Paragraph(inline(ln[3:]), H2)); i += 1; continue
        if ln.startswith("# "):
            out.append(Paragraph(inline(ln[2:]), H1)); i += 1; continue

        if ln.lstrip().startswith(("- ", "* ")):
            out.append(Paragraph(inline(ln.lstrip()[2:]), BULLET, bulletText="•"))
            i += 1
            continue

        # an ART directive with a matching asset becomes the picture itself
        m = re.match(r"\*\*ART ([A-Z0-9]+)[:.]?\*\*\s*(.*)", ln)
        if m:
            out.append(Paragraph(inline("**Art %s.** %s" % (m.group(1), m.group(2))),
                                 S("artnote", parent=BODY, textColor=GREY,
                                   fontName="Times-Italic")))
            i += 1
            continue

        out.append(Paragraph(inline(ln), BODY))
        i += 1
    return out


def main(out_pdf, sources):
    story = [Spacer(1, 2.1 * inch),
             Paragraph("The Guardians of Elaria", TITLE),
             Paragraph("Session 8: Underroot &bull; working draft for review", SUB),
             PageBreak()]
    for n, src in enumerate(sources):
        md = open(src, encoding="utf-8").read()
        story += convert(md)
        if n < len(sources) - 1:
            story.append(PageBreak())

    def frame(c, d):
        c.saveState()
        c.setFont("Times-Italic", 8)
        c.setFillColor(GREY)
        c.drawCentredString(letter[0] / 2, 0.42 * inch,
                            "The Guardians of Elaria  •  Session 8 draft  •  page %d" % d.page)
        c.restoreState()

    SimpleDocTemplate(out_pdf, pagesize=letter, leftMargin=0.8 * inch,
                      rightMargin=0.8 * inch, topMargin=0.7 * inch,
                      bottomMargin=0.7 * inch).build(story, onFirstPage=frame,
                                                     onLaterPages=frame)
    print("wrote", out_pdf)


if __name__ == "__main__":
    os.chdir(ROOT)
    main(sys.argv[1], sys.argv[2:])
