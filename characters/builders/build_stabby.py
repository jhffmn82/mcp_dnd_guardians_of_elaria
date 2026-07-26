#!/usr/bin/env python3
"""Stabby Sharpblade — reflowed to 2 pages on the locked template.
Page 1: combat dashboard + special moves (two columns). Page 2: gear + story.
Candy-red theme. All content verbatim from his existing 3-page sheet."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, PageBreak)

RED      = colors.HexColor('#C5283D')   # candy red primary
RED_DK   = colors.HexColor('#8E1B2B')
RED_LT   = colors.HexColor('#FBE6E9')   # pale fill
RED_MID  = colors.HexColor('#E39AA4')
INK      = colors.HexColor('#2A2026')
GREY     = colors.HexColor('#555555')
LINE     = colors.HexColor('#EBC2C8')

styles = getSampleStyleSheet()
def S(name, **kw):
    base = kw.pop('parent', styles['Normal'])
    return ParagraphStyle(name, parent=base, **kw)

title_st = S('t', fontName='Helvetica-Bold', fontSize=26, textColor=RED, leading=28)
sub_st   = S('s', fontName='Helvetica', fontSize=10.5, textColor=GREY, leading=13)
flav_st  = S('f', fontName='Helvetica-Oblique', fontSize=9.5, textColor=INK, leading=12.5)
h2_st    = S('h2', fontName='Helvetica-Bold', fontSize=13, textColor=RED, leading=15,
             spaceBefore=8, spaceAfter=3)
body_st  = S('b', fontName='Helvetica', fontSize=8.6, textColor=INK, leading=11)
small_it = S('si', fontName='Helvetica-Oblique', fontSize=8, textColor=GREY, leading=10)
cell_st  = S('c', fontName='Helvetica', fontSize=8.3, textColor=INK, leading=10)
cellb_st = S('cb', fontName='Helvetica-Bold', fontSize=8.3, textColor=INK, leading=10)
white_lbl= S('wl', fontName='Helvetica-Bold', fontSize=7.2, textColor=colors.white,
             leading=8, alignment=1)
big_num  = S('bn', fontName='Helvetica-Bold', fontSize=15, textColor=INK, leading=16, alignment=1)
note_st  = S('n', fontName='Helvetica', fontSize=8.4, textColor=INK, leading=11)
move_st  = S('mv', fontName='Helvetica', fontSize=7.8, textColor=INK, leading=9.6)

def stat_strip(pairs):
    labels=[Paragraph(l,white_lbl) for l,_ in pairs]
    vals=[Paragraph(str(v),big_num) for _,v in pairs]
    t=Table([labels,vals], colWidths=[7.3*inch/len(pairs)]*len(pairs))
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),RED),('BACKGROUND',(0,1),(-1,1),RED_LT),
        ('GRID',(0,0),(-1,-1),0.5,colors.white),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,0),3),('BOTTOMPADDING',(0,0),(-1,0),3),
        ('TOPPADDING',(0,1),(-1,1),5),('BOTTOMPADDING',(0,1),(-1,1),5),]))
    return t

def ability_strip(abils):
    labels=[Paragraph(l,white_lbl) for l,_,_ in abils]
    sc=[Paragraph(str(s),big_num) for _,s,_ in abils]
    mod_st=S('m',fontName='Helvetica',fontSize=8.5,textColor=GREY,alignment=1,leading=9)
    md=[Paragraph(m,mod_st) for _,_,m in abils]
    t=Table([labels,sc,md], colWidths=[7.3*inch/6]*6)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0),RED),('BACKGROUND',(0,1),(-1,2),RED_LT),
        ('GRID',(0,0),(-1,-1),0.5,colors.white),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,0),2),('BOTTOMPADDING',(0,0),(-1,0),2),
        ('TOPPADDING',(0,1),(-1,1),3),('BOTTOMPADDING',(0,1),(-1,1),0),
        ('TOPPADDING',(0,2),(-1,2),0),('BOTTOMPADDING',(0,2),(-1,2),3),]))
    return t

def section_table(data, col_widths, header=True):
    t=Table(data, colWidths=col_widths)
    style=[('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),0.5,LINE),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,RED_LT]),]
    if header:
        style+=[('BACKGROUND',(0,0),(-1,0),RED),('TEXTCOLOR',(0,0),(-1,0),colors.white),
            ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,0),8.3)]
    t.setStyle(TableStyle(style)); return t

def callout(text):
    p=Paragraph(text,note_st)
    t=Table([[p]],colWidths=[7.3*inch])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),RED_LT),('BOX',(0,0),(-1,-1),1,RED),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),]))
    return t

story=[]
# ===== PAGE 1 =====
hdr=Table([[Image('stabby_new.png',width=1.35*inch,height=1.35*inch),
    [Paragraph('Stabby Sharpblade',title_st),
     Paragraph('Goblin &bull; Monk (Way of the Kensei) &bull; Level 5',sub_st),Spacer(1,3),
     Paragraph('The wild one. Stabby is a tiny, lightning-fast goblin who fights with a '
               'candy-cane katana and his own two fists. Chaos with a smile.',flav_st)]]],
    colWidths=[1.5*inch,5.8*inch])
hdr.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(1,0),(1,0),10)]))
story.append(hdr); story.append(Spacer(1,8))

story.append(stat_strip([('ARMOR CLASS',18),('HIT POINTS',43),('SPEED','50 ft'),
                         ('INITIATIVE','+5'),('FOCUS DC',13),('FOCUS PTS',5)]))
story.append(Spacer(1,4))
story.append(ability_strip([('STR',8,'-1'),('DEX',20,'+5'),('CON',16,'+3'),
                            ('INT',8,'-1'),('WIS',14,'+2'),('CHA',8,'-1')]))
story.append(Paragraph('AC 18 normally \u2014 jumps to AC 20 right after Stabby punches and swings his '
    'katana the same turn (Agile Parry). Speed &amp; AC include his Sash. Best saves: Dex +8, Str +2.',small_it))

story.append(Paragraph("All of Stabby's Skills", h2_st))
TR='<b><font color="#7A1F1F">%s</font></b>'   # trained: red, per the caption
skills=[
    (TR%'Acrobatics +8',TR%'Athletics +2','Insight +2','Medicine +2','Performance -1','Sleight of Hand +5'),
    ('Animal Handling +2','Deception -1','Intimidation -1','Nature -1','Persuasion -1',TR%'Stealth +8'),
    ('Arcana -1','History -1','Investigation -1','Perception +2','Religion -1',TR%'Survival +5'),
]
sk=Table([[Paragraph(c,cell_st) for c in r] for r in skills], colWidths=[(7.3/6)*inch]*6)
sk.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.3,RED_LT),
    ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),3),]))
story.append(sk)
story.append(Paragraph('Red = trained. Best: Acrobatics &amp; Stealth +8 (sneaky and springy!).',small_it))

story.append(Paragraph("What Stabby Does in a Fight", h2_st))
atk=[['Attack','To Hit','Damage'],
    ['Candyfang Katana +1','+9','1d10+6 slashing + 2 cold'],
    ['Unarmed Strike (fist/foot)','+8','1d8+5 bludgeoning'],
    ['Repeating Longbow +1','+9','1d8 + 1d4 + 6 piercing (far away)']]
story.append(section_table([[Paragraph(c,cellb_st if i==0 else cell_st) for c in r]
    for i,r in enumerate(atk)], [3.0*inch,0.9*inch,3.4*inch]))
story.append(Spacer(1,4))
story.append(callout("<b>How Stabby's turn works:</b> He gets <b>2 attacks</b> with his Attack action, PLUS "
    "<b>1 extra punch</b> as a bonus action (Martial Arts). Spend Focus on <b>Flurry of Blows</b> for even "
    "more \u2014 up to <b>3\u20134 hits a turn!</b>"))

# Special moves in two columns (moved up from page 2)
story.append(Paragraph("Stabby's Special Moves", h2_st))
moves=[
    ('Flurry of Blows','Spend 1 Focus as a bonus action to make two extra punches. His big damage button.'),
    ('Stunning Strike','When he hits, spend 1 Focus to try to stun the enemy (Con save vs DC 13). A stunned enemy can barely act \u2014 huge in a boss fight!'),
    ('Patient Defense','Bonus action to Dodge (enemies hit him with disadvantage). Spend Focus to also Disengage.'),
    ('Step of the Wind','Bonus action to Dash. Spend Focus to also Disengage and double his jump. Super zoomy.'),
    ('Deflect Attack','Reaction: when hit by a punch/arrow/blade, lower the damage by 1d10+10. If it hits 0, fling it back at another enemy!'),
    ('Agile Parry','After he punches + swings his katana the same turn, he gets +2 AC until his next turn.'),
    ("Kensei's Shot",'Bonus action: his next longbow hit this turn deals an extra 1d4 damage.'),
    ('Slow Fall / Metabolism','Slow Fall: reaction to take 25 less falling damage. Uncanny Metabolism: once a day, regain all Focus + some HP when he rolls initiative.'),
    ('Fury of the Small','Once per short rest, when he hits something bigger than him (almost everyone!), deal +5 damage.'),
    ('Nimble Escape','He can Disengage or Hide as a bonus action every turn. Slippery little goblin.'),
    ('Goblin Senses','Sees in the dark 60 ft. Speaks Common, Goblin & Orc.'),
]
def move_cell(n,d):
    return Paragraph(f'<b>{n}.</b> {d}', move_st)
# split into two columns
left=moves[0::2]; right=moves[1::2]
maxlen=max(len(left),len(right))
rows=[]
for i in range(maxlen):
    lc=move_cell(*left[i]) if i<len(left) else Paragraph('',move_st)
    rc=move_cell(*right[i]) if i<len(right) else Paragraph('',move_st)
    rows.append([lc,rc])
mt=Table(rows,colWidths=[3.65*inch,3.65*inch])
mt.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.4,RED_LT),
    ('VALIGN',(0,0),(-1,-1),'TOP'),('BACKGROUND',(0,0),(-1,-1),colors.white),
    ('ROWBACKGROUNDS',(0,0),(-1,-1),[colors.white,RED_LT]),
    ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
    ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),]))
story.append(mt)

story.append(PageBreak())

# ===== PAGE 2 =====
story.append(Paragraph('Stabby Sharpblade', S('p2t',fontName='Helvetica-Bold',fontSize=15,textColor=RED,leading=18,spaceAfter=2)))
story.append(Paragraph('Page 2 — Gear &amp; Story', sub_st))
story.append(Spacer(1,8))

story.append(Paragraph("Stabby's Stuff", h2_st))
gear=[
    ('Candyfang Katana +1','His prized candy-cane katana. +1 to hit and damage, +2 cold. Has <b>Sugar Rush:</b> once a day, lick the blade (bonus action) for 2d8 + 3 temp HP and a jolt of chaos energy.'),
    ('Repeating Longbow +1','A magic bow that makes its own arrows \u2014 never runs out. +1 to hit and damage.'),
    ('Sash of the Swift Current<br/><i>(new! \u2605 Elaria\u2019s gift)</i>','Scarlet stage-silk from the Wraithpine chest. +1 AC, +10 speed, plus <b>Air Dance</b> (fly for 1 minute, 1/day) and <b>Feather Fall</b> (1/day). Attuned.'),
    ('Explorer\u2019s Pack','Backpack, bedroll, rope, torches, rations \u2014 the usual adventuring kit.'),
]
story.append(section_table([[Paragraph(n,cell_st),Paragraph(d,cell_st)] for n,d in gear],
    [1.9*inch,5.4*inch], header=False))

story.append(Paragraph("Stabby's Story", h2_st))
story.append(Paragraph(
    "Stabby was born into the <b>Bloodfang Clan</b>, a fierce goblin tribe deep in the twisted woods of "
    "Bloodthorn Hollow. In a clan where the biggest goblin wins, little Stabby survived on speed, cunning, and "
    "pure chaos \u2014 he earned the name Sharpblade after beating a whole group of rival goblins using nothing "
    "but a broken sword.", body_st))
story.append(Spacer(1,4))
story.append(Paragraph(
    "One day he met <b>Master Kaelon Windstep</b>, a graceful monk of the Whispering Breeze Clan. Stabby was "
    "amazed by the monk\u2019s smooth, flowing fighting style \u2014 so different from goblin brawling. He never "
    "became calm and disciplined, but he blended those moves into his own wild style: grace plus chaos. Then he "
    "left the Hollow looking for adventure\u2026 and found <b>Lilly</b> and <b>Ursa</b>, who were chasing magical "
    "creatures and enchanted potatoes. Stabby didn\u2019t need any convincing \u2014 he jumped right in for the fun.", body_st))

per=[
    ('Personality','Chaotic and mischievous \u2014 loves trouble, excitement, and stirring things up. Acts first, thinks later (maybe).'),
    ('Ideal — Freedom','\u201cNo one tells me what to do.\u201d Everyone should live life their own way.'),
    ('Bond — His Crew','Fiercely loyal to Lilly and Ursa \u2014 his first real friends. \u201cThey\u2019re my crew \u2014 no one messes with them but me.\u201d'),
    ('Flaw — Reckless','Leaps into danger with no plan. \u201cWho needs a plan when you\u2019ve got guts?\u201d'),
]
pc=[Paragraph(f'<b>{t}</b><br/>{d}',S('pc',fontName='Helvetica',fontSize=8,textColor=INK,leading=10)) for t,d in per]
pt=Table([[pc[0],pc[1]],[pc[2],pc[3]]],colWidths=[3.65*inch,3.65*inch])
pt.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.5,LINE),
    ('BACKGROUND',(0,0),(-1,-1),RED_LT),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
    ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),]))
story.append(Spacer(1,3)); story.append(pt); story.append(Spacer(1,4))
story.append(Paragraph('<b>Fun Facts:</b> &nbsp;Stabby is a boy goblin, age 8, just 2 feet 4 inches tall and 30 pounds '
    '\u2014 small but mighty! &bull; Green skin, red eyes, green hair. &bull; He carries a creepy little idol that gives '
    'him strange dreams. &bull; His old clan, the Bloodfang, are part of his past \u2014 and maybe future allies.', small_it))

doc=SimpleDocTemplate('/home/claude/Stabby_Sharpblade_Sheet.pdf',pagesize=letter,
    leftMargin=0.55*inch,rightMargin=0.55*inch,topMargin=0.45*inch,bottomMargin=0.4*inch)
doc.build(story)
print('built Stabby_Sharpblade_Sheet.pdf')
