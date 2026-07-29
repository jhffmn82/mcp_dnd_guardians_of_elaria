#!/usr/bin/env python3
"""Overlay crisp place-name labels and the journey route onto the AI-painted
region base. Image models garble text, so the base is generated with no labels
(templates/genart.py + the repaint prompt, from the authored layout reference),
and this script adds sharp, correctly-spelled serif labels positioned to the
painted landmarks, plus the dotted travel route. Keeps the painted compass and
border. Writes assets/world/elaria_region_map.png (use --scratch to preview).

Positions are fractions of the painted base image, tuned by eye to where each
landmark was actually painted.
"""
import sys, math
from PIL import Image, ImageDraw, ImageFont

BASE = 'assets/world/elaria_region_map_base.png'
if '--scratch' in sys.argv:
    BASE = ('C:/Users/jhffm/AppData/Local/Temp/claude/C--Users-jhffm-dnd-campaign/'
            'd55dee86-bf0a-4655-8235-d6a529a61fc9/scratchpad/map_painted_v1.png')

base = Image.open(BASE).convert('RGB')
UP = 1.6
W, H = int(base.width*UP), int(base.height*UP)
img = base.resize((W, H), Image.LANCZOS)
d = ImageDraw.Draw(img, 'RGBA')

def X(fx): return fx*W
def Y(fy): return fy*H
def P(fx, fy): return (X(fx), Y(fy))

PAL='C:/Windows/Fonts/pala.ttf'; PALB='C:/Windows/Fonts/palab.ttf'; PALI='C:/Windows/Fonts/palai.ttf'
def F(path, px): return ImageFont.truetype(path, int(px*UP))
SIZES={'region':F(PALB,21),'town':F(PALB,20),'townbig':F(PALB,25),'small':F(PALI,18),'sea':F(PALB,40)}
STROKES={'region':2.6,'town':2.5,'townbig':3.0,'small':2.2,'sea':3.6}
# Light ivory letters with a clean dark stroke: reads over the bright sea AND
# the dark forests. Sea label gets a cool tint.
IVORY=(250,244,228); DARK=(24,16,8); SEAFILL=(236,246,247); SEADARK=(14,40,50)

def label(fx, fy, text, sk, ck, align='c', track=0):
    fnt=SIZES[sk]; sw=max(1,int(STROKES[sk]*UP))
    fill = SEAFILL if ck=='seacol' else IVORY
    strk = SEADARK if ck=='seacol' else DARK
    if track:
        segs=list(text); widths=[d.textlength(c,font=fnt) for c in segs]
        total=sum(widths)+track*UP*(len(segs)-1)
        cx=X(fx)-(total/2 if align=='c' else 0); y0=Y(fy)
        for c,w in zip(segs,widths):
            d.text((cx,y0),c,font=fnt,fill=fill,stroke_width=sw,stroke_fill=strk); cx+=w+track*UP
        return
    bb=d.textbbox((0,0),text,font=fnt); tw=bb[2]-bb[0]
    x0=X(fx)-(tw/2 if align=='c' else 0); y0=Y(fy)
    d.text((x0,y0),text,font=fnt,fill=fill,stroke_width=sw,stroke_fill=strk)

# ---- route (draw first, under labels) ----
def dotted(waypts, r=4.2, gap=19, col=(186,38,28), edge=(28,14,8)):
    pts=[]
    for i in range(len(waypts)-1):
        a=waypts[i]; b=waypts[i+1]
        for t in [j/24 for j in range(24)]:
            pts.append((a[0]+(b[0]-a[0])*t, a[1]+(b[1]-a[1])*t))
    prev=pts[0]; dot=r*UP; ring=dot+max(2,int(1.7*UP)); acc=1e9
    for cur in pts:
        acc+=math.hypot(cur[0]-prev[0],cur[1]-prev[1])
        if acc>=gap*UP:
            # bright red dot with a crisp dark edge: stands out on sea and land alike
            d.ellipse([cur[0]-ring,cur[1]-ring,cur[0]+ring,cur[1]+ring],fill=edge)
            d.ellipse([cur[0]-dot,cur[1]-dot,cur[0]+dot,cur[1]+dot],fill=col)
            acc=0
        prev=cur

land=[P(0.075,0.44),P(0.14,0.34),P(0.265,0.31),P(0.335,0.15),P(0.235,0.42),P(0.315,0.50),P(0.155,0.57),P(0.36,0.65),P(0.295,0.83)]
sea =[P(0.315,0.84),P(0.47,0.81),P(0.585,0.785),P(0.655,0.76)]
east=[P(0.70,0.72),P(0.79,0.60),P(0.845,0.52)]
dotted(land); dotted(sea, gap=24); dotted(east)

# ---- labels (positions tuned to the painting) ----
LABELS=[
 (0.115,0.045,'FOREST OF WHISPERS','region','gold','c',3),
 (0.395,0.085,'Ravenstone Laboratory','town','ink','l',0),
 (0.245,0.215,'RAVENSTONE CLIFFS','region','gold','c',2),
 (0.265,0.40,'Oakshade Village','town','ink','c',0),
 (0.072,0.475,'Eldridge Village','town','ink','c',0),
 (0.195,0.445,'Whisperwind Meadow','small','ink','c',0),
 (0.345,0.545,'Brambleshadow Thicket','small','ink','c',0),
 (0.125,0.645,'Ironroot Hills','small','ink','c',0),
 (0.11,0.925,'Bloodthorn Hollow','town','ink','c',0),
 (0.375,0.705,'Stormwatch Cliffs','small','ink','c',0),
 (0.275,0.96,'HAVENMOOR','townbig','gold','c',2),
 (0.55,0.41,'THE OPEN SEA','sea','seacol','c',6),
 (0.675,0.905,'WRAITHPINE','townbig','gold','c',2),
 (0.86,0.63,'GEARHAVEN','townbig','gold','c',2),
 (0.815,0.235,'THE OLD SHRINE','region','gold','c',2),
]
for fx,fy,txt,sk,ck,al,tr in LABELS:
    label(fx,fy,txt,sk,ck,al,track=tr)

# ---- travel-time notes on the two sea/land legs ----
label(0.49,0.855,'by ship, ~3 days','small','ink','c')
label(0.78,0.565,'3-day road','small','ink','c')

out = 'assets/world/elaria_region_map.png'
if '--scratch' in sys.argv:
    out = ('C:/Users/jhffm/AppData/Local/Temp/claude/C--Users-jhffm-dnd-campaign/'
           'd55dee86-bf0a-4655-8235-d6a529a61fc9/scratchpad/map_labeled_draft.png')
img.convert('RGB').save(out)
print('wrote', out)
