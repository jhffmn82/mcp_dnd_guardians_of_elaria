#!/usr/bin/env python3
"""Ursa Catchum character sheet, built on the locked Lilly/Stabby template.
Three pages, starlight-purple theme, kid language, 2024 rules. All numbers
image-verified from ursa5.pdf and Session_7.docx; summons verified vs 2024 SRD.
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                Image, PageBreak, KeepTogether)
from reportlab.lib.enums import TA_LEFT, TA_CENTER

# ---- Published-book styling (shared, committed in sheet_style.py) ----
import sheet_style
from sheet_style import make_frame
INK  = sheet_style.INK
GREY = sheet_style.GREY
PURPLE      = sheet_style.ACCENTS['ursa']    # starlight-purple accent
PURPLE_DK   = colors.HexColor('#4A357A')
PURPLE_LT   = colors.HexColor('#EDE7F6')     # pale fill for table bands
PURPLE_MID  = colors.HexColor('#B9A4DC')
LINE        = colors.HexColor('#C9B9E6')

styles = getSampleStyleSheet()

def S(name, **kw):
    base = kw.pop('parent', styles['Normal'])
    return ParagraphStyle(name, parent=base, **kw)

_st = sheet_style.styles(PURPLE)
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
    """Top stat strip: list of (LABEL, big value) tuples."""
    labels = [Paragraph(l, white_lbl) for l, _ in pairs]
    vals   = [Paragraph(str(v), big_num) for _, v in pairs]
    t = Table([labels, vals], colWidths=[ (7.3*inch)/len(pairs) ]*len(pairs))
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0), PURPLE),
        ('BACKGROUND',(0,1),(-1,1), PURPLE_LT),
        ('GRID',(0,0),(-1,-1), 0.5, colors.white),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,0),3),('BOTTOMPADDING',(0,0),(-1,0),3),
        ('TOPPADDING',(0,1),(-1,1),5),('BOTTOMPADDING',(0,1),(-1,1),5),
    ]))
    return t

def ability_strip(abils):
    """abils: list of (LABEL, score, mod)."""
    labels = [Paragraph(l, white_lbl) for l,_,_ in abils]
    rows_score = [Paragraph(str(s), big_num) for _,s,_ in abils]
    mod_st = S('m', fontName='Helvetica', fontSize=8.5, textColor=GREY, alignment=TA_CENTER, leading=9)
    rows_mod = [Paragraph(m, mod_st) for _,_,m in abils]
    t = Table([labels, rows_score, rows_mod], colWidths=[7.3*inch/6]*6)
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,0), PURPLE),
        ('BACKGROUND',(0,1),(-1,2), PURPLE_LT),
        ('GRID',(0,0),(-1,-1),0.5, colors.white),
        ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
        ('TOPPADDING',(0,0),(-1,0),2),('BOTTOMPADDING',(0,0),(-1,0),2),
        ('TOPPADDING',(0,1),(-1,1),3),('BOTTOMPADDING',(0,1),(-1,1),0),
        ('TOPPADDING',(0,2),(-1,2),0),('BOTTOMPADDING',(0,2),(-1,2),3),
    ]))
    return t

def section_table(data, col_widths, header=True, header_bg=PURPLE):
    t = Table(data, colWidths=col_widths)
    style = [
        ('VALIGN',(0,0),(-1,-1),'TOP'),
        ('GRID',(0,0),(-1,-1),0.5, LINE),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),3),('BOTTOMPADDING',(0,0),(-1,-1),3),
        ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white, PURPLE_LT]),
    ]
    if header:
        style += [('BACKGROUND',(0,0),(-1,0), header_bg),
                  ('TEXTCOLOR',(0,0),(-1,0), colors.white),
                  ('FONTNAME',(0,0),(-1,0),'Helvetica-Bold'),
                  ('FONTSIZE',(0,0),(-1,0),8.3)]
    t.setStyle(TableStyle(style))
    return t

def callout(text):
    p = Paragraph(text, note_st)
    t = Table([[p]], colWidths=[7.3*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(-1,-1), PURPLE_LT),
        ('BOX',(0,0),(-1,-1),1, PURPLE),
        ('LEFTPADDING',(0,0),(-1,-1),8),('RIGHTPADDING',(0,0),(-1,-1),8),
        ('TOPPADDING',(0,0),(-1,-1),4),('BOTTOMPADDING',(0,0),(-1,-1),4),
    ]))
    return t

story = []

# ============================ PAGE 1 ============================
hdr = Table([[
    Image('ursa_new.png', width=1.35*inch, height=1.35*inch),
    [Paragraph('Ursa Catchum', title_st),
     Paragraph('Human (Mark of Handling) &bull; Druid (Circle of Stars) &bull; Level 7', sub_st),
     Spacer(1,3),
     Paragraph('The starwatcher. Ursa reads the night sky like a map, calls down starlight and beast-spirits, '
               'and spent a year walking his father’s trail east. Now the omens come to him in dreams.', flav_st)]
]], colWidths=[1.5*inch, 5.8*inch])
hdr.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                         ('LEFTPADDING',(1,0),(1,0),10)]))
story.append(hdr)
story.append(Spacer(1,4))

story.append(stat_strip([('ARMOR CLASS',18),('HIT POINTS',52),('SPEED','30 ft'),
                         ('INITIATIVE','+2'),('SAVE DC',16),('SPELL ATK','+10')]))
story.append(Spacer(1,4))
story.append(ability_strip([('STR',8,'-1'),('DEX',14,'+2'),('CON',14,'+2'),
                            ('INT',12,'+1'),('WIS',20,'+5'),('CHA',8,'-1')]))
story.append(Paragraph('WIS powers all his magic.', small_it))
sv=Table([[Paragraph(c,cell_st) for c in ['Str save -1', 'Dex save +2', 'Con save +2', '<b><font color="#4A357A">Int save +4</font></b>', '<b><font color="#4A357A">Wis save +8</font></b>', 'Cha save -1']]], colWidths=[(7.3/6)*inch]*6)
sv.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.3,PURPLE_LT),
    ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),3)]))
story.append(sv)

story.append(Paragraph("All of Ursa's Skills", h2_st))
TR = '<b><font color="#4A357A">%s</font></b>'   # trained: purple, per the caption
skills = [
    ('Acrobatics +2','Athletics -1','Insight +5','Medicine +5','Performance -1','Sleight of Hand +2'),
    (TR % 'Animal Handling +8','Deception -1','Intimidation -1','Nature +1','Persuasion -1','Stealth +2'),
    ('Arcana +1','History +1','Investigation +1',TR % 'Perception +8','Religion +1',TR % 'Survival +8'),
]
sk_data = [[Paragraph(c, cell_st) for c in row] for row in skills]
sk = Table(sk_data, colWidths=[(7.3/6)*inch]*6)
sk.setStyle(TableStyle([
    ('BOX',(0,0),(-1,-1),0.5, LINE),
    ('INNERGRID',(0,0),(-1,-1),0.3, PURPLE_LT),
    ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),3),
]))
story.append(sk)
story.append(Paragraph('Purple = trained. Best: Animal Handling, Perception & Survival +8. '
                       'Passive Perception 18, almost nothing sneaks past him.', small_it))

story.append(Paragraph("What Ursa Does in a Fight", h2_st))
atk = [
    ['Attack','To Hit','Damage'],
    ['Thorn Whip <i>(cantrip,</i> <b>melee</b><i>)</i>','+10','2d6+5 piercing, 30 ft, and <b>drag it 10 ft toward him</b>'],
    ['Guiding Bolt <i>(1st, ranged)</i>','+10','4d6 radiant + 1d8 (Starseed); next hit on it has advantage'],
    ['Star-Arrow <i>(Archer, ranged)</i>','+10','1d8+5 radiant, 60 ft. Free when he lights the form, then bonus action'],
    ['Starry Wisp <i>(cantrip, ranged)</i>','+10','2d8 + 5 radiant + 1d8 (Starseed); lights up the target (60 ft)'],
    ['<b>Conjure Animals</b> <i>(pack, no roll)</i>','<i>DC 16 Dex</i>','<b>3d10 slashing</b> per enemy it reaches; moves 30 ft free when he moves'],
]
atk_data = [[Paragraph(c, cellb_st if i==0 else cell_st) for c in row]
            for i,row in enumerate(atk)]
story.append(section_table(atk_data, [3.0*inch, 0.9*inch, 3.4*inch]))
story.append(Paragraph('<b>Ranged</b> attacks take <b>disadvantage</b> with an enemy within 5 ft. <b>Thorn Whip is MELEE</b>, so it never does: that is his answer when something is in his face.', small_it))

story.append(Spacer(1,4))
story.append(callout(
    "<b>Ursa's battle plan.</b> <b>Round 1:</b> bonus action lights <b>Starry Form "
    "(Archer)</b> (<b>free arrow at once</b>), action casts <b>Conjure Animals</b>. "
    "<b>After that, every round:</b> "
    "<b>star-arrow</b> (bonus) + <b>Starry Wisp</b> or a free <b>Guiding Bolt</b>, and the "
    "pack moves 30 ft free whenever he moves. Starry Form is <b>not</b> concentration, so "
    "it runs beside the pack all fight. <b>Free Guiding Bolts:</b> about <b>10 a day</b> "
    "(5 Star Map, up to 5 Staff) before he spends a slot."))

# Two summon stat blocks side by side (built here, RENDERED ON PAGE 2 so page 1
# has room for the Spells at a Glance tracker at its foot).
def summon_block(title, lines):
    rows = [[Paragraph(title, S('st', fontName='Helvetica-Bold', fontSize=9,
                                textColor=colors.white, leading=11))]]
    for ln in lines:
        rows.append([Paragraph(ln, S('sl', fontName='Times-Roman', fontSize=7.8,
                                     textColor=INK, leading=9.0))])
    t = Table(rows, colWidths=[3.55*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,0), PURPLE_DK),
        ('BACKGROUND',(0,1),(0,-1), PURPLE_LT),
        ('BOX',(0,0),(-1,-1),0.8, PURPLE),
        ('LINEBELOW',(0,0),(0,0),0.8, PURPLE),
        ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
        ('TOPPADDING',(0,0),(-1,-1),1.2),('BOTTOMPADDING',(0,0),(-1,-1),1.2),
    ]))
    return t

beast = summon_block("Spectral Pack: Conjure Animals (3rd)", [
    "<b>Nothing can attack it</b> — a spell effect, not a creature. No AC, no hit points.",
    "<b>Moves 30 ft FREE whenever Ursa moves.</b> No action.",
    "Anything it sweeps within <b>10 ft</b>, or that <b>enters or ends its turn</b> there: "
    "<b>Dex save DC 16</b> or <b>3d10 slashing</b>, once each per turn.",
    "<b>Park it ADJACENT and in their way.</b> Next to it they cannot step clear without "
    "staying inside 10 ft, and standing still sets it off too. At 10 ft they walk out free.",
    "<b>4th-level slot:</b> 4d10 — but that slot is Polymorph.",
])
fey = summon_block("Fey Spirit: Summon Fey (3rd)", [
    "<b>AC</b> 15 &nbsp; <b>HP</b> 30 &nbsp; <b>Speed</b> 30 ft, fly 30 ft",
    "<b>Fey Blade:</b> +8 to hit, <b>2d6+6 force</b>, <b>1 attack</b>.",
    "<b>Fey Step:</b> teleport up to 30 ft, then its mood triggers:",
    "<i>Fuming:</i> advantage on its next attack this turn.",
    "<i>Mirthful:</i> foe within 10 ft, Wis save DC 16 or Charmed.",
    "<i>Tricksy:</i> fills a 10-ft cube with magical Darkness.",
    "<b>Cast with a 4th-level slot:</b> AC 16, HP 40, 2d6+7, "
    "and <b>2 attacks a turn</b>.",
])
both = Table([[beast, fey]], colWidths=[3.65*inch, 3.65*inch])
both.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),
                          ('LEFTPADDING',(0,0),(-1,-1),0),('RIGHTPADDING',(0,0),(0,0),10)]))
story.append(Paragraph("Ursa's Summoned Spirits", h2_st))
story.append(both)
story.append(Paragraph('<b>ONE at a time</b> — both need Concentration, and so do Moonbeam, '
    'Entangle and Polymorph. The pack is his damage; the fey is a body that holds ground. The pack '
    'deals <b>slashing</b>, so it does nothing to the Underroot Spike: bring the fey there.', small_it))

# ---- Spells at a Glance (compact quick tracker, bottom of page 1) ----
story.append(Spacer(1,1))
story.append(Paragraph("Spells at a Glance &nbsp;"
    "<font size=7 color='#555555'>([ ] = one slot, check it when spent; full rules on page 3)</font>",
    S('sgh', fontName='Times-Bold', fontSize=11, textColor=PURPLE, leading=13,
      spaceBefore=3, spaceAfter=2)))
gl_st = S('gl', fontName='Times-Roman', fontSize=7.6, textColor=INK, leading=8.8)
def _glance(lbl, boxes, names):
    box = ('[ ]&nbsp;' * boxes) if boxes else '<i>at will</i>'
    return [Paragraph(f'<b>{lbl}</b>&nbsp; {box}', gl_st), Paragraph(names, gl_st)]
glance = [
    _glance('Cantrips', 0, 'Starry Wisp, Thorn Whip, Guidance, Druidcraft'),
    _glance('1st', 4, 'Healing Word, Entangle'),
    _glance('2nd', 3, 'Wither and Bloom, Spike Growth, Lesser Restoration'),
    _glance('3rd', 3, 'Conjure Animals, Summon Fey, Daylight, Revivify'),
    _glance('4th', 1, 'Polymorph, Ice Storm'),
    _glance('free', 0, 'Guiding Bolt, Guidance, Animal Friendship, Speak with Animals, Faerie Fire, Moonbeam <i>(sources on page 3)</i>'),
]
gt = Table(glance, colWidths=[2.3*inch, 5.0*inch])
gt.setStyle(TableStyle([
    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('GRID',(0,0),(-1,-1),0.5, LINE),
    ('ROWBACKGROUNDS',(0,0),(-1,-1),[colors.white, PURPLE_LT]),
    ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
    ('TOPPADDING',(0,0),(-1,-1),1.1),('BOTTOMPADDING',(0,0),(-1,-1),1.1),
]))
story.append(gt)

story.append(PageBreak())

# ============================ PAGE 2 ============================
story.append(Paragraph('Ursa Catchum', S('p2t', fontName='Times-Bold',
            fontSize=15, textColor=PURPLE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 2: Powers &amp; Gear', sub_st))
story.append(Spacer(1,8))

story.append(Paragraph("Ursa's Special Powers", h2_st))
powers = [
    ('★ Reader of Omens<br/><i>(the year on his father&rsquo;s trail)</i>',
     '<b>Omen Dreams.</b> After a long rest, roll <b>two d20s</b> and write them down: those are the day&rsquo;s omens. When he or anyone he can see is about to roll a d20, he can <b>replace that roll</b> with one of his dreamed numbers (no action, before the roll). Each is used once. <br/><b>Both Omens.</b> He has <b>both Weal and Woe</b> every day now, not one or the other. <br/><b>Read the Moment.</b> He can use his Cosmic Omen reaction <b>after the die is rolled</b>, before anyone knows if it worked, then choose Weal or Woe. <br/><b>Shared Tides.</b> One pool of <b>5 uses</b> per long rest, spent on either. <br/><b>The Stronger Tide.</b> His omens hit harder than an ordinary star-druid&rsquo;s: Weal adds <b>1d6 + 2</b> and Woe subtracts <b>1d6 + 2</b>. '),
    ('Starry Form (Bonus Action)', 'Spend a Wild Shape use to glow with starlight (10-ft bright light, 10 min). '
        'Pick a constellation each time:'),
    ('&nbsp;&nbsp;&bull; Archer', '<b>Free arrow the turn he lights it</b>, then bonus action each later turn: one enemy within 60 ft, <b>1d8+5 radiant</b>.'),
    ('&nbsp;&nbsp;&bull; Chalice', 'When he heals someone with a spell slot, he or a nearby friend also heals <b>1d8+5</b>.'),
    ('&nbsp;&nbsp;&bull; Dragon', 'Treat a roll of 9 or lower as a 10 on Int/Wis checks and concentration saves, super steady.'),
    ('Wild Shape (3/long rest)', 'Three uses that fuel his Starry Forms (or turn into a beast he has seen). Regain 1 on a short rest, all on a long rest.'),
    ('Wild Resurgence', 'Once per turn (no action), spend a spell slot to get back one Wild Shape use. Once per long rest, the reverse: spend a Wild Shape use to regain a 1st-level spell slot.'),
    ('Star Map', 'His star chart is a magic focus. Free <b>Guiding Bolt</b> 5×/day even without the Staff. Backup focus he still carries.'),
    ('Cosmic Omen (new at 6!)', '<b>Reaction.</b> When someone he can see within 30 ft rolls a d20, he can <b>wait until the die lands</b> and bend it then, before anyone knows if it worked: <b>Weal +1d6+2</b> or <b>Woe &minus;1d6&minus;2</b> (the waiting and the bigger numbers are both Reader of Omens). <b>5 uses per long rest</b>.'),
    ('Elemental Fury (new at 7!)', '<b>Potent Spellcasting:</b> add <b>+5 (Wis)</b> to the damage of any druid <b>cantrip</b>. <i>(House rule: it can ride the kindled staff once a turn instead, never both in the same turn.)</i>'),
    ('Wild Intuition', 'Add 1d4 to any Animal Handling or Nature check.'),
    ('Primal Connection (1/short rest)', 'Cast Animal Friendship or Speak with Animals for free, no materials.'),
    ('The Bigger They Are', 'Can charm or talk to beasts AND monstrosities (if their Intelligence is 3 or lower).'),
    ('Mark of Handling', 'His dragonmark lets him read animals’ feelings and calm wild or magical creatures with ease.'),
]
pw_data = [[Paragraph(f'<b>{n}</b>', cell_st), Paragraph(d, cell_st)] for n,d in powers]
story.append(section_table(pw_data, [2.15*inch, 5.15*inch], header=False))

story.append(Paragraph("Ursa's Stuff", h2_st))
gear = [
    ('Staff of Waking Constellations<br/><i>(new! ★ Elaria’s gift)</i>',
     'His Wraithpine relic, <b>awakened at his father&rsquo;s shrine</b>. <b>+2 quarterstaff &amp; druidic focus.</b> Holds <b>5 charges</b> (regain 1d4+1 at dawn): '
     '<i>Guiding Bolt</i> (1), <i>Faerie Fire</i> (1), <i>Moonbeam</i> (2). '
     '<b>Starseed:</b> once a turn, when a druid spell deals radiant damage, add <b>+1d8 radiant</b>. '
     '<b>Starlight:</b> bonus action to light a soft 10-ft glow and get advantage on night-navigation. <b>Attuned.</b>'),
    ('Ash&rsquo;s Sigil-Stone<br/><i>(new! found on the trail east)</i>',
     'A river-smooth stone etched with a half-finished sign of Elaria, <b>in his father&rsquo;s own hand</b>. '
     '<b>Aura of Vitality free once a day</b> (no slot): an <b>action</b> to light a 30-ft aura, then <b>2d6</b> healing to one creature in it right away and again at the start of each of his turns, costing him no action to keep going. <b>Concentration</b>, up to 1 minute, so no summon at the same time; out of a fight, just run the whole minute. <br/><b>2 charges for the visions</b> (back at dawn), a magic action each: <b>Ask the Day</b> (one truthful yes or no, or silence), <b>Glimpse the Trail</b>, or <b>Read the Heart</b>. <i>(No attunement.)</i>'),
    ('Wand of the War Mage +2<br/><i>(new! Lilly made this for him)</i>','A slim rune-cut wand she spent the year building. <b>While he is holding it</b>, every <b>spell attack</b> he makes gets <b>+2 to hit</b> (his Starry Wisp, his Guiding Bolts, and his star-arrow all go to <b>+10</b>), and he <b>ignores Half Cover</b>. <b>Attuned.</b> <i>(He holds the staff in one hand and the wand in the other.)</i>'),
    ('Star Map', 'A Tiny star chart that doubles as a spellcasting focus. Free Guiding Bolt 5×/day. (Backup focus.)'),
    ('Amulet of Guiding Light', '<b>Guiding Light:</b> during Starry Form, his <b>allies within 30 ft</b> get +1 to attacks and saves (allies only, not Ursa). '
        '<b>Starry Glow (1/day, reaction):</b> when he or a nearby ally is hit, the attacker takes 2d8 radiant and may be blinded (Con save DC 15). '
        '<b>Celestial Resilience (2/day):</b> reroll a natural 1.'),
    ('Spiked Armor &amp; Shield', 'Dwarf-made spiked armor plus a shield, together they make his <b>AC 18</b>.'),
    ('Explorer’s Pack', 'Backpack, bedroll, mess kit, tinderbox, 10 torches, 10 days of rations, waterskin, 50 ft of rope.'),
    ('Three Enchanted Potatoes', 'His mysterious quest trinket, the strange spuds tied to his father’s disappearance.'),
]
g_data = [[Paragraph(n, cell_st), Paragraph(d, cell_st)] for n,d in gear]
story.append(section_table(g_data, [1.9*inch, 5.4*inch], header=False))

story.append(PageBreak())

# ============================ PAGE 3: SPELLBOOK ============================
story.append(Paragraph('Ursa Catchum', S('p3t', fontName='Times-Bold',
            fontSize=15, textColor=PURPLE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 3: Spellbook', sub_st))
story.append(Spacer(1,7))
story.append(Paragraph('Slots per day: 4 first-level, 3 second-level, 3 third-level, 1 fourth-level. '
    'Cantrips (★) are free forever. He prepares <b>11</b> spells and can rebuild that whole list from scratch on every long rest (2024 druids swap freely, not one at a time); the ones marked <i>free</i> come from his Star Map, his Mark or his Staff and do not use up a prepared slot. '
    'Spell save DC 16 (the wand does not change it), spell attack <b>+10</b> holding the wand, +8 without.', small_it))
story.append(Spacer(1,4))

# Spell cards, richer format: name, meta line (action/range/duration), then full mechanics
def spell_card(name, meta, text):
    inner = [
        [Paragraph(f'<b>{name}</b>', S('scn', fontName='Times-Bold', fontSize=9,
                   textColor=PURPLE_DK, leading=11))],
        [Paragraph(meta, S('sct', fontName='Times-Italic', fontSize=6.8,
                   textColor=GREY, leading=8.2))],
        [Paragraph(text, S('scx', fontName='Times-Roman', fontSize=7.5,
                   textColor=INK, leading=8.7))],
    ]
    t = Table(inner, colWidths=[3.55*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,1), PURPLE_LT),
        ('BOX',(0,0),(-1,-1),0.6, PURPLE_MID),
        ('LINEBELOW',(0,1),(0,1),0.4, PURPLE_MID),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),2),('BOTTOMPADDING',(0,0),(-1,-1),2),
        ('TOPPADDING',(0,2),(0,2),3),('BOTTOMPADDING',(0,2),(0,2),3),
    ]))
    return t

cards = [
    spell_card('★ Thorn Whip',
        'Cantrip • Action • 30 ft • Instant',
        'A thorned vine lashes out. <b>Melee spell attack +10</b> at up to <b>30 ft</b>: <b>2d6+5 piercing</b>, and if the target is Large or smaller he can <b>drag it 10 ft toward him</b>. <i>The drag is the point: haul something into his Conjure Animals pack, across Spike Growth, or off a friend. Starry Wisp hits harder; use this when he wants something MOVED.</i>'),
    spell_card('★ Starry Wisp',
        'Cantrip • Action • 60 ft • Instant',
        'Ranged spell attack <b>+10 to hit</b>: <b>2d8 radiant + 1d8</b> (Starseed). The target glows '
        '(dim light) and can’t turn invisible until the end of his next turn.'),
    spell_card('★ Guidance &nbsp;<i>(free: Star Map)</i>',
        'Cantrip • Action • Touch • Concentration, 1 min',
        'Touch a willing friend. Once before it ends, they add <b>1d4</b> to one ability check '
        '(can roll the d4 after seeing the result). Great before a tricky skill roll.'),
    spell_card('★ Druidcraft',
        'Cantrip • Action • 30 ft • Instant',
        'Tiny nature magic: predict the next 24 hr of weather, bloom a flower, make a harmless '
        'sound/smell in a 5-ft cube, or light/snuff a small flame. Pure utility &amp; flavor.'),
    spell_card('Guiding Bolt &nbsp;<i>(free: Star Map, 5&times;/day)</i>',
        '1st • Action • 120 ft • 1 round &nbsp;(Star Map: free 5/day)',
        'Ranged spell attack <b>+10 to hit</b>. On a hit: <b>4d6 radiant + 1d8</b> (Starseed). '
        'The <b>next attack</b> against that target before Ursa’s next turn has <b>advantage</b>, set up a teammate.'),
    spell_card('Faerie Fire &nbsp;<i>(free: Staff, 1 charge)</i>',
        '1st • Action • 60 ft • Concentration, 1 min',
        'Foes in a 20-ft cube make a <b>Dex save DC 16</b>; on a fail they’re outlined in light. '
        'Attacks vs them have <b>advantage</b>, and they <b>can’t hide/be invisible</b>.'),
    spell_card('Conjure Animals &nbsp;<i>(his big damage spell)</i>',
        '3rd • Action • 60 ft • Concentration, 10 min',
        'A <b>ghost-pack</b> that <b>moves 30 ft free whenever he moves</b> (no action). Any enemy it sweeps within <b>10 ft</b> of, or that <b>enters</b> or ends its turn there: <b>Dex save DC 16</b> or <b>3d10 slashing</b>, once each per turn. <b>4th slot: 4d10.</b> <i>The pack OR a summon.</i>'),
    spell_card('Healing Word',
        '1st • Bonus Action • 60 ft • Instant',
        'Heal one creature you can see <b>2d4+5</b> HP, as a <b>bonus action</b>, so he can still '
        'cast or attack the same turn. Best for popping a downed friend back up from range.'),
    spell_card('Entangle',
        '1st • Action • 90 ft • Concentration, 1 min',
        'Grasping plants fill a <b>20-ft square</b>: <b>difficult terrain</b>, and everyone inside makes a <b>Str save DC 16</b> or is <b>restrained</b> (whole action + <b>DC 16 Athletics</b> to tear free). Cheap, and it stops a charge cold.'),
    spell_card('Speak with Animals &nbsp;<i>(free: his Mark)</i>',
        '1st • Ritual • Action • Self • 10 min',
        'Talk with beasts for 10 min: they can describe nearby places, monsters, and what they saw '
        'in the last day. Cast as a <b>ritual</b> (no slot) when there’s no rush.'),
    spell_card('Animal Friendship &nbsp;<i>(free: his Mark)</i>',
        '1st • Action • 30 ft • 24 hr',
        'One beast (Int 3 or lower) makes a <b>Wis save DC 16</b>; on a fail it’s <b>charmed</b> '
        'and friendly for 24 hr. With “The Bigger They Are,” he can target dumb monstrosities too.'),
    spell_card('Moonbeam &nbsp;<i>(free: Staff, 2 charges)</i>',
        '2nd • Action • 120 ft • Concentration, 1 min',
        'A 5-ft pillar of light. A creature that enters it or starts its turn there makes a <b>Con save DC 16</b>: '
        '<b>2d10 radiant + 1d8</b> (Starseed) on a fail, half on a success. <b>Move it 60 ft</b> each turn as part of the spell.'),
    spell_card('Daylight <i>(new!)</i>',
        '3rd • Action • 60 ft • 1 hour, NO concentration',
        'Real sunlight fills a <b>60-ft radius</b>, with dim light for 60 ft more, and it lasts an <b>hour with no concentration</b>. <b>Ursa cannot see in the dark and Underroot has no sun</b>, so without this he attacks at disadvantage. Cast it <b>on a stone he carries</b>, then cover the stone to go dark again.'),
    spell_card('Spike Growth',
        '2nd • Action • 150 ft • Concentration, 10 min',
        'A 20-ft circle sprouts hidden thorns: <b>difficult terrain</b>, and <b>2d4 piercing per 5 ft</b> '
        'moved through it. It looks like ordinary ground until someone is bleeding. Drop it between himself '
        'and whatever is charging: they either wade through it or go the long way round.'),
    spell_card('Lesser Restoration',
        '2nd • Bonus Action • Touch • Instant',
        'Touch a friend and end <b>one</b> of these: <b>blinded, deafened, paralyzed, or poisoned</b>. '
        'The answer to the boss blinding someone or a spider’s venom locking a friend down.'),
    spell_card('Wither and Bloom &nbsp;<i>(death and life at once)</i>',
        '2nd • Action • 60 ft • <b>Instant, no concentration</b>',
        'A <b>10-ft-radius sphere</b>: everything <b>he chooses</b> inside makes a <b>Con save DC '
        '16</b> for <b>3d6 necrotic</b>, half on a success. Friends are never caught, so drop it '
        'on the scrum. <b>Then one friend there may spend a Hit Die</b> to heal that roll <b>+5</b>. '
        'Works while the pack is out.'),
    spell_card('Ice Storm',
        '4th • Action • 300 ft • Instant <i>(no concentration!)</i>',
        'A <b>20-ft-wide</b> hail patch from far away: <b>Dex save DC 16</b> for <b>2d10 bludgeoning + 4d6 cold</b>, half on a success, and the ground stays <b>difficult terrain</b>. <b>His big blast that leaves his concentration free.</b>'),
    spell_card('Revivify',
        '3rd • Action • Touch • Instant &nbsp;(300 gp diamond)',
        'Touch a friend who died <b>within the last minute</b> and bring them back with <b>1 HP</b>. '
        'The single most important spell he owns. Keep the diamond.'),
    spell_card('Polymorph',
        '4th • Action • 60 ft • Concentration, 1 hr',
        'Turn a creature into a <b>beast</b>. <b>Foe:</b> Wis save DC 16 or it becomes a harmless animal. <b>Friend:</b> huge, with <b>temp HP equal to the beast’s whole HP</b>.'),
    spell_card('Summon Fey',
        '3rd • Action • 90 ft • Concentration, 1 hr',
        'Calls the <b>Fey Spirit</b> (full stats on page 1). Faster and hits harder than the beast, with a mood power '
        '(Fuming/Mirthful/Tricksy) and a 30-ft teleport. Acts on Ursa’s turn and obeys him for free.'),
]

# Lay cards into a 2-wide grid
rows = []
for i in range(0, len(cards), 2):
    chunk = cards[i:i+2]
    while len(chunk) < 2:
        chunk.append(Paragraph('', body_st))
    rows.append(chunk)
grid = Table(rows, colWidths=[3.66*inch]*2)
grid.setStyle(TableStyle([
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('LEFTPADDING',(0,0),(-1,-1),2),('RIGHTPADDING',(0,0),(-1,-1),2),
    ('TOPPADDING',(0,0),(-1,-1),0.8),('BOTTOMPADDING',(0,0),(-1,-1),0.8),
]))
story.append(grid)

story.append(PageBreak())

# ============================ PAGE 4: STORY ============================
story.append(Paragraph('Ursa Catchum', S('p2bt', fontName='Times-Bold',
            fontSize=15, textColor=PURPLE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 4: Story &amp; Personality', sub_st))
story.append(Spacer(1,8))

story.append(Paragraph("Ursa's Story", h2_st))
story.append(Paragraph(
    "Ursa grew up under the wide, dark skies of a quiet farming village, raised on his father’s tales of the "
    "stars and the secrets they keep. His father, a wandering sky-reader and beast-friend who carried the "
    "<b>Mark of Handling</b>, vanished one night chasing a mystery tied to a handful of <b>enchanted potatoes</b>, "
    "leaving Ursa only a star chart and a promise to follow it. Ursa studied the constellations until he could call "
    "their light down to earth, becoming a <b>Druid of the Circle of Stars</b>. Determined to find out what happened "
    "to his father, he set out and crossed paths with <b>Lilly</b> and her Essence Sphere, and the wild goblin "
    "<b>Stabby</b>. The three became an unlikely family, chasing planar cracks, enchanted potatoes, and the guiding "
    "hand of the sleeping goddess <b>Elaria</b>.", body_st))
story.append(Spacer(1,4))
story.append(Paragraph(
    "Two years on, Ursa has read the sky over half of Elaria: haunted forests, a drowned ship, the "
    "bell-towers of Wraithpine where the chest gave him his <b>Staff of Waking Constellations</b>, and "
    "the Rift Hall of Gearhaven, with gentle <b>Floraburst</b> becoming <b>Ghostbloom</b> along the way. In "
    "the year apart he went east, alone, carrying his father's field notes: eleven months of walking, a "
    "country with no sky crossed cairn to cairn, and at the end of the road his father's camp, empty "
    "for only <b>three years, not nine</b>. Under a flat rock he found a river stone carved with half of "
    "Elaria's star, and it has been warm ever since. On his eighth night at the old shrine the clouds "
    "broke, <b>Elaria showed him three things</b>, and he walked home a <b>Reader of Omens</b> carrying a "
    "word from his father's notes: <b>Betelgeuse</b>, the first star to go out.", body_st))

per = [
    ('Personality', 'Determined and resilient. Quiet and watchful, but never gives up. '
        '“I won’t stop until I find the answers.”'),
    ('Ideal: Fate', 'The stars guide every destiny, and his path is part of a greater cosmic plan. '
        '“The stars have written my path, and I will follow it.”'),
    ('Bond: His Crew', 'Fiercely loyal to Lilly and Stabby, his new family. '
        '“Together, we will uncover the truth and face whatever comes.”'),
    ('Flaw: Fear of Failure', 'He worries he can’t live up to his father’s legacy, which can make him '
        'hesitate or push too hard. “What if I’m not strong enough?”'),
]
per_cells = [Paragraph(f'<b>{t}</b><br/>{d}', S('pc', fontName='Times-Roman', fontSize=8,
             textColor=INK, leading=10)) for t,d in per]
pt = Table([[per_cells[0], per_cells[1]],[per_cells[2], per_cells[3]]],
           colWidths=[3.65*inch,3.65*inch])
pt.setStyle(TableStyle([
    ('BOX',(0,0),(-1,-1),0.5, LINE),('INNERGRID',(0,0),(-1,-1),0.5, LINE),
    ('BACKGROUND',(0,0),(-1,-1), PURPLE_LT),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
    ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6),
]))
story.append(Spacer(1,3))
story.append(pt)
story.append(Spacer(1,4))
story.append(Paragraph('<b>Fun Facts:</b> &nbsp;Ursa is a boy, follows the dragon-god Bahamut, and was a Folk Hero '
    'before adventuring. &bull; Auburn hair, purple eyes, freckles, and a fur-lined cloak for cold nights. '
    '&bull; He speaks Common, Sylvan, and Druidic (a secret nature-language for hidden messages).', small_it))


doc = SimpleDocTemplate('../ursa_catchum_sheet_v3.pdf', pagesize=letter,
                        leftMargin=0.55*inch, rightMargin=0.55*inch,
                        topMargin=0.45*inch, bottomMargin=0.5*inch)
frame = make_frame('Ursa Catchum')
doc.build(story, onFirstPage=frame, onLaterPages=frame)
print('built ../ursa_catchum_sheet_v3.pdf')
