#!/usr/bin/env python3
"""Lilly Glimmergear character sheet, 3 pages, frost-blue theme, 2024 rules.
Ported onto the shared published-book template (sheet_style.py) and content-
synced to the committed lilly_glimmergear_sheet_v3.pdf, which is newer than
the original browser-session script (WIS 12, 2024 deep gnome printing, house-
ruled pick-a-blast cannon, Tinker's Magic with Mending, plain steel shield).
Page 1: combat dashboard + cannon. Page 2: powers and gear. Page 3: spellbook and
Puff. Page 4: story and personality."""
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
BLUE_MID = colors.HexColor('#8FB4DA')        # spell-card border/divider (matches Ursa's mid tone)
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
     Paragraph('Deep Gnome &bull; Artificer (Artillerist) &bull; Level 7',sub_st),Spacer(1,3),
     Paragraph('Played by the inventor of the group. Lilly builds a magic cannon, fires Boomstick, and '
               'carries the Essence Sphere that holds Pikachu’s spark. Puff rides on her shoulder.',flav_st)]]],
    colWidths=[1.5*inch,5.8*inch])
hdr.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(1,0),(1,0),10)]))
story.append(hdr); story.append(Spacer(1,8))

story.append(stat_strip([('ARMOR CLASS',20),('HIT POINTS',52),('SPEED','25 ft'),
                         ('INITIATIVE','+2'),('SAVE DC',16),('SPELL ATK','+8')]))
story.append(Spacer(1,4))
story.append(ability_strip([('STR',8,'-1'),('DEX',14,'+2'),('CON',14,'+2'),
                            ('INT',20,'+5'),('WIS',12,'+1'),('CHA',8,'-1')]))
story.append(Paragraph('INT powers all her magic.',small_it))
sv=Table([[Paragraph(c,cell_st) for c in ['Str save -1', 'Dex save +2', '<b><font color="#134A7A">Con save +5</font></b>', '<b><font color="#134A7A">Int save +8</font></b>', 'Wis save +1', 'Cha save -1']]], colWidths=[(7.3/6)*inch]*6)
sv.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.3,BLUE_LT),
    ('TOPPADDING',(0,0),(-1,-1),2.5),('BOTTOMPADDING',(0,0),(-1,-1),2.5),
    ('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),3)]))
story.append(sv)

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
    ['True Strike (Boomstick)','+10','1d10 + 2 + 5 thunder + 1d6 radiant + 1d8 (30/90 ft)'],
    ['Cannon: Flamethrower','DC 16 Dex','2d8+2 fire in a 15-ft cone'],
    ['Cannon: Force Ballista','+8','2d8+2 force, push 5 ft (120 ft away)'],
    ['Fire Bolt (cantrip)','+8','2d10 fire + 1d8 thunder (120 ft, her long shot)'],
    ['Scorching Ray (2nd)','+8','three rays, 2d6 fire each, +1d8 on one']]
story.append(section_table([atk[0]] + [[Paragraph(c,cell_st) for c in r] for r in atk[1:]],
    [3.0*inch,1.0*inch,3.3*inch]))
story.append(Spacer(1,4))
story.append(callout("<b>How Lilly's turn works:</b> She fires her cannon as a <b>BONUS action</b> AND does "
    "something else with her main action (cast a spell, fire Boomstick with True Strike, or Fire Bolt). She gets to do "
    "<b>both every turn!</b> &nbsp;<b>Her best opening:</b> cast <b>Web</b> from a <b>2nd-level slot</b> through Boomstick, because that is <b>DC 16</b> and the wand is only DC 13. Save the wand for when the slots run out. <b>Do not set the web on fire</b> unless she wants them loose: burnt webbing stops holding."))


h2("Lilly's Eldritch Cannon")
story.append(Paragraph('The Cannon can be attacked and broken. Mending repairs it 2d6.', small_it))
cannon = stat_strip([('AC',18),('HIT POINTS',35),('SIZE','Small/Tiny'),('SPEED','15 ft (legs)')])
story.append(cannon)
story.append(Spacer(1,3))
LBL='<b><font color="%s">%%s</font></b>' % BLUE_HEX   # row labels: accent bold
cdata=[
    [Paragraph(LBL%'Pick the blast when she fires',cell_st), Paragraph('<b>New rule: the cannon is no longer '
        'locked to one mode!</b> Each time she fires it, choose: <b>Flamethrower</b> (15-ft cone, 2d8+2 fire), '
        '<b>Force Ballista</b> (one faraway enemy, 2d8+2 force, push 5 ft), or <b>Protector</b> (shield-points '
        'to Lilly &amp; friends within 10 ft, 1d8+5).',cell_st)],
    [Paragraph(LBL%'How to use it',cell_st), Paragraph('Fire it with a <b>bonus action</b>, so Lilly still gets '
        'her main action the same turn! Free to deploy or recall (Pocket Dynamo), +2 damage, lasts a full 24 hours. '
        'Ignores conditions/poison/psychic; enemies must smash it to 0 HP.',cell_st)],
]
story.append(section_table(cdata, [1.4*inch, 5.9*inch], header=False))

# ---- Spells at a Glance (compact quick tracker, bottom of page 1) ----
story.append(Spacer(1,4))
story.append(Paragraph("Spells at a Glance &nbsp;"
    "<font size=7 color='#6F6046'>([ ] = one slot, check it when spent; * = Always Prepared, "
    "free from her subclass; full rules on page 3)</font>",
    S('sgh', fontName='Times-Bold', fontSize=11, textColor=BLUE, leading=13,
      spaceBefore=3, spaceAfter=2)))
gl_st = S('gl', fontName='Times-Roman', fontSize=7.6, textColor=INK, leading=9.2)
def _glance(lbl, boxes, names):
    box = ('[ ]&nbsp;' * boxes) if boxes else '<i>at will</i>'
    return [Paragraph(f'<b>{lbl}</b>&nbsp; {box}', gl_st), Paragraph(names, gl_st)]
glance = [
    _glance('Cantrips', 0, 'True Strike, Fire Bolt, Mending'),
    _glance('1st', 4, 'Shield*, Thunderwave*, Faerie Fire, Grease, Cure Wounds'),
    _glance('2nd', 3, "Scorching Ray*, Shatter*, Homunculus Servant, Dragon's Breath, Aid, Web"),
]
gt = Table(glance, colWidths=[2.3*inch, 5.0*inch])
gt.setStyle(TableStyle([
    ('VALIGN',(0,0),(-1,-1),'MIDDLE'),
    ('GRID',(0,0),(-1,-1),0.5, LINE),
    ('ROWBACKGROUNDS',(0,0),(-1,-1),[colors.white, BLUE_LT]),
    ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
    ('TOPPADDING',(0,0),(-1,-1),1.8),('BOTTOMPADDING',(0,0),(-1,-1),1.8),
]))
story.append(gt)

story.append(PageBreak())

# ===== PAGE 2 =====
story.append(Paragraph('Lilly Glimmergear', S('p2t',fontName='Times-Bold',fontSize=15,
            textColor=BLUE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 2: Powers &amp; Gear', sub_st))
story.append(Spacer(1,8))

h2("Lilly's Special Powers")
powers=[
    ('★ Aether Channeler<br/><i>(the year chasing the Sphere)</i>',
        'The year taught her what her mother’s Sphere really is, and how to draw on it. '
        'Every Sphere power costs her <b>action</b>, and they all share the same pool: '
        '<b>2 uses, back on a short rest.</b> She gains one more power for every rift’s Mote '
        'she brings home and sockets into the Sphere.<br/>'
        '&bull;&nbsp;<b>Aether Ward.</b> She and every friend <b>within 30 ft</b> gain '
        '<b>2d8 + 5 temporary hit points</b>.'),
    ('Replicate Magic Item','Lilly builds magic gear from arcane <b>plans</b>. She knows <b>5 plans</b> and can keep <b>3 creations</b> going at once. <b>All three slots are full:</b> her <b>+1 Half Plate</b>, her new <b>Spell-Refueling Ring</b>, and <b>Puff&rsquo;s Wand of Magic Missiles</b>. <i>Stabby&rsquo;s +1 Repeating Longbow used to hold that middle slot; he fights with the Nichirin now, so she reshaped it.</i>'),
    ('Magic Item Tinker (new at 6!)','<b>Charge</b> (bonus action, spend a slot to refill a creation&rsquo;s charges), <b>Drain</b> (bonus action, destroy one for a spell slot, 1/long rest), <b>Transmute</b> (reshape one into another plan, 1/long rest).'),
    ('Flash of Genius (new at 7!)','<b>Reaction.</b> When she <i>or any friend within 30 ft</i> fails an ability check or saving throw, add <b>+5 (Int)</b> to the roll and maybe turn it into a success. <b>5 uses per long rest.</b>'),
    ("Tinker's Magic",'Knows the Mending cantrip (fix broken things). Can also conjure handy mundane gear (rope, a torch, ball bearings) that lasts until her next rest. Great for puzzles and traps.'),
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
    ('Essence Sphere','A steampunk orb holding Pikachu’s spark. Lilly’s big quest item: she wants to give Pikachu a body again.'),
    ('Boomstick <i>(new! built with her mother)</i>','The repeating pistol she and Poots built together at the kitchen-table forge, +2. <b>Range 30/90.</b> It is her <b>weapon, her spell focus, and her Arcane Firearm</b> all at once: any artificer spell she casts through it adds <b>1d8 thunder</b> to one of its damage rolls.'),
    ('Frostbite Shard Dagger +1 <i>(retired to her belt)</i>','Her old frost dagger, kept as a keepsake. Boomstick has taken over as focus and Arcane Firearm, so the dagger&rsquo;s riders no longer apply.'),
    ('Pocket Dynamo (★ Elaria’s gift)','From the Wraithpine chest. Summon/recall her cannon for free, lasts 24 hours, +2 damage. Reformat (1/long rest, action), now mostly spare, since every cannon picks its blast when it fires. Needs attunement.'),
    ('+1 Half Plate <i>(Replicate creation 1 of 3)</i>','Her armour, the base of her <b>AC 20</b>. She keeps it going with Replicate Magic Item, so it uses one of her three creation slots.'),
    ('Shield','A sturdy steel shield. Adds +2 to her armor.'),
    ('Wand of Web <i>(new! she made it during the year)</i>','<b>Hers, attuned.</b> 7 charges; spend <b>1 charge</b> to cast <b>Web</b>: a 20-ft cube of sticky webbing, difficult terrain, and anything caught makes a <b>Dex save DC 13</b> or is <b>Restrained</b> (it can break out with a Str check against the same DC). <i>The wand casts at its own DC 13, not her DC 16, and gets no Boomstick 1d8.</i> Regains 1d6+1 at dawn; spend the <b>last</b> charge and roll 1d20: on a <b>1</b> the wand crumbles to ash.'),
    ('Spell-Refueling Ring <i>(new! Replicate creation 2 of 3)</i>','<b>Hers, attuned.</b> <b>Bonus action:</b> get back <b>one spent spell slot</b> of level 3 or lower, so for her that is a <b>2nd-level slot</b>: another Web, Scorching Ray or Shatter out of nothing. <b>Once, then not again until the next dawn.</b> <i>She reshaped Stabby&rsquo;s old bow into it at camp.</i>'),
    ('Wand of Magic Missiles <i>(new! Puff carries it)</i>','<b>No attunement, so Puff can use it.</b> 7 charges. Spend <b>1 charge</b> for <b>three darts</b> that <b>never miss</b>, <b>1d4+1 force</b> each, range <b>120 ft</b>, split among any targets she can see. She may spend up to <b>3 charges at once</b>: each extra charge adds <b>one more dart</b>, so 3 charges means <b>five darts</b>. Regains 1d6+1 at dawn. <i>(Replicate creation 3 of 3.)</i>'),
    ('Ring of Spell Storing <i>(new! attuned to Puff)</i>','Holds up to <b>5 levels of spells</b>. Any caster can put a spell of level 1 to 5 into it by touching it while casting, and the slot level used is how much room it takes. Puff can then cast anything stored in it, using <b>the original caster&rsquo;s</b> slot level, save DC and attack bonus, so a spell Lilly stores comes back out at <b>DC 16 and +8</b>. Casting it frees that space again.'),
    ('Pipes of Haunting <i>(new! Puff carries them)</i>','<b>No attunement.</b> 3 charges, regains 1d3 at dawn. <b>Magic action</b>, spend 1 charge to play an eerie tune: each creature she chooses within <b>30 ft</b> makes a <b>Wis save DC 15</b> or is <b>Frightened for 1 minute</b>, re-saving at the end of each of its turns. Anything that saves is immune to the pipes for 24 hours.'),
    ('Attunement: 3 of 3 used','Lilly is attuned to the <b>Pocket Dynamo</b>, the <b>Wand of Web</b> and the <b>Spell-Refueling Ring</b>, so she has <b>no slot free</b>. Puff attunes separately and holds the <b>Ring of Spell Storing</b>. Boomstick, the Wand of Magic Missiles and the Pipes need no attunement at all.'),
]
story.append(section_table([[Paragraph(LBL%n,cell_st),Paragraph(d,cell_st)] for n,d in gear],
    [1.9*inch,5.4*inch], header=False))

story.append(PageBreak())

# ===== PAGE 3: SPELLBOOK =====
story.append(Paragraph('Lilly Glimmergear', S('p3t',fontName='Times-Bold',fontSize=15,
            textColor=BLUE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 3: Spellbook', sub_st))
story.append(Spacer(1,7))
story.append(Paragraph('Slots per day: 4 first-level, 3 second-level. Cantrips (★) are free forever. '
    'She prepares 7 spells; the four marked Always Prepared are free from her Artillerist subclass and '
    'don’t count toward that. The <b>+1d8 thunder</b> is <b>Boomstick</b>, her arcane firearm: it adds to one '
    'damage roll of <b>every</b> artificer spell she casts through it.', small_it))
story.append(Spacer(1,6))

# Open two-column spell list (name / meta / text), per the living sheet
sp_name = S('spn', fontName='Times-Bold', fontSize=9.2, textColor=BLUE, leading=11, spaceBefore=6)
sp_meta = S('spm', fontName='Times-Italic', fontSize=7.2, textColor=GREY, leading=8.6, spaceAfter=1)
sp_text = S('spx', fontName='Times-Roman', fontSize=7.9, textColor=INK, leading=9.9)

spells=[
    ('★ True Strike',
        'Cantrip • Action • fires Boomstick, 30/90 ft • Instant',
        'Fire Boomstick using <b>INT for both the attack and the damage</b>. Ranged attack <b>+10</b> to hit. '
        'On a hit: <b>1d10 + 2 + 5</b> thunder, <b>+1d6 radiant</b> (the cantrip grows with her level), and '
        '<b>+1d8 thunder</b> from Boomstick as her arcane firearm. Radiant instead of thunder when that hurts more. '
        'Her hardest single shot.'),
    ('★ Fire Bolt',
        'Cantrip • Action • 120 ft • Instant',
        'Hurl fire at one target. Ranged spell attack +8 to hit: <b>2d10 fire + 1d8 thunder</b> '
        '(Boomstick). Never runs out, and at 120 ft it outreaches Boomstick.'),
    ('★ Mending',
        'Cantrip • 1 minute • Touch • Instant',
        'Repair one break or tear in an object up to 1 ft: a snapped chain, a cracked '
        'gear. Free from Tinker’s Magic. Heals her cannon 2d6!'),
    ('Shield: Always Prepared',
        '1st • Reaction (when hit / by Magic Missile) • Self • 1 round',
        'Snap up a force wall: +5 AC until the start of her next turn (can turn a hit into a '
        'miss) and take no damage from Magic Missile. Cast after seeing the attack roll.'),
    ('Thunderwave: Always Prepared',
        '1st • Action • Self (15-ft cube) • Instant',
        'Foes in a 15-ft cube make a Con save DC 16: on a fail, <b>2d8 + 1d8 thunder</b> (Boomstick) '
        'and shoved 10 ft away; half and no shove on a success.'),
    ('Faerie Fire',
        '1st • Action • 60 ft • Concentration, 1 min',
        'Foes in a 20-ft cube make a Dex save DC 16; on a fail they’re outlined in light. '
        'Attacks against them have advantage, and they cannot hide. Strong setup.'),
    ('Scorching Ray: Always Prepared',
        '2nd • Action • 120 ft • Instant',
        'Fire three rays. Each is a separate ranged spell attack +8 to hit: 2d6 fire each, plus '
        '<b>1d8 thunder on one ray</b> (Boomstick). Aim them all at one foe or split them up.'),
    ('Shatter: Always Prepared',
        '2nd • Action • 60 ft (10-ft sphere) • Instant',
        'A loud burst. Creatures in a 10-ft sphere make a Con save DC 16: <b>3d8 + 1d8 thunder</b> '
        '(Boomstick) on a fail, half on success. Extra effective against metal and stone foes.'),
    ('Grease',
        '1st • Action • 60 ft (10-ft square) • 1 min',
        'Slick the floor in a 10-ft square: it becomes difficult terrain, and anyone standing, '
        'entering, or ending a turn there makes a Dex save DC 16 or falls prone. '
        'No concentration needed.'),
    ('Cure Wounds',
        '1st • Action • Touch • Instant',
        'Touch a friend and heal them 2d8 + 5. Her emergency button when nobody '
        'else can reach them in time.'),
    ('Homunculus Servant',
        '2nd • 1 hr 10 min as a RITUAL (no spell slot!) • 10 ft • Permanent',
        'She builds her little brass companion. The ritual costs NO spell slot and never '
        'expires. Puff flies, acts right after her, and costs her nothing. Stat block below.'),
    ("Dragon's Breath",
        '2nd • Bonus Action • Touch • Concentration, 1 min',
        'Touch a willing friend (Puff!) and pick acid, cold, fire, lightning or poison. '
        'For 1 minute it can use its action to breathe a 15-ft cone: Dex save DC 16, '
        '3d6 (<b>+1d8</b> on the first breath, Boomstick), half on a success. Pick what it is weak to!'),
    ('Web',
        '2nd • Action • 60 ft • Concentration, 1 hr',
        'Fill a 20-ft cube with sticky webs: <b>difficult terrain</b>, and anything caught makes a '
        '<b>Dex save</b> or is <b>Restrained</b> (Str check, same DC, to tear free). Cast it <b>from a slot '
        'through Boomstick for DC 16</b>, plus <b>1d8</b>; the wand is only DC 13. Anything Restrained is '
        '<b>attacked with advantage</b> and makes <b>Dex saves with disadvantage</b>. <b>Careful:</b> fire '
        'burns webs away (2d4) and frees what they held.'),
    ('Aid',
        '2nd • Action • 30 ft • 8 hours',
        'Choose three friends: each gains <b>+5 hit point maximum and +5 current HP</b> for eight hours. '
        '<i>Worth a slot on a quiet morning, not on a run like tonight.</i>'),
]
# Boxed spell cards in Lilly's blue, matching Ursa's page-3 format.
def spell_card(name, meta, text):
    inner = [
        [Paragraph(f'<b>{name}</b>', S('lscn', fontName='Times-Bold', fontSize=9,
                   textColor=BLUE, leading=11))],
        [Paragraph(meta, S('lsct', fontName='Times-Italic', fontSize=6.8,
                   textColor=GREY, leading=8.2))],
        [Paragraph(text, S('lscx', fontName='Times-Roman', fontSize=7.6,
                   textColor=INK, leading=9.1))],
    ]
    t = Table(inner, colWidths=[3.55*inch])
    t.setStyle(TableStyle([
        ('BACKGROUND',(0,0),(0,1), BLUE_LT),
        ('BOX',(0,0),(-1,-1),0.6, BLUE_MID),
        ('LINEBELOW',(0,1),(0,1),0.4, BLUE_MID),
        ('LEFTPADDING',(0,0),(-1,-1),5),('RIGHTPADDING',(0,0),(-1,-1),5),
        ('TOPPADDING',(0,0),(-1,-1),1.5),('BOTTOMPADDING',(0,0),(-1,-1),1.5),
        ('TOPPADDING',(0,2),(0,2),3),('BOTTOMPADDING',(0,2),(0,2),3.5),
    ]))
    return t

cards = [spell_card(*sp) for sp in spells]
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
    ('TOPPADDING',(0,0),(-1,-1),0.4),('BOTTOMPADDING',(0,0),(-1,-1),0.4),
]))
story.append(grid)

# ---- Homunculus Servant stat block (her permanent ritual companion) ----
story.append(Spacer(1, 5))
story.append(Paragraph('Puff, Lilly&rsquo;s Homunculus Servant',
    S('homh', fontName='Times-Bold', fontSize=11.5, textColor=BLUE, leading=13, spaceAfter=1)))
story.append(HRFlowable(width='100%', thickness=0.7, color=BLUE, spaceAfter=3))

hom_stats = [
    Paragraph('<b>Tiny construct.</b> Built, not summoned: ritual-cast in 1 hour 10 minutes for '
              '<b>no spell slot</b>, and it never expires. Fairy-sized, small enough to sit in her '
              'cupped hands.', cell_st),
    Spacer(1, 2),
    Paragraph('<b>AC</b> 13 &nbsp; <b>HP</b> 15 &nbsp; <b>Speed</b> 20 ft, <b>Fly 30 ft</b>', cell_st),
    Paragraph('<b>Saves</b> Str &minus;1 &nbsp; <b>Dex +4</b> &nbsp; <b>Con +3</b> &nbsp; '
              'Int +2 &nbsp; Wis +2 &nbsp; Cha +0 &nbsp; '
              '<font size=6.5 color="#6F6046">(Magic Bond&rsquo;s +2 already included)</font>', cell_st),
    Paragraph('<b>Senses</b> darkvision 60 ft &nbsp; <b>Telepathy</b> with Lilly, 1 mile', cell_st),
    Paragraph('<b>Immune</b> poison damage; poisoned, exhaustion', cell_st),
    Spacer(1, 2),
    Paragraph('<b>Force Strike.</b> +8 to hit, reach 5 ft or range 30 ft: <b>1d6 + 2 force</b>. '
              'Force punches through the Voltcrawlers&rsquo; blink.', cell_st),
    Paragraph('<b>Evasion.</b> On a Dex save for half damage it takes <b>none</b> on a success, '
              'half on a failure.', cell_st),
    Paragraph('<b>Magic Bond.</b> Add +2 to any check or save it makes.', cell_st),
    Paragraph('<b>Channel Magic (Reaction).</b> When Lilly casts a touch spell and it is within '
              '120 ft, it can deliver that spell instead.', cell_st),
    Spacer(1, 3),
    Paragraph('<b>What she carries.</b> The <b>Ring of Spell Storing</b> (attuned to her), the <b>Wand of Magic '
              'Missiles</b> and the <b>Pipes of Haunting</b>. Full rules for all three are on page 2 under '
              'Lilly&rsquo;s Stuff. Puff has a single action, so she can use only <b>one of them per turn</b>.', cell_st),
    Spacer(1, 2),
    Paragraph('It shares Lilly&rsquo;s initiative and acts right after her, obeying with <b>no '
              'action needed from her</b>; give it no orders and it Dodges. Touch it with '
              '<i>Dragon&rsquo;s Breath</i> and it breathes a 15-ft cone for 3d6, choosing the '
              'type the enemy is weak to.', small_it),
]
homt = Table([[Image('homunculus_new.png', width=1.3*inch, height=1.3*inch), hom_stats]],
             colWidths=[1.45*inch, 5.85*inch])
homt.setStyle(TableStyle([
    ('VALIGN',(0,0),(0,0),'TOP'),
    ('VALIGN',(1,0),(1,0),'TOP'),
    ('BACKGROUND',(0,0),(-1,-1), BLUE_LT),
    ('BOX',(0,0),(-1,-1),0.8, BLUE_MID),
    ('LINEAFTER',(0,0),(0,0),0.5, BLUE_MID),
    ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
    ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
]))
story.append(homt)

# ===== PAGE 4: STORY & PERSONALITY =====
story.append(PageBreak())
story.append(Paragraph('Lilly Glimmergear', S('p4t',fontName='Times-Bold',fontSize=15,
            textColor=BLUE, leading=18, spaceAfter=2)))
story.append(Paragraph('Page 4: Story &amp; Personality', sub_st))
h2("Lilly's Story")
story.append(Paragraph(
    "Lilly grew up in Deepforge Hollow, a svirfneblin (deep gnome) city deep in the Underdark, surrounded by "
    "the hum of machines and magic. Her mother, Poots Glimmergear, was a famous artificer and adventurer who "
    "inspired Lilly to tinker from the time she was tiny. Lilly trained at the Glimmerspire Academy of Artifice "
    "under Master Droven Sparkwick, and her proudest creation was her very own arcane turret, the cannon she "
    "still fights with today.", body_st))
story.append(Spacer(1,4))
story.append(Paragraph(
    "On her seventh birthday, Poots handed Lilly the Essence Sphere, a device holding the spark of "
    "Pikachu, a lost companion from her mother’s adventuring days. Lilly’s quest became clear: find a way to "
    "give Pikachu a body again. That mission led her out of the Underdark to find Ursa, and along the way she "
    "met Stabby. The three became an unlikely team, chasing the mystery of the Essence Sphere, and the "
    "planar cracks tied to the sleeping goddess Elaria.", body_st))
story.append(Spacer(1,4))
story.append(Paragraph(
    "Two years of adventuring later, Lilly has zapped shadow beasts, survived the sinking of the "
    "<b>Stormwind</b>, walked the haunted lanes of <b>Wraithpine</b> (where Elaria's chest gave her the "
    "<b>Pocket Dynamo</b>), and helped free the clockwork city of <b>Gearhaven</b>, where she built "
    "<b>Puff</b> with her own hands. When Vane's great ring needed a year to finish, she went home first: "
    "she set the Sphere on her mother's kitchen table and said <i>tell me everything</i>. The answer was "
    "not in the stories, but the visit gave her something better: eleven evenings at the kitchen-table "
    "forge with Poots teaching, arguing, and finally just watching, and at the end of them "
    "<b>Boomstick</b>, which nobody gave her because the two of them built it. The answer she went "
    "for she earned on the trade roads, one workshop at a time, until the "
    "forty-first time she opened the housing she found <b>older marks under her mother's sigils</b>: the "
    "Sphere is not a machine holding a spark, it is a <b>seed that grows</b>. She came back to Gearhaven "
    "with her craft gone from clever to formidable, and with proof.", body_st))

h2("Personality")
per=[
    ('Inventive and curious','Always tinkering, always asking “why settle for what’s already made when you can build something better?”'),
    ('Ideal: Creativity','“There’s always a new way to make something better.” Lilly believes creativity solves any problem.'),
    ('Bond: Her Friends','Fiercely loyal to Ursa and Stabby. “Together, we’ll solve these mysteries and prove ourselves.”'),
    ('Flaw: Impatient','When a plan doesn’t work right away, she gets frustrated. “Why isn’t this working already?”'),
]
pc=[Paragraph(f'<b><font color="{BLUE_HEX}">{t}</font></b><br/><i>{d}</i>',
              S('pc',fontName='Times-Roman',fontSize=8,textColor=INK,leading=10)) for t,d in per]
pt=Table([[pc[0],pc[1]],[pc[2],pc[3]]],colWidths=[3.65*inch,3.65*inch])
pt.setStyle(TableStyle([('BOX',(0,0),(-1,-1),0.5,LINE),('INNERGRID',(0,0),(-1,-1),0.5,LINE),
    ('VALIGN',(0,0),(-1,-1),'TOP'),
    ('TOPPADDING',(0,0),(-1,-1),5),('BOTTOMPADDING',(0,0),(-1,-1),5),
    ('LEFTPADDING',(0,0),(-1,-1),6),('RIGHTPADDING',(0,0),(-1,-1),6)]))
story.append(Spacer(1,3)); story.append(pt)

doc=SimpleDocTemplate('../lilly_glimmergear_sheet_v3.pdf',pagesize=letter,
    leftMargin=0.55*inch,rightMargin=0.55*inch,topMargin=0.45*inch,bottomMargin=0.5*inch)
frame = make_frame('Lilly Glimmergear')
doc.build(story, onFirstPage=frame, onLaterPages=frame)
print('built ../lilly_glimmergear_sheet_v3.pdf')
