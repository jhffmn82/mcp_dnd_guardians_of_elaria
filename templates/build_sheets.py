# build_sheets.py
# The Guardians of Elaria: readable, book-styled character sheet pages.
# Part IV of the merged compendium. Every number is transcribed faithfully
# from the v3 sheet PDFs in characters/ (the sources of truth):
#   characters/lilly_glimmergear_sheet_v3.pdf
#   characters/stabby_sharpblade_sheet_v3.pdf
#   characters/ursa_catchum_sheet_v3.pdf
#   characters/historical/ghostbloom_statblock_v3.pdf
# House rules (memory/house_rules.md) are already baked into those sheets;
# never regress them here (Shillelagh over Primal Savagery, Patient Defense
# = free Disengage, Goodberry eat = Bonus Action, Starseed on druid spells
# only, Air spirit HP 20, 2024 deep gnome printing, cannon picks its blast).
#
# NOTE ON S[0]: build_compendium_full.py's part() helper drops blocks[0]
# and replaces it with its own "Part IV: ..." h1, so S opens with the plain
# h1 rather than a titlepage. The standalone build below prepends a
# titlepage of its own.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

S = [
    ("h1", "The Guardians' Character Sheets"),
    ("body", "Three heroes, every number and spell, exactly as they stood at the close of the "
             "Gearhaven chapter (Session 7): level 5, relics attuned, cannon smoking. These pages "
             "are the table copies, set large enough to read at arm's length, with the house rules "
             "already baked in. Ghostbloom, the party's spectral companion, closes the chapter."),

    # ==================================================================
    # LILLY GLIMMERGEAR
    # ==================================================================
    # Whitespace pass 2026-07: Part IV flows continuously, exactly like the
    # bestiary's session sections. With per-hero hardbreaks, the part opener
    # page carried only the h1 and intro (seven-eighths empty) and every
    # hero's tail page stranded roughly half a page of whitespace.
    ("h1", "Lilly Glimmergear"),
    ("imgfloat", "assets/characters/lilly_v3_portrait.png", 2.9),
    ("body", "**Deep Gnome Artificer (Artillerist), Level 5.** The inventor of the group. Lilly "
             "builds a magic cannon, zaps things with frost, and carries the Essence Sphere that "
             "holds Pikachu's spark."),
    ("dm", "**Armor Class** 20 (+1 half plate and shield)   **Hit Points** 38   **Speed** 25 ft.   "
           "**Initiative** +2   **Proficiency** +3", {"size": 11}),
    ("dm", "**STR** 8 (-1)   **DEX** 14 (+2)   **CON** 14 (+2)   **INT** 20 (+5)   "
           "**WIS** 12 (+1)   **CHA** 8 (-1)", {"size": 11}),
    ("dm", "**Spell save DC** 16   **Spell attack** +8. Intelligence powers all her magic.", {"size": 11}),
    ("slots", "lilly", [("Spell Slots, 1st Level", 4), ("Spell Slots, 2nd Level", 2)]),

    ("stat", "Saving Throws & Skills", [
        "**Saving Throws.** Str -1, Dex +2, **Con +5**, **Int +8**, Wis +1, Cha -1 "
        "(bold = proficient; her best are Con and Int).",
        "**Skills.** Acrobatics +2, **Animal Handling +4**, **Arcana +8**, Athletics -1, "
        "Deception -1, History +5, Insight +1, Intimidation -1, **Investigation +8**, "
        "Medicine +1, Nature +5, Perception +1, Performance -1, Persuasion -1, Religion +5, "
        "Sleight of Hand +2, Stealth +2, **Survival +4** (bold = trained; her best are Arcana "
        "and Investigation, +8).",
    ]),
    ("stat", "What Lilly Does in a Fight", [
        "**True Strike (frost dagger).** Melee, +9 to hit. Hit: 1d4 + 1d4 cold + 6, plus 1d6 "
        "radiant, plus 1d8 + 2 frost. Her best up-close hit.",
        "**Cannon: Flamethrower.** DC 16 Dex save: 2d8 + 2 fire in a 15-ft cone.",
        "**Cannon: Force Ballista.** +8 to hit, range 120 ft: 2d8 + 2 force, push 5 ft.",
        "**Cannon: Protector.** Shield-points (temporary HP) to Lilly and friends within "
        "10 ft: 1d8 + 5.",
        "**Fire Bolt (cantrip).** +8 to hit, range 120 ft: 2d10 fire + 1d8 + 2 frost (dagger).",
    ]),
    ("dm", "**How Lilly's turn works.** She fires her cannon as a BONUS action AND does something "
           "else with her main action (cast a spell, stab with True Strike, or Fire Bolt). She "
           "gets to do both every turn.", {"size": 11}),

    ("h2", "Lilly's Eldritch Cannon"),
    ("stat", "The Eldritch Cannon", [
        "**AC** 18   **Hit Points** 25   **Size** Small or Tiny   **Speed** 15 ft. (on little "
        "legs). It can be attacked and broken; Mending repairs it 2d6. It ignores conditions, "
        "poison, and psychic damage; enemies must smash it to 0 HP.",
        "**Pick the blast when she fires (house rule).** The cannon is no longer locked to one "
        "mode. Each time she fires it, choose: Flamethrower (15-ft cone, 2d8 + 2 fire), Force "
        "Ballista (one faraway enemy, 2d8 + 2 force, push 5 ft), or Protector (shield-points to "
        "Lilly and friends within 10 ft, 1d8 + 5).",
        "**How to use it.** Fire it with a bonus action, so Lilly still gets her main action the "
        "same turn. Free to deploy or recall (Pocket Dynamo), +2 damage, lasts a full 24 hours.",
    ]),

    ("h2", "Special Powers & Deep Gnome Gifts"),
    ("stat", "Class Features & Species Traits", [
        "**Replicate Magic Item.** Lilly builds magic gear for the team. Her two creations in "
        "use now: her own +1 Half Plate and the +1 Repeating Longbow she made for Stabby.",
        "**Tinker's Magic.** Knows the Mending cantrip (fix broken things). Can also conjure "
        "handy mundane gear (rope, a torch, ball bearings) that lasts until her next rest. "
        "Great for puzzles and traps.",
        "**The Right Tool.** With her tools, Lilly can magically make any set of artisan's "
        "tools she needs (1 hour).",
        "**Gnomish Magic Resistance.** Advantage on Int, Wis, and Cha saves against spells.",
        "**Svirfneblin Camouflage.** Advantage on Stealth checks.",
        "**Gift of the Svirfneblin.** Casts Disguise Self and Nondetection free, 1/long rest each.",
        "**Senses & Languages.** Sees in the dark 120 ft. Speaks Common, Gnomish, and "
        "Undercommon.",
    ]),

    ("h2", "Lilly's Signature Gear"),
    ("stat", "Lilly's Stuff", [
        "**Essence Sphere.** A steampunk orb holding Pikachu's spark. Lilly's big quest item: "
        "she wants to give Pikachu a body again.",
        "**Frostbite Shard Dagger +1.** Her magic frost dagger (1d4 piercing + 1d4 cold). Spell "
        "focus AND arcane firearm: adds 1d8 frost to one spell she casts through it, plus +2 "
        "frost on any spell. +1 to hit.",
        "**Glimmerspire Pocket Dynamo, Mk II (Elaria's gift).** From the Wraithpine chest. "
        "Summon or recall her cannon for free, lasts 24 hours, +2 damage. Reformat (1/long "
        "rest, action), now mostly spare, since every cannon picks its blast when it fires. "
        "Needs attunement.",
        "**+1 Half Plate (her creation).** Half plate she replicated with Replicate Magic Item. "
        "Base of her AC 20.",
        "**Shield.** A sturdy steel shield. Adds +2 to her armor.",
    ]),

    ("h2", "Lilly's Spellbook"),
    ("body", "Slots per day: 4 first-level, 2 second-level. Cantrips are free forever. She "
             "prepares 7 spells; the four marked Always Prepared are free from her Artillerist "
             "subclass and don't count toward that. The +1d8 frost is her dagger's arcane "
             "firearm (it rides one spell she casts each turn), and the +2 frost rides along on "
             "any spell cast through the dagger."),
    ("stat", "Cantrips (free forever)", [
        "**True Strike.** Action, melee. Stab with the Frostbite dagger using INT: +9 to hit; "
        "1d4 + 1d4 cold + 6, plus 1d6 radiant, plus 1d8 frost (arcane firearm) and 2 frost.",
        "**Fire Bolt.** Action, 120 ft. Ranged spell attack +8: 2d10 fire + 1d8 + 2 frost "
        "(dagger). Her reliable ranged poke; never runs out.",
        "**Mending.** 1 minute, touch. Repair a single break or tear in an object no bigger "
        "than 1 ft. Free from Tinker's Magic. Also heals her cannon 2d6!",
    ]),
    ("stat", "1st-Level Spells", [
        "**Shield (Always Prepared).** Reaction. Snap up a force wall: +5 AC until the start of "
        "her next turn (can turn a hit into a miss) and no damage from Magic Missile.",
        "**Thunderwave (Always Prepared).** Action, self (15-ft cube). Con save DC 16: on a "
        "fail, 2d8 thunder + 1d8 + 2 frost (dagger) and shoved 10 ft away; half and no shove "
        "on a success.",
        "**Absorb Elements.** Reaction when she takes acid/cold/fire/lightning/thunder: take "
        "half of it, and her next melee hit deals +1d6 of that type.",
        "**Catapult.** Action, 60 ft. Fling a loose object (up to 5 lb). Dex save DC 16: on a "
        "fail, 3d8 bludgeoning + 1d8 + 2 frost (dagger); no damage on a success.",
        "**Snare.** 1 minute to set, touch, 8-hour trap. First creature to step in makes a Dex "
        "save DC 16 or is yanked upside-down, restrained in the air.",
        "**Faerie Fire.** Action, 60 ft, concentration 1 min. Foes in a 20-ft cube, Dex save "
        "DC 16; on a fail they are outlined in light: attacks against them have advantage and "
        "they can't be invisible.",
        "**Tasha's Caustic Brew.** Action, 30-ft line, concentration 1 min. Dex save or be "
        "coated in acid: 2d4 acid + 1d8 + 2 frost (dagger) at the start of each of its turns "
        "until it spends an action to wash off.",
    ]),
    ("stat", "2nd-Level Spells", [
        "**Scorching Ray (Always Prepared).** Action, 120 ft. Three rays, each a separate "
        "ranged spell attack +8: 2d6 fire each, plus 1d8 + 2 frost (dagger, once).",
        "**Shatter (Always Prepared).** Action, 60 ft (10-ft sphere). Con save DC 16: 3d8 "
        "thunder + 1d8 + 2 frost (dagger) on a fail, half on success. Extra effective against "
        "metal and stone foes.",
        "**Heat Metal.** Action, 60 ft, concentration 1 min. A metal object or armor glows "
        "red-hot: 2d8 fire + 1d8 + 2 frost (dagger) instantly, and a bonus action each turn to "
        "deal it again. The holder makes a Con save or drops the item.",
        "**Web.** Action, 60 ft (20-ft cube), concentration 1 hr. Sticky webs: difficult "
        "terrain, Dex save DC 16 or restrained (retry with a Str check). Locks down a crowd.",
    ]),

    # ==================================================================
    # STABBY SHARPBLADE
    # ==================================================================
    ("h1", "Stabby Sharpblade"),
    # Whitespace pass 2026-07: 2.3in (was 2.9) - see the Ursa portrait note.
    ("imgfloat", "assets/characters/stabby_v3_portrait.png", 2.3),
    ("body", "**Goblin Monk (Way of the Kensei), Level 5.** The wild one. Stabby is a tiny, "
             "lightning-fast goblin who fights with a candy-cane katana and his own two fists. "
             "Chaos with a smile."),
    ("dm", "**Armor Class** 18   **Hit Points** 43   **Speed** 50 ft.   **Initiative** +5   "
           "**Proficiency** +3", {"size": 11}),
    ("dm", "**STR** 8 (-1)   **DEX** 20 (+5)   **CON** 16 (+3)   **INT** 8 (-1)   "
           "**WIS** 14 (+2)   **CHA** 8 (-1)", {"size": 11}),
    ("dm", "**Focus save DC** 13. All Focus Points come back on a short rest. AC 18 normally; "
           "it jumps to 20 right after Stabby punches and swings his katana the same turn "
           "(Agile Parry). Speed and AC include his Sash.", {"size": 11}),
    ("slots", "stabby", [("Focus Points", 5)]),

    ("stat", "Saving Throws & Skills", [
        "**Saving Throws.** **Str +2**, **Dex +8**, Con +3, Int -1, Wis +2, Cha -1 "
        "(bold = proficient; his best are Dex and Str).",
        "**Skills.** **Acrobatics +8**, Animal Handling +2, Arcana -1, **Athletics +2**, "
        "Deception -1, History -1, Insight +2, Intimidation -1, Investigation -1, Medicine +2, "
        "Nature -1, Perception +2, Performance -1, Persuasion -1, Sleight of Hand +5, "
        "**Stealth +8**, **Survival +5** (bold = trained; his best are Acrobatics and Stealth, "
        "+8: sneaky and springy!).",
    ]),
    ("stat", "What Stabby Does in a Fight", [
        "**Candyfang Katana +1.** Melee, +9 to hit: 1d10 + 6 slashing + 2 cold.",
        "**Unarmed Strike (fist or foot).** Melee, +8 to hit: 1d8 + 5 bludgeoning.",
        "**Repeating Longbow +1.** Ranged, +9 to hit: 1d8 + 6 piercing; +1d4 via Kensei's Shot.",
    ]),
    ("dm", "**How Stabby's turn works.** He gets 2 attacks with his Attack action, PLUS 1 extra "
           "punch as a bonus action (Martial Arts). Spend Focus on Flurry of Blows for even "
           "more: up to 3 or 4 hits a turn!", {"size": 11}),

    ("h2", "Stabby's Special Moves"),
    ("stat", "Focus Moves (1 Focus each)", [
        "**Flurry of Blows.** Spend 1 Focus as a bonus action to make two extra punches. His "
        "big damage button.",
        "**Stunning Strike.** When he hits, spend 1 Focus to try to stun the enemy (Con save "
        "vs DC 13). Fail: stunned until his next turn, huge in a boss fight! Success: the "
        "enemy is still slowed (speed halved) and the next attack against it has advantage.",
        "**Patient Defense.** Bonus action to Disengage for free (house rule). Spend 1 Focus "
        "to also Dodge (enemies hit him with disadvantage).",
        "**Step of the Wind.** Bonus action to Dash for free. Spend 1 Focus to also Disengage "
        "and double his jump. Super zoomy.",
        "**Deflect Attack.** Reaction when hit by a punch, arrow, or blade: lower the damage "
        "by 1d10 + 10. If it hits 0, spend 1 Focus to fling it back at another enemy within "
        "5 ft (DC 13 Dex save, 2d8 + 5).",
    ]),
    ("stat", "Kensei, Monk & Goblin Traits", [
        "**Agile Parry.** After he punches and swings his katana the same turn, he gets +2 AC "
        "until his next turn. (House rule: his bonus-action punch counts.)",
        "**Kensei's Shot.** Bonus action: his next longbow hit this turn deals an extra 1d4 "
        "damage.",
        "**Slow Fall.** Reaction to take 25 less falling damage.",
        "**Uncanny Metabolism.** Once a day, when he rolls initiative: regain all Focus and "
        "heal 5 + 1d8 HP.",
        "**Fury of the Small.** When he hits a creature bigger than him (almost everyone!), "
        "deal +3 extra damage. 3 times per long rest, once per turn.",
        "**Nimble Escape.** He can Disengage or Hide as a bonus action every turn. Slippery "
        "little goblin.",
        "**Fey Ancestry.** A touch of fey blood: advantage on saves to avoid or shake off the "
        "charmed condition.",
        "**Senses & Languages.** Sees in the dark 60 ft. Speaks Common, Goblin, and Orc.",
    ]),

    ("h2", "Stabby's Signature Gear"),
    ("stat", "Stabby's Stuff", [
        "**Candyfang Katana +1.** His prized candy-cane katana. +1 to hit and damage, +2 cold. "
        "Sugar Rush: once a day, lick the blade (bonus action) for 2d8 + 3 temporary HP and a "
        "jolt of chaos energy.",
        "**Repeating Longbow +1.** A magic bow that makes its own arrows; it never runs out. "
        "+1 to hit and damage. (Lilly made it for him.)",
        "**Sash of the Swift Current (Elaria's gift).** Scarlet stage-silk from the Wraithpine "
        "chest. +1 AC, +10 ft. speed, plus Air Dance (fly for 1 minute, 1/day) and Feather "
        "Fall (1/day). Attuned.",
        "**Explorer's Pack.** Backpack, bedroll, rope, torches, rations: the usual adventuring "
        "kit.",
    ]),
    ("dm", "**Fun facts.** Stabby is a boy goblin, age 8, just 2 feet 4 inches tall and 30 "
           "pounds: small but mighty! Green skin, red eyes, green hair. He carries a creepy "
           "little idol that gives him strange dreams, and his old clan, the Bloodfang, are "
           "part of his past (and maybe future allies).", {"size": 11}),

    # ==================================================================
    # URSA CATCHUM
    # ==================================================================
    ("h1", "Ursa Catchum"),
    # Whitespace pass 2026-07: 2.5in (was 2.9) widens the stat lines wrapping
    # beside the portrait so the book's last DM box no longer splits onto a
    # two-line orphan final page.
    ("imgfloat", "assets/characters/ursa_v3_portrait.png", 2.5),
    ("body", "**Human (Mark of Handling) Druid (Circle of the Stars), Level 5.** The "
             "starwatcher. Ursa reads the night sky like a map, calls down starlight and "
             "beast-spirits, and follows the constellations toward his destiny."),
    ("dm", "**Armor Class** 18 (spiked armor and shield)   **Hit Points** 38   **Speed** 30 ft.   "
           "**Initiative** +2   **Proficiency** +3", {"size": 11}),
    ("dm", "**STR** 8 (-1)   **DEX** 14 (+2)   **CON** 14 (+2)   **INT** 12 (+1)   "
           "**WIS** 20 (+5)   **CHA** 8 (-1)", {"size": 11}),
    ("dm", "**Spell save DC** 16   **Spell attack** +8. Wisdom powers all his magic. Passive "
           "Perception 18: almost nothing sneaks past him.", {"size": 11}),
    ("slots", "ursa", [("Spell Slots, 1st Level", 4), ("Spell Slots, 2nd Level", 3),
                       ("Spell Slots, 3rd Level", 2)]),

    ("stat", "Saving Throws & Skills", [
        "**Saving Throws.** Str -1, Dex +2, Con +2, **Int +4**, **Wis +8**, Cha -1 "
        "(bold = proficient; his best are Wis and Int).",
        "**Skills.** Acrobatics +2, **Animal Handling +8**, Arcana +1, Athletics -1, "
        "Deception -1, History +1, Insight +5, Intimidation -1, Investigation +1, Medicine +5, "
        "Nature +1, **Perception +8**, Performance -1, Persuasion -1, Religion +1, Sleight of "
        "Hand +2, Stealth +2, **Survival +8** (bold = trained; his best are Animal Handling, "
        "Perception, and Survival, +8).",
    ]),
    ("stat", "What Ursa Does in a Fight", [
        "**Staff of Waking Constellations (+1), unlit.** Melee, +3 (+4) to hit: 1d6 "
        "bludgeoning (1d8 two-handed). See Shillelagh!",
        "**Staff + Shillelagh (ignited).** Melee, +9 (+10) to hit: 1d10 + 6 force or "
        "bludgeoning. Bonus action to light, lasts 1 minute.",
        "**Guiding Bolt (1st, from Staff or Star Map).** +8 to hit, 120 ft: 4d6 radiant "
        "+ 1d4 (Starseed); the next hit on that target has advantage.",
        "**Star-Arrow (Starry Form: Archer).** Bonus action, +8 to hit: 1d8 + 5 radiant, "
        "one enemy within 60 ft.",
        "**Starry Wisp (cantrip).** +8 to hit, 60 ft: 2d8 radiant + 1d4 (Starseed); "
        "lights up the target.",
        "*While his Starry Form glows, the Amulet of Guiding Light gives +1 to attacks and "
        "saves to his nearby FRIENDS (allies only, not Ursa himself, DM ruling): it is a party "
        "buff, so his own to-hit stays +8.*",
    ]),
    ("dm", "**How Ursa's turn works.** His summoned spirit acts on its own turn for free; Ursa "
           "just tells it what to do. His bonus action each turn goes to one move: fire a "
           "star-arrow (Starry Form: Archer), move a Moonbeam or Flaming Sphere, cast Healing "
           "Word, or ignite Shillelagh. And he still casts a spell or cantrip with his action "
           "the same turn.", {"size": 11}),
    ("dm", "**Free Guiding Bolts.** Before touching his real spell slots, he can throw about 10 "
           "Guiding Bolts a day for free: 5 from the Star Map (per long rest) plus up to 5 "
           "from the Staff's charges. **Starseed (+1d4 radiant).** Once a turn, rides his "
           "druid spells that deal radiant damage (Guiding Bolt, Moonbeam, Starry Wisp), NOT "
           "the Archer arrow (a form feature, not a spell; house rule).", {"size": 11}),

    ("h2", "Ursa's Special Powers"),
    ("stat", "Class Features & Mark of Handling", [
        "**Starry Form (Bonus Action).** Spend a Wild Shape use to glow with starlight (10-ft "
        "bright light, 10 min). Pick a constellation each time: **Archer** (bonus action: a "
        "star-arrow at one enemy within 60 ft, 1d8 + 5 radiant), **Chalice** (when he heals "
        "someone with a spell slot, he or a nearby friend also heals 1d8 + 5), or **Dragon** "
        "(treat a roll of 9 or lower as a 10 on Int and Wis checks and concentration saves).",
        "**Wild Shape (2 uses).** Two uses that fuel his Starry Forms (or turn into a beast "
        "he has seen). Regain 1 on a short rest, all on a long rest.",
        "**Wild Resurgence.** Once per turn (no action), spend a spell slot to get back one "
        "Wild Shape use. And once per long rest, the reverse: spend a Wild Shape use (no "
        "action) to regain a 1st-level spell slot.",
        "**Star Map.** His star chart is a magic focus. Free Guiding Bolt 5/day even without "
        "the Staff. Backup focus he still carries.",
        "**Wild Intuition.** Add 1d4 to any Animal Handling or Nature check.",
        "**Primal Connection (1/short rest).** Cast Animal Friendship or Speak with Animals "
        "for free, no materials; they're always ready and never use up a prepared spell.",
        "**The Bigger They Are.** Can charm or talk to beasts AND monstrosities (if their "
        "Intelligence is 3 or lower).",
        "**Mark of Handling.** His dragonmark lets him read animals' feelings and calm wild "
        "or magical creatures with ease.",
    ]),
    ("stat", "Ursa's Summoned Spirits", [
        "**Bestial Spirit (Summon Beast, 2nd).** AC 13, HP 30 (Air: 20, house rule), Speed 40 "
        "ft. (Land), or fly/swim 30 ft. Pick Air, Land, or Water when summoned. Maul/Rend: +8 "
        "to hit, 1d8 + 6, 1 attack. Flyby (Air): no opportunity attacks. Great scout and "
        "striker; shares Ursa's turn and obeys his commands for free.",
        "**Fey Spirit (Summon Fey, 3rd).** AC 15, HP 30, Speed 40 ft., fly 40 ft. Fey Blade: "
        "+8 to hit, 2d6 + 6 force, 1 attack. Fey Step: teleport up to 30 ft., then its mood "
        "triggers. Fuming: advantage on its next attack this turn. Mirthful: foe within 10 "
        "ft., Wis save DC 16 or Charmed. Tricksy: fills a 10-ft cube with magical Darkness.",
    ]),

    ("h2", "Ursa's Signature Gear"),
    ("stat", "Ursa's Stuff", [
        "**Staff of Waking Constellations (Elaria's gift).** His Wraithpine relic. +1 "
        "quarterstaff and druidic focus. Holds 5 charges (regain 1d4 + 1 at dawn): Guiding "
        "Bolt (1), Faerie Fire (1), Moonbeam (2). Starseed: once a turn, when a druid spell "
        "deals radiant damage, add +1d4 radiant. Starlight: bonus action to light a soft "
        "10-ft glow and get advantage on night navigation. Attuned.",
        "**Star Map.** A Tiny star chart that doubles as a spellcasting focus. Free Guiding "
        "Bolt 5/day. (Backup focus.)",
        "**Amulet of Guiding Light.** Guiding Light: during Starry Form, Ursa and allies in "
        "the bright light get +1 to attacks and saves. Starry Glow (1/day, reaction): when he "
        "or a nearby ally is hit, the attacker takes 2d8 radiant and may be blinded (Con save "
        "DC 15). Celestial Resilience (2/day): reroll a natural 1.",
        "**Three Enchanted Potatoes.** His mysterious quest trinket: the strange spuds tied "
        "to his father's disappearance.",
        "**Spiked Armor & Shield.** Dwarf-made spiked armor plus a shield; together they make "
        "his AC 18.",
        "**Explorer's Pack.** Backpack, bedroll, mess kit, tinderbox, 10 torches, 10 days of "
        "rations, waterskin, 50 ft. of rope.",
    ]),

    ("h2", "Ursa's Spellbook"),
    ("body", "Slots per day: 4 first-level, 3 second-level, 2 third-level. Cantrips are free "
             "forever. He prepares 9 spells (2024 rules) and can swap one on a long rest, and "
             "he stretches them: Speak with Animals and Animal Friendship come free from his "
             "Mark of Handling, and Faerie Fire fires from the Staff's charges, so none of "
             "those use his 9. Spell save DC 16, spell attack +8."),
    ("stat", "Cantrips (free forever)", [
        "**Shillelagh.** Bonus action, self, 1 minute. Starlight sheathes his staff: for 1 "
        "minute it swings with WISDOM, +9 to hit (+10 in Starry Form), 1d10 + 6 force or "
        "bludgeoning, his choice. Recast any time. His answer when something gets right in "
        "his face. (House rule: replaces Primal Savagery, 2024 rules.)",
        "**Starry Wisp.** Action, 60 ft. Ranged spell attack +8: 2d8 radiant + 1d4 (Starseed). "
        "The target glows (dim light) and can't turn invisible until the end of his next turn.",
        "**Guidance.** Action, touch, concentration 1 min. Once before it ends, a willing "
        "friend adds 1d4 to one ability check (roll the d4 after seeing the result).",
        "**Druidcraft.** Action, 30 ft. Tiny nature magic: predict the next 24 hours of "
        "weather, bloom a flower, make a harmless sound or smell, or light and snuff a small "
        "flame.",
    ]),
    ("stat", "1st-Level Spells", [
        "**Guiding Bolt.** Action, 120 ft (Star Map: free 5/day). Ranged spell attack +8: 4d6 "
        "radiant + 1d4 (Starseed), and the next attack against that target before Ursa's next "
        "turn has advantage.",
        "**Healing Word.** Bonus action, 60 ft. Heal one creature he can see 2d4 + 5 HP, and "
        "he can still cast a cantrip or attack the same turn. Best for popping a downed "
        "friend back up from range.",
        "**Goodberry.** Action, touch, lasts 24 hr. Creates 10 berries; eating one is a Bonus "
        "Action (2024 rules) and heals 1 HP and feeds someone for a day. Cast before a fight "
        "to bank 10 little heals.",
        "**Faerie Fire (via Staff charge).** Action, 60 ft, concentration 1 min. Foes in a "
        "20-ft cube, Dex save DC 16; on a fail they are outlined in light: attacks against "
        "them have advantage and they can't hide or turn invisible. Cast from the Staff (1 "
        "charge), so it doesn't use a prepared slot.",
        "**Speak with Animals (free, Mark).** Ritual, action, self, 10 min. Talk with beasts: "
        "they can describe nearby places, monsters, and what they've seen. Free once per "
        "short rest from his Mark of Handling.",
        "**Animal Friendship (free, Mark).** Action, 30 ft, 24 hr. One beast (Int 3 or lower) "
        "makes a Wis save DC 16 or is charmed and friendly for 24 hours. With The Bigger They "
        "Are, he can target dumb monstrosities too. Free once per short rest from his Mark.",
    ]),
    ("stat", "2nd-Level Spells", [
        "**Moonbeam.** Action, 120 ft, concentration 1 min (Staff: 2 charges). A 5-ft pillar "
        "of light. Con save DC 16 when the beam appears on a creature, when it enters, or "
        "when it ends its turn there: 2d10 radiant + 1d4 (Starseed) on a fail, half on a "
        "success. Move it 60 ft each turn as part of the spell.",
        "**Flaming Sphere.** Action, 60 ft, concentration 1 min. A 5-ft fire ball. A creature "
        "ending its turn within 5 ft makes a Dex save DC 16: 2d6 fire on a fail, half on "
        "success. Bonus action to roll it 30 ft (ram a foe to force the save).",
        "**Spike Growth.** Action, 150 ft, concentration 10 min. A 20-ft circle of ground "
        "sprouts hidden thorns: difficult terrain, and 2d4 piercing for every 5 ft a creature "
        "moves through. It looks like normal ground; herd foes across it or drop it under a "
        "charging monster.",
        "**Summon Beast.** Action, 90 ft, concentration 1 hr. Calls the Bestial Spirit (stats "
        "above). It acts right after Ursa on his initiative and obeys his commands for free. "
        "His go-to summon: a sturdy front-line ally that lasts a whole hour.",
    ]),
    ("stat", "3rd-Level Spells", [
        "**Call Lightning.** Action, 120 ft, concentration 10 min. Make a storm cloud; each "
        "turn, use an action to strike: creatures within 5 ft of the point make a Dex save "
        "DC 16, 3d10 lightning on a fail, half on success. +1d10 if it's already stormy.",
        "**Summon Fey.** Action, 90 ft, concentration 1 hr. Calls the Fey Spirit (stats "
        "above). Faster and hits harder than the beast, with a mood power and a 30-ft "
        "teleport. Acts on Ursa's turn and obeys him for free.",
    ]),

    # ==================================================================
    # GHOSTBLOOM, THE PARTY'S COMPANION
    # ==================================================================
    ("h1", "The Party's Companion: Ghostbloom"),
    ("body", "Once the party's little plant-friend Floraburst, reborn in Wraithpine's "
             "ghost-light as a pale, glowing, chiming spirit who floats beside the Guardians."),
    ("statblock", {
        "name": "Ghostbloom, Spectral Blossom",
        "type": "Tiny Fey (Ghost/Grass), Chaotic Good, Companion of the Guardians",
        "ac": "15",
        "hp": "52 (8d4 + 32)",
        "speed": "30 ft., fly 30 ft. (hover)",
        "abilities": {"STR": 8, "DEX": 18, "CON": 18, "INT": 12, "WIS": 14, "CHA": 16},
        "saves": "Dex +7, Con +7, Wis +5",
        "skills": "Perception +5, Stealth +7",
        "vulnerabilities": "Fire, Cold (mind the friendly fire!)",
        "resistances": "Necrotic; nonmagical attacks",
        "condition_immunities": "Charmed, Frightened",
        "senses": "Darkvision 60 ft., Passive Perception 15",
        "languages": "Sylvan, telepathy 30 ft.",
        # Whitespace pass 2026-07: 1.6in wide (2.4in tall at this art's 2:3
        # aspect); at the default clamp the float outran the head text by
        # ~12pt and pushed the closing DM note onto a two-line orphan page.
        "img": "assets/characters/ghostbloom.png", "img_w": 1.6,
        "traits": [
            ("Fey Step (1/Short Rest)", "As a bonus action, teleport up to 20 feet to an "
             "unoccupied space you can see. Your next attack roll before the end of your turn "
             "has advantage."),
            ("Spectral Form", "You can move through other creatures and objects as if they "
             "were difficult terrain. If you end your turn inside an object, you are shunted "
             "to the nearest unoccupied space and take 5 force damage."),
            ("Guardian's Light (3/Short Rest)", "*Reaction, 30 ft.* When an ally you can see "
             "takes damage, that ally regains 1d8 + 3 hit points and immediately ends the "
             "charmed or frightened condition on itself."),
        ],
        "actions": [
            ("Multiattack", "Ghostbloom makes two Spectral Lash attacks."),
            ("Spectral Lash", "*Melee Weapon Attack:* +7 to hit, reach 15 ft., one target. "
             "*Hit:* 1d8 + 5 slashing plus 1d6 necrotic damage, and the target must succeed "
             "on a DC 15 Wisdom saving throw or be frightened until the end of its next turn."),
            ("Ghostly Wail (1/Long Rest)", "A haunting cry in a 15-foot cone. Each creature "
             "in that area must succeed on a DC 15 Wisdom saving throw, taking 4d6 necrotic "
             "damage on a failed save, or half as much on a success. On a failed save, the "
             "target is frightened until the end of its next turn."),
        ],
    }),
    ("dm", "**Running Ghostbloom at the table.** Guardian's Light is the party's safety net: "
           "budget it (3 per short rest) and save one for the boss. Ghostbloom fears the "
           "rifts: play its guttering glow near planar wrongness, and let helping cost it "
           "courage. And keep it well clear of Lilly's flamethrower cone and cold bursts; "
           "fire and cold hit it double.", {"size": 11}),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    NOTE = "A running reference for The Guardians of Elaria. Updated as the chronicle grows."
    standalone = [("titlepage", "THE GUARDIANS OF ELARIA", "CHARACTER SHEETS",
                   "The Heroes at Level 5", NOTE)] + S
    print("built", build_doc(standalone, "compendium/character_sheets.docx"))
