#!/usr/bin/env python3
"""Shared published-book styling for the Guardians character sheets.

This is the reusable capability that used to live only in a browser session
and got lost. It is now COMMITTED code: the exact look of the living sheets
(parchment page, double gold border, Times serif, per-hero accent, footer),
reverse-engineered from characters/*_sheet_v3.pdf so it can never be lost
again. Each per-hero builder (build_lilly/stabby/ursa.py) imports this.

Spec (extracted from the living PDFs, do not guess these):
  background  #F7F1E1  (parchment)          fonts: Times-Roman/Bold/Italic
  border      #8A6D1F  (gold, double frame) stat-box labels+numbers: Helvetica-Bold
  ink         #2B2313   grey #6F6046        accents: Lilly #1F6FB8, Stabby #A32B2B,
  footer      "<Hero>  *  The Guardians of Elaria  *  Page N"   Ursa #6B4FA8
"""
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER

PARCHMENT = colors.HexColor('#F7F1E1')
GOLD      = colors.HexColor('#8A6D1F')
INK       = colors.HexColor('#2B2313')
GREY      = colors.HexColor('#6F6046')

ACCENTS = {'lilly': colors.HexColor('#1F6FB8'),
           'stabby': colors.HexColor('#A32B2B'),
           'ursa': colors.HexColor('#6B4FA8')}


def make_frame(footer_name):
    """Return an onPage callback drawing the parchment page, gold double
    border, and footer. Pass it as onFirstPage AND onLaterPages."""
    def frame(canvas, doc):
        canvas.saveState()
        W, H = doc.pagesize
        canvas.setFillColor(PARCHMENT)
        canvas.rect(0, 0, W, H, fill=1, stroke=0)
        canvas.setStrokeColor(GOLD)
        canvas.setLineWidth(1.6)
        canvas.rect(0.30 * inch, 0.30 * inch, W - 0.60 * inch, H - 0.60 * inch, fill=0, stroke=1)
        canvas.setLineWidth(0.5)
        canvas.rect(0.38 * inch, 0.38 * inch, W - 0.76 * inch, H - 0.76 * inch, fill=0, stroke=1)
        canvas.setFont('Times-Italic', 7.5)
        canvas.setFillColor(GREY)
        # Footer sits just above the inner border line (0.38"), inside the frame;
        # at 0.30" it collided with the double border.
        canvas.drawCentredString(W / 2.0, 0.41 * inch,
                                 f"{footer_name}  •  The Guardians of Elaria  •  Page {doc.page}")
        canvas.restoreState()
    return frame


def styles(accent):
    """Paragraph styles matching the living sheets. `accent` is the hero's
    accent colour (from ACCENTS). Stat-box labels and big numbers stay
    Helvetica-Bold per the spec; everything else is Times."""
    def S(name, **kw):
        return ParagraphStyle(name, **kw)
    return {
        'title':    S('t',  fontName='Times-Bold',   fontSize=24,  textColor=accent, leading=26),
        'sub':      S('s',  fontName='Times-Bold',   fontSize=9.5, textColor=GREY,   leading=12),
        'flav':     S('f',  fontName='Times-Italic', fontSize=9,   textColor=INK,    leading=12),
        'h2':       S('h2', fontName='Times-Bold',   fontSize=12.5, textColor=accent, leading=15,
                      spaceBefore=7, spaceAfter=3),
        'body':     S('b',  fontName='Times-Roman',  fontSize=8.6, textColor=INK,    leading=11),
        'small_it': S('si', fontName='Times-Italic', fontSize=7.6, textColor=GREY,   leading=10),
        'cell':     S('c',  fontName='Times-Roman',  fontSize=8.3, textColor=INK,    leading=10),
        'cellb':    S('cb', fontName='Times-Bold',   fontSize=8.3, textColor=INK,    leading=10),
        'white_lbl':S('wl', fontName='Helvetica-Bold', fontSize=7.2, textColor=colors.white,
                      leading=8, alignment=TA_CENTER),
        'big_num':  S('bn', fontName='Helvetica-Bold', fontSize=14.5, textColor=INK,
                      leading=16, alignment=TA_CENTER),
        'note':     S('n',  fontName='Times-Roman',  fontSize=8.4, textColor=INK,    leading=11),
    }
