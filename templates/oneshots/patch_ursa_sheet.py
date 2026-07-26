# -*- coding: utf-8 -*-
import io, re
p = r"C:\Users\jhffm\dnd-campaign\characters\builders\build_ursa.py"
t = io.open(p, encoding="utf-8").read()

# Normalize literal \\uXXXX escapes to real characters so every match below
# uses actual chars (reportlab renders them identically at build time).
t = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), t)

def rep(old, new, n=1):
    global t
    c = t.count(old)
    assert c == n, f"expected {n} of {old[:45]!r}, found {c}"
    t = t.replace(old, new)

# R1: combat table
rep(
"""    ['Staff of Waking Constellations (+1)','+5','1d8+3 bludgeoning (a starlit quarterstaff)'],
    ['Guiding Bolt (1st, from Staff or Star Map)','+8','4d6 radiant + 1d4 (Starseed); next hit on it has advantage'],
    ['Star-Arrow (Starry Form: Archer)','+8','1d8+5 radiant, one enemy within 60 ft (bonus action)'],
    ['Primal Savagery (cantrip)','+8','2d10 acid (close-up bite of magic)'],
    ['Produce Flame (cantrip)','+8','2d8 fire, thrown up to 30 ft'],""",
"""    ['Staff of Waking Constellations (+1), unlit','+3','1d6 bludgeoning (1d8 two-handed). See Shillelagh!'],
    ['Staff + Shillelagh (ignited)','+9','1d10+6 force or bludgeoning; bonus action to light, 1 min'],
    ['Guiding Bolt (1st, from Staff or Star Map)','+8','4d6 radiant + 1d4 (Starseed); next hit on it has advantage'],
    ['Star-Arrow (Starry Form: Archer)','+8','1d8+5 radiant, one enemy within 60 ft (bonus action)'],
    ['Starry Wisp (cantrip)','+8','2d8 radiant + 1d4 (Starseed); lights up the target (60 ft)'],""")

# R2: allies-only aura note after the combat table
rep(
"story.append(section_table(atk_data, [3.0*inch, 0.9*inch, 3.4*inch]))\n",
"story.append(section_table(atk_data, [3.0*inch, 0.9*inch, 3.4*inch]))\n"
"story.append(Paragraph('While his Starry Form glows, the Amulet of Guiding Light gives '\n"
"    '+1 to attacks and saves to his nearby FRIENDS (allies only, not Ursa himself): '\n"
"    'a party buff, so his own to-hit stays +8.', small_it))\n")

# R3: free Guiding Bolts 8->10, 3->5
rep("8 Guiding Bolts a day", "10 Guiding Bolts a day")
rep("<b>3</b> from the Star Map", "<b>5</b> from the Star Map")

# R4: add Wild Resurgence
rep(
"    ('Wild Shape (2/short rest)', 'Two uses that fuel his Starry Forms (or turn into a beast he has seen).'),\n",
"    ('Wild Shape (2/short rest)', 'Two uses that fuel his Starry Forms (or turn into a beast he has seen). Regain 1 on a short rest, all on a long rest.'),\n"
"    ('Wild Resurgence', 'Once per turn (no action), spend a spell slot to get back one Wild Shape use. Once per long rest, the reverse: spend a Wild Shape use to regain a 1st-level spell slot.'),\n")

# R5: Star Map free-bolt count 3->5 (actual multiplication sign in file)
rep("Free <b>Guiding Bolt</b> 3×/day", "Free <b>Guiding Bolt</b> 5×/day")
rep("Free Guiding Bolt 3×/day. (Backup focus.)", "Free Guiding Bolt 5×/day. (Backup focus.)")

# R6: Amulet aura allies-only
rep(
"during Starry Form, Ursa and allies in the bright light get +1 to attacks and saves.",
"during Starry Form, his <b>allies</b> in the bright light get +1 to attacks and saves (allies only, not Ursa).")

# R7: prepared count 10 -> 9
rep("He prepares 10 spells and can swap them on a long rest.",
    "He prepares 9 spells and can swap one on a long rest.")

# R8: Primal Savagery card -> Shillelagh (file stores backslash-u escapes)
rep(
r"""    spell_card('★ Primal Savagery',
        'Cantrip • Action • Self (5 ft reach) • Instant',
        'His teeth/claws sharpen with acid. Make a melee spell attack: <b>+8 to hit</b>, '
        '<b>2d10 acid</b> on a hit. No save — it’s an attack roll. Good when something’s right next to him.'),""",
r"""    spell_card('★ Shillelagh',
        'Cantrip • Bonus Action • Self • 1 min',
        'Starlight sheathes his staff: for 1 minute it swings with <b>WISDOM</b>, <b>+9 to hit</b>, '
        '<b>1d10+6</b> force or bludgeoning (his choice). Recast any time. His answer when something '
        'gets right in his face. (House rule: replaces Primal Savagery.)'),""")

# R9: Produce Flame card -> Starry Wisp
rep(
r"""    spell_card('★ Produce Flame',
        'Cantrip • Action • Self / 30 ft throw • 10 min',
        'A flame in his hand gives <b>10-ft bright light</b> (10 more dim) and lasts 10 min. '
        'Or hurl it: ranged spell attack <b>+8 to hit</b>, <b>2d8 fire</b> (ends the light). Lantern + weapon in one.'),""",
r"""    spell_card('★ Starry Wisp',
        'Cantrip • Action • 60 ft • Instant',
        'Ranged spell attack <b>+8 to hit</b>: <b>2d8 radiant + 1d4</b> (Starseed). The target glows '
        '(dim light) and can’t turn invisible until the end of his next turn.'),""")

# R10: Guiding Bolt card free 3/day -> 5/day
rep("(Star Map: free 3/day)", "(Star Map: free 5/day)")

# R11: Healing Word 1d4+5 -> 2d4+5
rep("<b>1d4+5</b> HP", "<b>2d4+5</b> HP")

# R12: Healing Spirit card -> Spike Growth
rep(
r"""    spell_card('Healing Spirit',
        '2nd • Bonus Action • 60 ft • Concentration, 1 min',
        'A spirit fills a 5-ft cube. When a friend enters or starts its turn there, heal <b>1d6</b> '
        '(no action) — up to <b>6 times</b> total. <b>Move it 30 ft</b> with a bonus action. Great in a clustered scrap.'),""",
r"""    spell_card('Spike Growth',
        '2nd • Action • 150 ft • Concentration, 10 min',
        'A 20-ft circle of ground sprouts hidden thorns: <b>difficult terrain</b>, and <b>2d4 piercing</b> '
        'for every 5 ft a creature moves through. It looks like normal ground; herd foes across it or '
        'drop it under a charging monster.'),""")

# R13: output path
rep("doc = SimpleDocTemplate('/home/claude/Ursa_Catchum_Sheet.pdf', pagesize=letter,",
    "doc = SimpleDocTemplate('../ursa_catchum_sheet_v3.pdf', pagesize=letter,")
rep("print('built Ursa_Catchum_Sheet.pdf')", "print('built ../ursa_catchum_sheet_v3.pdf')")

for gone in ["Primal Savagery (cantrip)", "Produce Flame", "Healing Spirit", "3×/day", "free 3/day", "prepares 10"]:
    assert gone not in t, f"stale remains: {gone!r}"

io.open(p, "w", encoding="utf-8", newline="\n").write(t)
print("OK. Primal Savagery refs left:", t.count("Primal Savagery"), "(expect 1: the house-rule note)")
