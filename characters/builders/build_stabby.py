#!/usr/bin/env python3
"""Stabby Sharpblade character sheet, 2 pages, candy-red theme, 2024 rules.
Ported onto the shared published-book template (sheet_style.py) and content-
synced to the committed stabby_sharpblade_sheet_v3.pdf, which is newer than
the original browser-session script (2024 Patient Defense, 2024 goblin traits
with Fey Ancestry, Uncanny Metabolism heal, Deflect Attack throw-back).
Page 1: combat dashboard + special moves. Page 2: gear + story."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, PageBreak, HRFlowable)

# ---- Published-book styling (shared, committed in sheet_style.py) ----
import sheet_style
from sheet_style import make_frame
INK  = sheet_style.INK
GREY = sheet_style.GREY
RED     = sheet_style.ACCENTS['stabby']      # candy-red accent
RED_HEX = '#A32B2B'
RED_LT  = colors.HexColor('#FBE6E9')         # pale fill for table bands
LINE    = colors.HexColor('#EBC2C8')

styles = getSampleStyleSheet()
def S(name, **kw):
    base = kw.pop('parent', styles['Normal'])
    return ParagraphStyle(name, parent=base, **kw)

_st = sheet_style.styles(RED)
title_st  = _st['title']
sub_st    = _st['sub']
flav_st   = _st['flav']
h2_st     = _st['h2']
body_st   = _st['body']
small_it  = _st['small_it']
cell_st   = _st['cell']
cellb_st  = _st['cellb']
white_lbl = _st['white_lbl']
big_num   = _st['big_num']
note_st   = _st['note']
move_st   = S('mv', fontName='Times-Roman', fontSize=8, textColor=INK, leading=9.8)

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
            ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,0),7.6)]
    t.setStyle(TableStyle(style)); return t

def callout(text, fill=RED_LT):
    p=Paragraph(text,note_st)
    t=Table([[p]],colWidths=[7.3*inch])
    style=[('BOX',(0,0),(-1,-1),1,RED),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]
    if fill is not None:
        style.append(('BACKGROUND',(0,0),(-1,-1),fill))
    t.setStyle(TableStyle(style))
    return t

story=[]
def h2(text):
    # Section header with the thin accent rule the living sheets use
    story.append(Paragraph(text, S('h2r', parent=h2_st, spaceAfter=1)))
    story.append(HRFlowable(width='100%', thickness=0.7, color=RED, spaceAfter=3))

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
story.append(Paragraph('AC 18 normally — jumps to AC 20 right after Stabby punches and swings his '
    'katana the same turn (Agile Parry). Speed &amp; AC include his Sash. Best saves: Dex +8, Str +2.',small_it))

h2("All of Stabby's Skills")
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

h2("What Stabby Does in a Fight")
atk=[['Attack','To Hit','Damage'],
    ['Candyfang Katana +1','+9','1d10+6 slashing + 2 cold'],
    ['Unarmed Strike (fist/foot)','+8','1d8+5 bludgeoning'],
    ['Repeating Longbow +1','+9',"1d8+6 piercing; +1d4 via Kensei's Shot"]]
story.append(section_table([atk[0]] + [[Paragraph(c,cell_st) for c in r] for r in atk[1:]],
    [3.0*inch,0.9*inch,3.4*inch]))
story.append(Spacer(1,4))
story.append(callout("<b>How Stabby's turn works:</b> He gets <b>2 attacks</b> with his Attack action, PLUS "
    "<b>1 extra punch</b> as a bonus action (Martial Arts). Spend Focus on <b>Flurry of Blows</b> for even "
    "more — up to <b>3–4 hits a turn!</b>"))

# Special moves in two columns
h2("Stabby's Special Moves")
moves=[
    ('Flurry of Blows','Spend 1 Focus as a bonus action to make two extra punches. His big damage button.'),
    ('Stunning Strike','When he hits, spend 1 Focus to try to stun the enemy (Con save vs DC 13). '
        '<b>Fail:</b> stunned until his next turn — huge in a boss fight! <b>Success:</b> the enemy is '
        'still slowed (speed halved) and the next attack against it has advantage.'),
    ('Patient Defense','Bonus action to <b>Disengage for free.</b> Spend 1 Focus to also <b>Dodge</b> '
        '(enemies hit him with disadvantage).'),
    ('Step of the Wind','Bonus action to Dash for free. Spend 1 Focus to also Disengage and double his jump. Super zoomy.'),
    ('Deflect Attack','Reaction: when hit by a punch/arrow/blade, lower the damage by 1d10+10. If it hits 0, '
        'spend 1 Focus to fling it back at another enemy within 5 ft (DC 13 Dex save, 2d8+5).'),
    ('Agile Parry','After he punches + swings his katana the same turn, he gets +2 AC until his next turn. '
        '<i>(House rule: his bonus-action punch counts.)</i>'),
    ("Kensei's Shot",'Bonus action: his next longbow hit this turn deals an extra 1d4 damage.'),
    ('Slow Fall / Metabolism','Slow Fall: reaction to take 25 less falling damage. Uncanny Metabolism: '
        'once a day, when he rolls initiative, regain all Focus + heal 5 + 1d8 HP.'),
    ('Fury of the Small','When he hits a creature bigger than him (almost everyone!), deal +3 extra damage. '
        'He can do this 3 times per long rest — once per turn.'),
    ('Nimble Escape','He can Disengage or Hide as a bonus action every turn. Slippery little goblin.'),
    ('Goblin Senses','Sees in the dark 60 ft. Speaks Common, Goblin &amp; Orc.'),
    ('Fey Ancestry','Goblins have a touch of fey blood: advantage on saves to avoid or shake off the charmed condition.'),
]
def move_cell(n,d):
    return Paragraph(f'<b><font color="{RED_HEX}">{n}.</font></b> {d}', move_st)
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
story.append(Paragraph('Stabby Sharpblade', S('p2t',fontName='Times-Bold',fontSize=15,textColor=RED,leading=18,spaceAfter=2)))
story.append(Paragraph('Page 2 — Gear &amp; Story', sub_st))
story.append(Spacer(1,8))

h2("Stabby's Stuff")
GN='<b><font color="%s">%%s</font></b>' % RED_HEX   # gear names: accent bold
gear=[
    ('Candyfang Katana +1','His prized candy-cane katana. +1 to hit and damage, +2 cold. Has Sugar Rush: once a day, lick the blade (bonus action) for 2d8 + 3 temp HP and a jolt of chaos energy.'),
    ('Repeating Longbow +1','A magic bow that makes its own arrows — never runs out. +1 to hit and damage.'),
    ('Sash of the Swift Current (★ Elaria’s gift)','Scarlet stage-silk from the Wraithpine chest. +1 AC, +10 speed, plus Air Dance (fly for 1 minute, 1/day) and Feather Fall (1/day). Attuned.'),
    ('Explorer’s Pack','Backpack, bedroll, rope, torches, rations — the usual adventuring kit.'),
]
story.append(section_table([[Paragraph(GN%n,cell_st),Paragraph(d,cell_st)] for n,d in gear],
    [1.9*inch,5.4*inch], header=False))

h2("Stabby's Story")
story.append(Paragraph(
    "Stabby was born into the Bloodfang Clan, a fierce goblin tribe deep in the twisted woods of "
    "Bloodthorn Hollow. In a clan where the biggest goblin wins, little Stabby survived on speed, cunning, and "
    "pure chaos — he earned the name Sharpblade after beating a whole group of rival goblins using nothing "
    "but a broken sword.", body_st))
story.append(Spacer(1,4))
story.append(Paragraph(
    "One day he met Master Kaelon Windstep, a graceful monk of the Whispering Breeze Clan. Stabby was "
    "amazed by the monk’s smooth, flowing fighting style — so different from goblin brawling. He never "
    "became calm and disciplined, but he blended those moves into his own wild style: grace plus chaos. Then he "
    "left the Hollow looking for adventure… and found Lilly and Ursa, who were chasing magical "
    "creatures and enchanted potatoes. Stabby didn’t need any convincing — he jumped right in for the fun.", body_st))

h2("Personality")
per=[
    ('Chaotic and mischievous','Loves trouble, excitement, and stirring things up. Acts first, thinks later (maybe).'),
    ('Ideal — Freedom','“No one tells me what to do.” Everyone should live life their own way.'),
    ('Bond — His Crew','Fiercely loyal to Lilly and Ursa — his first real friends. “They’re my crew — no one messes with them but me.”'),
    ('Flaw — Reckless','Leaps into danger with no plan. “Who needs a plan when you’ve got guts?”'),
]
pc=[Paragraph(f'<b><font color="{RED_HEX}">{t}</font></b><br/><i>{d}</i>',
              S('pc',fontName='Times-Roman',fontSize=8,textColor=INK,leading=10)) for t,d in per]
pt=Table([[pc[0],pc[1]],[pc[2],pc[3]]],colWidths=[3.65*inch,3.65*inch])
pt.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.5,LINE),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
    ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),]))
story.append(Spacer(1,3)); story.append(pt); story.append(Spacer(1,8))
story.append(callout('<b>Fun Facts:</b> &nbsp;Stabby is a boy goblin, age 8, just 2 feet 4 inches tall and 30 pounds '
    '— small but mighty! &bull; Green skin, red eyes, green hair. &bull; He carries a creepy little idol that gives '
    'him strange dreams. &bull; His old clan, the Bloodfang, are part of his past — and maybe future allies.', fill=None))

doc=SimpleDocTemplate('../stabby_sharpblade_sheet_v3.pdf',pagesize=letter,
    leftMargin=0.55*inch,rightMargin=0.55*inch,topMargin=0.45*inch,bottomMargin=0.5*inch)
frame = make_frame('Stabby Sharpblade')
doc.build(story, onFirstPage=frame, onLaterPages=frame)
print('built ../stabby_sharpblade_sheet_v3.pdf')
