# build_bestiary.py
# The Guardians of Elaria: THE BESTIARY.
# A comprehensive, illustrated field guide to every creature, companion, and
# enemy the party has met across the whole chronicle (Sessions 1-7), each in
# the Session 7 / Gearhaven CARD format that all session appendices now use:
# ("enemy_cards", [...]) rows, regulars doubled up two or three to a row,
# bosses and stars solo at full width, companions under teal banners, and
# every creature's italic lore lead kept right before its card.
#
# Stats are transcribed AS WRITTEN from the previous house-box edition of this
# file, which itself took them from the session documents:
#   sessions/session_01_gathering_of_friends.docx (Lickgloom, Duckleaf, Cognifin, Mist Stalker)
#   sessions/session_02_oakshade_village.docx (Mudskip, Grimfang war band, Terranox)
#   sessions/session_03_quest_for_knowledge.docx (Shadowflame, Displacer Beasts, Shroomyte,
#                                                  companions Floraburst/Aqualump/Emberpaws)
#   sessions/session_04_encounter_tables_and_stat_blocks.docx (the Krampusshade winter court)
#   sessions/session_05_stat_blocks.docx (Davy Jones and his drowned crew)
#   sessions/session_06_wraithpine.docx (the False Hydra, Scarecrows, Strawlings, rats, undead)
#   sessions/session_07_gearhaven.docx (the clockwork enemies; this doc's style is the model)
#   lore/floraburst_statblock.docx (the evolved Floraburst / Ghostbloom line)
#
# Build:  python templates/build_bestiary.py   ->   compendium/bestiary.docx
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

NOTE = "A running reference for The Guardians of Elaria. Updated as the chronicle grows."

# Companions and friends carry the Ghostbloom teal banner instead of crimson.
TEAL = "1F7A78"

B = [
    ("titlepage", "THE GUARDIANS OF ELARIA", "THE BESTIARY",
     "Creatures of the Chronicle", NOTE),

    ("gold", "Here is every creature the Guardians have faced, freed, or befriended, gathered "
             "with its lore and its complete statistics. When a planar creature falls, it leaves "
             "no body: a gleaming mote of its home plane rises, hangs a moment, and fades (and the "
             "Essence Sphere tugs toward it). Read on, brave heroes, and know your monsters."),
    ("lore", "The Wakened",
     "The scholars of Ravenstone keep trying to sort the wondrous creatures of the Darkening "
     "into families, and the creatures keep declining. A duck with a leek. A fish that swims "
     "through air. A plant that chose three children. The only taxonomy that has ever held is "
     "the Circle's: some things wake up when the worlds lean close, and what they become "
     "depends entirely on who finds them first."),

    # ==================================================================
    ("h1", "Companions & Friends"),
    ("gold", "Not every creature in this book is an enemy. Some walk the road beside the Guardians."),
    ("lore", "Why the Guardians",
     "The Warden's safeguards do not choose the strong. Every tale of the scattered gifts "
     "agrees on this one point: they choose the kind, because kindness is the only power "
     "Maldrith has never once predicted correctly. The friends who walk beside the Guardians "
     "were won the same way, one small mercy at a time."),

    ("body", "*Ghostbloom is the party's dearest companion, chosen in Session 3 as Floraburst, "
             "changed aboard the sinking Dutchman and again in Wraithpine's ghost-light. Her petals "
             "are glass-pale now and chime like frost; she floats, speaks in soft telepathy, and "
             "glows brighter near planar wounds. Some say she is Elaria's own little voice.*"),
    # Reconciled 2026-07-06 to characters/historical/ghostbloom_statblock_v3.pdf
    # (recency rule); the full companion sheet lives in Part IV.
    ("enemy_cards", [{
        "name": "Ghostbloom, Spectral Blossom",
        "sub": "Tiny fey (Ghost/Grass), chaotic good ✦ the party's companion",
        "img": "assets/characters/ghostbloom.png", "img_w": 2.4,
        "banner": TEAL,
        "stats": [
            "**AC** 15 (natural armor)  **HP** 52 (8d4 + 32)  **Speed** 30 ft., fly 30 ft. (hover)",
            "**STR** 8  **DEX** 18  **CON** 18  **INT** 12  **WIS** 14  **CHA** 16",
            "**Saves** Dex +7, Con +7, Wis +5  **Skills** Perception +5, Stealth +7",
            "**Vulnerable** fire, cold (mind the friendly fire)",
            "**Resist** necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
            "**Imm.** (cond) charmed, frightened",
            "**Senses** darkvision 60 ft., passive Perception 15",
            "**Languages** Sylvan, telepathy 30 ft. (to her keeper)",
        ],
        "traits": [
            ("Fey Step (1/Short Rest)", "As a bonus action, teleport up to 20 ft. to an unoccupied space "
             "she can see. Her next attack this turn has advantage."),
            ("Spectral Form", "She can move through creatures and objects as difficult terrain. If she "
             "ends her turn inside an object, she is shunted to the nearest space and takes 5 force damage."),
            ("Guardian's Light (3/Short Rest)", "*Reaction, 30 ft.* When an ally she can see takes damage, "
             "that ally regains 1d8 + 3 hit points and immediately ends the charmed or frightened "
             "condition on itself."),
        ],
        "actions": [
            ("Multiattack", "She makes two Spectral Lash attacks."),
            ("Spectral Lash", "*Melee Weapon Attack:* +7 to hit, reach 15 ft., one target. *Hit:* 9 (1d8 + 5) "
             "slashing plus 3 (1d6) necrotic, and the target must succeed on a DC 15 Wisdom save or be "
             "frightened until the end of its next turn."),
            ("Ghostly Wail (1/Long Rest)", "A haunting cry in a 15-ft. cone. Each creature there makes a DC 15 "
             "Wisdom save, taking 14 (4d6) necrotic and frightened until the end of its next turn on a fail, "
             "or half damage and no fear on a success."),
        ],
    }]),

    ("body", "*The rift arc asks more of her than the road ever did. This is Ghostbloom as she "
             "stands at the party's side from the Earth Rift onward: the same creature, grown "
             "into the work. Her older card above is kept for the Sessions 1 to 7 chronicle.*"),
    # Level-7 companion card (DM directive 2026-07-18): +1 AC, +1 proficiency,
    # +10 HP, +1 weapon damage, and one more die on Guardian's Light and the
    # Wail. She is the generalist the rift specialists are measured against.
    ("enemy_cards", [{
        "name": "Ghostbloom, Spectral Blossom (Level 7)",
        "sub": "Tiny fey (Ghost/Grass), chaotic good \u2726 the party's companion, rift arc",
        "img": "assets/characters/ghostbloom_l7.png", "img_w": 2.4,
        "banner": TEAL,
        "stats": [
            "**AC** 16 (natural armor)  **HP** 62 (8d4 + 42)  **Speed** 30 ft., fly 30 ft. (hover)",
            "**STR** 8  **DEX** 18  **CON** 18  **INT** 12  **WIS** 14  **CHA** 16",
            "**Saves** Dex +8, Con +8, Wis +6  **Skills** Perception +6, Stealth +8",
            "**Vulnerable** fire, cold (mind the friendly fire)",
            "**Resist** necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
            "**Imm.** (cond) charmed, frightened",
            "**Senses** darkvision 60 ft., passive Perception 16",
            "**Languages** Sylvan, telepathy 30 ft. (to her keeper)",
        ],
        "traits": [
            ("Fey Step (1/Short Rest)", "As a bonus action, teleport up to 20 ft. to an unoccupied space "
             "she can see. Her next attack this turn has advantage."),
            ("Spectral Form", "She can move through creatures and objects as difficult terrain. If she "
             "ends her turn inside an object, she is shunted to the nearest space and takes 5 force damage."),
            ("Guardian's Light (3/Short Rest)", "*Reaction, 30 ft.* When an ally she can see takes damage, "
             "that ally regains 12 (2d8 + 3) hit points and immediately ends the charmed or frightened "
             "condition on itself."),
        ],
        "actions": [
            ("Multiattack", "She makes two Spectral Lash attacks."),
            ("Spectral Lash", "*Melee Weapon Attack:* +8 to hit, reach 15 ft., one target. *Hit:* 10 (1d8 + 6) "
             "slashing plus 3 (1d6) necrotic, and the target must succeed on a DC 16 Wisdom save or be "
             "frightened until the end of its next turn."),
            ("Ghostly Wail (2/Long Rest)", "A haunting cry in a 15-ft. cone. Each creature there makes a DC 16 "
             "Wisdom save, taking 17 (5d6) necrotic and frightened until the end of its next turn on a fail, "
             "or half damage and no fear on a success."),
        ],
    }]),

    ("h2", "The Companion Swap (from Session 8 on)"),
    ("body", "The Essence Sphere is the roster. **One companion walks in the world at a "
             "time**; everybody else rides inside the Sphere, safe and awake and perfectly "
             "fine. **Swapping is Lilly's Action**: she calls the name, the one outside "
             "steps into the light, and the one she called steps out. \"Sandshrew, I choose "
             "you!\" **Nobody ever dies in there**: a companion knocked to 0 hit points "
             "faints and the Sphere recalls it on the spot, not lost, not hurt for keeps, "
             "not gone. Choose before you go, not in the middle: picking wrong for a plane "
             "is a real mistake and an entirely survivable one. **The roster grows by one "
             "per rift.**"),

    ("body", "*The Underroot's own answer to a charge. Sandshrew plants itself between the party "
             "and whatever is coming, dares the whole pack to come through him, and makes the "
             "ground they would have to cross buck and split beneath them.*"),
    # Earth-rift companion (DM directive 2026-07-18): the TANK of the roster.
    # No expendable uses: the Action and the Reaction are the whole limiter.
    ("enemy_cards", [{
        "name": "Sandshrew",
        "sub": "Medium beast (Ground), unaligned \u2726 Earth-rift companion",
        "img": "assets/characters/sandshrew.png", "img_w": 2.4,
        "banner": TEAL,
        "stats": [
            "**AC** 17 (natural armor)  **HP** 78 (12d8 + 24)  **Speed** 30 ft., burrow 40 ft.",
            "**STR** 18  **DEX** 14  **CON** 15  **INT** 6  **WIS** 12  **CHA** 10",
            "**Saves** Str +7, Con +5  **Skills** Athletics +7, Perception +4",
            "**Vulnerable** cold",
            "**Resist** bludgeoning, piercing, and slashing from nonmagical attacks",
            "**Senses** darkvision 60 ft., tremorsense 30 ft., passive Perception 14",
            "**Languages** understands its handler, speaks none",
        ],
        "traits": [
            ("Sand Veil", "Dust curls constantly from its plates. Attack rolls against Sandshrew "
             "made from more than 15 feet away have Disadvantage."),
            ("Curl Up", "*Reaction.* When Sandshrew is hit by an attack, it tucks behind its "
             "plates. Reduce that attack's damage by 10."),
        ],
        "actions": [
            ("Multiattack", "It makes two Claw attacks."),
            ("Claw", "*Melee Weapon Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 10 (1d10 + 5) "
             "slashing damage."),
            ("Challenge", "*Bonus Action, 30 ft., one enemy that can see it.* Sandshrew rears "
             "up with a rattling hiss and dares that one to try it. Until the start of "
             "Sandshrew's next turn, the target has Disadvantage on attack rolls against any "
             "target other than Sandshrew."),
            ("Earthquake", "Sandshrew slams both forefeet down and the ground bucks and splits in "
             "a 20-foot Cube centered on itself. Each creature of Sandshrew's choice in that area "
             "makes a DC 15 Dexterity saving throw, taking 10 (3d6) Bludgeoning damage on a failed "
             "save, or half as much damage on a successful one. The broken ground is Difficult "
             "Terrain until the start of Sandshrew's next turn."),
        ],
    }]),

    ("body", "*The Undersea's gift, promised for the Water rift: a very small, very proud "
             "field medic. Piplup holds the backline, mends whoever is bleeding, shields "
             "whoever is next, and slows whatever comes wading in after them.*"),
    # Water-rift companion (DM 2026-08-18): the HEALER of the roster. Fragile on
    # purpose: AC 13 and 45 HP are the price of the kit. Healing lane outclasses
    # Ghostbloom by design (roster rule: each specialist beats her in one lane).
    # REBUILT 2026-08-20 from a 60-day sim bake-off against Ghostbloom and
    # Sandshrew. v1 topped BOTH damage and control, squatting on the Fire and Air
    # lanes; it also died constantly once Shardwings began hunting the weakest.
    # v4 keeps him last in damage and control and first in healing and
    # prevention: 7.5% of party damage, 48 healed and 48 prevented per day, and
    # the LOWEST hero-knockdown rate in the roster (0.10/day vs Sandshrew 0.17,
    # Ghostbloom 0.23). Ice Beam went to one attack at +8 (the roster standard;
    # +6 was the outlier), the slow dropped to 10 ft so it stops crowding Air,
    # Water Jet retired, and Mistguard replaced it as an after-the-roll +5 AC.
    # NOTE for play: Piplup covers the BACKLINE. Only ~29% of the attacks Stabby
    # takes land within Mistguard's 30 ft, because he fights at 60. That is the
    # reason to field Sandshrew instead on a day the monk is the one bleeding.
    ("enemy_cards", [{
        "name": "Piplup",
        "sub": "Small beast (Water), unaligned \u2726 Water-rift companion (joins in Session 9)",
        "img": "assets/companions/piplup.png", "img_w": 2.6,
        "banner": TEAL,
        "stats": [
            "**AC** 13  **HP** 45 (10d6 + 10)  **Speed** 25 ft., swim 50 ft.",
            "**STR** 6  **DEX** 16  **CON** 12  **INT** 10  **WIS** 16  **CHA** 14",
            "**Saves** Dex +6, Wis +6  **Skills** Medicine +6, Performance +5",
            "**Resist** cold",
            "**Senses** darkvision 60 ft., passive Perception 13",
            "**Languages** understands its handler; says only his own name, with total clarity",
        ],
        "traits": [
            ("Proud Heart", "Piplup has Advantage on saving throws against being Frightened, "
             "and nothing can make him retreat while a friend is down."),
            ("Slipstream", "While swimming, Piplup doesn't provoke Opportunity Attacks."),
        ],
        "actions": [
            ("Multiattack", "Piplup makes two Ice Beam attacks."),
            ("Ice Beam", "*Ranged Attack:* +8 to hit, range 60/120 ft., one target. *Hit:* 10 "
             "(2d6 + 3) Cold damage, and the target's Speed drops by 10 feet until the end "
             "of its next turn (the slow doesn't stack)."),
            ("Heal Bubble (Bonus Action, 5/Short Rest)", "A shimmering bubble drifts to one "
             "creature Piplup can see within 30 feet and pops into cool silver mist: it "
             "regains 14 (2d8 + 5) hit points and is cured of the Poisoned condition."),
            ("Sea Mist (2/Day)", "Piplup breathes out a rolling bank of cool silver fog: a "
             "20-foot-radius Sphere centered on a point he can see within 60 feet, lasting "
             "**1 round**. His friends always know where each other are inside it and nothing "
             "else does, so while in the fog **allies have Advantage on attack rolls, attacks "
             "against them have Disadvantage, and they can Disengage for free**."),
        ],
        "reactions": [
            ("Mistguard", "*Reaction.* When a creature Piplup can see within 30 feet is hit by "
             "an attack, cold haze closes over it: that creature gains **+5 AC against that "
             "attack**, which may turn the hit into a miss. Decide **after the roll**, the way "
             "Lilly's Shield works."),
        ],
    }]),

    ("body", "*The Ignis rift's gift and the roster's striker: it runs up walls, spins "
             "through a crowd as a burning hoop, and hits hardest when it is closest to "
             "going down.*"),
    # Fire-rift companion, DM design 2026-08-21, sim field-tested for role fit.
    #
    # *** CHIMCHAR IS A DELIBERATE TRAP. DO NOT "FIX" HIM. (DM, 2026-08-22) ***
    # He deals the most damage of any companion by a wide margin and is still the
    # WORST of the five at the thing companions are for. Measured over 200-day
    # sweeps: at the design point he is last in hero knockdowns (0.20 against
    # Piplup's 0.06), and as encounters scale up he degrades faster than anything
    # else on the board, roughly nine times faster than Piplup:
    #     enemy HP     x1   x1.25   x1.5   x1.75    x2
    #     Chimchar      0       6     15      41    64   party wipes / 200 days
    #     Piplup        0       0      0       4     7
    # The cause is structural and not a tuning error: party damage is capped by
    # the enemies' hit points, so a damage companion DISPLACES hero damage rather
    # than shortening the fight, while healing and mitigation scale with fight
    # length. Tested a Fire Wheel buff to 12.5 average damage: it improved
    # knockdowns at the design point (0.20 to 0.12) and moved wipes under pressure
    # from 15 to 14. It cannot fix this, because more damage is not the missing
    # thing.
    # The DM's intent is that the party LEARN this: big numbers are the bait, and
    # working out that a companion's job is support rather than damage is the
    # lesson. The swap is Lilly's Action and a fainted companion is recalled
    # unharmed, so discovering the trap costs them a turn, not a character.
    # NOTE: the trap is nearly invisible at x1 (zero wipes, 77 percent floor). It
    # only bites from about x1.25 upward, so it teaches nothing in an encounter
    # that is not applying real pressure.
    # The STRIKER lane: highest single-target output in the roster, and the only
    # companion whose numbers rise as its hit points fall (Blaze).
    ("enemy_cards", [{
        "name": "Chimchar",
        "sub": "Medium beast (Fire), unaligned \u2726 Fire-rift companion (joins in Session 10)",
        "img": "assets/companions/chimchar.png", "img_w": 2.25,
        "banner": TEAL,
        "stats": [
            "**AC** 16 (singed hide)  **HP** 71 (13d8 + 13)  **Speed** 40 ft., climb 30 ft.",
            "**STR** 14  **DEX** 16  **CON** 12  **INT** 8  **WIS** 12  **CHA** 12",
            "**Saves** Dex +6, Con +4  **Skills** Acrobatics +6, Athletics +5, Perception +4",
            "**Immune** fire  **Vulnerable** cold",
            "**Senses** darkvision 60 ft., passive Perception 14",
            "**Languages** understands its handler, speaks none",
        ],
        "traits": [
            ("Blaze", "While Chimchar has half its hit points or fewer, the fire on its tail "
             "roars up and the air around it boils: it deals an extra 1d6 + 3 Fire damage with "
             "**every** source of damage it deals, it has Advantage on its Ember Claw attacks, "
             "and attack rolls against it have Disadvantage."),
            ("Sure-Footed", "Chimchar can move across vertical surfaces and along ceilings "
             "without spending extra movement, and it doesn't lose its grip when it takes "
             "damage."),
        ],
        "actions": [
            ("Multiattack", "Chimchar makes two Ember Claw attacks."),
            ("Ember Claw", "*Melee Attack:* +8 to hit, reach 5 ft., one target. *Hit:* 10 "
             "(1d10 + 5) Fire damage."),
            ("Fire Wheel (Bonus Action)", "Chimchar tucks and spins, a burning hoop of "
             "itself. Each creature in a 20-foot Emanation originating from Chimchar makes a "
             "DC 15 Dexterity saving throw, taking 7 (2d6) Fire damage on a failure, or half as "
             "much on a success."),
            ("Flare Blitz (2/Day)", "Chimchar takes a run-up and becomes a comet. Each creature "
             "within 40 feet makes a DC 15 Dexterity saving throw, taking 17 (5d6) Fire damage "
             "on a failure, or half as much on a success."),
        ],
        "reactions": [
            ("Backdraft", "*Reaction.* When Chimchar is hit by a melee attack, the attacker "
             "takes 6 (1d6 + 3) Fire damage for getting that close."),
        ],
    }]),

    ("body", "*The Aer rift's gift, and the roster's controller. Togekiss never lands, never "
             "hurries, and quietly decides who in the room is allowed to see straight and who "
             "is allowed to act at all.*"),
    # Air-rift companion, DM design 2026-08-21, sim field-tested for role fit.
    # The CONTROL lane: blindness on every gleam, a 3-round area shutdown, and an
    # ally buff on its Bonus Action. Damage is deliberately last in the roster.
    ("enemy_cards", [{
        "name": "Togekiss",
        "sub": "Medium beast (Fairy), unaligned \u2726 Air-rift companion (joins in Session 11)",
        "img": "assets/companions/togekiss.png", "img_w": 2.6,
        "banner": TEAL,
        "stats": [
            "**AC** 14  **HP** 50 (9d8 + 10)  **Speed** 20 ft., fly 40 ft.",
            "**STR** 8  **DEX** 16  **CON** 12  **INT** 12  **WIS** 12  **CHA** 18",
            "**Saves** Con +4, Wis +4, Cha +7  **Skills** Perception +4, Performance +7",
            "**Immune** radiant  **Vulnerable** necrotic",
            "**Senses** darkvision 60 ft., passive Perception 14",
            "**Languages** understands its handler, speaks none",
        ],
        "traits": [
            ("Flyby", "Togekiss doesn't provoke Opportunity Attacks when it flies out of an "
             "enemy's reach."),
            ("Gentle Heart", "Togekiss has Advantage on saving throws against being Frightened, "
             "and it will not leave an ally who is down."),
        ],
        "actions": [
            ("Multiattack", "Togekiss makes two Dazzling Gleam attacks."),
            ("Dazzling Gleam", "*Ranged Attack:* +8 to hit, range 60 ft., one target. *Hit:* 9 "
             "(2d6 + 2) Radiant damage, and the target makes a DC 15 Wisdom saving throw. On a "
             "failed save, it has the Blinded condition until the end of its next turn."),
            ("Sing (3/Day)", "Togekiss settles on the air and begins to hum. Each enemy within "
             "30 feet makes a DC 15 Wisdom saving throw or has the Incapacitated condition, "
             "repeating the save at the end of each of its turns to end the effect, up to 3 "
             "rounds. Creatures that don't sleep are unaffected."),
            ("Serene Grace (Bonus Action)", "One ally Togekiss can see within 60 feet has "
             "Advantage on attack rolls and a +2 bonus to AC until the start of Togekiss's next "
             "turn."),
        ],
        "reactions": [
            ("Charm", "*Reaction.* When a creature Togekiss can see hits it with an attack, that "
             "creature makes a DC 15 Wisdom saving throw. On a failed save, it has Disadvantage "
             "on attack rolls until the end of its next turn."),
        ],
    }]),

    ("lore", "The Kept Company",
     "The sky-readers keep a gentler list beside their catalogue of frights: the wonders "
     "that chose to stay. A creature woken by the Darkening can turn wild or turn kind, and "
     "the Circle has never found a rule for which, only a pattern, that the ones met with a "
     "shared meal and a true name tend to follow the heroes home. A companion, the old "
     "teaching runs, is a mote that decided to belong to someone. They are counted among the "
     "Guardians' truest treasures, and guarded twice as fiercely for having been freely given."),

    ("body", "*Floraburst, as she was before the change: a leafy sprout-backed creature who loved "
             "sunlight and berries. This is the form the party first knew and loved in Session 3.*"),
    ("enemy_cards", [{
        "name": "Floraburst",
        "sub": "Small fey, neutral good ✦ the companion as she was chosen",
        "img": "assets/characters/floraburst.png", "img_w": 3.0,
        "banner": TEAL,
        "stats": [
            "**AC** 14 (natural armor)  **HP** 45 (6d6 + 18)  **Speed** 30 ft.",
            "**STR** 14  **DEX** 12  **CON** 16  **INT** 10  **WIS** 14  **CHA** 10",
            "**Skills** Nature +4, Survival +4  **Resist** poison",
            "**Senses** darkvision 60 ft., passive Perception 12",
            "**Languages** understands Sylvan and Common but cannot speak",
        ],
        "traits": [
            ("Plant Camouflage", "Advantage on Stealth checks to hide in heavy foliage."),
            ("Photosynthesis", "During a short or long rest in sunlight, Floraburst recovers 10 extra hit points."),
        ],
        "actions": [
            ("Razor Leaf", "*Ranged Weapon Attack:* +4 to hit, range 30 ft., one target. *Hit:* 10 (2d8 + 2) slashing."),
            ("Vine Lash", "*Melee Weapon Attack:* +4 to hit, reach 15 ft., one target. *Hit:* 8 (1d10 + 2) "
             "bludgeoning, and the target must succeed on a DC 13 Strength save or be restrained until the end "
             "of its next turn."),
            ("Floraberry (3/Day)", "Floraburst produces 1d4 + 1 magical berries. A creature can use a Bonus "
             "Action to eat one and restore 3 hit points (house rule 4, as Goodberry)."),
        ],
    }]),

    ("lore", "Motes",
     "A mote is a crumb of another world, and the world it lands in treats it the way a "
     "pond treats a dropped lantern: strange light, strange ripples, and every fish in the "
     "pond suddenly having opinions. The wondrous creatures of the chronicle, the talking, "
     "glowing, impossible ones, are what happens when the ripples reach something alive."),

    ("body", "*In Session 3, Professor Aelwyn offered the party three little wards; they chose Floraburst. "
             "The two who stayed behind, Aqualump and Emberpaws, are catalogued here too, for they are "
             "part of the story.*"),
    ("enemy_cards", [
        {
            "name": "Aqualump",
            "sub": "Small elemental, neutral good ✦ stayed with Aelwyn",
            "img": "assets/characters/aqualump.png",
            "banner": TEAL,
            "stats": [
                "**AC** 16 (natural armor, Shell Defense)  **HP** 54 (7d6 + 21)",
                "**Speed** 25 ft., swim 30 ft.",
                "**STR** 15  **DEX** 14  **CON** 17  **INT** 10  **WIS** 13  **CHA** 11",
                "**Skills** Athletics +4, Perception +3  **Resist** cold",
                "**Senses** darkvision 60 ft., passive Perception 13",
                "**Languages** understands Aquan and Common but cannot speak",
            ],
            "traits": [
                ("Shell Defense", "As a bonus action, Aqualump withdraws into its shell, gaining +4 AC until the "
                 "start of its next turn; while in its shell its speed is 0."),
                ("Water Veil", "Aqualump cannot be set on fire and has advantage on saves against being ignited or burned."),
            ],
            "actions": [
                ("Water Bolt", "*Ranged Weapon Attack:* +4 to hit, range 30 ft., one target. *Hit:* 10 (2d8 + 2) "
                 "bludgeoning, and the target must succeed on a DC 14 Strength save or be knocked prone."),
                ("Surf (Recharge 5-6)", "A 15-ft. cone of water. Each creature there makes a DC 14 Dexterity save, "
                 "taking 14 (4d6) cold on a fail (half on a success); those who fail are knocked prone."),
                ("Frost Shell", "*Ranged Weapon Attack:* +4 to hit, range 20 ft., one target. *Hit:* 8 (1d10 + 2) "
                 "cold, and the target's speed is reduced by 10 ft. until the end of its next turn."),
            ],
        },
        {
            "name": "Emberpaws",
            "sub": "Small elemental, chaotic good ✦ stayed with Aelwyn",
            "img": "assets/characters/emberpaws.png",
            "banner": TEAL,
            "stats": [
                "**AC** 15 (natural armor)  **HP** 42 (6d6 + 15)",
                "**Speed** 30 ft.",
                "**STR** 13  **DEX** 16  **CON** 15  **INT** 10  **WIS** 12  **CHA** 12",
                "**Skills** Acrobatics +5, Perception +3  **Imm.** fire",
                "**Senses** darkvision 60 ft., passive Perception 13",
                "**Languages** understands Ignan and Common but cannot speak",
            ],
            "traits": [
                ("Fiery Spirit", "When reduced to 0 hit points, Emberpaws bursts into flame. Each creature within "
                 "10 ft. makes a DC 13 Dexterity save, taking 7 (2d6) fire on a fail (half on a success)."),
                ("Heatwave (3/Day)", "As a bonus action, Emberpaws radiates heat for 1 minute; any creature that "
                 "hits it with a melee attack takes 4 (1d8) fire."),
            ],
            "actions": [
                ("Ember", "*Ranged Weapon Attack:* +5 to hit, range 30 ft., one target. *Hit:* 9 (2d6 + 2) fire."),
                ("Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 8 (1d8 + 3) piercing."),
                ("Tail Flame Whip", "*Melee Weapon Attack:* +5 to hit, reach 10 ft., one target. *Hit:* 10 (2d6 + 3) "
                 "fire, and the target must succeed on a DC 13 Dexterity save or be ignited, taking 2 (1d4) fire at "
                 "the start of each of its turns until the flames are put out."),
            ],
        },
    ]),

    ("body", "*Lickgloom was the party's very first friend, met on their first night by a pond in the "
             "Forest of Whispers: round-bodied, endlessly curious, with a tongue longer than it is tall "
             "and a telepathic voice of pure feeling ('Food? Friend?'). It chose to stay among Professor "
             "Aelwyn's creatures at Ravenstone. Visits are owed.*"),
    ("enemy_cards", [{
        "name": "Lickgloom",
        "sub": "Small fey (Feywild), neutral ✦ CR 1 (200 XP) ✦ the first friend",
        "img": "assets/monsters/lickgloom.png", "img_w": 3.0,
        "banner": TEAL,
        "stats": [
            "**AC** 13 (natural armor)  **HP** 27 (5d6 + 10)  **Speed** 30 ft.",
            "**STR** 14  **DEX** 12  **CON** 14  **INT** 6  **WIS** 10  **CHA** 8",
            "**Saves** Dex +3  **Skills** Perception +2, Stealth +4",
            "**Resist** acid, poison",
            "**Senses** darkvision 60 ft., passive Perception 12",
            "**Languages** understands Common but cannot speak; telepathic impressions",
            "**Challenge** 1 (200 XP)",
        ],
        "traits": [
            ("Helpful Tongue", "Traveling with the party, Lickgloom can fetch small objects with its "
             "10 foot tongue, and once per scene its tasting tongue grants one hero advantage on a "
             "Wisdom (Perception) or Intelligence (Investigation) check."),
        ],
        "actions": [
            ("Tongue Whip", "*Melee Attack:* +4 to hit, reach 10 ft. *Hit:* 1d6 + 2 bludgeoning, and the "
             "target must succeed on a DC 12 Strength saving throw or be grappled (escape DC 12)."),
            ("Sticky Lick (Recharge 5-6)", "One creature within 10 ft. must succeed on a DC 13 Dexterity "
             "saving throw or lose one small item (a weapon, potion, or trinket), which Lickgloom pulls "
             "to itself."),
        ],
    }]),

    ("lore", "The Forest of Whispers",
     "The old grove roads are kept by creatures rather than kingdoms, and the etiquette that "
     "holds there is the same one the Long Peace taught: walk through singing, take nothing "
     "green, and leave a bite of supper at the trailhead. The kind ones answer kindness, the "
     "sky-readers say, which is why the first friend a traveler makes in the Forest of "
     "Whispers is so often the truest."),

    ("body", "**Pikachu, the Spark Fox.** *An old friend of the Glimmergear family, bodiless since before "
             "the chronicle began, sleeping inside the Essence Sphere. His golden projection first appeared "
             "in Gearhaven: two long ears, a lightning-bolt tail, and a warning carried through Ursa's Mark. "
             "He has no statistics yet; he is more a key than a creature, and his full return is still to come.*"),

    # ==================================================================
    ("h1", "Session 1: The Forest of Whispers", {"hardbreak": True}),
    ("gold", "The first creatures the Guardians ever faced, all touched by the thinning boundary "
             "between the planes. Each left behind a fading mote, the party's very first clue."),

    ("body", "*A duck grown huge and wind-wrapped, roosting in an old rune-carved stone circle; "
             "its furious quacks arrive straight in the mind.*"),
    ("enemy_cards", [{
        "name": "Duckleaf",
        "sub": "Small beast (Elemental Air), neutral ✦ CR 4 (1,100 XP) ✦ guardian of the stone circle",
        "img": "assets/monsters/duckleaf_stone_circle.png", "img_w": 3.0,
        "stats": [
            "**AC** 15 (natural armor)  **HP** 52 (8d8 + 16)  **Speed** 30 ft., fly 30 ft.",
            "**STR** 14  **DEX** 16  **CON** 14  **INT** 10  **WIS** 12  **CHA** 10",
            "**Saves** Dex +5, Wis +3  **Skills** Acrobatics +5, Perception +3",
            "**Resist** slashing, bludgeoning (wind-shielded)",
            "**Senses** darkvision 60 ft., passive Perception 13",
            "**Languages** telepathy 30 ft. (in quacks)",
            "**Challenge** 4 (1,100 XP)",
        ],
        "traits": [
            ("Winged Leap", "Duckleaf can leap 30 ft. in any direction without provoking opportunity attacks. "
             "Disrupting a stone of the rune-circle ends this ability for the rest of the battle."),
        ],
        "actions": [
            ("Leek Strike", "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 2d8 + 4 slashing."),
            ("Aerial Slash", "*Ranged Weapon Attack:* +5 to hit, range 20/60 ft., one target. *Hit:* 3d6 + 3 "
             "slashing, a blade of wind."),
            ("Quack of Fury (Recharge 5-6)", "A thunderous telepathic quack. Each creature within 15 ft. makes "
             "a DC 14 Wisdom save or is frightened for 1 minute (repeat save at end of each turn)."),
        ],
    }]),

    ("lore", "The Rings and Their Keepers",
     "Where a plane leans closest to the world, the old builders raised a ring of stones and "
     "asked one creature to keep it: a duck grown huge and wind-wrapped, a fish that swims the "
     "open air, a hound woven of mist that hunts the lantern-edge. The keepers were never meant "
     "to be fierce, the sky-readers say, only faithful, and a keeper turns dangerous only when "
     "the wall it guards begins to fail. Meet one swinging, the Circle teaches, and the kinder "
     "question is not how to beat it but what it is so frightened of losing."),

    ("body", "*A fish that swims through open air above its grove pool, trailing glowing water "
             "and speaking in pictures pressed gently into the mind.*"),
    ("enemy_cards", [{
        "name": "Cognifin",
        "sub": "Small beast (Elemental Water), neutral ✦ CR 3 (700 XP) ✦ the grove's test",
        "img": "assets/monsters/cognifin_grove.png", "img_w": 3.0,
        "stats": [
            "**AC** 14 (natural armor)  **HP** 45 (6d8 + 18)  **Speed** 0 ft., fly 30 ft. (hover)",
            "**STR** 10  **DEX** 14  **CON** 16  **INT** 10  **WIS** 14  **CHA** 12",
            "**Saves** Dex +4, Wis +4  **Skills** Perception +4, Arcana +2",
            "**Resist** cold, psychic",
            "**Senses** darkvision 60 ft., passive Perception 14",
            "**Languages** telepathy 60 ft. (images and feelings)",
            "**Challenge** 3 (700 XP)",
        ],
        "actions": [
            ("Headache Blast", "*Ranged Attack:* +4 to hit, range 30 ft., one target. *Hit:* 2d6 + 2 psychic."),
            ("Water Pulse", "*Ranged Spell Attack:* +4 to hit, range 30 ft., one target. *Hit:* 2d6 + 2 "
             "bludgeoning, and the target must make a DC 12 Strength save or be knocked prone."),
            ("Confusion Pulse (Recharge 5-6)", "A wave of psychic energy in a 15-ft. radius. Each creature there "
             "makes a DC 13 Wisdom save or is confused (as the *confusion* spell) for 1 minute (repeat save at "
             "end of each turn)."),
        ],
        "reactions": [
            ("Psychic Shield", "When hit by an attack, Cognifin gains +2 AC until the start of its next turn."),
        ],
        "legendary": [
            ("Whirlpool", "Cognifin makes a 5-ft.-radius whirlpool; creatures there make a DC 12 Strength save "
             "or be pulled 10 ft. to its center and restrained until the end of their next turn."),
            ("Tidal Wave", "A 10-ft. line of water. Creatures in its path make a DC 12 Dexterity save or take "
             "2d4 bludgeoning and are pushed back 5 ft."),
        ],
    }]),

    ("body", "*A shape of fog and hunger that hunts at the edge of lantern-light, more shadow "
             "than wolf.*"),
    ("enemy_cards", [{
        "name": "Mist Stalker",
        "sub": "Medium fey (Feywild), unaligned ✦ CR 2 (450 XP) ✦ they hunt in pairs",
        "img": "assets/monsters/mist_stalker.png", "img_w": 3.0,
        "stats": [
            "**AC** 13  **HP** 39 (6d8 + 12)  **Speed** 40 ft.",
            "**STR** 14  **DEX** 16  **CON** 14  **INT** 6  **WIS** 12  **CHA** 8",
            "**Skills** Perception +3, Stealth +5",
            "**Senses** darkvision 60 ft., passive Perception 13",
            "**Challenge** 2 (450 XP)",
        ],
        "traits": [
            ("Fog Cloak (Bonus Action)", "The stalker wraps itself in mist, becoming heavily obscured "
             "until the start of its next turn."),
        ],
        "actions": [
            ("Multiattack", "The mist stalker makes one bite attack and one claw attack."),
            ("Bite", "*Melee Attack:* +5 to hit, reach 5 ft. *Hit:* 1d8 + 3 piercing."),
            ("Claw", "*Melee Attack:* +5 to hit, reach 5 ft. *Hit:* 2d4 + 3 slashing."),
            ("Howl of the Mist (Recharge 5-6)", "A howl rolls through the fog from every direction at "
             "once. Each enemy within 30 ft. must succeed on a DC 13 Wisdom saving throw or be "
             "frightened until the end of the stalker's next turn."),
        ],
    }]),

    # ==================================================================
    ("h1", "Session 2: The Road to Ravenstone", {"hardbreak": True}),
    ("gold", "On the road to Oakshade and Ravenstone the party met slick water-elementals, an old "
             "goblin grudge come calling, and a serpent of living stone."),

    ("body", "*Slick little elementals of the wayside ponds, harmless-looking right up until the "
             "mud starts flying.*"),
    ("enemy_cards", [{
        "name": "Mudskip",
        "sub": "Small elemental (Plane of Water), neutral ✦ CR 1/2 (100 XP) ✦ mischief in numbers",
        "img": "assets/monsters/mudskip.png", "img_w": 3.0,
        "stats": [
            "**AC** 13 (natural armor)  **HP** 22 (4d6 + 8)  **Speed** 20 ft., swim 30 ft.",
            "**STR** 12  **DEX** 14  **CON** 14  **INT** 6  **WIS** 12  **CHA** 8",
            "**Skills** Stealth +4, Perception +3",
            "**Vulnerable** lightning  **Resist** fire",
            "**Senses** darkvision 60 ft., passive Perception 13",
            "**Languages** understands Aquan but can't speak",
            "**Challenge** 1/2 (100 XP)",
        ],
        "traits": [
            ("Amphibious", "The Mudskip can breathe air and water."),
            ("Mud Dweller", "It ignores difficult terrain made of mud or shallow water."),
            ("Slippery", "Advantage on checks and saves to escape a grapple."),
        ],
        "actions": [
            ("Multiattack", "One Mud Spit and one Tail Slap."),
            ("Mud Spit", "*Ranged Weapon Attack:* +4 to hit, range 30 ft. *Hit:* 5 (1d6 + 2) bludgeoning, and "
             "on a failed DC 12 Dexterity save the target's speed drops by 10 ft. until end of its next turn."),
            ("Tail Slap", "*Melee Weapon Attack:* +4 to hit, reach 5 ft. *Hit:* 6 (1d8 + 2) bludgeoning."),
            ("Mud Splash (Recharge 5-6)", "A 15-ft. cone of mud. DC 12 Dexterity save; 9 (2d6 + 2) bludgeoning "
             "and blinded until end of next turn on a fail, half and no blind on a success."),
        ],
    }]),

    ("body", "**The Grimfang war band.** *A rival goblin clan carrying an old grudge against Stabby's "
             "Bloodfang: two goblin archers, a worg, a club-swinging orc, a hobgoblin sniper, and a "
             "scar-faced Goblin Boss who taunted Stabby and regretted it. Driven off, not destroyed; "
             "grudges keep. Their statistics are the standard Monster Manual entries.*"),
    ("enemy_cards", [{
        "name": "Goblin Boss (the Grimfang leader)",
        "sub": "Small humanoid (goblinoid), neutral evil ✦ CR 1 (200 XP) ✦ leads the war band",
        "img": "assets/monsters/grimfang_warband.png", "img_w": 3.2,
        "stats": [
            "**AC** 17 (chain shirt, shield)  **HP** 21 (6d6)  **Speed** 30 ft.",
            "**STR** 10  **DEX** 14  **CON** 10  **INT** 10  **WIS** 8  **CHA** 10",
            "**Skills** Stealth +6",
            "**Senses** darkvision 60 ft., passive Perception 9",
            "**Languages** Common, Goblin",
            "**Challenge** 1 (200 XP)",
        ],
        "traits": [
            ("Nimble Escape", "The boss can Disengage or Hide as a bonus action on each of its turns."),
        ],
        "actions": [
            ("Multiattack", "Two attacks with its scimitar (the second only if the first hits)."),
            ("Scimitar", "*Melee Weapon Attack:* +4 to hit, reach 5 ft., one target. *Hit:* 5 (1d6 + 2) slashing."),
            ("Javelin", "*Melee or Ranged Weapon Attack:* +4 to hit, reach 5 ft. or range 30/120 ft. *Hit:* "
             "5 (1d6 + 2) piercing."),
        ],
        "reactions": [
            ("Redirect Attack", "When a creature the boss can see targets it with an attack, it swaps places "
             "with a goblin ally within 5 ft.; that ally becomes the target instead."),
        ],
    }]),
    ("body", "*The band also fielded standard **Goblins** (AC 15, HP 7), a **Worg** (AC 13, HP 26), an "
             "**Orc** (AC 13, HP 15), and a **Hobgoblin** sniper (AC 18, HP 11).*"),
    ("lore", "The Thorn Clans",
     "Goblins tell it plainly: when the world was woven, some threads stuck out, quick and "
     "bright and impossible to trim flat. Those threads became goblins. The briar-maze of "
     "Bloodthorn Hollow grew up around the clans, they say, because even the thorns wanted "
     "to keep them, and a grudge between two clans can outlast the briar itself."),

    ("body", "*The serpent of living stone itself: patient as a mountain, and about as easy to "
             "push over.*"),
    ("enemy_cards", [{
        "name": "Terranox",
        "sub": "Large elemental (Plane of Earth), unaligned ✦ CR 4 (1,100 XP) ✦ the boss of Session 2",
        "img": "assets/monsters/terranox.png", "img_w": 3.0,
        "stats": [
            "**AC** 16 (natural armor)  **HP** 95 (10d10 + 40)  **Speed** 30 ft., burrow 30 ft.",
            "**STR** 20  **DEX** 10  **CON** 18  **INT** 5  **WIS** 11  **CHA** 6",
            "**Resist** bludgeoning, piercing, and slashing from nonmagical, non-adamantine weapons",
            "**Imm.** fire, poison ✦ (cond) exhaustion, paralyzed, petrified, poisoned, prone",
            "**Senses** darkvision 60 ft., tremorsense 60 ft., passive Perception 10",
            "**Challenge** 4 (1,100 XP)",
        ],
        "traits": [
            ("Earth Glide", "Terranox burrows through unworked earth and stone without disturbing it."),
            ("Siege Monster", "Deals double damage to objects and structures."),
            ("Elemental Resilience", "Advantage on saves against spells and magical effects."),
            ("Immutable Form", "Immune to any effect that would alter its form."),
        ],
        "actions": [
            ("Multiattack", "One Bite and one Tail Slam."),
            ("Bite", "*Melee Weapon Attack:* +7 to hit, reach 10 ft., one target. *Hit:* 16 (2d10 + 5) piercing."),
            ("Tail Slam", "*Melee Weapon Attack:* +7 to hit, reach 15 ft., one target. *Hit:* 13 (2d8 + 5) "
             "bludgeoning, and the target must succeed on a DC 15 Strength save or be knocked prone."),
            ("Stone Coil (Recharge 5-6)", "One creature within 10 ft. makes a DC 15 Dexterity save or is grappled "
             "and restrained (escape DC 15), taking 9 (1d8 + 5) bludgeoning at the start of each of its turns."),
            ("Earthquake Stomp (Recharge 6)", "A tremor in a 20-ft. radius; each creature on the ground makes a "
             "DC 15 Dexterity save, taking 14 (4d6) bludgeoning and knocked prone on a fail (half, no prone, on a success)."),
        ],
    }]),
    ("lore", "The Stone Rings",
     "The standing stones scattered across the vales are older than every road. Each ring "
     "was raised where a plane leans close to the world, and each was given a guardian, "
     "feathered, finned, or worse, to keep the leaning from becoming a fall. When the "
     "Darkening thinned the walls, some of those old guardians woke confused and swinging."),

    # ==================================================================
    ("h1", "Session 3: The Road South", {"hardbreak": True}),
    ("gold", "South toward the sea, the party crossed shadowed thickets and glowing fungal groves, "
             "and learned that the planar wounds are teaching old monsters new tricks."),

    ("body", "*A hollow shape of darkness crowned in cold blue flame, hiding among perfect copies "
             "of itself.*"),
    ("enemy_cards", [{
        "name": "Shadowflame",
        "sub": "Medium undead, chaotic evil ✦ CR 4 (1,100 XP) ✦ fights alone",
        "img": "assets/monsters/shadowflame.png", "img_w": 3.0,
        "stats": [
            "**AC** 14 (natural armor)  **HP** 58 (9d8 + 18)  **Speed** 0 ft., fly 40 ft. (hover)",
            "**STR** 8  **DEX** 18  **CON** 14  **INT** 12  **WIS** 15  **CHA** 18",
            "**Skills** Stealth +8, Intimidation +6",
            "**Resist** acid, fire, lightning, necrotic; bludgeoning, piercing, and slashing from "
            "nonmagical weapons",
            "**Imm.** poison, psychic ✦ (cond) charmed, frightened, grappled, paralyzed, poisoned, "
            "prone, restrained",
            "**Senses** darkvision 60 ft., passive Perception 12",
            "**Languages** understands Common, Sylvan, and Abyssal (does not speak)",
            "**Challenge** 4 (1,100 XP)",
        ],
        "traits": [
            ("Illusions of Fear", "At the start of combat, the Shadowflame conjures three identical illusions "
             "(AC 14). A creature attacking one must succeed on a DC 18 Arcana or Perception check to know it is "
             "false; on a failure the attack misses and the illusion remains."),
        ],
        "actions": [
            ("Shadow Claw", "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 13 (2d8 + 4) "
             "necrotic, and the target must succeed on a DC 14 Wisdom save or be frightened until end of next turn."),
            ("Terror Wave (Recharge 5-6)", "A 15-ft. cone of dark energy. Each creature makes a DC 14 Wisdom save, "
             "taking 16 (3d10) necrotic and frightened for 1 minute on a fail (repeat save at end of each turn)."),
        ],
        "reactions": [
            ("Shadowmeld", "When hit, the Shadowflame teleports up to 20 ft. to an unoccupied space it can see, "
             "becoming lightly obscured until the start of its next turn."),
        ],
    }]),

    ("body", "**Displacer Beasts (a pair).** *Six-legged, tentacled, and impossibly TALKING ('Fresh prey... "
             "too easy.'): the planar distortion had given old monsters new voices. Their shimmering forms "
             "impose disadvantage on attacks against them until they take damage; their barbed tentacles "
             "strike at 10 ft. Their fall revealed rune-tears in the forest floor. (Statistics as the "
             "standard Displacer Beast, CR 3, AC 13, HP 85.)*"),

    ("body", "*A guardian of the glowing fungal groves, all soft lantern-light and stubborn "
             "spores.*"),
    ("enemy_cards", [{
        "name": "Shroomyte",
        "sub": "Small plant, neutral ✦ CR 2 (450 XP) ✦ they defend the grove in fours",
        "img": "assets/monsters/shroomyte_grove.png", "img_w": 3.0,
        "stats": [
            "**AC** 13 (natural armor)  **HP** 27 (5d8 + 5)  **Speed** 20 ft.",
            "**STR** 12  **DEX** 12  **CON** 14  **INT** 6  **WIS** 12  **CHA** 7",
            "**Saves** Con +4, Wis +3  **Skills** Stealth +3, Perception +3",
            "**Resist** poison  **Imm.** (cond) poisoned",
            "**Senses** darkvision 60 ft., passive Perception 13",
            "**Languages** understands Sylvan but can't speak",
            "**Challenge** 2 (450 XP)",
        ],
        "traits": [
            ("Bioluminescent Glow", "The Shroomyte sheds dim light in a 10-ft. radius, which it can suppress or "
             "rekindle as a bonus action."),
            ("Fungal Resilience", "Advantage on saves against being charmed, frightened, or stunned."),
        ],
        "actions": [
            ("Multiattack", "One Spore Blast and one Mycelium Tendrils."),
            ("Spore Blast", "*Ranged Spell Attack:* +4 to hit, range 30 ft. *Hit:* 9 (2d6 + 2) poison, and the "
             "target must succeed on a DC 13 Constitution save or be poisoned until end of its next turn."),
            ("Mycelium Tendrils", "*Melee Weapon Attack:* +4 to hit, reach 10 ft. *Hit:* 7 (2d4 + 2) bludgeoning, "
             "and a DC 13 Strength save or restrained until end of its next turn."),
        ],
        "reactions": [
            ("Fungal Retribution", "When a creature within 5 ft. hits it in melee, the Shroomyte bursts spores; "
             "the attacker makes a DC 13 Constitution save or takes 5 (2d4) poison."),
        ],
    }]),
    ("lore", "The Glowing Groves",
     "South of the vale the forest thins and the light begins to come up out of the ground "
     "instead of down through the leaves. Whole hillsides of luminous fungus keep a slow green "
     "daylight there, and the Shroomytes tend it the way shepherds tend a flock, kindling and "
     "hooding their own glow to signal one another across the dark. Travelers of the Long Peace "
     "learned the grove's single rule quickly: the light is not yours to carry off, only to walk "
     "by, and a grove left unspoiled will light you the whole way to the coast. Trample it, the "
     "old warning ends, and the spores remember longer than you will."),

    # ==================================================================
    ("h1", "Session 4: The Longest Night of Havenmoor", {"hardbreak": True}),
    ("gold", "A whole winter court had risen with the Krampusshade. These are the dangers that stalked "
             "the frozen roads of Havenmoor, and the fiend that ruled them."),

    ("body", "*The fiend of the longest night itself: horned, chain-draped, and smiling, striding "
             "the snows with a sack of cursed gifts over one shoulder.*"),
    ("enemy_cards", [{
        "name": "The Krampusshade",
        "sub": "Large fiend, chaotic evil ✦ CR 5 (1,800 XP) ✦ the boss of Session 4",
        "img": "assets/monsters/krampusshade.png", "img_w": 3.2,
        "stats": [
            "**AC** 15 (natural armor)  **HP** 102 (12d10 + 36)  **Speed** 40 ft.",
            "**STR** 18  **DEX** 14  **CON** 16  **INT** 12  **WIS** 14  **CHA** 17",
            "**Saves** Wis +5, Cha +6",
            "**Resist** cold, necrotic; bludgeoning, piercing, and slashing from nonmagical attacks",
            "**Imm.** poison ✦ (cond) charmed, frightened, poisoned",
            "**Senses** darkvision 120 ft., passive Perception 14",
            "**Languages** Abyssal, Common, Infernal",
            "**Challenge** 5 (1,800 XP)",
        ],
        "actions": [
            ("Multiattack", "One Claw and one Chains of Despair."),
            ("Claw", "*Melee Weapon Attack:* +7 to hit, reach 10 ft., one target. *Hit:* 12 (2d6 + 4) slashing "
             "plus 5 (1d10) cold."),
            ("Chains of Despair", "*Melee Weapon Attack:* +7 to hit, reach 15 ft., one target. *Hit:* 11 (2d6 + 4) "
             "bludgeoning, and a DC 14 Strength save or restrained until end of its next turn."),
            ("Gift of Despair (Recharge 5-6)", "It hurls a cursed gift box at a target within 30 ft.; DC 14 Wisdom "
             "save or frightened for 1 minute (repeat save at end of each turn)."),
        ],
        "reactions": [
            ("Icy Retaliation", "When hit by a melee attack, the attacker makes a DC 14 Constitution save or takes "
             "7 (2d6) cold and has its speed reduced by 10 ft. until end of its next turn."),
        ],
        "legendary": [
            ("Shadow Step", "The Krampusshade teleports up to 20 ft. to an unoccupied space in dim light or "
             "darkness. (Rung together, the eight Winter Bells strip away its power.)"),
        ],
    }]),

    ("body", "*A red-eyed sliver of shadow that giggles in the dark between the lantern posts.*"),
    ("body", "*Sneak-thieves of the winter court: shadowy imps with glowing red eyes and jagged claws, "
             "leaping from cover to steal whatever shone brightest in a hero's pack.*"),
    ("body", "*And the gift-box mimics were the season's cruelest joke: presents that bit back, and stuck "
             "fast to any hand that reached for them.*"),
    ("enemy_cards", [
        {
            "name": "Krampus's Imp",
            "sub": "Small fiend (shadow), chaotic evil ✦ CR 2 (450 XP)",
            "img": "assets/monsters/krampus_imp.png",
            "stats": [
                "**AC** 14 (natural armor)  **HP** 22 (5d6 + 5)",
                "**Speed** 30 ft., fly 40 ft.",
                "**STR** 10  **DEX** 16  **CON** 12  **INT** 13  **WIS** 11  **CHA** 14",
                "**Skills** Stealth +6, Deception +4",
                "**Resist** cold, fire, necrotic; nonmagical B/P/S",
                "**Imm.** poison ✦ (cond) poisoned",
                "**Senses** darkvision 120 ft.",
                "**Languages** Infernal, Common",
                "**Challenge** 2 (450 XP)",
            ],
            "traits": [
                ("Shadow Stealth", "Can Hide as a bonus action in dim light or darkness."),
                ("Invisibility (3/short rest)", "Turns invisible as a bonus action until it attacks or casts a spell."),
                ("Magic Resistance", "Advantage on saves against spells and magical effects."),
                ("Shadow Glide", "Can move through creatures' spaces in dim light or darkness."),
            ],
            "actions": [
                ("Shadow Claws", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 8 (2d4 + 3) slashing "
                 "plus 3 (1d6) cold."),
                ("Shadowy Grasp (Recharge 5-6)", "A target makes a DC 13 Dexterity save or is restrained until "
                 "end of the imp's next turn, taking 5 (1d10) cold at the start of each of its turns while "
                 "restrained."),
            ],
        },
        {
            "name": "Krampusshade Minion",
            "sub": "Small fiend, chaotic evil ✦ CR 2 (450 XP)",
            "img": "assets/monsters/krampusshade_imps.png",
            "stats": [
                "**AC** 15 (natural armor)  **HP** 33 (6d6 + 12)",
                "**Speed** 40 ft., fly 30 ft.",
                "**Skills** Stealth +6, Sleight of Hand +6",
                "**Resist** cold, necrotic; nonmagical B/P/S",
                "**Senses** darkvision 120 ft., passive Perception 12",
                "**Languages** Common, Infernal",
                "**Challenge** 2 (450 XP)",
            ],
            "actions": [
                ("Shadow Claw", "*Melee Weapon Attack:* +6 to hit, reach 5 ft., one target. *Hit:* 9 (2d4 + 4) "
                 "slashing, and the target must succeed on a DC 13 Wisdom save or be frightened until the end "
                 "of its next turn."),
                ("Steal Object", "The minion tries to snatch a small item; the target must succeed on a DC 14 "
                 "Dexterity save or lose the item."),
            ],
        },
        {
            "name": "Mimic (Gift Box)",
            "sub": "Medium monstrosity (shapechanger), neutral ✦ CR 2 (450 XP)",
            "img": "assets/monsters/gift_mimic.png", "img_w": 2.2,
            "stats": [
                "**AC** 12 (natural armor)  **HP** 58 (9d8 + 18)",
                "**Speed** 15 ft.",
                "**Skills** Stealth +5",
                "**Imm.** acid ✦ (cond) prone",
                "**Senses** darkvision 60 ft., passive Perception 11",
                "**Languages** none",
                "**Challenge** 2 (450 XP)",
            ],
            "traits": [
                ("Shapechanger", "The mimic can use its action to polymorph into an object (a wrapped gift box, "
                 "most often) or back into its true, toothy form."),
            ],
            "actions": [
                ("Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft., one target. *Hit:* 7 (1d8 + 3) piercing "
                 "plus 4 (1d8) acid."),
                ("Adhesive", "The mimic adheres to anything that touches it; a creature grappled by the mimic "
                 "must succeed on a DC 13 Strength check to escape."),
            ],
        },
    ]),

    ("body", "*Winter-touched wolves with frost-blue eyes, running the drifts in hungry packs.*"),
    ("body", "*A wicked little wisp of a fey, all giggles and ice needles.*"),
    ("body", "*And a mournful spirit of the deep cold that drifts through walls and wails away "
             "courage.*"),
    ("enemy_cards", [
        {
            "name": "Frozen Wolf",
            "sub": "Medium beast, neutral evil ✦ pack hunters",
            "img": "assets/monsters/frozen_wolf.png",
            "stats": [
                "**AC** 15 (natural armor)  **HP** 45 (6d10 + 12)",
                "**Speed** 40 ft.",
                "**STR** 16  **DEX** 15  **CON** 14  **INT** 3  **WIS** 12  **CHA** 6",
                "**Imm.** cold",
                "**Senses** darkvision 60 ft., passive Perception 14",
                "**Languages** understands Sylvan but cannot speak",
            ],
            "traits": [
                ("Pack Tactics", "Advantage on attacks against a creature if an ally is within 5 ft. of it and "
                 "not incapacitated."),
                ("Icy Terrain", "The ground within 10 ft. of the wolf is difficult terrain for other creatures."),
            ],
            "actions": [
                ("Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 12 (2d6 + 3) piercing plus "
                 "4 (1d8) cold, and a DC 13 Constitution save or speed reduced by 10 ft. until end of its "
                 "next turn."),
                ("Frost Breath (Recharge 5-6)", "A 15-ft. cone of icy air. Each creature makes a DC 13 Dexterity "
                 "save, taking 18 (4d8) cold on a fail (half on a success); those who fail are slowed until "
                 "end of next turn."),
            ],
        },
        {
            "name": "Frostbite Pixie",
            "sub": "Tiny fey, chaotic neutral ✦ CR 1/4 (50 XP)",
            "img": "assets/monsters/frostbite_pixie.png",
            "stats": [
                "**AC** 15  **HP** 14 (4d4 + 4)",
                "**Speed** 20 ft., fly 60 ft.",
                "**STR** 3  **DEX** 20  **CON** 12  **INT** 14  **WIS** 11  **CHA** 16",
                "**Skills** Stealth +7",
                "**Imm.** cold",
                "**Languages** Sylvan, Common",
                "**Challenge** 1/4 (50 XP)",
            ],
            "actions": [
                ("Ray of Frost", "*Ranged Spell Attack:* +5 to hit, range 60 ft. *Hit:* 7 (2d8) cold, and the "
                 "target's speed is reduced by 10 ft. until end of its next turn."),
                ("Invisibility", "The pixie turns invisible until it attacks or casts a spell."),
            ],
        },
        {
            "name": "Icy Specter",
            "sub": "Medium undead, neutral evil ✦ drifts through walls",
            "img": "assets/monsters/icy_specter.png",
            "stats": [
                "**AC** 12  **HP** 45 (10d8)",
                "**Speed** 0 ft., fly 50 ft. (hover)",
                "**STR** 1  **DEX** 14  **CON** 11  **INT** 10  **WIS** 10  **CHA** 16",
                "**Resist** cold, necrotic; nonmagical B/P/S",
                "**Imm.** poison ✦ (cond) charmed, exhaustion, grappled, paralyzed, poisoned, "
                "prone, restrained",
            ],
            "actions": [
                ("Chilling Touch", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 10 (3d6) cold."),
                ("Wail of Despair (Recharge 5-6)", "Each creature within 30 ft. makes a DC 14 Wisdom save or is "
                 "frightened for 1 minute (repeat save at end of each turn)."),
            ],
        },
    ]),

    ("body", "*The great black cat of midwinter tales, silent on the snow and quick to pounce; and "
             "she who waits by the roadside with warm pastries and a warmer smile, neither of which "
             "is what it seems.*"),
    ("enemy_cards", [
        {
            "name": "Yule Cat",
            "sub": "Large fey beast, neutral ✦ CR 3 (700 XP) ✦ prowls alone",
            "img": "assets/monsters/yule_cat.png", "img_w": 2.75,
            "stats": [
                "**AC** 15 (natural armor)  **HP** 52 (7d10 + 14)",
                "**Speed** 40 ft., climb 30 ft.",
                "**STR** 18  **DEX** 16  **CON** 14  **INT** 6  **WIS** 14  **CHA** 10",
                "**Skills** Perception +4, Stealth +6  **Resist** cold",
                "**Senses** darkvision 60 ft., passive Perception 14",
                "**Challenge** 3 (700 XP)",
            ],
            "actions": [
                ("Frost Claw", "*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 10 (2d6 + 3) slashing "
                 "plus 3 (1d6) cold."),
                ("Frostbite Pounce", "If the Yule Cat moves 20 ft. and hits with Frost Claw, the target makes "
                 "a DC 14 Strength save or is knocked prone; if prone, the cat makes another Frost Claw as a "
                 "bonus action."),
                ("Chilling Gaze (Recharge 5-6)", "One target within 30 ft. makes a DC 14 Constitution save or "
                 "takes 9 (2d8) cold and is paralyzed until end of its next turn."),
            ],
        },
        {
            "name": "Frost Hag (disguised)",
            "sub": "Medium fey, neutral evil ✦ CR 4 (1,100 XP) ✦ alone at her cauldron",
            "img": "assets/monsters/frost_hag_disguised.png", "img_w": 2.75,
            "stats": [
                "**AC** 15  **HP** 52",
                "**Speed** 30 ft.",
                "**STR** 14  **DEX** 14  **CON** 14  **INT** 13  **WIS** 12  **CHA** 14",
                "**Challenge** 4 (1,100 XP)",
            ],
            "traits": [
                ("Kindly Guise", "The hag appears as a sweet old woman offering sugared pastries; those who eat "
                 "them make a DC 13 Constitution save or are poisoned for 1 hour, taking 1d4 cold."),
            ],
            "actions": [
                ("Icy Claw", "*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 10 (2d6 + 3) slashing plus "
                 "4 (1d6) cold."),
                ("Frostbite Breath (Recharge 5-6)", "A 15-ft. cone; DC 14 Constitution save, 16 (4d6) cold "
                 "(half on a success); on a fail the target is slowed until its next turn."),
                ("Misty Step (Bonus Action)", "The hag teleports 30 ft."),
            ],
        },
    ], {"pack": True}),

    ("body", "*Walking snowdrifts with hearts of blue ice; top-hatted snowmen gone slightly wrong; "
             "crystal-bodied spiders whose webs glitter like spun frost; and cold lights that bob "
             "invitingly over the snow, luring travelers off the safe path.*"),
    ("enemy_cards", [
        {
            "name": "Enchanted Snowman",
            "sub": "Small construct, unaligned ✦ CR 1 (200 XP)",
            "img": "assets/monsters/enchanted_snowman.png",
            "stats": [
                "**AC** 13  **HP** 30 (4d8 + 12)",
                "**Speed** 20 ft.",
                "**STR** 12  **DEX** 10  **CON** 16  **INT** 3  **WIS** 10  **CHA** 6",
                "**Challenge** 1 (200 XP)",
            ],
            "actions": [
                ("Frostball", "*Ranged Weapon Attack:* +4 to hit. *Hit:* 2d4 cold, and a DC 12 Constitution "
                 "save or speed halved until end of its next turn."),
            ],
        },
        {
            "name": "Ice Spider",
            "sub": "Medium beast, unaligned ✦ CR 1 (200 XP)",
            "img": "assets/monsters/ice_spider.png",
            "stats": [
                "**AC** 14 (natural armor)  **HP** 26 (4d10 + 4)",
                "**Speed** 30 ft., climb 30 ft.",
                "**STR** 12  **DEX** 14  **CON** 12  **INT** 2  **WIS** 11  **CHA** 4",
                "**Challenge** 1 (200 XP)",
            ],
            "actions": [
                ("Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 9 (1d8 + 1) piercing plus "
                 "4 (1d6) cold, and a DC 13 Constitution save or poisoned for 1 minute."),
                ("Web (Recharge 5-6)", "*Ranged Weapon Attack:* +4 to hit, range 30 ft. On a hit the target "
                 "is restrained by webbing (DC 13 Strength to escape)."),
            ],
        },
        {
            "name": "Frozen Will-o'-Wisp",
            "sub": "Tiny undead, chaotic evil ✦ CR 2 (450 XP)",
            "img": "assets/monsters/frozen_will_o_wisps.png",
            "stats": [
                "**AC** 15  **HP** 22 (5d8)",
                "**Speed** 0 ft., fly 50 ft. (hover)",
                "**STR** 1  **DEX** 18  **CON** 10  **INT** 10  **WIS** 12  **CHA** 11",
                "**Resist** cold, lightning; nonmagical B/P/S",
                "**Imm.** poison ✦ (cond) exhaustion, grappled, paralyzed, prone",
                "**Challenge** 2 (450 XP)",
            ],
            "actions": [
                ("Icy Shock", "*Melee Spell Attack:* +5 to hit, reach 5 ft. *Hit:* 9 (2d8) lightning plus "
                 "4 (1d6) cold."),
                ("Invisibility", "The wisp turns invisible until it attacks."),
            ],
        },
    ], {"pack": True}),

    # The gentle-ones note sits between rows on purpose: it fills the page
    # foot under the snowman trio so the bandit row's page opens clean.
    ("body", "*Kinder meetings walked the same roads: a resting reindeer whose glowing nose blessed kind "
             "travelers, a friendly caribou that healed the weary, and Aurora Spirits, gentle messengers of "
             "Elaria who traded a prophecy for a moment's respect. None of these gentle ones has statistics; "
             "they were never for fighting.*"),
    ("body", "*Not villains so much as frozen, starving folk; a warm meal has ended more of these "
             "fights than any sword. The frost golems that rise beside them argue less.*"),
    ("enemy_cards", [
        {
            "name": "Snowbound Bandit Leader",
            "sub": "Medium humanoid, neutral ✦ leads a desperate band",
            "img": "assets/monsters/snowbound_bandits.png",
            "stats": [
                "**AC** 14  **HP** 32",
                "**Speed** 30 ft.",
                "**STR** 14  **DEX** 13  **CON** 12  **INT** 10  **WIS** 11  **CHA** 11",
            ],
            "traits": [
                ("Desperate, Not Cruel", "Driven mad by the cold; kindness (food, warmth) or a DC 14 "
                 "Intimidation check can end the fight before it begins."),
            ],
            "actions": [
                ("Scimitar", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 7 (1d6 + 3) slashing."),
                ("Dagger", "*Melee or Ranged Weapon Attack:* +5 to hit. *Hit:* 5 (1d4 + 3) piercing."),
                ("Frostbite Strike (Recharge 5-6)", "+5 to hit; an extra 1d6 cold, and a DC 13 Constitution "
                 "save or speed reduced by 10 ft. until its next turn."),
            ],
        },
        {
            "name": "Snowbound Bandit",
            "sub": "Medium humanoid, neutral ✦ the rank and file",
            "img": "assets/monsters/snowbound_bandit.png", "img_w": 2.2,
            "stats": [
                "**AC** 12  **HP** 20",
                "**Speed** 30 ft.",
            ],
            "traits": [
                ("Desperate, Not Cruel", "Like their leader, the bandits fight out of hunger and cold; "
                 "kindness can end the fight before it begins."),
            ],
            "actions": [
                ("Scimitar", "*Melee Weapon Attack:* +4 to hit, reach 5 ft. *Hit:* 5 (1d6 + 2) slashing."),
                ("Shortbow", "*Ranged Weapon Attack:* +4 to hit. *Hit:* 5 (1d6 + 2) piercing."),
            ],
        },
        {
            "name": "Frost Golem",
            "sub": "Medium elemental, neutral ✦ CR 2 (450 XP)",
            "img": "assets/monsters/frost_golems.png",
            "stats": [
                "**AC** 14 (natural armor)  **HP** 42 (5d10 + 15)",
                "**Speed** 20 ft.",
                "**STR** 16  **DEX** 10  **CON** 16  **INT** 6  **WIS** 10  **CHA** 5",
                "**Resist** cold; nonmagical B/P/S",
                "**Imm.** (cond) exhaustion, poisoned",
                "**Challenge** 2 (450 XP)",
            ],
            "traits": [
                ("Frost Aura", "At the start of each creature's turn within 5 ft. of the golem, that creature "
                 "takes 2 cold."),
            ],
            "actions": [
                ("Icy Slam", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 7 (2d6 + 3) bludgeoning "
                 "plus 3 (1d4) cold."),
            ],
        },
    ]),
    ("lore", "The Longest Night",
     "The Circle marks one night a year when the dark leans hardest on the world, and teaches "
     "that it is not to be feared but outlasted. Kindle a light, share a warm meal, ring a "
     "true bell, and keep one another company until dawn, the old rule runs, for the longest "
     "night has never once failed to end, and the things that walk it are hungriest for the "
     "lonely."),

    # ==================================================================
    ("h1", "Session 5: The Flying Dutchman", {"hardbreak": True}),
    ("gold", "Aboard the ghost-ship of Davy Jones the party fought a drowned crew of smugglers and "
             "spirits, all of them (like the Captain) undone by cold and by the sea taking back its own."),

    ("body", "*The Captain himself: barnacle-armored, tentacle-bearded, master of the Dutchman "
             "and keeper of the souls that serve aboard her.*"),
    ("enemy_cards", [{
        "name": "Davy Jones, Captain of the Flying Dutchman",
        "sub": "Medium undead (formerly humanoid), chaotic evil ✦ CR 6 (2,300 XP) ✦ the boss of Session 5",
        "img": "assets/npcs/davy_jones.png", "img_w": 3.1,
        "stats": [
            "**AC** 17 (barnacle armor)  **HP** 85 (10d10 + 30)  **Speed** 30 ft., swim 30 ft.",
            "**STR** 18  **DEX** 12  **CON** 16  **INT** 14  **WIS** 12  **CHA** 16",
            "**Saves** Con +6, Wis +4, Cha +6",
            "**Skills** Intimidation +6, Perception +4, Athletics +7, Survival +4",
            "**Resist** bludgeoning, piercing, and slashing from nonmagical attacks",
            "**Imm.** (cond) charmed, frightened, poisoned, exhaustion",
            "**Senses** darkvision 60 ft., passive Perception 14",
            "**Languages** Common, Aquan",
            "**Challenge** 6 (2,300 XP)",
        ],
        "traits": [
            ("Barnacle Armor", "Nonmagical melee attacks against him deal half damage."),
            ("Legendary Resistance (3/Day)", "If Davy fails a save, he can choose to succeed instead."),
            ("Amphibious", "He can breathe air and water."),
        ],
        "actions": [
            ("Multiattack", "Two Tentacle Slams and one Hook Strike."),
            ("Tentacle Slam", "*Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 10 (2d6 + 4) bludgeoning, and "
             "the target is grappled (escape DC 15)."),
            ("Hook Strike", "*Melee Weapon Attack:* +7 to hit, reach 5 ft. *Hit:* 8 (1d6 + 4) piercing plus 7 (2d6) necrotic."),
            ("Soul Siphon (Recharge 5-6)", "One creature makes a DC 14 Constitution save or takes 18 (4d8) psychic; "
             "Davy heals half the damage dealt."),
        ],
        "legendary": [
            ("Tentacle Strike", "Davy makes one Tentacle Slam."),
            ("Raise Tide (2 actions)", "A 20-ft. line; DC 14 Dexterity save or 13 (3d8) bludgeoning."),
        ],
    }]),

    ("body", "*The rank and file of the drowned crew, still following orders long past their "
             "last breath; and a ghost still at its post at the wheel, pale scimitars of force in "
             "both hands.*"),
    ("enemy_cards", [
        {
            "name": "Drowned Pirate",
            "sub": "Medium undead, chaotic evil ✦ CR 1 (200 XP) ✦ the deck crew",
            "img": "assets/monsters/drowned_pirate.png",
            "stats": [
                "**AC** 14 (studded leather or chain shirt)  **HP** 58 (9d8 + 18)",
                "**Speed** 30 ft., swim 30 ft.",
                "**STR** 18  **DEX** 14  **CON** 14  **INT** 6  **WIS** 10  **CHA** 7",
                "**Saves** Wis +2  **Skills** Perception +2",
                "**Resist** nonmagical B/P/S",
                "**Imm.** poison ✦ (cond) charmed, exhaustion, frightened, paralyzed, poisoned",
                "**Senses** darkvision 60 ft., passive Perception 12",
                "**Languages** understands Common but can't speak",
                "**Challenge** 1 (200 XP)",
            ],
            "traits": [
                ("Amphibious", "The pirate can breathe air and water."),
                ("Undead Fortitude", "If reduced to 0 HP (not by radiant or a crit), a DC 5 + damage "
                 "Constitution save drops it to 1 HP instead."),
            ],
            "actions": [
                ("Multiattack", "Two melee attacks."),
                ("Cutlass", "*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 8 (1d8 + 4) slashing."),
                ("Harpoon", "*Melee or Ranged Weapon Attack:* +6 to hit, reach 10 ft. or range 30/120 ft. "
                 "*Hit:* 9 (1d10 + 4) piercing, and the target is grappled (escape DC 14)."),
            ],
            "reactions": [
                ("Death Burst", "When the pirate dies it bursts; each creature within 5 ft. makes a DC 12 "
                 "Constitution save or takes 5 (2d4) cold and gains one level of exhaustion."),
            ],
        },
        {
            "name": "Spectral Helmsman",
            "sub": "Medium undead, chaotic evil ✦ CR 1 (200 XP) ✦ still at the wheel",
            "img": "assets/monsters/spectral_helmsman.png",
            "stats": [
                "**AC** 12  **HP** 45 (6d8 + 18)",
                "**Speed** 0 ft., fly 50 ft. (hover)",
                "**STR** 6  **DEX** 14  **CON** 16  **INT** 10  **WIS** 12  **CHA** 11",
                "**Saves** Wis +3, Cha +2  **Skills** Perception +3, Stealth +4",
                "**Resist** acid, fire, lightning, thunder; nonmagical B/P/S",
                "**Imm.** cold, necrotic, poison ✦ (cond) charmed, exhaustion, grappled, "
                "paralyzed, petrified, poisoned, prone, restrained",
                "**Senses** darkvision 60 ft., passive Perception 13",
                "**Languages** understands Common but can't speak",
                "**Challenge** 1 (200 XP)",
            ],
            "traits": [
                ("Incorporeal Movement", "Can move through creatures and objects as difficult terrain."),
                ("Sea-Wraith Aura", "At the start of each of its turns, creatures within 5 ft. make a DC 12 "
                 "Wisdom save or are frightened until their next turn."),
            ],
            "actions": [
                ("Multiattack", "Two Spectral Scimitar attacks."),
                ("Spectral Scimitar", "*Melee Weapon Attack:* +4 to hit, reach 5 ft. *Hit:* 7 (1d6 + 4) force."),
                ("Harpoon Throw", "*Ranged Weapon Attack:* +4 to hit, range 20/60 ft. *Hit:* 9 (1d10 + 4) "
                 "piercing and the target is pulled up to 10 ft."),
            ],
            "reactions": [
                ("Phantom Helm Block", "When attacked, it imposes disadvantage on one weapon attack roll."),
            ],
        },
    ]),

    ("body", "*Deeper in the ship waited the hold guard: a hulking crate-stacker built to guard cargo "
             "and happy to crush anything else, duelists with sorcery stitched into their sabers, and a "
             "flickering lantern-spirit of the rigging, nearly impossible to see and harder to catch.*"),
    ("enemy_cards", [
        {
            "name": "Smuggler's Golem",
            "sub": "Large construct, unaligned ✦ CR 2 (450 XP)",
            "img": "assets/monsters/smugglers_golem.png",
            "stats": [
                "**AC** 14 (natural armor)  **HP** 85 (10d10 + 30)",
                "**Speed** 30 ft.",
                "**STR** 19  **DEX** 9  **CON** 16  **INT** 3  **WIS** 10  **CHA** 5",
                "**Vulnerable** cold",
                "**Resist** fire, lightning, acid",
                "**Imm.** poison, psychic; nonmagical B/P/S ✦ (cond) charmed, exhaustion, "
                "frightened, paralyzed, petrified, poisoned, prone",
                "**Senses** darkvision 60 ft., tremorsense 30 ft., passive Perception 10",
                "**Languages** understands its creator's commands",
                "**Challenge** 2 (450 XP)",
            ],
            "traits": [
                ("Immutable Form", "Immune to effects that would alter its form."),
                ("Magic Resistance", "Advantage on saves against spells."),
                ("Siege Monster", "Deals double damage to objects."),
            ],
            "actions": [
                ("Multiattack", "Two Slam attacks."),
                ("Slam", "*Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 2d8 + 5 bludgeoning."),
                ("Crush Crate (Recharge 5-6)", "One object or creature takes 6d6 (DC 15 Dexterity save for "
                 "half); a creature that fails is knocked prone."),
            ],
            "reactions": [
                ("Reinforced Hide", "+2 AC against one melee attack."),
            ],
        },
        {
            "name": "Arcane Corsair",
            "sub": "Medium humanoid, chaotic neutral ✦ CR 1 (200 XP)",
            "img": "assets/monsters/arcane_corsair.png",
            "stats": [
                "**AC** 14 (studded leather)  **HP** 52 (7d8 + 21)",
                "**Speed** 30 ft.",
                "**STR** 16  **DEX** 16  **CON** 16  **INT** 12  **WIS** 11  **CHA** 14",
                "**Vulnerable** cold  **Saves** Dex +5, Cha +4",
                "**Skills** Acrobatics +5, Perception +2",
                "**Resist** fire, lightning",
                "**Imm.** (cond) frightened",
                "**Languages** Common, Thieves' Cant",
                "**Challenge** 1 (200 XP)",
            ],
            "traits": [
                ("Sneak Attack (1/turn)", "+2d6 damage when it has advantage or an ally is adjacent to the "
                 "target."),
                ("Parry", "+2 AC against one melee attack."),
            ],
            "actions": [
                ("Multiattack", "Two Arcane Saber attacks."),
                ("Arcane Saber", "*Melee Weapon Attack:* +5 to hit. *Hit:* 1d8 + 3 slashing plus 1d6 force."),
                ("Riposte (Recharge 5-6)", "A reaction attack after an enemy misses it in melee."),
            ],
            "reactions": [
                ("Evasive Step", "It Disengages, moving without provoking opportunity attacks."),
            ],
        },
        {
            "name": "Ghost-Light Engineer",
            "sub": "Tiny undead, neutral evil ✦ CR 2 (450 XP)",
            "img": "assets/monsters/ghost_light_engineer.png",
            "stats": [
                "**AC** 15 (natural armor)  **HP** 27 (6d4 + 12)",
                "**Speed** 0 ft., fly 50 ft. (hover)",
                "**STR** 1  **DEX** 18  **CON** 14  **INT** 12  **WIS** 14  **CHA** 16",
                "**Vulnerable** cold  **Saves** Wis +4, Cha +5",
                "**Skills** Arcana +3, Perception +4, Stealth +8",
                "**Resist** acid, fire, lightning, thunder; nonmagical B/P/S",
                "**Imm.** necrotic, poison, psychic ✦ (cond) charmed, exhaustion, frightened, "
                "grappled, paralyzed, petrified, poisoned, prone, restrained",
                "**Senses** darkvision 60 ft., passive Perception 14",
                "**Languages** Common, its creator's languages",
                "**Challenge** 2 (450 XP)",
            ],
            "traits": [
                ("Invisibility (Recharge 4-6)", "Turns invisible until it attacks, casts, or its concentration "
                 "ends."),
                ("Glowing Core", "A faint glow is visible within 5 ft. even while invisible."),
            ],
            "actions": [
                ("Shock Touch", "*Melee Spell Attack:* +6 to hit. *Hit:* 2d6 + 2 lightning."),
                ("Arcane Pulse (Recharge 5-6)", "A 10-ft. cone; DC 13 Dexterity save, 4d6 force (half on a "
                 "success)."),
            ],
            "reactions": [
                ("Engineered Reflexes", "Halves the damage from one attack or harmful spell."),
            ],
        },
    ]),

    # ==================================================================
    ("h1", "Session 6: The False Hydra of Wraithpine", {"hardbreak": True}),
    ("gold", "The worst monster the Guardians ever faced, because no one knew it was there. Beneath the "
             "Old Theater of Wraithpine, its endless song made the whole village forget the people it took. "
             "Beeswax in the ears let the truth through."),

    ("body", "*The first glimpse of the horror: a single pale head and neck rising through the "
             "tavern trapdoor, singing all the while.*"),
    ("body", "*Each head is pale, blind-eyed, and always singing, even as it bites.*"),
    ("enemy_cards", [{
        "name": "False Hydra: Tavern Head",
        "sub": "Large aberration (one head and neck), unaligned ✦ it has been in the taproom all along",
        "img": "assets/monsters/false_hydra.png", "img_w": 1.9,
        "stats": [
            "**AC** 14  **HP** 70 (9d10 + 18)  **Speed** 10 ft., climb 10 ft.",
            "**STR** 16  **DEX** 12  **CON** 14  **INT** 6  **WIS** 14  **CHA** 7",
            "**Resist** psychic  **Imm.** (cond) charmed, frightened, prone",
            "**Senses** blindsight 10 ft., tremorsense 30 ft., darkvision 60 ft., passive Perception 14",
        ],
        "traits": [
            ("Mind-Humming Aura", "Creatures without beeswax that start their turn within 30 ft. make a DC 13 "
             "Wisdom save or have disadvantage on attack rolls that turn. Beeswax grants advantage on the save."),
            ("Segmented Neck", "The head ignores forced movement and prone unless it chooses otherwise. When it "
             "takes 20+ damage in a turn, it recoils 5 ft. (no opportunity attacks) and can't take reactions "
             "until the start of its next turn."),
        ],
        "actions": [
            ("Bite", "*Melee Weapon Attack:* +6 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) piercing, and the target "
             "is grappled (escape DC 14). While grappling it can't bite a different target."),
            ("Lurch & Drag", "A grappled target is dragged 5 ft. toward the trapdoor and, on a failed DC 13 Wisdom "
             "save, loses a word or thought for a heartbeat."),
        ],
        "reactions": [
            ("Recoil from Flame", "When it takes fire damage, it has disadvantage on its next attack."),
        ],
    }, {
        "name": "False Hydra Head (x4)",
        "sub": "Large aberration (an extension of the body), unaligned ✦ four in the pit",
        "img": "assets/monsters/false_hydra_head.png", "img_w": 2.2,
        "stats": [
            "**AC** 14  **HP** 45 (6d10 + 12) each  **Speed** 30 ft. (platforms, tunnels), climb 20 ft.",
            "**STR** 16  **DEX** 12  **CON** 14  **INT** 6  **WIS** 14  **CHA** 7",
            "**Saves** Wis +4",
            "**Resist** psychic  **Imm.** (cond) charmed, frightened, prone",
        ],
        "actions": [
            ("Bite", "*Melee Weapon Attack:* +7 to hit, reach 15 ft. *Hit:* 14 (2d10 + 3) piercing and grappled "
             "(escape DC 14). While grappling it can't bite a different target."),
            ("Reel", "A creature grappled by the head makes a DC 14 Strength save or is pulled 10 ft. toward the "
             "port and knocked prone."),
        ],
        "reactions": [
            ("Snap", "When a creature moves within 15 ft., the head makes one Bite against it."),
        ],
    }]),

    ("body", "*Deeper still, in the drowned orchestra pit, waited the true body and its four heads, all "
             "singing as one. The moment the song stopped, every stolen name came flooding home.*"),
    ("enemy_cards", [{
        "name": "False Hydra (Adult): Body",
        "sub": "Huge aberration, unaligned ✦ the boss of Session 6",
        "img": "assets/monsters/false_hydra_body.png", "img_w": 3.0,
        "stats": [
            "**AC** 15  **HP** 130 (12d12 + 48)  **Speed** 10 ft., climb 10 ft.",
            "**STR** 18  **DEX** 10  **CON** 18  **INT** 7  **WIS** 14  **CHA** 8",
            "**Saves** Con +8, Wis +5",
            "**Resist** psychic  **Imm.** (cond) charmed, frightened, prone",
            "**Senses** tremorsense 60 ft., darkvision 60 ft., blindsight 10 ft., passive Perception 12",
        ],
        "traits": [
            ("Song of Unremembering", "While any head lives, creatures without earplugs that start their turn "
             "within 60 ft. make a DC 15 Wisdom save or have disadvantage on attacks and can't take reactions "
             "until their next turn. Beeswax grants advantage and no reaction-lock."),
            ("Many-Minds", "For each head alive, the body has 1 Legendary Action (max 3 per round)."),
            ("Vital Link", "While at least one head lives, the body has resistance to all weapon damage; each head "
             "destroyed removes one instance of this protection."),
        ],
        "actions": [
            ("Thrash", "*Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) bludgeoning."),
            ("Regurgitate Remnants (Recharge 5-6)", "A 15-ft. cone of bone and cloth; DC 14 Dexterity save, 13 "
             "(3d8) necrotic and slowed (speed -10) until end of next turn. A shattered skull and ribbon clatter free."),
        ],
        "legendary": [
            ("Hum Surge", "One creature within 60 ft. (no earplugs) makes a DC 15 Wisdom save or loses "
             "concentration and can move only 10 ft. on its next turn."),
            ("Bone Shift", "Move the body 5 ft. and reshape a 10-ft. square within 20 ft. into (or out of) "
             "difficult terrain."),
            ("Coordinate Strike", "One head makes a Snap."),
        ],
    }]),

    ("lore", "Where the Silence Pools",
     "In the deepest drowned places, the flooded warrens and the sunken halls, silence gathers "
     "the way cold water gathers at the bottom of a well. Something learned long ago to live in "
     "that silence and to feed on the memory of itself, so that the ones it takes are not "
     "mourned but only, quietly, forgotten. The Circle's warning for such places is the oldest "
     "kind: count your companions by name, out loud, and if the count will not come right, do "
     "not go deeper. Sing instead, for the one thing the silence has never been able to swallow "
     "is a song freely shared."),

    ("body", "**Festival frights.** *Before the theater, the hydra's hungry song had stirred lesser echoes "
             "all over Wraithpine: animated Scarecrows and rustling Strawlings on Pumpkin Row, rats and rat "
             "swarms in Maera's cellar, and restless Zombies (and, if things went loud, Skeletons) at the "
             "graveyard rite.*"),
    ("enemy_cards", [
        {
            "name": "Animated Scarecrow",
            "sub": "Medium construct, neutral ✦ CR 1 (200 XP) ✦ Pumpkin Row",
            "img": "assets/monsters/scarecrow.png",
            "stats": [
                "**AC** 11  **HP** 36 (8d8)  **Speed** 30 ft.",
                "**STR** 16  **DEX** 12  **CON** 11  **INT** 10  **WIS** 10  **CHA** 10",
                "**Vulnerable** fire",
                "**Resist** nonmagical B/P/S",
                "**Imm.** (cond) charmed, frightened, paralyzed, poisoned",
                "**Senses** darkvision 60 ft., passive Perception 10",
                "**Languages** understands its creator's languages but can't speak",
                "**Challenge** 1 (200 XP)",
            ],
            "traits": [
                ("Terrifying Glare", "One creature within 30 ft. must succeed on a DC 11 Wisdom save or be "
                 "frightened for 1 minute (repeat save at end of each turn)."),
                ("Heart-Gourd", "A coin-sized gourd charm is sewn under its ribs; snipping it (an action within "
                 "5 ft., no roll) makes the scarecrow fall limp."),
            ],
            "actions": [
                ("Claw", "*Melee Weapon Attack:* two claws, +5 to hit, reach 5 ft. *Hit:* 6 (2d4 + 1) slashing."),
            ],
        },
        {
            "name": "Strawling",
            "sub": "Medium plant, neutral ✦ CR 1/4 (50 XP) ✦ more startling than deadly",
            "img": "assets/monsters/strawling.png",
            "stats": [
                "**AC** 12  **HP** 11 (2d8 + 2)  **Speed** 30 ft.",
                "**STR** 12  **DEX** 12  **CON** 12  **INT** 4  **WIS** 10  **CHA** 3",
                "**Senses** passive Perception 10",
                "**Challenge** 1/4 (50 XP)",
            ],
            "actions": [
                ("Needles", "*Melee or Ranged Weapon Attack:* a bristle of straw-needles; easily bowled over "
                 "by a hay cart or a kicked pumpkin stack."),
            ],
        },
    ]),
    ("body", "*The cellar vermin were ordinary **Rats** (AC 12, HP 7, CR 1/8) and a **Swarm of Rats** (AC 10, "
             "HP 24, CR 1/4). The graveyard undead were standard **Zombies** (AC 8, HP 22, CR 1/4; Undead "
             "Fortitude) and, only if the rite went loud, **Skeletons** (AC 13, HP 13, CR 1/4).*"),

    # ==================================================================
    # DM-adjudicated numbering 2026-07-06: Gearhaven is Session 7; the
    # chronicle reads 1 through 7 with no gap.
    ("h1", "Session 7: Gearhaven, the Clockwork City", {"hardbreak": True}),
    ("gold", "In the clockwork city, the enemy was no monster at all but corruption bleeding up through "
             "the cracks, reaching INTO the machines the people loved. Note the rotation: the lightning "
             "eaters and the fire eaters trade off. Freed, not killed: these were innocents."),

    ("body", "*Cogtooth Market's little brass helpers gone haywire, sparks snapping from every joint; "
             "and a dockside lifter the size of a shed, swinging its forklift arms like siege weapons.*"),
    ("enemy_cards", [
        {
            "name": "Rogue Servitor",
            "sub": "Small construct, unaligned ✦ CR 2 ✦ freed, not killed",
            "img": "assets/session_07/beat_2/rogue_servitor.png",
            "stats": [
                "**AC** 15  **HP** 39 (6d6 + 18)  **Speed** 30 ft.",
                "**STR** 13  **DEX** 16  **CON** 16  **INT** 3  **WIS** 8  **CHA** 5",
                "**Resist** poison; nonmagical B/P/S",
                "**Imm.** (cond) charmed, frightened, poisoned, exhaustion",
                "**Senses** darkvision 60 ft.",
                "**Challenge** 2",
            ],
            "traits": [
                ("Overclocked Death-Spark", "At 0 HP, each creature within 10 ft. makes a DC 13 Dexterity save "
                 "or takes 7 (2d6) lightning."),
                ("Shutdown Switch", "An action within 5 ft. plus a DC 14 Arcana or Sleight of Hand check shuts "
                 "it down instantly, no kill needed."),
            ],
            "actions": [
                ("Multiattack", "Two Flailing Slams."),
                ("Flailing Slam", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 8 (1d10 + 3) bludgeoning."),
                ("Spark Lash (Recharge 5-6)", "*Ranged Attack:* +5 to hit, range 30 ft. *Hit:* 10 (3d6) "
                 "lightning; the target's speed is halved until end of its next turn."),
            ],
        },
        {
            "name": "Cargo Hauler",
            "sub": "Large construct, unaligned ✦ CR 3 ✦ the dockside lifter",
            "img": "assets/session_07/beat_2/cargo_hauler.png",
            "stats": [
                "**AC** 16  **HP** 76 (8d10 + 32)  **Speed** 30 ft.",
                "**STR** 19  **DEX** 8  **CON** 18  **INT** 3  **WIS** 8  **CHA** 5",
                "**Vulnerable** lightning (overloaded core; telegraph the crackling blue!)",
                "**Resist** nonmagical B/P/S",
                "**Imm.** (cond) charmed, exhaustion, frightened, paralyzed, petrified, poisoned",
                "**Challenge** 3",
            ],
            "traits": [
                ("Out-of-Reach Switch", "Its shutdown lever is 15 ft. up on its back; reaching it (climb DC 13 "
                 "or flight) plus an action and a DC 15 Arcana or Sleight of Hand check disables it."),
            ],
            "actions": [
                ("Multiattack", "Two Forklift Slams, or one Slam and one Hurl Crate."),
                ("Forklift Slam", "*Melee Weapon Attack:* +6 to hit, reach 10 ft. *Hit:* 13 (2d8 + 4) "
                 "bludgeoning, and a DC 14 Strength save or knocked prone."),
                ("Hurl Crate", "*Ranged Weapon Attack:* +6 to hit, range 60 ft. *Hit:* 14 (3d6 + 4) bludgeoning."),
                ("Grab & Crush (Recharge 5-6)", "One creature within 10 ft. makes a DC 14 Dexterity save or is "
                 "grappled (escape DC 14), taking 10 (3d6) at the start of each of its turns until it escapes."),
            ],
        },
    ]),

    ("body", "*Spark-yellow skitterers of the Underworks, flickering in and out of the Real; and the "
             "nest-queen of the swarm, spinning webs of living lightning.*"),
    ("enemy_cards", [
        {
            "name": "Voltcrawler",
            "sub": "Small aberration (planar intruder), unaligned ✦ the swarm",
            "img": "assets/session_07/beat_4/volt_crawler.png",
            "stats": [
                "**AC** 15  **HP** 22 (5d6 + 5)  **Speed** 30 ft., climb 30 ft.",
                "**STR** 7  **DEX** 17  **CON** 13  **INT** 5  **WIS** 10  **CHA** 6",
                "**Resist** lightning",
                "**Senses** darkvision 60 ft.",
            ],
            "traits": [
                ("Phase-Blink", "At the start of its turn, roll a d6: on a 1-2 it goes Unreal, resisting all "
                 "damage except force and radiant, and attacks against it have disadvantage; it can't be webbed "
                 "or grappled and must become Real to attack. (Force and radiant are the counter.)"),
                ("Static Cling", "The first time it hits a creature each turn, that target's lightning "
                 "resistance is ignored and its allies have advantage on their next attack against it."),
            ],
            "actions": [
                ("Spark Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 1d6 + 3 piercing plus "
                 "1d6 lightning."),
                ("Arc (Recharge 5-6)", "A 15-ft. line; DC 13 Dexterity save, 2d8 lightning (half on a success). "
                 "Two or more Voltcrawlers within 15 ft. can chain into one 3d8 line."),
            ],
        },
        {
            "name": "Voltcrawler Broodmother",
            "sub": "Medium aberration (planar intruder), unaligned ✦ the nest-queen",
            "img": "assets/session_07/beat_4/broodmother.png",
            "stats": [
                "**AC** 16  **HP** 95 (10d8 + 50)  **Speed** 40 ft., climb 40 ft.",
                "**STR** 14  **DEX** 18  **CON** 20  **INT** 6  **WIS** 12  **CHA** 8",
                "**Saves** Dex +7, Con +8",
                "**Resist** lightning; nonmagical B/P/S",
                "**Senses** darkvision 60 ft.",
            ],
            "traits": [
                ("Phase-Blink (greater)", "She chooses to go Unreal as a free action once per round (no roll)."),
                ("Crackling Web", "At the start of her turn, one creature she sees within 30 ft. makes a DC 15 "
                 "Dexterity save or is restrained by planar silk (action plus DC 15 Strength to break; web AC 12, "
                 "15 HP, immune lightning, VULNERABLE fire and cold)."),
            ],
            "actions": [
                ("Multiattack", "Two Lash attacks."),
                ("Lash", "*Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 1d10 + 4 slashing plus "
                 "1d8 lightning."),
                ("Overcharge (Recharge 6)", "A 20-ft.-radius burst; DC 15 Constitution save, 4d8 lightning "
                 "(half on a success). On a fail the target also can't take reactions until end of its next turn."),
            ],
        },
    ]),

    ("body", "*Worker-machines with corrupted vine knotted through their gears: slow, sad, and "
             "unstoppable. Around their feet, fist-sized knots of corrupted vine keep coming as long "
             "as the engine feeds them.*"),
    ("enemy_cards", [
        {
            "name": "Iron Drudge",
            "sub": "Large construct (planar-corrupted), unaligned ✦ CR 3 ✦ freed, not killed",
            "img": "assets/session_07/beat_5/iron_drudge.png",
            "stats": [
                "**AC** 17  **HP** 68 (8d10 + 24)  **Speed** 25 ft.",
                "**STR** 19  **DEX** 8  **CON** 17  **INT** 3  **WIS** 8  **CHA** 1",
                "**Vulnerable** fire (corrupted wood and vine in its joints; telegraph the smoke!)",
                "**Resist** nonmagical B/P/S",
                "**Imm.** (cond) charmed, frightened, exhaustion, poisoned",
                "**Senses** darkvision 60 ft.",
                "**Challenge** 3",
            ],
            "traits": [
                ("Slow but Unstoppable", "Can't be knocked prone; ignores difficult terrain. It is slow enough "
                 "to outrun, but it keeps coming."),
                ("Corruption Leak", "At 0 HP the blue light gutters out and it slumps, harmless. No death-burst: "
                 "these were innocent worker-machines, freed rather than destroyed."),
            ],
            "actions": [
                ("Multiattack", "Two Cargo-Arm Slams."),
                ("Cargo-Arm Slam", "*Melee Weapon Attack:* +6 to hit, reach 10 ft. *Hit:* 2d8 + 4 bludgeoning."),
                ("Sweep (Recharge 5-6)", "A wide swing; each creature within 10 ft. makes a DC 14 Dexterity "
                 "save, taking 2d6 + 4 bludgeoning (half on a success) and shoved 10 ft. on a fail."),
            ],
        },
        {
            "name": "Corrupted Sproutling",
            "sub": "Small plant (planar-corrupted), unaligned ✦ weak but many",
            "img": "assets/session_07/beat_5/corrupted_sproutling.png",
            "stats": [
                "**AC** 12  **HP** 7 (2d6)  **Speed** 10 ft., climb 10 ft.",
                "**STR** 8  **DEX** 14  **CON** 10  **INT** 2  **WIS** 6  **CHA** 4",
                "**Vulnerable** fire",
                "**Senses** darkvision 30 ft.",
            ],
            "traits": [
                ("Weak but Many", "Dies to almost any solid hit; an area effect clears several at once "
                 "(reward AoE)."),
                ("Group Turn & Spawn", "All Sproutlings act together on one shared initiative. While the engine "
                 "runs corrupt, a new one crawls from a crack each time one dies."),
            ],
            "actions": [
                ("Thorn-Lash", "*Melee Weapon Attack:* +4 to hit, reach 5 ft. *Hit:* 1d6 + 2 piercing."),
                ("Latch", "Instead of attacking, it grabs a hero (no damage); the next attack against that "
                 "hero has advantage."),
            ],
        },
    ]),

    ("body", "*And then the boss: not a monster, but the city's beloved gentle giant, possessed and "
             "grieving inside its own iron. The Guardians broke its legs to bring the core into reach, and "
             "the last blow drained the corruption away rather than killing it. A gentle death, never an execution.*"),
    ("enemy_cards", [{
        "name": "The Grand Custodian (possessed)",
        "sub": "Gargantuan construct (planar-possessed), unaligned ✦ the boss of Session 7 ✦ a two-phase fight",
        # Landscape plate (1672x941): 4.5 in. wide renders ~2.5 in. tall, the
        # same visual weight the square boss portraits get at 3.0-3.4.
        "img": "assets/session_07/beat_5/grand_custodian.png", "img_w": 4.5,
        "stats": [
            "**AC** 17 (Body); Legs (x2) AC 15  **HP** 220 (Body); Legs 90 each  **Speed** 30 ft.",
            "**STR** 24  **DEX** 6  **CON** 22  **INT** 3  **WIS** 10  **CHA** 5",
            "**Resist** bludgeoning, piercing, and slashing from nonmagical attacks",
            "**Imm.** (cond) charmed, frightened, exhaustion, poisoned, paralyzed, petrified",
        ],
        "traits": [
            ("The Core Is High", "Standing, the core is 40-50 ft. up: only 60-ft.+ ranged attacks and flyers reach "
             "it. The legs are ground-level and anyone can strike them."),
            ("Topple", "Drop both legs (90 HP each) and it crashes to its knees (Phase 2), stops rampaging, and "
             "the core drops to 15-20 ft. within everyone's reach. It may slowly repair a leg (to 25 HP) to rise; re-topple it."),
        ],
        "actions": [
            ("Crushing Stomp", "*Melee:* +8 to hit, reach 15 ft. *Hit:* 2d10 + 5 bludgeoning, and a DC 15 Dexterity "
             "save or knocked prone. (Phases 1 and 2.)"),
            ("Sweeping Backhand (Recharge 5-6)", "(Phase 1) A 15-ft. cone; DC 15 Dexterity save, 3d8 and shoved "
             "10 ft. (half and no shove on a success)."),
            ("Corrupt Bolt", "(Phase 1) +8 to hit, range 60 ft. *Hit:* 3d8 lightning, once per round at someone hanging back."),
            ("Clockwork Barrage (Recharge 4-6)", "(Phase 2) Three projectiles, +8 each. *Hit:* 2d8 + 3 bludgeoning."),
            ("Chain Lightning Burst (Recharge 5-6)", "(Phase 2) +8 to hit, 4d8 lightning, arcing to two more within "
             "15 ft. for 2d8 (DC 15 Dexterity save for half). Meant to be ANSWERED, not to drop a hero."),
            ("Core Flare", "(Phase 2, body below half HP) Each creature within 20 ft. makes a DC 15 Constitution "
             "save or takes 2d6 force and is blinded until end of its next turn."),
        ],
    }]),
    ("h1", "The Earth Rift: Underroot"),
    ("gold", "*The first plane the Guardians ever walked. A world made of ground all the way "
             "through, breathing once a minute, patient beyond patience, and bleeding from a "
             "wound somebody put there on purpose.*"),

    ("h2", 'Rotbloom'),
    ("enemy_cards", [{
        "name": 'Rotbloom',
        "sub": 'Small plant (corrupted), unaligned ✦ CR 1/2 (100 XP) ✦ Session 8',
        "img": 'assets/monsters/rotbloom.png', "img_w": 2.4,
        "stats": [
            '**AC** 12  **HP** 22 (4d6 + 8)  **Speed** 25 ft.',
            '**STR** 10  **DEX** 12  **CON** 14  **INT** 4  **WIS** 8  **CHA** 6',
            '**Resist** poison ✦ **Imm.** (cond) blinded, deafened, poisoned',
            '**Senses** blindsight 30 ft., passive Perception 9',
            '**Challenge** 1/2 (100 XP)',
        ],
        "traits": [
            ('Re-Bloom', 'At the start of its turn, if it took damage since its last turn and is not at 0 HP, it regains 5 hit points. It cannot re-bloom if it has taken radiant damage, or been hit by Cleansing Edge, since its last turn.'),
            ('Still Smiling', 'It cannot be frightened, and its face never changes, whatever is happening to it.'),
        ],
        "actions": [
            ('Cap Slam', '*Melee Weapon Attack:* +3 to hit, reach 5 ft. *Hit:* 6 (2d4 + 1) bludgeoning.'),
            ('Spore Puff (Recharge 5-6)', '10-ft cone, DC 12 Constitution save, 7 (2d6) poison and poisoned until the end of its next turn; half and no poisoning on a success.'),
        ],
    }]),

    ("h2", 'Mossmite'),
    ("enemy_cards", [{
        "name": 'Mossmite',
        "sub": 'Tiny beast (corrupted), unaligned ✦ CR 1/8 (25 XP) ✦ Session 8',
        "img": 'assets/monsters/mossmite.png', "img_w": 2.2,
        "stats": [
            '**AC** 13  **HP** 7 (2d4 + 2)  **Speed** 40 ft., climb 40 ft.',
            '**STR** 6  **DEX** 16  **CON** 12  **INT** 2  **WIS** 10  **CHA** 4',
            '**Senses** blindsight 30 ft., passive Perception 10',
            '**Challenge** 1/8 (25 XP)',
        ],
        "traits": [
            ('Skitter', 'It does not provoke opportunity attacks.'),
            ('Pack Nerve', 'Advantage on attacks against a creature if another Mossmite is within 5 ft. of it.'),
        ],
        "actions": [
            ('Nip', '*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 5 (1d4 + 3) piercing.'),
        ],
    }]),

    ("h2", 'Chimestone'),
    ("enemy_cards", [{
        "name": 'Chimestone',
        "sub": 'Medium elemental (Plane of Earth), unaligned ✦ CR 3 (700 XP) ✦ Session 8',
        "img": 'assets/monsters/chimestone.png', "img_w": 2.6,
        "stats": [
            '**AC** 16 (rock plate)  **HP** 52 (7d8 + 21)  **Speed** 25 ft.',
            '**STR** 18  **DEX** 8  **CON** 16  **INT** 5  **WIS** 12  **CHA** 6',
            '**Resist** piercing, slashing ✦ **Vulnerable** thunder',
            '**Imm.** poison ✦ (cond) charmed, exhaustion, frightened, poisoned',
            '**Senses** tremorsense 60 ft., passive Perception 11',
            '**Challenge** 3 (700 XP)',
        ],
        "traits": [
            ('Resonant Body', 'Whenever it takes thunder damage it is **stunned** until the end of its next turn, and it takes **double damage** from every source while stunned. This is how you beat them.'),
            ('Struck Chord', "A creature can use an action to strike one of the reef's spires (DC 13 Athletics). Every Chimestone within 30 ft. makes a DC 14 Constitution save or is stunned as above. The striker takes 1d6 thunder from standing that close."),
        ],
        "actions": [
            ('Multiattack', 'Two Crystal Rams.'),
            ('Crystal Ram', '*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 11 (2d6 + 4) bludgeoning.'),
            ('Shard Volley', '*Ranged Weapon Attack:* +6 to hit, range 40 ft. *Hit:* 9 (2d8) piercing.'),
        ],
    }]),

    ("h2", 'Shardwing'),
    ("enemy_cards", [{
        "name": 'Shardwing',
        "sub": 'Small elemental (Plane of Earth), unaligned ✦ CR 1 (200 XP) ✦ Session 8',
        "img": 'assets/monsters/shardwing.png', "img_w": 2.4,
        "stats": [
            '**AC** 14  **HP** 22 (5d6 + 5)  **Speed** 10 ft., fly 50 ft.',
            '**STR** 8  **DEX** 18  **CON** 12  **INT** 4  **WIS** 12  **CHA** 6',
            '**Vulnerable** thunder ✦ **Imm.** poison ✦ (cond) poisoned, prone',
            '**Senses** tremorsense 30 ft., passive Perception 11',
            '**Challenge** 1 (200 XP)',
        ],
        "traits": [
            ('Glide', 'It can fly at full speed without provoking opportunity attacks from creatures it starts its turn adjacent to.'),
        ],
        "actions": [
            ('Dive', '*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 9 (2d6 + 2) slashing, plus an extra 1d6 if it moved at least 30 ft. straight toward the target first.'),
            ('Shard Spit', '*Ranged Weapon Attack:* +6 to hit, range 60 ft. *Hit:* 7 (1d10 + 2) piercing.'),
        ],
    }]),

    ("h2", 'Cinderoll'),
    ("enemy_cards", [{
        "name": 'Cinderoll',
        "sub": 'Small elemental (corrupted), unaligned ✦ CR 1/2 (100 XP) ✦ Session 8',
        "img": 'assets/monsters/cinderoll.png', "img_w": 2.2,
        "stats": [
            '**AC** 15 (glassy coal)  **HP** 18 (4d6 + 4)  **Speed** 40 ft. (rolling)',
            '**STR** 12  **DEX** 14  **CON** 12  **INT** 3  **WIS** 8  **CHA** 3',
            '**Imm.** fire, poison ✦ (cond) blinded, charmed, deafened, poisoned',
            '**Senses** blindsight 60 ft., passive Perception 9',
            '**Challenge** 1/2 (100 XP)',
        ],
        "traits": [
            ('Rolling Charge', 'If it moves at least 20 ft. straight toward a target before hitting it, the attack deals an extra 3 (1d6) damage and the target makes a DC 12 Strength save or is knocked prone.'),
            ('Burst', 'At 0 hit points it cracks open: each creature within 10 ft. makes a DC 12 Dexterity save or takes 7 (2d6) fire. They arrive in packs, so a chain reaction is very much on the table.'),
        ],
        "actions": [
            ('Slam', '*Melee Weapon Attack:* +4 to hit, reach 5 ft. *Hit:* 7 (2d4 + 2) bludgeoning plus 3 (1d6) fire.'),
        ],
    }]),

    ("h2", 'Glassling'),
    ("enemy_cards", [{
        "name": 'Glassling',
        "sub": 'Tiny construct (spawned by the spike), unaligned ✦ CR 1/4 (50 XP) ✦ Session 8',
        "img": 'assets/monsters/glassling.png', "img_w": 2.2,
        "stats": [
            '**AC** 14  **HP** 10 (3d4 + 3)  **Speed** 30 ft., climb 30 ft.',
            '**STR** 8  **DEX** 16  **CON** 12  **INT** 1  **WIS** 6  **CHA** 1',
            '**Imm.** poison, psychic ✦ (cond) blinded, charmed, deafened, frightened, poisoned',
            '**Senses** blindsight 30 ft., passive Perception 8',
            '**Challenge** 1/4 (50 XP)',
        ],
        "traits": [
            ('Spike-Born', "The spike in Groudon's back creates one Glassling at the start of each of his turns. **When the spike is destroyed, every Glassling collapses into ordinary sand at once.**"),
            ('Shatterburst', 'At 0 hit points, each creature within 5 ft. makes a DC 12 Dexterity save or takes 5 (2d4) slashing.'),
        ],
        "actions": [
            ('Glass Bite', '*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 6 (1d6 + 3) slashing.'),
        ],
    }]),

    ("h2", 'Thumpaw'),
    ("enemy_cards", [{
        "name": 'Thumpaw',
        "sub": 'Large beast (Plane of Earth), unaligned ✦ CR 3 (700 XP) ✦ random encounters only',
        "img": 'assets/monsters/thumpaw.png', "img_w": 2.8,
        "stats": [
            '**AC** 14 (mossy hide)  **HP** 76 (8d10 + 32)  **Speed** 30 ft., burrow 30 ft.',
            '**STR** 20  **DEX** 8  **CON** 18  **INT** 3  **WIS** 12  **CHA** 6',
            '**Senses** tremorsense 60 ft., passive Perception 13',
            '**Challenge** 3 (700 XP)',
        ],
        "traits": [
            ('Not Actually Angry', 'It never pursues and it never finishes a downed creature. It is in the way, and it was there first.'),
            ('Immovable', 'Advantage on saves and checks against being moved, and it cannot be knocked prone.'),
        ],
        "actions": [
            ('Multiattack', 'Two Shovel Slams.'),
            ('Shovel Slam', '*Melee Weapon Attack:* +8 to hit, reach 10 ft. *Hit:* 14 (2d8 + 5) bludgeoning.'),
        ],
    }]),

    ("h2", 'Gleamoth Swarm'),
    ("enemy_cards", [{
        "name": 'Gleamoth Swarm',
        "sub": 'Medium swarm of tiny beasts, unaligned ✦ CR 1 (200 XP) ✦ random encounters only',
        "img": 'assets/monsters/gleamoth_swarm.png', "img_w": 3.0,
        "stats": [
            '**AC** 12  **HP** 26 (4d8 + 8)  **Speed** 5 ft., fly 40 ft. (hover)',
            '**STR** 4  **DEX** 14  **CON** 14  **INT** 1  **WIS** 10  **CHA** 4',
            '**Resist** bludgeoning, piercing, slashing ✦ **Vulnerable** fire, thunder',
            '**Imm.** (cond) charmed, frightened, grappled, prone, restrained, stunned',
            '**Senses** blindsight 20 ft., passive Perception 10',
            '**Challenge** 1 (200 XP)',
        ],
        "traits": [
            ('Drawn to Warmth', 'It always moves toward the warmest or brightest thing it can sense, which is the Essence Sphere. If Lilly is carrying it, the swarm comes for her every turn.'),
            ('Swarm', "It can occupy another creature's space and move through any opening large enough for a single moth."),
        ],
        "actions": [
            ('Smother', '*Melee Weapon Attack:* +4 to hit, reach 0 ft., one creature in its space. *Hit:* 10 (4d4) piercing, or 5 (2d4) at half hit points or fewer, and the target is **blinded** until the end of its next turn.'),
        ],
    }]),

    ("h2", "Glass Weeper"),
    ("enemy_cards", [{
        "name": "Glass Weeper",
        "sub": "Large aberration (corrupted guardian-beast), unaligned \u2726 CR 6 (2,300 XP) \u2726 Session 8",
        "img": "assets/monsters/glass_weeper.png", "img_w": 3.0,
        "stats": [
            "**AC** 16 (black glass)  **HP** 115 (11d10 + 55)  **Speed** 20 ft.",
            "**STR** 18  **DEX** 8  **CON** 20  **INT** 4  **WIS** 12  **CHA** 5",
            "**Resist** bludgeoning, piercing, slashing from nonmagical weapons",
            "**Imm.** poison \u2726 (cond) charmed, frightened, poisoned",
            "**Senses** blindsight 60 ft., passive Perception 11",
            "**Challenge** 6 (2,300 XP)",
        ],
        "traits": [
            ("Glassbound", "It regains 10 hit points at the start of its turn unless it took radiant or force "
             "damage, or was hit by Cleansing Edge, since its last turn."),
            ("Grieving", "It has disadvantage on attacks against any creature that has not damaged it since "
             "the start of its last turn. It is not hunting anyone. It is lashing out."),
            ("Tending", "If a creature spends an action helping the glassed roots (DC 14 Nature or Medicine, "
             "or any healing magic spent on the roots rather than a creature), the Weeper loses its next turn "
             "and its AC drops by 2 permanently as it calms. Three successes end the encounter without a kill."),
        ],
        "actions": [
            ("Multiattack", "Two Glass Rakes."),
            ("Glass Rake", "*Melee Weapon Attack:* +7 to hit, reach 10 ft. *Hit:* 14 (2d8 + 5) slashing."),
            ("Keening (Recharge 5-6)", "30-ft cone, DC 15 Constitution save, 21 (6d6) psychic and frightened "
             "until the end of its next turn; half and no fear on a success."),
        ],
    }]),

    ("h2", "Groudon, the Continent-Maker"),
    ("body", "**The Guardian of Underroot, and not an enemy.** Somebody drove a spike of black glass into "
             "his back where he could not reach it, and every crack in that plane spreads out from that one "
             "point. He is the reason there is dry land at all. The encounter is a rescue, and it ends the "
             "instant the spike breaks, whatever his hit points are. He is not meant to die."),
    ("enemy_cards", [{
        "name": "Groudon (corrupted)",
        "sub": "Gargantuan elemental (Guardian of the Plane of Earth), unaligned \u2726 CR 11 (7,200 XP) "
               "\u2726 Session 8",
        "img": "assets/monsters/groudon_corrupted.png", "img_w": 3.4,
        "stats": [
            "**AC** 18 (mountain plate)  **HP** 230  **Speed** 40 ft., burrow 40 ft.",
            "**STR** 26  **DEX** 6  **CON** 24  **INT** 8  **WIS** 14  **CHA** 12",
            "**Resist** all damage from nonmagical weapons \u2726 **Imm.** fire, poison",
            "**Senses** tremorsense 120 ft., passive Perception 12",
            "**Challenge** 11 (7,200 XP)",
        ],
        "traits": [
            ("THE SPIKE (the whole encounter)", "A shard of black glass driven into his shoulder. **AC 17, 60 "
             "hit points**, immune to all damage except radiant, force, and Cleansing Edge. Reaching it means "
             "climbing him, flying, or shooting at disadvantage. **When the spike is destroyed the encounter "
             "ends immediately.** Do not run Groudon to 0 hit points."),
            ("Unstoppable", "Cannot be frightened, charmed, restrained or knocked prone, and ignores difficult "
             "terrain."),
            ("Agony", "While the spike is intact, at the start of each of his turns he takes 10 damage and every "
             "creature within 20 ft. makes a DC 16 Dexterity save or takes 10 (3d6) bludgeoning."),
            ("He Does Not Finish Them", "When Groudon reduces a creature to 0 hit points he immediately moves "
             "away from it. He is swatting at pain, not hunting children."),
        ],
        "actions": [
            ("Continental Step", "He moves up to his speed. Every creature on the ground within 30 ft. of his "
             "path makes a DC 16 Dexterity save or is knocked prone and takes 11 (2d10) bludgeoning."),
            ("Magma Vent (Recharge 4-6)", "A 60-ft line, 10 ft. wide. DC 17 Dexterity save, 35 (10d6) fire, "
             "half on a success."),
            ("Claw", "*Melee Weapon Attack:* +12 to hit, reach 15 ft. *Hit:* 22 (3d10 + 8) slashing."),
            ("Thrash (1/round, no action, when the spike takes damage)", "Every creature climbing him makes a "
             "DC 15 Strength or Acrobatics check or falls, taking 3d6 bludgeoning."),
        ],
    }]),
    ("lore", "What the Guardians Are For",
     "Every world keeps one. Not a king and not a god: a creature that is somehow the shape of "
     "that world's health, so that when the world sickens the guardian sickens first and worst. "
     "The Guardians of Elaria have now freed two, a clockwork giant under a city and a mountain "
     "with a spine, and both times the cure was the same. Find what is hurting it. Take that out. "
     "The world does the rest itself."),

    ("lore", "The Machines Remember",
     "Machines feel the Darkening before people do. A machine is a promise written in brass, "
     "and promises are exactly what the Weaver of Fractures unpicks first. When the mills and "
     "servitors of the world began to stumble, the made folk of Gearhaven understood it the "
     "way sailors understand a red sky, and grieved for the gentle giant most of all."),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    print("built", build_doc(B, "compendium/bestiary.docx"))
