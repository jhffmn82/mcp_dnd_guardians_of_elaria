#!/usr/bin/env python3
"""Authored region map for The Guardians of Elaria (replaces the DALL-E map,
whose generator ignored placement/scale: it drew Gearhaven as a coastal port
across from Havenmoor and omitted the route). This one fixes the geography by
hand so every location is in its correct place and to scale.

Canonical layout (west to east):
  WEST LANDMASS: Eldridge Village + Forest of Whispers (NW), Oakshade,
    Ravenstone Cliffs/Laboratory (N highlands), the road south through
    Whisperwind Meadow, Brambleshadow Thicket, Ironroot Hills, Stormwatch
    Cliffs, down to HAVENMOOR on the south-east coast. Bloodthorn Hollow SW.
  THE OPEN SEA fills the centre. Havenmoor sits on its shore.
  EAST LANDMASS across the sea: WRAITHPINE on the near (west) shore, directly
    across the water from Havenmoor (the landfall in Session 6); GEARHAVEN
    inland east of it, a clockwork mountain-city reached by a 3-day road
    (spires visible from the sea); THE OLD SHRINE far to the north-east in
    deep old-growth forest.
The dotted journey traces: Eldridge -> Forest of Whispers -> Oakshade ->
  Ravenstone -> south chain -> Havenmoor -> (by ship, ~3 days) Wraithpine ->
  (3-day road) Gearhaven. The Old Shrine is a road not yet taken.

Output: assets/world/elaria_region_map.png  (run with --scratch to preview).
"""
import os, sys, math
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

SS = 2
W, H = 2400, 1560
CW, CH = W*SS, H*SS

PARCH = (240, 229, 202); PARCH_D = (223, 208, 172)
INK   = (48, 39, 22);    INK_S = (92, 78, 48)
GOLD  = (138, 109, 31)
SEA   = (150, 184, 190); SEA_D = (104, 146, 158); SEA_L = (190, 214, 214)
LAND  = (210, 212, 174)
FOREST= (78, 108, 74);   FOREST_D=(54, 82, 54)
HILL  = (166, 120, 78)
MOUNT = (124, 114, 94);  MOUNT_D=(88, 78, 60)
THORN = (96, 74, 52);    ROUTE = (150, 58, 44)

def F(path, px): return ImageFont.truetype(path, int(px*SS))
PAL='C:/Windows/Fonts/pala.ttf'; PALB='C:/Windows/Fonts/palab.ttf'; PALI='C:/Windows/Fonts/palai.ttf'

img = Image.new('RGB', (CW, CH), PARCH)
def X(fx): return fx*CW
def Y(fy): return fy*CH
def P(fx, fy): return (X(fx), Y(fy))

# ---- parchment mottling ----
rng = np.random.default_rng(7)
noise = rng.normal(0, 1, (CH//8, CW//8))
nb = Image.fromarray(((noise-noise.min())/(np.ptp(noise))*255).astype('uint8')).resize((CW, CH)).filter(ImageFilter.GaussianBlur(6))
img = Image.composite(Image.new('RGB',(CW,CH),PARCH_D), img, nb.point(lambda v: int(v*0.26)))
d = ImageDraw.Draw(img, 'RGBA')

# ---- organic coastlines ----
def coast(fx_top, fx_bot, seed, lobe_amp=64, jit=11, n=220):
    r=np.random.default_rng(seed); ts=np.linspace(0,1,n)
    xb=(fx_top+(fx_bot-fx_top)*ts)*CW
    lobe=np.zeros(n)
    for _ in range(5):
        lobe+=r.uniform(0.4,1)*np.sin(2*math.pi*r.uniform(1.1,3.0)*ts+r.uniform(0,6.28))
    lobe=lobe/(np.abs(lobe).max() or 1)*lobe_amp*SS
    j=np.cumsum(r.normal(0,1,n)); j-=j.mean(); j=j/(np.abs(j).max() or 1)*jit*SS
    return list(zip(xb+lobe+j, ts*CH))
def x_at(pts, fy):
    yt=fy*CH; return min(pts, key=lambda p:abs(p[1]-yt))[0]

wc=coast(0.44,0.405,seed=3,lobe_amp=60)
ec=coast(0.705,0.725,seed=14,lobe_amp=74)

# land fills, then sea gradient masked between the coasts
d.polygon([(0,0)]+wc+[(0,CH)], fill=LAND)
d.polygon([(CW,0)]+ec+[(CW,CH)], fill=LAND)
grad=Image.new('RGB',(CW,CH),SEA); gd=ImageDraw.Draw(grad)
for xx in range(0,CW,3):
    t=max(0.0,min(1.0,1-abs((xx/CW)-0.565)/0.20))
    gd.line([(xx,0),(xx,CH)],fill=tuple(int(round(SEA[i]+(SEA_D[i]-SEA[i])*t)) for i in range(3)))
seamask=Image.new('L',(CW,CH),0); ImageDraw.Draw(seamask).polygon(wc+ec[::-1],fill=255)
img.paste(grad,(0,0),seamask); d=ImageDraw.Draw(img,'RGBA')

def stroke(points,color,wpx): d.line(points,fill=color,width=max(1,int(wpx*SS)),joint='curve')
stroke(wc,INK_S,2.4); stroke(ec,INK_S,2.4)
for k in range(1,4):
    stroke([(x+(6+8*k)*SS,y) for (x,y) in wc], (SEA_L[0],SEA_L[1],SEA_L[2],110-28*k),1.4)
    stroke([(x-(6+8*k)*SS,y) for (x,y) in ec], (SEA_L[0],SEA_L[1],SEA_L[2],110-28*k),1.4)
r=np.random.default_rng(5)
for _ in range(150):
    fx=r.uniform(0.47,0.66); fy=r.uniform(0.04,0.96); w0=r.uniform(16,38)*SS
    xx,yy=X(fx),Y(fy); d.arc([xx,yy,xx+w0,yy+7*SS],200,340,fill=(SEA_D[0],SEA_D[1],SEA_D[2],80),width=int(1.2*SS))

# coastal-town anchors (guaranteed on the water)
HAVEN=(x_at(wc,0.865)/CW-0.004, 0.865)
WRAITH=(x_at(ec,0.60)/CW+0.006, 0.60)

# ---- terrain glyphs ----
def fir(x,y,s,col=FOREST,cold=FOREST_D):
    s*=SS; d.polygon([(x,y-s),(x-s*0.62,y+s*0.5),(x+s*0.62,y+s*0.5)],fill=col,outline=cold)
    d.line([(x,y+s*0.5),(x,y+s*0.82)],fill=cold,width=max(1,int(1.4*SS)))
def forest_patch(cx,cy,rx,ry,n,seed,s=(11,17)):
    r=np.random.default_rng(seed); pts=[]
    for _ in range(n):
        a=r.uniform(0,2*math.pi); rr=r.uniform(0.2,1.0)
        pts.append((X(cx)+math.cos(a)*rx*SS*rr, Y(cy)+math.sin(a)*ry*SS*rr))
    for (x,y) in sorted(pts,key=lambda p:p[1]): fir(x,y,r.uniform(*s))
def scatter_firs(coords,seed):
    r=np.random.default_rng(seed)
    for fx,fy in coords: fir(X(fx),Y(fy),r.uniform(10,15))
def mountains(cx,cy,spread,n,seed,h=(20,34),col=MOUNT,cold=MOUNT_D):
    r=np.random.default_rng(seed); base=[(X(cx)+r.uniform(-spread,spread)*SS,Y(cy)+r.uniform(-spread*0.3,spread*0.3)*SS) for _ in range(n)]
    for (x,y) in sorted(base,key=lambda p:p[1]):
        hh=r.uniform(*h)*SS; d.polygon([(x-hh*0.8,y),(x,y-hh),(x+hh*0.8,y)],fill=col,outline=cold)
        d.line([(x,y-hh),(x-hh*0.22,y-hh*0.55)],fill=(255,255,255,120),width=max(1,int(1.3*SS)))
def hills(cx,cy,spread,n,seed):
    r=np.random.default_rng(seed)
    for _ in range(n):
        x=X(cx)+r.uniform(-spread,spread)*SS; y=Y(cy)+r.uniform(-spread*0.35,spread*0.35)*SS; w0=r.uniform(20,34)*SS
        d.arc([x-w0/2,y-w0*0.5,x+w0/2,y+w0*0.5],185,355,fill=HILL,width=int(1.8*SS))
def thicket(cx,cy,rx,ry,seed):
    r=np.random.default_rng(seed)
    for _ in range(70):
        x=X(cx)+r.uniform(-rx,rx)*SS; y=Y(cy)+r.uniform(-ry,ry)*SS; a=r.uniform(0,2*math.pi); l=r.uniform(6,13)*SS
        d.line([(x,y),(x+math.cos(a)*l,y+math.sin(a)*l)],fill=THORN,width=max(1,int(1.3*SS)))
def meadow(cx,cy,rx,ry,seed):
    r=np.random.default_rng(seed)
    for _ in range(120):
        x=X(cx)+r.uniform(-rx,rx)*SS; y=Y(cy)+r.uniform(-ry,ry)*SS
        d.line([(x,y),(x,y-r.uniform(4,8)*SS)],fill=(120,140,86,150),width=max(1,int(1*SS)))

# ---- landmark icons ----
def house(x,y,s,col=(150,120,86)):
    s*=SS; d.rectangle([x-s*0.5,y-s*0.2,x+s*0.5,y+s*0.5],fill=col,outline=INK_S)
    d.polygon([(x-s*0.6,y-s*0.2),(x,y-s*0.8),(x+s*0.6,y-s*0.2)],fill=(120,70,55),outline=INK_S)
def village(x,y,seed=0):
    r=np.random.default_rng(seed)
    for dx,dy in [(-16,4),(6,-2),(20,8),(-2,14)]: house(x+dx*SS,y+dy*SS,r.uniform(11,15))
def tower(x,y):
    s=16*SS; d.rectangle([x-s*0.34,y-s*1.4,x+s*0.34,y+s*0.2],fill=(150,150,158),outline=INK_S,width=max(1,int(1.4*SS)))
    d.polygon([(x-s*0.5,y-s*1.4),(x,y-s*2.0),(x+s*0.5,y-s*1.4)],fill=(70,80,120),outline=INK_S)
    d.rectangle([x-s*0.12,y-s*0.9,x+s*0.12,y-s*0.5],fill=(40,45,70))
def harbour(x,y,seed=0):
    village(x,y,seed); d.line([(x+22*SS,y+16*SS),(x+44*SS,y+26*SS)],fill=INK_S,width=int(2.2*SS))
    d.line([(x+30*SS,y+13*SS),(x+30*SS,y+30*SS)],fill=INK_S,width=int(1.6*SS))
def gearcity(x,y):
    mountains(x/CW,y/CH+0.028,40,5,seed=21,h=(30,46)); rr=22*SS
    d.ellipse([x-rr,y-rr,x+rr,y+rr],outline=(120,92,34),width=int(3*SS))
    for a in range(0,360,30):
        a0=math.radians(a); d.line([(x+math.cos(a0)*rr,y+math.sin(a0)*rr),(x+math.cos(a0)*(rr+7*SS),y+math.sin(a0)*(rr+7*SS))],fill=(120,92,34),width=int(2.4*SS))
    d.ellipse([x-rr*0.4,y-rr*0.4,x+rr*0.4,y+rr*0.4],fill=(150,118,44))
    for dx in (-1,0,1): d.rectangle([x+dx*10*SS-3*SS,y-rr-16*SS,x+dx*10*SS+3*SS,y-rr],fill=(120,110,90),outline=INK_S)
def fogvillage(x,y,seed=0):
    village(x,y,seed)
    for k in range(3): d.arc([x-30*SS,y-26*SS-k*10*SS,x+30*SS,y-6*SS-k*10*SS],200,340,fill=(238,238,238,150),width=int(2.2*SS))
    for dx,dy in [(-18,-2),(16,2)]: d.ellipse([x+dx*SS-2*SS,y+dy*SS-2*SS,x+dx*SS+2*SS,y+dy*SS+2*SS],fill=(230,190,90))
def shrine(x,y):
    s=15*SS
    for dx in (-1,0,1): d.rectangle([x+dx*s*0.5-2*SS,y-s,x+dx*s*0.5+2*SS,y+s*0.4],fill=(190,188,178),outline=INK_S)
    d.rectangle([x-s*0.9,y-s*1.15,x+s*0.9,y-s*0.9],fill=(170,168,158),outline=INK_S)
def thornring(x,y):
    for a in range(0,360,20):
        a0=math.radians(a); rr=24*SS; d.line([(x,y),(x+math.cos(a0)*rr,y+math.sin(a0)*rr)],fill=THORN,width=max(1,int(1.4*SS)))
    d.ellipse([x-6*SS,y-6*SS,x+6*SS,y+6*SS],fill=(60,45,35))
def cliffs(x,y):
    for k in range(6):
        x0=x-40*SS+k*16*SS; d.line([(x0,y-8*SS),(x0,y+22*SS)],fill=(120,116,104),width=int(2*SS))
    d.line([(x-46*SS,y-8*SS),(x+52*SS,y-8*SS)],fill=INK_S,width=int(2*SS))

# ---- terrain fills ----
forest_patch(0.085,0.14,62,46,60,seed=11)            # Forest of Whispers
forest_patch(0.955,0.30,58,78,90,seed=12)            # Old Shrine wood
scatter_firs([(0.80,0.34),(0.84,0.30),(0.90,0.42),(0.80,0.70),(0.90,0.72),(0.86,0.78),(0.78,0.50)],seed=33)  # east greenery
meadow(0.27,0.36,55,34,4)                            # Whisperwind Meadow
thicket(0.25,0.50,44,30,6)                           # Brambleshadow
hills(0.24,0.63,46,10,8)                             # Ironroot Hills
hills(0.80,0.62,30,6,44)                             # east foothills toward Gearhaven
mountains(0.33,0.135,55,7,2,h=(24,40))               # Ravenstone Cliffs ridge

# ---- locations ----
LOC = [
 (0.085,0.14,'FOREST OF WHISPERS',None,(0,70),'region','c'),
 (0.215,0.225,'Oakshade Village','village',(0,34),'town','c'),
 (0.335,0.145,'Ravenstone Laboratory','tower',(72,-40),'town','l'),
 (0.315,0.235,'RAVENSTONE CLIFFS',None,(-30,0),'region','c'),
 (0.085,0.46,'Eldridge Village','village',(0,34),'town','c'),
 (0.27,0.36,'Whisperwind Meadow',None,(0,6),'small','c'),
 (0.25,0.50,'Brambleshadow Thicket',None,(0,40),'small','c'),
 (0.24,0.63,'Ironroot Hills',None,(0,36),'small','c'),
 (0.075,0.78,'Bloodthorn Hollow','thornring',(0,40),'town','c'),
 (0.36,0.735,'Stormwatch Cliffs','cliffs',(0,42),'small','c'),
 (HAVEN[0],HAVEN[1],'HAVENMOOR','harbour',(0,48),'townbig','c'),
 (WRAITH[0],WRAITH[1],'WRAITHPINE','fogvillage',(6,48),'townbig','l'),
 (0.85,0.55,'GEARHAVEN','gearcity',(0,58),'townbig','c'),
 (0.95,0.29,'THE OLD SHRINE','shrine',(0,42),'region','c'),
]
FONTS={'region':F(PALB,26),'town':F(PALB,21),'townbig':F(PALB,30),'small':F(PALI,18)}
def draw_label(x,y,text,kind,off,align):
    fnt=FONTS[kind]; col=GOLD if kind in ('region','townbig') else INK
    tx,ty=x+off[0]*SS, y+off[1]*SS
    bb=d.textbbox((0,0),text,font=fnt); tw=bb[2]-bb[0]
    ax = tx-tw/2 if align=='c' else tx
    for ox,oy in [(-2,0),(2,0),(0,-2),(0,2)]: d.text((ax+ox*SS,ty+oy*SS),text,font=fnt,fill=(240,229,202,215))
    d.text((ax,ty),text,font=fnt,fill=col)

for fx,fy,name,kind,off,fk,al in LOC:
    x,y=X(fx),Y(fy)
    {'village':lambda:village(x,y,int(fx*1000)),'tower':lambda:tower(x,y),'harbour':lambda:harbour(x,y,7),
     'fogvillage':lambda:fogvillage(x,y,3),'gearcity':lambda:gearcity(x,y),'shrine':lambda:shrine(x,y),
     'thornring':lambda:thornring(x,y),'cliffs':lambda:cliffs(x,y)}.get(kind,lambda:None)()
    draw_label(x,y,name,fk,off,al)

# ---- Open Sea label ----
sf=F(PALI,52); txt='THE OPEN SEA'; bb=d.textbbox((0,0),txt,font=sf)
d.text((X(0.565)-(bb[2]-bb[0])/2,Y(0.44)),txt,font=sf,fill=(58,92,102))

# ---- route ----
def dotted(points,color,r=3.2,gap=15):
    prev=points[0]; dot=r*SS
    for cur in points[1:]:
        seg=math.hypot(cur[0]-prev[0],cur[1]-prev[1]); steps=int(seg//(gap*SS)) or 1
        for i in range(steps):
            t=i/steps; x=prev[0]+(cur[0]-prev[0])*t; y=prev[1]+(cur[1]-prev[1])*t
            d.ellipse([x-dot,y-dot,x+dot,y+dot],fill=color)
        prev=cur
def smooth(wp,n=26):
    out=[]
    for i in range(len(wp)-1):
        for t in np.linspace(0,1,n): out.append((wp[i][0]+(wp[i+1][0]-wp[i][0])*t, wp[i][1]+(wp[i+1][1]-wp[i][1])*t))
    return out
RC=(ROUTE[0],ROUTE[1],ROUTE[2],235)
land_wp=[P(0.085,0.47),P(0.105,0.20),P(0.215,0.245),P(0.335,0.185),P(0.29,0.34),P(0.265,0.49),P(0.25,0.62),P(0.34,0.74),P(HAVEN[0],HAVEN[1]-0.01)]
dotted(smooth(land_wp),RC,3.2,15)
sea_wp=[P(HAVEN[0]+0.005,HAVEN[1]-0.005),P(0.50,0.79),P(0.62,0.69),P(WRAITH[0]-0.006,WRAITH[1])]
dotted(smooth(sea_wp),RC,3.2,22)
east_wp=[P(WRAITH[0]+0.02,WRAITH[1]-0.01),P(0.80,0.565),P(0.835,0.555)]
dotted(smooth(east_wp),RC,3.2,15)
d.text((X(0.505),Y(0.735)),'by ship, ~3 days',font=F(PALI,18),fill=ROUTE)
d.text((X(0.775),Y(0.515)),'3-day road',font=F(PALI,16),fill=ROUTE)

# ---- compass rose ----
cx,cy=X(0.935),Y(0.115); R=42*SS
for a in (0,90,180,270):
    a0=math.radians(a)
    d.polygon([(cx+math.cos(a0)*R,cy+math.sin(a0)*R),(cx+math.cos(a0+math.pi/2)*R*0.16,cy+math.sin(a0+math.pi/2)*R*0.16),(cx+math.cos(a0-math.pi/2)*R*0.16,cy+math.sin(a0-math.pi/2)*R*0.16)],fill=(GOLD if a in (270,90) else (198,176,120)),outline=INK_S)
d.ellipse([cx-6*SS,cy-6*SS,cx+6*SS,cy+6*SS],fill=GOLD)
cf=F(PALB,20)
for a,l in [(0,'E'),(90,'S'),(180,'W'),(270,'N')]:
    a0=math.radians(a); lx=cx+math.cos(a0)*(R+18*SS); ly=cy+math.sin(a0)*(R+18*SS); bb=d.textbbox((0,0),l,font=cf)
    d.text((lx-(bb[2]-bb[0])/2,ly-(bb[3]-bb[1])/2),l,font=cf,fill=INK)

# ---- scale bar ----
sx,sy=X(0.055),Y(0.95); seg=90*SS
d.text((sx,sy-28*SS),'Scale of leagues',font=F(PALI,16),fill=INK_S)
for i in range(4):
    d.rectangle([sx+i*seg,sy,sx+(i+1)*seg,sy+9*SS],fill=(INK if i%2==0 else PARCH),outline=INK)
scf=F(PAL,15)
for i,lbl in [(0,'0'),(2,'25'),(4,'50')]:
    bb=d.textbbox((0,0),lbl,font=scf); d.text((sx+i*seg-(bb[2]-bb[0])/2,sy+13*SS),lbl,font=scf,fill=INK)

# ---- title ----
tf=F(PALB,40); d.text((X(0.055),Y(0.05)),'THE LANDS OF ELARIA',font=tf,fill=GOLD)
bb=d.textbbox((0,0),'THE LANDS OF ELARIA',font=tf)
d.text((X(0.055),Y(0.05)+bb[3]+6*SS),'and the road the Guardians walked',font=F(PALI,20),fill=INK_S)

# ---- border ----
for inset,wpx in [(16,3),(27,1.4)]:
    d.rectangle([inset*SS,inset*SS,CW-inset*SS,CH-inset*SS],outline=GOLD,width=max(1,int(wpx*SS)))

out=img.resize((W,H),Image.LANCZOS)
dest=('C:/Users/jhffm/AppData/Local/Temp/claude/C--Users-jhffm-dnd-campaign/'
      'd55dee86-bf0a-4655-8235-d6a529a61fc9/scratchpad/region_map_draft.png') if '--scratch' in sys.argv else 'assets/world/elaria_region_map.png'
out.save(dest); print('wrote',dest)
