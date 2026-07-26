#!/usr/bin/env python3
"""Lilly Glimmergear character sheet, 3 pages, frost-blue theme, 2024 rules.
Ported onto the shared published-book template (sheet_style.py) and content-
synced to the committed lilly_glimmergear_sheet_v3.pdf, which is newer than
the original browser-session script (WIS 12, 2024 deep gnome printing, house-
ruled pick-a-blast cannon, Tinker's Magic with Mending, plain steel shield).
Page 1: combat dashboard + cannon. Page 2: powers, gear, story. Page 3: spellbook."""
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
BLUE     = sheet_style.ACCENTS['lilly']      # frost-blue accent
BLUE_HEX = '#1F6FB8'
BLUE_LT  = colors.HexColor('#E4EFF8')        # pale fill for table bands
LINE     = colors.HexColor('#BBD6EC')

styles = getSampleStyleSheet()
def S(name, **kw):
    base = kw.pop('parent', styles['Normal'])
    return ParagraphStyle(name, parent=base, **kw)

_st = sheet_style.styles(BLUE)
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

def stat_strip(pairs):
    labels=[Paragraph(l,white_lbl) for l,_ in pairs]
    vals=[Paragraph(str(v),big_num) for _,v in pairs]
    t=Table([labels,vals], colWidths=[7.3*inch/len(pairs)]*len(pairs))
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE),('BACKGROUND',(0,1),(-1,1),BLUE_LT),
        ('GRID',(0,0),(-1,-1),0.5,colors.white),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,0),3),('BOTTOMPADDING',(0,0),(-1,0),3),
        ('TOPPADDING',(0,1),(-1,1),5),('BOTTOMPADDING',(0,1),(-1,1),5)]))
    return t

def ability_strip(abils):
    labels=[Paragraph(l,white_lbl) for l,_,_ in abils]
    sc=[Paragraph(str(s),big_num) for _,s,_ in abils]
    mod_st=S('m',fontName='Helvetica',fontSize=8.5,textColor=GREY,alignment=1,leading=9)
    md=[Paragraph(m,mod_st) for _,_,m in abils]
    t=Table([labels,sc,md], colWidths=[7.3*inch/6]*6)
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,0),BLUE),('BACKGROUND',(0,1),(-1,2),BLUE_LT),
        ('GRID',(0,0),(-1,-1),0.5,colors.white),('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,0),2),('BOTTOMPADDING',(0,0),(-1,0),2),
        ('TOPPADDING',(0,1),(-1,1),3),('BOTTOMPADDING',(0,1),(-1,1),0),
        ('TOPPADDING',(0,2),(-1,2),0),('BOTTOMPADDING',(0,2),(-1,2),3)]))
    return t

def section_table(data, col_widths, header=True):
    t=Table(data, colWidths=col_widths)
    style=[('VALIGN',(0,0),(-1,-1),'TOP'),('GRID',(0,0),(-1,-1),0.5,LINE),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,BLUE_LT])]
    if header:
        style+=[('BACKGROUND',(0,0),(-1,0),BLUE),('TEXTCOLOR',(0,0),(-1,0),colors.white),
            ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),('FONTSIZE',(0,0),(-1,0),7.6)]
    t.setStyle(TableStyle(style)); return t

def callout(text):
    p=Paragraph(text,note_st); t=Table([[p]],colWidths=[7.3*inch])
    t.setStyle(TableStyle([('BACKGROUND',(0,0),(-1,-1),BLUE_LT),('BOX',(0,0),(-1,-1),1,BLUE),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6)]))
    return t

story=[]
def h2(text):
    # Section header with the thin accent rule the living sheets use
    story.append(Paragraph(text, S('h2r', parent=h2_st, spaceAfter=1)))
    story.append(HRFlowable(width='100%', thickness=0.7, color=BLUE, spaceAfter=3))

# ===== PAGE 1 =====
hdr=Table([[Image('lilly_new.png',width=1.35*inch,height=1.35*inch),
    [Paragraph('Lilly Glimmergear',title_st),
     Paragraph('Deep Gnome &bull; Artificer (Artillerist) &bull; Level 5',sub_st),Spacer(1,3),
     Paragraph('Played by the inventor of the group. Lilly builds a magic cannon, zaps things with '
               'frost, and carries the Essence Sphere that holds Pikachu’s spark.',flav_st)]]],
    colWidths=[1.5*inch,5.8*inch])
hdr.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(1,0),(1,0),10)]))
story.append(hdr); story.append(Spacer(1,8))

story.append(stat_strip([('ARMOR CLASS',20),('HIT POINTS',38),('SPEED','25 ft'),
                         ('INITIATIVE','+2'),('SAVE DC',16),('SPELL ATK','+8')]))
story.append(Spacer(1,4))
story.append(ability_strip([('STR',8,'-1'),('DEX',14,'+2'),('CON',14,'+2'),
                            ('INT',20,'+5'),('WIS',12,'+1'),('CHA',8,'-1')]))
story.append(Paragraph('Best saves: Con +5, Int +8. INT powers all her magic.',small_it))

h2("All of Lilly's Skills")
TR='<b><font color="#134A7A">%s</font></b>'   # trained: blue, per the caption
skills=[
    ('Acrobatics +2','Athletics -1','Insight +1','Medicine +1','Performance -1','Sleight of Hand +2'),
    (TR%'Animal Handling +4','Deception -1','Intimidation -1','Nature +5','Persuasion -1','Stealth +2'),
    (TR%'Arcana +8','History +5',TR%'Investigation +8','Perception +1','Religion +5',TR%'Survival +4'),
]
sk=Table([[Paragraph(c,cell_st) for c in r] for r in skills], colWidths=[(7.3/6)*inch]*6)
sk.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.3,BLUE_LT),
    ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),3)]))
story.append(sk)
story.append(Paragraph('Blue = trained. Best: Arcana &amp; Investigation +8.',small_it))

h2("What Lilly Does in a Fight")
atk=[['Attack','To Hit','Damage'],
    ['True Strike (frost dagger)','+9','1d4 + 1d4 cold + 6 + 1d6 radiant + 1d8 + 2 frost'],
    ['Cannon: Flamethrower','DC 16 Dex','2d8+2 fire in a 15-ft cone'],
    ['Cannon: Force Ballista','+8','2d8+2 force, push 5 ft (120 ft away)'],
    ['Fire Bolt (cantrip)','+8','2d10 fire + 1d8 + 2 frost (120 ft)']]
story.append(section_table([atk[0]] + [[Paragraph(c,cell_st) for c in r] for r in atk[1:]],
    [3.0*inch,1.0*inch,3.3*inch]))
story.append(Spacer(1,4))
story.append(callout("<b>How Lilly's turn works:</b> She fires her cannon as a <b>BONUS action</b> AND does "
    "something else with her main action (cast a spell, stab with True Strike, or Fire Bolt). She gets to do "
    "<b>both every turn!</b>"))

h2("Lilly's Eldritch Cannon")
story.append(Paragraph('The Cannon — can be attacked and broken. Mending repairs it 2d6.', small_it))
cannon = stat_strip([('AC',18),('HIT POINTS',25),('SIZE','Small/Tiny'),('SPEED','15 ft (legs)')])
story.append(cannon)
story.append(Spacer(1,3))
LBL='<b><font color="%s">%%s</font></b>' % BLUE_HEX   # row labels: accent bold
cdata=[
    [Paragraph(LBL%'Pick the blast when she fires',cell_st), Paragraph('<b>New rule — the cannon is no longer '
        'locked to one mode!</b> Each time she fires it, choose: <b>Flamethrower</b> (15-ft cone, 2d8+2 fire), '
        '<b>Force Ballista</b> (one faraway enemy, 2d8+2 force, push 5 ft), or <b>Protector</b> (shield-points '
        'to Lilly &amp; friends within 10 ft, 1d8+5).',cell_st)],
    [Paragraph(LBL%'How to use it',cell_st), Paragraph('Fire it with a <b>bonus action</b> — so Lilly still gets '
        'her main action the same turn! Free to deploy or recall (Pocket Dynamo), +2 damage, lasts a full 24 hours. '
        'Ignores conditions/poison/psychic; enemies must smash it to 0 HP.',cell_st)],
]
story.append(section_table(cdata, [1.4*inch, 5.9*inch], header=False))

story.append(PageBreak())

# ===== PAGE 2 =====
story.append(Paragraph('Lilly Glimmergear', S('p2t',fontName='Times-Bold',fontSize=15,
            textColor=BLUE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 2 — Powers, Gear &amp; Story', sub_st))
story.append(Spacer(1,8))

h2("Lilly's Special Powers")
powers=[
    ('Replicate Magic Item','Lilly builds magic gear for the team! Her two creations are in use now — her own +1 Half Plate and the +1 Repeating Longbow she made for Stabby.'),
    ("Tinker's Magic",'Knows the Mending cantrip (fix broken things). Can also conjure handy mundane gear — rope, a torch, ball bearings — that lasts until her next rest. Great for puzzles and traps.'),
    ('The Right Tool','With her tools, Lilly can magically make any set of artisan tools she needs (1 hour).'),
    ('Deep Gnome Gifts','<b>Gnomish Magic Resistance:</b> advantage on Int, Wis &amp; Cha saves vs spells. '
        '<b>Svirfneblin Camouflage:</b> advantage on Stealth checks. <b>Gift of the Svirfneblin:</b> casts '
        '<i>Disguise Self</i> and <i>Nondetection</i> free, 1/long rest each. Sees in the dark 120 ft. '
        'Speaks Common, Gnomish &amp; Undercommon.'),
]
story.append(section_table([[Paragraph(LBL%n,cell_st),Paragraph(d,cell_st)] for n,d in powers],
    [2.0*inch,5.3*inch], header=False))

h2("Lilly's Stuff")
gear=[
    ('Essence Sphere','A steampunk orb holding Pikachu’s spark. Lilly’s big quest item — she wants to give Pikachu a body again.'),
    ('Frostbite Shard Dagger +1','Her magic frost dagger (1d4 piercing + 1d4 cold). Spell focus AND ‘arcane firearm’ — adds 1d8 frost to one spell she casts through it, plus +2 frost on any spell. +1 to hit.'),
    ('Pocket Dynamo (★ Elaria’s gift)','From the Wraithpine chest. Summon/recall her cannon for free, lasts 24 hours, +2 damage. Reformat (1/long rest, action) — now mostly spare, since every cannon picks its blast when it fires. Needs attunement.'),
    ('+1 Half Plate (her creation)','Half plate she replicated with Replicate Magic Item. Base of her AC 20.'),
    ('Shield','A sturdy steel shield. Adds +2 to her armor.'),
]
story.append(section_table([[Paragraph(LBL%n,cell_st),Paragraph(d,cell_st)] for n,d in gear],
    [1.9*inch,5.4*inch], header=False))

h2("Lilly's Story")
story.append(Paragraph(
    "Lilly grew up in Deepforge Hollow, a svirfneblin (deep gnome) city deep in the Underdark, surrounded by "
    "the hum of machines and magic. Her mother, Poots Glimmergear, was a famous artificer and adventurer who "
    "inspired Lilly to tinker from the time she was tiny. Lilly trained at the Glimmerspire Academy of Artifice "
    "under Master Droven Sparkwick, and her proudest creation was her very own arcane turret — the cannon she "
    "still fights with today.", body_st))
story.append(Spacer(1,4))
story.append(Paragraph(
    "On her seventh birthday, Poots handed Lilly the Essence Sphere — a device holding the spark of "
    "Pikachu, a lost companion from her mother’s adventuring days. Lilly’s quest became clear: find a way to "
    "give Pikachu a body again. That mission led her out of the Underdark to find Ursa, and along the way she "
    "met Stabby. The three became an unlikely team, chasing the mystery of the Essence Sphere — and the "
    "planar cracks tied to the sleeping goddess Elaria.", body_st))

h2("Personality")
per=[
    ('Inventive and curious','Always tinkering, always asking “why settle for what’s already made when you can build something better?”'),
    ('Ideal — Creativity','“There’s always a new way to make something better.” Lilly believes creativity solves any problem.'),
    ('Bond — Her Friends','Fiercely loyal to Ursa and Stabby. “Together, we’ll solve these mysteries and prove ourselves.”'),
    ('Flaw — Impatient','When a plan doesn’t work right away, she gets frustrated. “Why isn’t this working already?”'),
]
pc=[Paragraph(f'<b><font color="{BLUE_HEX}">{t}</font></b><br/><i>{d}</i>',
              S('pc',fontName='Times-Roman',fontSize=8,textColor=INK,leading=10)) for t,d in per]
pt=Table([[pc[0],pc[1]],[pc[2],pc[3]]],colWidths=[3.65*inch,3.65*inch])
pt.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.5,LINE),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
    ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6)]))
story.append(Spacer(1,3)); story.append(pt)

story.append(PageBreak())

# ===== PAGE 3 — SPELLBOOK =====
story.append(Paragraph('Lilly Glimmergear', S('p3t',fontName='Times-Bold',fontSize=15,
            textColor=BLUE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 3 — Spellbook', sub_st))
story.append(Spacer(1,7))
story.append(Paragraph('Slots per day: 4 first-level, 2 second-level. Cantrips (★) are free forever. '
    'She prepares 7 spells; the four marked Always Prepared are free from her Artillerist subclass and '
    'don’t count toward that. The +1d8 frost on a spell is her dagger’s arcane firearm — it adds to one '
    'spell she casts each turn (she only casts one anyway). The +2 frost rides along on any spell cast '
    'through the dagger.', small_it))
story.append(Spacer(1,6))

# Open two-column spell list (name / meta / text), per the living sheet
sp_name = S('spn', fontName='Times-Bold', fontSize=9.2, textColor=BLUE, leading=11, spaceBefore=6)
sp_meta = S('spm', fontName='Times-Italic', fontSize=7.2, textColor=GREY, leading=8.6, spaceAfter=1)
sp_text = S('spx', fontName='Times-Roman', fontSize=7.9, textColor=INK, leading=9.9)

spells=[
    ('★ True Strike',
        'Cantrip • Action • Self (5 ft reach) • Instant',
        'Stab with the Frostbite dagger using INT. Melee attack +9 to hit. On a hit: 1d4 + '
        '1d4 cold + 6 + 1d6 radiant + 1d8 frost (arcane firearm) + 2 frost (frostbite). Her '
        'best up-close hit.'),
    ('★ Fire Bolt',
        'Cantrip • Action • 120 ft • Instant',
        'Hurl fire at one target. Ranged spell attack +8 to hit: 2d10 fire + 1d8 + 2 frost '
        '(dagger). Her reliable ranged poke — never runs out.'),
    ('★ Mending',
        'Cantrip • 1 minute • Touch • Instant',
        'Repair a single break or tear in an object — a snapped chain, a torn cloak, a '
        'cracked gear. No bigger than 1 ft. Free from Tinker’s Magic. Also heals her '
        'cannon 2d6!'),
    ('Absorb Elements',
        '1st • Reaction (when hit by the damage) • Self • 1 round',
        'Trigger when she takes acid/cold/fire/lightning/thunder: take half of it, and her '
        'next melee hit deals +1d6 of that type. A great defensive reaction.'),
    ('Shield — Always Prepared',
        '1st • Reaction (when hit / by Magic Missile) • Self • 1 round',
        'Snap up a force wall: +5 AC until the start of her next turn (can turn a hit into a '
        'miss) and take no damage from Magic Missile. Cast after seeing the attack roll.'),
    ('Thunderwave — Always Prepared',
        '1st • Action • Self (15-ft cube) • Instant',
        'Foes in a 15-ft cube make a Con save DC 16: on a fail, 2d8 thunder + 1d8 + 2 '
        'frost (dagger) and shoved 10 ft away; half and no shove on a success.'),
    ('Catapult',
        '1st • Action • 60 ft • Instant',
        'Fling a loose object (up to 5 lb) at a foe. Dex save DC 16: on a fail, 3d8 '
        'bludgeoning + 1d8 + 2 frost (dagger); no damage on a success. No attack roll — '
        'it’s a save.'),
    ('Snare',
        '1st • 1 minute to set • Touch • 8 hr trap',
        'Lay a hidden magic rope-trap on the floor. The first creature to step in makes a '
        'Dex save DC 16 or is yanked upside-down, restrained in the air. Set it before a '
        'fight as a surprise.'),
    ('Faerie Fire',
        '1st • Action • 60 ft • Concentration, 1 min',
        'Foes in a 20-ft cube make a Dex save DC 16; on a fail they’re outlined in light. '
        'Attacks vs them have advantage and they can’t be invisible. Strong team setup.'),
    ("Tasha's Caustic Brew",
        '1st • Action • 30 ft line • Concentration, 1 min',
        'Spray acid in a 30-ft line (Dex save to avoid being coated). A coated creature '
        'takes 2d4 acid + 1d8 + 2 frost (dagger) at the start of each of its turns until it uses '
        'an action to wash off.'),
    ('Scorching Ray — Always Prepared',
        '2nd • Action • 120 ft • Instant',
        'Fire three rays. Each is a separate ranged spell attack +8 to hit: 2d6 fire each, plus '
        '1d8 + 2 frost (dagger, once). Aim them all at one foe or split them up.'),
    ('Shatter — Always Prepared',
        '2nd • Action • 60 ft (10-ft sphere) • Instant',
        'A loud burst. Creatures in a 10-ft sphere make a Con save DC 16: 3d8 thunder + '
        '1d8 + 2 frost (dagger) on a fail, half on success. Extra effective vs metal/stone '
        'foes.'),
    ('Heat Metal',
        '2nd • Action • 60 ft • Concentration, 1 min',
        'Make a metal object/armor glow red-hot: 2d8 fire + 1d8 + 2 frost (dagger) '
        'instantly, and bonus action each turn to deal it again. The holder makes a Con '
        'save or drops the item. Brutal vs armored foes.'),
    ('Web',
        '2nd • Action • 60 ft (20-ft cube) • Concentration, 1 hr',
        'Fill a 20-ft cube with sticky webs (difficult terrain). Creatures there make a Dex '
        'save DC 16 or are restrained; restrained creatures can retry with a Str check. '
        'Locks down a crowd.'),
]
def spell_entry(name, meta, text):
    return [Paragraph(name, sp_name), Paragraph(meta, sp_meta), Paragraph(text, sp_text)]
half=(len(spells)+1)//2
lcol=[f for sp in spells[:half] for f in spell_entry(*sp)]
rcol=[f for sp in spells[half:] for f in spell_entry(*sp)]
grid=Table([[lcol,rcol]],colWidths=[3.65*inch]*2)
grid.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LINEAFTER',(0,0),(0,0),0.5,LINE),
    ('LEFTPADDING',(0,0),(0,0),0),('RIGHTPADDING',(0,0),(0,0),9),
    ('LEFTPADDING',(1,0),(1,0),9),('RIGHTPADDING',(1,0),(1,0),0)]))
story.append(grid)

doc=SimpleDocTemplate('../lilly_glimmergear_sheet_v3.pdf',pagesize=letter,
    leftMargin=0.55*inch,rightMargin=0.55*inch,topMargin=0.45*inch,bottomMargin=0.5*inch)
frame = make_frame('Lilly Glimmergear')
doc.build(story, onFirstPage=frame, onLaterPages=frame)
print('built ../lilly_glimmergear_sheet_v3.pdf')
