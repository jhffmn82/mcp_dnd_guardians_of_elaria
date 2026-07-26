#!/usr/bin/env python3
"""Lilly Glimmergear — rebuilt on the locked template with new portrait.
Frost-blue theme, 3 pages, all content verbatim from her finalized sheet."""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, PageBreak)

BLUE     = colors.HexColor('#2F73B5')   # frost blue primary
BLUE_DK  = colors.HexColor('#1F4F80')
BLUE_LT  = colors.HexColor('#E4EFF8')
BLUE_MID = colors.HexColor('#A9CBE8')
INK      = colors.HexColor('#22272E')
GREY     = colors.HexColor('#555555')
LINE     = colors.HexColor('#BBD6EC')

styles = getSampleStyleSheet()
def S(name, **kw):
    base = kw.pop('parent', styles['Normal']); return ParagraphStyle(name, parent=base, **kw)

title_st = S('t', fontName='Helvetica-Bold', fontSize=26, textColor=BLUE, leading=28)
sub_st   = S('s', fontName='Helvetica', fontSize=10.5, textColor=GREY, leading=13)
flav_st  = S('f', fontName='Helvetica-Oblique', fontSize=9.5, textColor=INK, leading=12.5)
h2_st    = S('h2', fontName='Helvetica-Bold', fontSize=13, textColor=BLUE, leading=15, spaceBefore=8, spaceAfter=3)
body_st  = S('b', fontName='Helvetica', fontSize=8.6, textColor=INK, leading=11)
small_it = S('si', fontName='Helvetica-Oblique', fontSize=8, textColor=GREY, leading=10)
cell_st  = S('c', fontName='Helvetica', fontSize=8.3, textColor=INK, leading=10)
cellb_st = S('cb', fontName='Helvetica-Bold', fontSize=8.3, textColor=INK, leading=10)
white_lbl= S('wl', fontName='Helvetica-Bold', fontSize=7.2, textColor=colors.white, leading=8, alignment=1)
big_num  = S('bn', fontName='Helvetica-Bold', fontSize=15, textColor=INK, leading=16, alignment=1)
note_st  = S('n', fontName='Helvetica', fontSize=8.4, textColor=INK, leading=11)

def stat_strip(pairs):
    labels=[Paragraph(l,white_lbl) for l,_ in pairs]; vals=[Paragraph(str(v),big_num) for _,v in pairs]
    t=Table([labels,vals], colWidths=[7.3*inch/len(pairs)]*len(pairs))
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE),('BACKGROUND',(0,1),(-1,1),BLUE_LT),
        ('GRID',(0,0),(-1,-1),0.5,colors.white),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,0),3),('BOTTOMPADDING',(0,0),(-1,0),3),
        ('TOPPADDING',(0,1),(-1,1),5),('BOTTOMPADDING',(0,1),(-1,1),5)])); return t

def ability_strip(abils):
    labels=[Paragraph(l,white_lbl) for l,_,_ in abils]; sc=[Paragraph(str(s),big_num) for _,s,_ in abils]
    mod_st=S('m',fontName='Helvetica',fontSize=8.5,textColor=GREY,alignment=1,leading=9)
    md=[Paragraph(m,mod_st) for _,_,m in abils]
    t=Table([labels,sc,md], colWidths=[7.3*inch/6]*6)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE),('BACKGROUND',(0,1),(-1,2),BLUE_LT),
        ('GRID',(0,0),(-1,-1),0.5,colors.white),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,0),2),('BOTTOMPADDING',(0,0),(-1,0),2),
        ('TOPPADDING',(0,1),(-1,1),3),('BOTTOMPADDING',(0,1),(-1,1),0),
        ('TOPPADDING',(0,2),(-1,2),0),('BOTTOMPADDING',(0,2),(-1,2),3)])); return t

def section_table(data, col_widths, header=True):
    t=Table(data, colWidths=col_widths)
    style=[('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),0.5,LINE),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,BLUE_LT])]
    if header:
        style+=[('BACKGROUND',(0,0),(-1,0),BLUE),('TEXTCOLOR',(0,0),(-1,0),colors.white),
            ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,0),8.3)]
    t.setStyle(TableStyle(style)); return t

def callout(text):
    p=Paragraph(text,note_st); t=Table([[p]],colWidths=[7.3*inch])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),BLUE_LT),('BOX',(0,0),(-1,-1),1,BLUE),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)])); return t

story=[]
# ===== PAGE 1 =====
hdr=Table([[Image('lilly_new.png',width=1.35*inch,height=1.35*inch),
    [Paragraph('Lilly Glimmergear',title_st),
     Paragraph('Deep Gnome &bull; Artificer (Artillerist) &bull; Level 5',sub_st),Spacer(1,3),
     Paragraph('Played by the inventor of the group. Lilly builds a magic cannon, zaps things with '
               'frost, and carries the Essence Sphere that holds Pikachu\u2019s spark.',flav_st)]]],
    colWidths=[1.5*inch,5.8*inch])
hdr.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(1,0),(1,0),10)]))
story.append(hdr); story.append(Spacer(1,8))

story.append(stat_strip([('ARMOR CLASS',20),('HIT POINTS',38),('SPEED','25 ft'),
                         ('INITIATIVE','+2'),('SAVE DC',16),('SPELL ATK','+8')]))
story.append(Spacer(1,4))
story.append(ability_strip([('STR',8,'-1'),('DEX',14,'+2'),('CON',14,'+2'),
                            ('INT',20,'+5'),('WIS',8,'-1'),('CHA',8,'-1')]))
story.append(Paragraph('Best saves: Con +5, Int +8. INT powers all her magic.',small_it))

story.append(Paragraph("All of Lilly's Skills", h2_st))
skills=[
    ('Acrobatics +3','<b>History +5</b>','<b>Nature +5</b>','Sleight of Hand +3'),
    ('<b>Animal Handling +2</b>','Insight -1','Perception -1','Stealth +3'),
    ('<b>Arcana +8</b>','Intimidation -1','Performance -1','<b>Survival +2</b>'),
    ('Athletics -1','<b>Investigation +8</b>','Persuasion -1',''),
    ('Deception -1','Medicine -1','<b>Religion +5</b>',''),
]
sk=Table([[Paragraph(c,cell_st) for c in r] for r in skills], colWidths=[1.825*inch]*4)
sk.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.3,BLUE_LT),
    ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),('LEFTPADDING',(0,0),(-1,-1),5)]))
story.append(sk)
story.append(Paragraph('Blue = trained. Best: Arcana &amp; Investigation +8.',small_it))

story.append(Paragraph("What Lilly Does in a Fight", h2_st))
atk=[['Attack','To Hit','Damage'],
    ['True Strike (frost dagger)','+9','1d4+1 + 1d6 radiant + 1d8+2 frost'],
    ['Cannon: Flamethrower','DC 16 Dex','2d8 +2 fire in a 15-ft cone'],
    ['Cannon: Force Ballista','+8','2d8 +2 force, push 5 ft (120 ft away)'],
    ['Fire Bolt (cantrip)','+8','2d10 fire + 1d8 + 2 frost (120 ft)']]
story.append(section_table([[Paragraph(c,cellb_st if i==0 else cell_st) for c in r]
    for i,r in enumerate(atk)], [3.0*inch,1.0*inch,3.3*inch]))
story.append(Spacer(1,4))
story.append(callout("<b>How Lilly's turn works:</b> She fires her cannon as a <b>BONUS action</b> AND does "
    "something else with her main action (cast a spell, stab with True Strike, or Fire Bolt). She gets to do "
    "<b>both every turn!</b>"))

story.append(Paragraph("Lilly's Eldritch Cannon", h2_st))
story.append(Paragraph('The Cannon \u2014 can be attacked and broken.', small_it))
cannon = stat_strip([('AC',18),('HIT POINTS',25),('SIZE','Small/Tiny'),('SPEED','15 ft (legs)')])
story.append(cannon)
story.append(Spacer(1,3))
cdata=[
    [Paragraph('<b>Three blasts</b>',cell_st), Paragraph('<b>Flamethrower:</b> burns a 15-ft cone (2d8+2 fire). '
        '<b>Force Ballista:</b> blasts one faraway enemy (2d8+2 force, push 5 ft). '
        '<b>Protector:</b> gives Lilly &amp; friends shield-points (1d8+5).',cell_st)],
    [Paragraph('<b>How to use it</b>',cell_st), Paragraph('Fire it with a <b>bonus action</b> \u2014 so Lilly still gets '
        'her main action for a spell or attack the same turn! Free to deploy (Pocket Dynamo). Ignores '
        'conditions/poison/psychic; enemies must smash it to 0 HP. Lasts a full day.',cell_st)],
]
story.append(section_table(cdata, [1.4*inch, 5.9*inch], header=False))

story.append(PageBreak())

# ===== PAGE 2 =====
story.append(Paragraph('Lilly Glimmergear', S('p2t',fontName='Helvetica-Bold',fontSize=15,
            textColor=BLUE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 2 — Powers, Gear &amp; Story', sub_st))
story.append(Spacer(1,8))

story.append(Paragraph("Lilly's Special Powers", h2_st))
powers=[
    ('Replicate Magic Item','Lilly already built magic gear for the team! Her two creations are in use now \u2014 her own +1 Armor and +1 Shield.'),
    ('Magic Tinkering','Give a tiny object a fun trick: glow like a light, play a 6-second message, make a sound, or show a picture. Great for puzzles and pranks.'),
    ('The Right Tool','With her tools, Lilly can magically make any set of artisan tools she needs (1 hour).'),
    ('Gnome Tricks','Hard to fool: advantage on Int, Wis &amp; Cha saves vs spells. Stone Camouflage: advantage on Stealth in rocky places. Sees in the dark 120 ft. Speaks Common, Gnomish &amp; Undercommon.'),
]
story.append(section_table([[Paragraph(f'<b>{n}</b>',cell_st),Paragraph(d,cell_st)] for n,d in powers],
    [2.0*inch,5.3*inch], header=False))

story.append(Paragraph("Lilly's Stuff", h2_st))
gear=[
    ('Essence Sphere','A steampunk orb holding Pikachu\u2019s spark. Lilly\u2019s big quest item \u2014 she wants to give Pikachu a body again.'),
    ('Frostbite Shard Dagger +1','Her magic frost dagger. Spell focus AND \u2018arcane firearm\u2019 \u2014 spells cast through it hit harder and add frost. +1 to hit and damage.'),
    ('Pocket Dynamo<br/><i>(new! \u2605 Elaria\u2019s gift)</i>','From the Wraithpine chest. Summon/recall her cannon for free, lasts 24 hours, +2 damage, change its type once per rest. Needs attunement.'),
    ('+1 Armor (her creation)','Half plate she enchanted herself. Part of her AC 20.'),
    ('+1 Shield (her creation)','A shield she enchanted. Adds +3 to her armor.'),
]
story.append(section_table([[Paragraph(n,cell_st),Paragraph(d,cell_st)] for n,d in gear],
    [1.9*inch,5.4*inch], header=False))

story.append(Paragraph("Lilly's Story", h2_st))
story.append(Paragraph(
    "Lilly grew up in <b>Deepforge Hollow</b>, a svirfneblin (deep gnome) city deep in the Underdark, surrounded by "
    "the hum of machines and magic. Her mother, <b>Poots Glimmergear</b>, was a famous artificer and adventurer who "
    "inspired Lilly to tinker from the time she was tiny. Lilly trained at the <b>Glimmerspire Academy of Artifice</b> "
    "under Master Droven Sparkwick, and her proudest creation was her very own arcane turret \u2014 the cannon she "
    "still fights with today.", body_st))
story.append(Spacer(1,4))
story.append(Paragraph(
    "On her seventh birthday, Poots handed Lilly the <b>Essence Sphere</b> \u2014 a device holding the spark of "
    "Pikachu, a lost companion from her mother\u2019s adventuring days. Lilly\u2019s quest became clear: find a way to "
    "give Pikachu a body again. That mission led her out of the Underdark to find <b>Ursa</b>, and along the way she "
    "met <b>Stabby</b>. The three became an unlikely team, chasing the mystery of the Essence Sphere \u2014 and the "
    "planar cracks tied to the sleeping goddess <b>Elaria</b>.", body_st))

per=[
    ('Personality','Inventive and curious \u2014 always tinkering, always asking \u201cwhy settle for what\u2019s already made when you can build something better?\u201d'),
    ('Ideal — Creativity','\u201cThere\u2019s always a new way to make something better.\u201d Lilly believes creativity solves any problem.'),
    ('Bond — Her Friends','Fiercely loyal to Ursa and Stabby. \u201cTogether, we\u2019ll solve these mysteries and prove ourselves.\u201d'),
    ('Flaw — Impatient','When a plan doesn\u2019t work right away, she gets frustrated. \u201cWhy isn\u2019t this working already?\u201d'),
]
pc=[Paragraph(f'<b>{t}</b><br/>{d}',S('pc',fontName='Helvetica',fontSize=8,textColor=INK,leading=10)) for t,d in per]
pt=Table([[pc[0],pc[1]],[pc[2],pc[3]]],colWidths=[3.65*inch,3.65*inch])
pt.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.5,LINE),
    ('BACKGROUND',(0,0),(-1,-1),BLUE_LT),('VALIGN',(0,0),(-1,-1),'TOP'),
    ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
    ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6)]))
story.append(Spacer(1,3)); story.append(pt)

story.append(PageBreak())

# ===== PAGE 3 — SPELLBOOK =====
story.append(Paragraph('Lilly Glimmergear', S('p3t',fontName='Helvetica-Bold',fontSize=15,
            textColor=BLUE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 3 — Spellbook', sub_st))
story.append(Spacer(1,7))
story.append(Paragraph('Slots per day: 4 first-level, 2 second-level. Cantrips (\u2605) are free forever.', small_it))
story.append(Spacer(1,4))

def spell_card(name, meta, text):
    inner=[[Paragraph(f'<b>{name}</b>',S('scn',fontName='Helvetica-Bold',fontSize=9,textColor=BLUE_DK,leading=11))],
        [Paragraph(meta,S('sct',fontName='Helvetica-Oblique',fontSize=6.8,textColor=GREY,leading=8.2))],
        [Paragraph(text,S('scx',fontName='Helvetica',fontSize=7.6,textColor=INK,leading=9.6))]]
    t=Table(inner,colWidths=[3.55*inch])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(0,1),BLUE_LT),('BOX',(0,0),(-1,-1),0.6,BLUE_MID),
        ('LINEBELOW',(0,1),(0,1),0.4,BLUE_MID),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2),
        ('TOPPADDING',(0,2),(0,2),4),('BOTTOMPADDING',(0,2),(0,2),5)])); return t

cards=[
    spell_card('\u2605 True Strike',
        'Cantrip \u2022 Action \u2022 Self (5 ft reach) \u2022 Instant',
        'Stab with the Frostbite dagger using INT. Melee attack <b>+9 to hit</b>. On a hit: '
        '<b>1d4+1</b> + <b>1d6 radiant</b> + <b>1d8 frost</b> (arcane firearm) + <b>2 frost</b> (frostbite). Her best up-close hit.'),
    spell_card('\u2605 Fire Bolt',
        'Cantrip \u2022 Action \u2022 120 ft \u2022 Instant',
        'Hurl fire at one target. Ranged spell attack <b>+8 to hit</b>: <b>2d10 fire</b> + '
        '<b>1d8 + 2 frost</b> (dagger). Her reliable ranged poke \u2014 never runs out.'),
    spell_card('Absorb Elements',
        '1st \u2022 Reaction (when hit by the damage) \u2022 Self \u2022 1 round',
        'Trigger when she takes acid/cold/fire/lightning/thunder: <b>take half</b> of it, and her '
        '<b>next melee hit</b> deals +1d6 of that type. A great defensive reaction.'),
    spell_card('Shield',
        '1st \u2022 Reaction (when hit / by Magic Missile) \u2022 Self \u2022 1 round',
        'Snap up a force wall: <b>+5 AC</b> until the start of her next turn (can turn a hit into a miss) '
        'and take <b>no damage from Magic Missile</b>. Cast after seeing the attack roll.'),
    spell_card('Thunderwave',
        '1st \u2022 Action \u2022 Self (15-ft cube) \u2022 Instant',
        'Foes in a 15-ft cube make a <b>Con save DC 16</b>: on a fail, <b>2d8 thunder</b> + '
        '<b>1d8 + 2 frost</b> (dagger) and shoved <b>10 ft</b> away; half and no shove on a success.'),
    spell_card('Catapult',
        '1st \u2022 Action \u2022 60 ft \u2022 Instant',
        'Fling a loose object (up to 5 lb) at a foe. <b>Dex save DC 16</b>: on a fail, <b>3d8 bludgeoning</b> + '
        '<b>1d8 + 2 frost</b> (dagger); no damage on a success. No attack roll \u2014 it\u2019s a save.'),
    spell_card('Snare',
        '1st \u2022 1 minute to set \u2022 Touch \u2022 8 hr trap',
        'Lay a hidden magic rope-trap on the floor. The first creature to step in makes a <b>Dex save DC 16</b> '
        'or is <b>yanked upside-down, restrained</b> in the air. Set it before a fight as a surprise.'),
    spell_card('Faerie Fire',
        '1st \u2022 Action \u2022 60 ft \u2022 Concentration, 1 min',
        'Foes in a 20-ft cube make a <b>Dex save DC 16</b>; on a fail they\u2019re outlined in light. '
        'Attacks vs them have <b>advantage</b> and they <b>can\u2019t be invisible</b>. Strong team setup.'),
    spell_card("Tasha's Caustic Brew",
        '1st \u2022 Action \u2022 30 ft line \u2022 Concentration, 1 min',
        'Spray acid in a 30-ft line (Dex save to avoid being coated). A coated creature takes '
        '<b>2d4 acid</b> + <b>1d8 + 2 frost</b> (dagger) at the start of each of its turns until it uses an action to wash off.'),
    spell_card('Scorching Ray',
        '2nd \u2022 Action \u2022 120 ft \u2022 Instant',
        'Fire <b>three</b> rays. Each is a separate ranged spell attack <b>+8 to hit</b>: <b>2d6 fire</b> each, '
        'plus <b>1d8 + 2 frost</b> (dagger, once). Aim them all at one foe or split them up.'),
    spell_card('Shatter',
        '2nd \u2022 Action \u2022 60 ft (10-ft sphere) \u2022 Instant',
        'A loud burst. Creatures in a 10-ft sphere make a <b>Con save DC 16</b>: <b>3d8 thunder</b> + '
        '<b>1d8 + 2 frost</b> (dagger) on a fail, half on success. Extra effective vs metal/stone foes.'),
    spell_card('Heat Metal',
        '2nd \u2022 Action \u2022 60 ft \u2022 Concentration, 1 min',
        'Make a metal object/armor glow red-hot: <b>2d8 fire</b> + <b>1d8 + 2 frost</b> (dagger) instantly, '
        'and <b>bonus action each turn</b> to deal it again. The holder takes a <b>Con save</b> or drops the item. Brutal vs armored foes.'),
    spell_card('Web',
        '2nd \u2022 Action \u2022 60 ft (20-ft cube) \u2022 Concentration, 1 hr',
        'Fill a 20-ft cube with sticky webs (difficult terrain). Creatures there make a <b>Dex save DC 16</b> '
        'or are <b>restrained</b>; restrained creatures can retry with a <b>Str check</b>. Locks down a crowd.'),
]
rows=[]
for i in range(0,len(cards),2):
    chunk=cards[i:i+2]
    while len(chunk)<2: chunk.append(Paragraph('',body_st))
    rows.append(chunk)
grid=Table(rows,colWidths=[3.66*inch]*2)
grid.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2),
    ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3)]))
story.append(grid)

doc=SimpleDocTemplate('/home/claude/Lilly_Glimmergear_Sheet.pdf',pagesize=letter,
    leftMargin=0.55*inch,rightMargin=0.55*inch,topMargin=0.45*inch,bottomMargin=0.4*inch)
doc.build(story)
print('built Lilly_Glimmergear_Sheet.pdf')
