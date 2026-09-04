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
     Paragraph('Goblin &bull; Monk (Warrior of Beast Breathing) &bull; Level 7',sub_st),Spacer(1,3),
     Paragraph('The wild one. Stabby is a tiny, lightning-fast goblin who fights with a '
               'sun-forged katana and his own two fists. Chaos with a smile, and a breath that burns.',flav_st)]]],
    colWidths=[1.5*inch,5.8*inch])
hdr.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(1,0),(1,0),10)]))
story.append(hdr); story.append(Spacer(1,8))

story.append(stat_strip([('ARMOR CLASS',18),('HIT POINTS',59),('SPEED','55 ft'),
                         ('INITIATIVE','+5'),('FOCUS DC',13),('FOCUS PTS',7)]))
story.append(Spacer(1,4))
story.append(ability_strip([('STR',8,'-1'),('DEX',20,'+5'),('CON',16,'+3'),
                            ('INT',8,'-1'),('WIS',14,'+2'),('CHA',8,'-1')]))
story.append(Paragraph('AC 18. '
    'Speed 45 on his own feet, <b>55</b> with the Sash, <b>65</b> while his breath is ignited. AC includes the Sash.',small_it))
sv=Table([[Paragraph(c,cell_st) for c in ['<b><font color="#7A1F1F">Str save +2</font></b>', '<b><font color="#7A1F1F">Dex save +8</font></b>', 'Con save +3', 'Int save -1', 'Wis save +2', 'Cha save -1']]], colWidths=[(7.3/6)*inch]*6)
sv.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.3,RED_LT),
    ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),3)]))
story.append(sv)

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
    ['Nichirin Katana +2 <i>(new!)</i>','+10','1d10+7 slashing, +2 Force while ignited'],
    ['Unarmed Strike (fist/foot) <i>(wraps!)</i>','+10','1d8+7 bludgeoning <i>or Force</i>'],
    ['Repeating Longbow +1','+9','1d8+6 piercing (just a very good bow now)'],
    ['First Form: Devour <i>(bonus action, 1 Focus)</i>','+10','3d8+9 <b>Force</b>, move 15 ft free first']]
story.append(section_table([atk[0]] + [[Paragraph(c,cell_st) for c in r] for r in atk[1:]],
    [3.0*inch,0.9*inch,3.4*inch]))
story.append(Spacer(1,4))
story.append(callout("<b>How Stabby's turn works:</b> He gets <b>2 attacks</b> with his Attack action, PLUS "
    "<b>1 extra punch</b> as a bonus action (Martial Arts), <i>or</i> spend 1 Focus on <b>First Form: Devour</b> "
    "for a big 3d8+9 Force strike. That is <b>3 hits a turn</b>, and Devour gives the Focus back if it drops "
    "the target."))

# Special moves in two columns
h2("Stabby's Special Moves")
moves=[
    ('★ Igniting the Breath','<b>When he rolls initiative</b>, spend 1 Focus to light his breath. It burns until the fight ends. Every hit with the katana deals <b>+2 Force</b>, his Speed goes up <b>10 ft</b>, and he gets <b>advantage on Dexterity saves</b>.'),
    ('★ First Form: Devour','<b>Bonus action, 1 Focus.</b> Move up to 15 ft without provoking, then one katana strike for <b>3d8+9 Force</b> instead of normal damage. <b>If it drops the target, he gets the Focus back.</b> <i>(This replaces Flurry of Blows.)</i>'),
    ('★ Beast Sense','Advantage on Survival to track, on Perception using smell or hearing, and on <b>Intimidation</b>.'),
    ('Stunning Strike','When he hits, spend 1 Focus: Con save DC 13. <b>Fail:</b> stunned until his '
        'next turn (huge in a boss fight). <b>Success:</b> still slowed, and the next attack on it '
        'has advantage.'),
    ('Patient Defense / Step of the Wind','Bonus action, free: <b>Disengage</b> (Patient Defense) or <b>Dash</b> (Step of the Wind). Spend <b>1 Focus</b> to upgrade either: Dodge as well (enemies hit him with disadvantage), or Disengage plus a doubled jump.'),
    ('Deflect Attack','Reaction: when hit by a punch/arrow/blade, lower the damage by <b>1d10+12</b>. If it hits 0, '
        'spend 1 Focus to fling it back at another enemy within 5 ft (DC 13 Dex save, 2d8+5).'),
    ('★ Empowered Strikes <i>(from level 6)</i>','On any <b>Unarmed Strike</b> he chooses <b>Force</b> damage or the normal type. Almost nothing resists Force, so his fists get through what his katana cannot. <i>(His own, not the wraps.)</i>'),
    ('Evasion <i>(new at 7!)</i> / Slow Fall / Metabolism','<b>Evasion:</b> on a Dex save for half damage, he takes <b>none</b> if he saves, half if he fails. <b>Slow Fall:</b> reaction, <b>35</b> less falling damage. <b>Uncanny Metabolism:</b> 1/day on initiative, regain <b>every spent Focus</b> + heal <b>7 + 1d8</b>. <i>(Save it for when he is hurt.)</i>'),
    ('Fury of the Small','When he hits a creature bigger than him (almost everyone!), deal +3 extra damage. '
        'He can do this 3 times per long rest, once per turn.'),
    ('Goblin Tricks','<b>Nimble Escape:</b> Disengage or Hide as a bonus action, every turn. <b>Goblin Gifts:</b> darkvision 60 ft; advantage on saves vs being charmed. Speaks Common, Goblin &amp; Orc.'),
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
story.append(Paragraph('Page 2: Gear &amp; Story', sub_st))
story.append(Spacer(1,8))

h2("Stabby's Stuff")
GN='<b><font color="%s">%%s</font></b>' % RED_HEX   # gear names: accent bold
gear=[
    ('Nichirin Katana <i>(new! the demon-slayer&rsquo;s blade)</i>','Sun-forged crimson steel, <b>+2</b> to hit and damage, and it counts as a Monk weapon. <b>Breath-Kindled Steel:</b> it glows blood-red when he ignites. <b>Cleansing Edge:</b> once a turn, when he hits a fiend, undead, shadow thing or anything twisted by planar corruption, that creature <b>cannot heal</b> and cannot hide from him in darkness until his next turn. <b>Attuned.</b>'),
    ('Candyfang Katana +1 <i>(kept, not carried)</i>','His old candy-striped blade, an heirloom on his belt now that the Nichirin has the job. Not attuned, so no cold rider and no Sugar Rush.'),
    ('Wraps of Unarmed Power +2<br/><i>(new! Lilly made these for him)</i>','Cloth hand-wraps she spent the year building, stitched with her own sigils. His <b>fists and feet</b> now hit at <b>+2 to hit and +2 damage</b>. <b>No attunement.</b> <i>(The Force option on his punches is Empowered Strikes, a class feature he already has; the wraps are the +2.)</i> <i>(They do nothing for the katana: this is a punching gift.)</i>'),
    ('Repeating Longbow +1','A magic bow that makes its own arrows, never runs out. +1 to hit and damage. <i>Lilly built this one for him too, back at level 5.</i>'),
    ('Sash of the Swift Current (★ Elaria’s gift)','Scarlet stage-silk from the Wraithpine chest. +1 AC, +10 speed, plus Air Dance (fly for 1 minute, 1/day) and Feather Fall (1/day). Attuned.'),
    ('Explorer’s Pack','Backpack, bedroll, rope, torches, rations (the usual adventuring kit).'),
]
story.append(section_table([[Paragraph(GN%n,cell_st),Paragraph(d,cell_st)] for n,d in gear],
    [1.9*inch,5.4*inch], header=False))

h2("Stabby's Story")
story.append(Paragraph(
    "Stabby was born into the Bloodfang Clan, a fierce goblin tribe deep in the twisted woods of "
    "Bloodthorn Hollow. In a clan where the biggest goblin wins, little Stabby survived on speed, cunning, and "
    "pure chaos, he earned the name Sharpblade after beating a whole group of rival goblins using nothing "
    "but a broken sword.", body_st))
story.append(Spacer(1,4))
story.append(Paragraph(
    "One day he met Master Kaelon Windstep, a graceful monk of the Whispering Breeze Clan. Stabby was "
    "amazed by the monk’s smooth, flowing fighting style, so different from goblin brawling. He never "
    "became calm and disciplined, but he blended those moves into his own wild style: grace plus chaos. Then he "
    "left the Hollow looking for adventure… and found Lilly and Ursa, who were chasing magical "
    "creatures and enchanted potatoes. Stabby didn’t need any convincing, he jumped right in for the fun.", body_st))
story.append(Spacer(1,4))
story.append(Paragraph(
    "Two years of adventuring later, Stabby has fought shadow beasts, swum away from the sinking "
    "<b>Stormwind</b>, walked haunted <b>Wraithpine</b> (where Elaria's chest gave him the <b>Sash of the "
    "Swift Current</b>), and helped free the clockwork city of <b>Gearhaven</b>. When the heroes parted "
    "for a year, he went home. He walked into the twisted woods of Bloodthorn Hollow and <b>burned the "
    "blight out of them</b>, root and all, then climbed the mountain called Kettlecrown, where the "
    "<b>Sunward Vigil</b> taught him stillness and forged him the <b>Nichirin</b>, a blade that burns "
    "corruption. He came down a <b>Warrior of Beast Breathing</b>, taught the smallest goblins of the "
    "Hollow his one-second count, and was offered his father's seat; he said <b>not yet</b>. Nobody in "
    "the Hollow calls him the runt anymore.", body_st))

h2("Personality")
per=[
    ('Chaotic and mischievous','Loves trouble, excitement, and stirring things up. Acts first, thinks later (maybe).'),
    ('Ideal: Freedom','“No one tells me what to do.” Everyone should live life their own way.'),
    ('Bond: His Crew','Fiercely loyal to Lilly and Ursa, his first real friends. “They’re my crew, no one messes with them but me.”'),
    ('Flaw: Reckless','Leaps into danger with no plan. “Who needs a plan when you’ve got guts?”'),
]
pc=[Paragraph(f'<b><font color="{RED_HEX}">{t}</font></b><br/><i>{d}</i>',
              S('pc',fontName='Times-Roman',fontSize=8,textColor=INK,leading=10)) for t,d in per]
pt=Table([[pc[0],pc[1]],[pc[2],pc[3]]],colWidths=[3.65*inch,3.65*inch])
pt.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.5,LINE),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
    ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),]))
story.append(Spacer(1,3)); story.append(pt); story.append(Spacer(1,8))
story.append(callout('<b>Fun Facts:</b> &nbsp;Stabby is a boy goblin, age 9, just 2 feet 4 inches tall and 30 pounds, '
    'small but mighty! &bull; Green skin, red eyes, green hair. &bull; He carries a creepy little idol that gives '
    'him strange dreams. &bull; His old clan, the Bloodfang, are part of his past, and maybe future allies.', fill=None))

doc=SimpleDocTemplate('../stabby_sharpblade_sheet_v3.pdf',pagesize=letter,
    leftMargin=0.55*inch,rightMargin=0.55*inch,topMargin=0.45*inch,bottomMargin=0.5*inch)
frame = make_frame('Stabby Sharpblade')
doc.build(story, onFirstPage=frame, onLaterPages=frame)
print('built ../stabby_sharpblade_sheet_v3.pdf')
