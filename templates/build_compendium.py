# build_compendium.py
# The Guardians of Elaria: running reference volumes.
# Builds two docx files in compendium/: magic items and custom content.
# (The bestiary is built elsewhere.)
# Rebuild after each session revision; add entries as play continues.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

NOTE = "A running reference for The Guardians of Elaria. Updated as the chronicle grows."

def title(kicker, sub):
    return ("titlepage", "THE GUARDIANS OF ELARIA", kicker, sub, NOTE)

# ----------------------------------------------------------------------
# VOLUME: MAGIC ITEMS & RELICS
# ----------------------------------------------------------------------
I = [
    title("TREASURES & RELICS", "The Magic of the Chronicle"),
    ("gold", "Every treasure of the Guardians' road, from a mother's parting gift to the relics of "
             "a sleeping goddess. Items marked with the seven-point star are Elaria's own."),

    ("h1", "The Great Mysteries"),
    ("h2", "The Essence Sphere"),
    ("imgfloat", "assets/items/essence_sphere.png", 2.6),
    ("body", "Brass and crystal, warm as a heartbeat, made by the deep-gnome masters of Glimmerspire "
             "BEFORE the cracks ever opened (how they knew is a question nobody has answered). It "
             "holds Pikachu's sleeping spark, and it is a GATHERER: it pulls loose planar motes to "
             "itself and survives holding them, which no other vessel can. It is the missing anchor "
             "of Vane's Rift Portal, and it never leaves the party's keeping. Gained **Planar "
             "Attunement** at the Whispering Glade (advantage on Arcana concerning planar magic)."),
    ("body", "The Circle has no proper word for what the Sphere is, only what it does: it keeps. "
             "Whatever loose scrap of another world drifts past, the Sphere gathers it in and holds "
             "it steady, the way a lantern keeps a single flame out of the wind. Every other vessel "
             "the deep gnomes ever tried cracked, dimmed, or worse. This one only glows a little "
             "warmer, and waits."),
    ("lore", "The Sign of Seven Points",
     "The old tellings agree that Elaria signed her safeguards the way a mother sews a name "
     "into a coat: not so the gift would be admired, but so it could always find its way home. "
     "The seven points are said to be the seven planes she kept turning, and the leafed vine "
     "that wraps them is the world itself, holding on. When one of her gifts is near, the sign "
     "is said to warm, as if glad to be recognized."),

    ("h2", "The Three Enchanted Potatoes"),
    ("imgfloat", "assets/items/three_potatoes.png", 2.6),
    ("body", "Ash Catchum's legacy to his son: three unassuming potatoes that are anything but. The "
             "goddess named them **remnants of a shattered covenant**, safeguards bound from her own "
             "essence in the old lore (Healing, Transformation, Insight). They pulse when the world "
             "thins, a slow warm beat you feel in the palm more than hear, and they have never once "
             "spoiled, sprouted crooked, or agreed to be eaten. Their hour has not yet come, but the "
             "Circle is patient, and so, apparently, are the potatoes."),
    ("body", "Ursa carries them wrapped in a cloth his father knotted, and will not say why he trusts "
             "three root vegetables with the fate of anything. He only shrugs and says they came from "
             "Ash, and that Ash was rarely wrong about which small things turned out to matter."),
    ("lore", "The Enchanted Potatoes",
     "The Circle keeps a very old, very short list titled \"Safeguards, Probable.\" Entry "
     "nine reads: \"The traveling potatoes. Warm to the touch. Kindly disposition. Keep "
     "planting them.\" Nobody knows who wrote it. The handwriting is extremely old."),

    ("h2", "Stabby's Idol"),
    ("imgfloat", "assets/items/stabbys_doll.png", 2.2, "left"),
    ("body", "A small carved figure Stabby found tucked in his bag after Wraithpine, though nobody "
             "saw who put it there. It goes ice cold near rifts, and corruption recoils from it. It "
             "has dreams in it. That is all anyone knows, yet."),
    ("body", "Stabby will not part with it, and cannot say why. He only knows the dark feels friendlier "
             "when the idol rides in his pack, that the coldest nights on the road are the ones it warns "
             "him of, and that once, half asleep, he heard it breathing in time with him. The idol keeps "
             "its own counsel. So, for now, does he."),
    ("lore", "The Scattered Safeguards",
     "No one has ever counted the safeguards, which is the point of scattering. Some hang in "
     "plain sight in tavern rafters. Some sleep in root cellars, humble as potatoes. The old "
     "rule of the Circle is: treat every odd little thing kindly, in case it is holding up "
     "the sky."),

    ("h1", "Relics of Elaria (the Wraithpine Chest)"),
    ("body", "One half-buried chest, bound in vines of silver and root, opened by Ghostbloom's song "
             "beneath the Old Theater. Inside, three gifts, each bearing the seven-point star."),
    ("lore", "One Chest, Three Gifts",
     "The Circle teaches that the Warden never gave a gift to one hand alone. Her safeguards "
     "came in sets, they say, because a thing meant to hold up the sky is too heavy for any "
     "single pair of arms. The chest that opened to a song beneath the old theater held three "
     "gifts and one lesson: a stave for the sky, a sash for the swift, and a small bright core "
     "for the maker, and none of the three was meant to be carried without the other two."),
    ("img", "assets/items/wraithpine_chest.png", "The Wraithpine chest, bound in silver vines.", 3.4),
    ("h2", "Staff of Waking Constellations (Ursa)"),
    ("stat", "Staff of Waking Constellations", [
        "+1 quarterstaff, druidic focus (a +2 once awakened on the Reader of Omens road). 5 charges, regain 1d4 + 1 at dawn: guiding bolt (1), faerie fire (1), moonbeam (2).",
        "**Starseed.** Once per turn, +1d4 radiant when Ursa deals radiant damage with a druid spell, rising to +1d8 once the staff is awakened (house rule: druid spells only).",
        "**Starlight.** Bonus action: 10 ft. dim light; advantage on night navigation.",
        "The counter-weapon: after every great victory, one new star brightens on its haft. The enemy puts stars out; the Staff lights them.",
    ]),
    ("h2", "Sash of the Swift Current, Rewoven (Stabby)"),
    ("stat", "Sash of the Swift Current (Rewoven)", [
        "Scarlet stage-silk rewoven with theater rigging thread. +1 AC (stacks with Unarmored Defense).",
        "**Fleetstep.** +10 ft. walking speed. **Air Dance.** 1/day bonus action: fly speed equal to walking, 1 minute.",
        "**Feather Fall.** 1/day, no components. Its star sigil is cupped by a pair of wings.",
    ]),
    ("h2", "Glimmerspire Pocket Dynamo, Mk II (Lilly)"),
    ("stat", "Glimmerspire Pocket Dynamo (Mk II)", [
        "A thumb-sized brass core stamped PROP ROOM in stage-engraver script (a mystery unexplained).",
        "**Pocket Arsenal.** Deploy or recall the Eldritch Cannon as a free action. **Endurance Overhaul.** Cannon lasts 24 hours.",
        "**Power Sync.** Cannon deals +2 damage. **Reformat.** 1/long rest, action: change the cannon's model.",
        "Near Ghostbloom, the core glows soft ghost-green, like a stage cue waiting for its moment.",
    ]),
    # The three relics share one gallery row instead of stacking dead space.
    ("imgrow", [("assets/items/staff_of_waking_constellations.png",
                 "The Staff of Waking Constellations."),
                ("assets/items/sash_of_the_swift_current.png",
                 "The Sash of the Swift Current, rewoven."),
                ("assets/characters/lilly_with_dynamo.png",
                 "Lilly with the Pocket Dynamo.")], 2.05),

    ("h1", "Gifts of Faelan (Havenmoor, Session 4)"),
    ("h2", "Frostbite Shard Dagger (Lilly)"),
    ("stat", "Frostbite Shard Dagger", [
        "Rare, attunement by an Artificer. Crystalline ice that never melts. 1d4 piercing + 1d4 cold, +1 to attack.",
        "**Spell focus and Arcane Firearm.** +1d8 frost to one spell damage roll cast through it; +2 frost on spell damage.",
    ]),
    ("h2", "Amulet of Guiding Light (Ursa)"),
    ("stat", "Amulet of Guiding Light", [
        "Rare, attunement by a Circle of Stars druid.",
        "**Guiding Light.** Sheds light; allies gain +1 to attacks and saves while Ursa is in Starry Form. Once the amulet is awakened on the Reader of Omens road, this reaches every ally within 30 feet.",
        "**Starry Glow.** Reaction, 1/long rest: 2d8 radiant, DC 15 Con or blinded. **Celestial Resilience.** Reroll natural 1s, 2/long rest.",
    ]),
    ("h2", "Candyfang Katana (Stabby)"),
    ("stat", "Candyfang Katana", [
        "Rare, attunement by a Monk. A katana of impossible candy-striped steel. 1d8/1d10 slashing, +1 attack and damage.",
        "**Sugar Rush.** Bonus action lick, 1/long rest: 2d8 + Con temporary HP. **Frostbite Infusion.** +2 frost on hit.",
        "Destined to become a Bloodfang heirloom when the Nichirin blade comes.",
    ]),
    # The three gifts share one gallery row instead of stacking dead space.
    ("imgrow", [("assets/items/frostbite_shard_dagger.png",
                 "The Frostbite Shard Dagger."),
                ("assets/items/amulet_of_guiding_light.png",
                 "The Amulet of Guiding Light."),
                ("assets/items/candyfang_katana.png",
                 "The Candyfang Katana.")], 2.05),

    ("h1", "Boons, Baubles & Blessings"),
    ("imgfloat", "assets/items/carol_rune_tablet.png", 2.0),
    ("body", "**Elaria's boons (the Whispering Glade, Session 2):** Ursa, Planar Awareness (sense "
             "planar disturbances, 24 hours); Lilly, the Sphere's Planar Attunement; Stabby, Glimpse "
             "of Possibility (one reroll, because the goddess smiled at the goblin)."),
    ("body", "**The eight Winter Bells (Session 4).** C, D, E, F, G, A, B, High C: relics of "
             "Elaria's light hidden across Havenmoor. Rung in harmony they unmade the Krampusshade. "
             "**Faelan's Frosted Cookies:** 2d8 healing, a short rest's comfort, and one spell slot, "
             "in cookie form."),
    ("body", "**Curios of the road.** The Shadow-Touched Rune Fragment (advantage vs fear, 1 hour); "
             "the Dark Fragment of Stormwatch Cliffs (crystallized chaos, evidence of sabotage); "
             "Terranox's stone fragments and the elemental mud samples of the Grove of Elemental "
             "Waters; beeswax earplugs that beat a monster's song; a bell-handled "
             "blue lantern from Pumpkin Row; Alwen's flasks of lucky seawater."),
    ("lore", "The Bells of the Coast",
     "When the safeguards were scattered, eight fell along the southern coast as bells, each "
     "holding one clear note of the song Elaria sang while she worked. Havenmoor built its "
     "festival around them centuries before anyone remembered why the bells mattered. The "
     "town rang them every winter anyway. Traditions are how a town remembers what its people "
     "forget, and one winter the ringing unmade a fiend."),
]

# ----------------------------------------------------------------------
# VOLUME III: CUSTOM CONTENT (feats, subclasses, house rules)
# ----------------------------------------------------------------------
C = [
    title("THE CUSTOM COMPENDIUM", "Subclasses, Paths & House Rules"),
    ("gold", "Homebrew and rulings of this table: the paths the heroes may walk after the year "
             "apart, and the standing rules of the campaign. 2024 rules throughout; house rules "
             "override the books. The heroes themselves, every number, slot, and spell, now live "
             "in Part IV: The Guardians' Character Sheets."),

    ("h1", "House Rules & Standing Rulings"),
    ("body", "**House rules (adjudications beyond the printed rules).**"),
    ("body", "1. Ursa's Starseed +1d4 applies only to actual druid spells, never the Starry Form "
             "Archer's luminous arrow."),
    ("body", "2. Potent Spellcasting rides the kindled staff once per turn (Ursa, from level 7; "
             "no double-dipping with a cantrip in the same turn)."),
    ("body", "**2024 notes (these are the printed rules, recorded so the table never slips back "
             "to older text).** Patient Defense's free tier is Disengage; Dodge costs 1 Focus "
             "Point. Eating a Goodberry is a Bonus Action. Shillelagh replaced Primal Savagery "
             "on Ursa's sheet. Deep gnome uses the current printing (Svirfneblin Camouflage; "
             "Disguise Self and Nondetection 1/long rest each). The Eldritch Cannon picks its "
             "mode on every activation. The Air Bestial Spirit has 20 Hit Points by its own "
             "stat block."),
    ("lore", "The First Listeners",
     "Before there were villages there were listeners. The first druids did not learn magic; "
     "they learned quiet, and the forests, glad of the company, taught them the rest. The "
     "Circle of the Eternal Stars still opens every gathering with a full minute of silence, "
     "in honor of the age when that was the whole religion."),

    ("h1", "The Three Doors"),
    ("gold", "At the close of the Gearhaven chapter the Guardians parted for a year: a year of "
             "workshops and roads and night skies, each hero following their own heart home. "
             "Before each of them stand three doors, three ways that year apart might be spent, "
             "and behind every door waits a different gift."),
    ("body", "The chapters that follow set down what waits behind all nine: Stabby's three breathing "
             "styles, Ursa's three paths of the stars, and Lilly's three artifacts. Each Guardian "
             "will choose exactly one door, and none of the three has chosen yet. When they do, the "
             "doors not taken will remain in these pages, roads not walked, ready for other heroes "
             "in other tellings."),
    # The three heroes at the parting: each stands before a different set of
    # doors. Fills the tail before Stabby's path opens on a fresh page.
    ("imgrow", [("assets/characters/stabby_v3_portrait.png",
                 "Stabby, before the three breathing styles."),
                ("assets/characters/ursa_v3_portrait.png",
                 "Ursa, before the three paths of the stars."),
                ("assets/characters/lilly_v3_portrait.png",
                 "Lilly, before the three artifacts.")], 1.95),
    ("lore", "The Roads Not Taken",
     "The old tellings are gentle about the doors a hero leaves closed. A road not walked is "
     "not a road lost, the Circle says, only a road lent to someone else. Every path in these "
     "pages was true; a Guardian simply cannot be three heroes at once, and the year apart is "
     "the world's kind way of asking each of them who they most wish to become."),
    # The parting itself fills the chapter-turn page (DM directive 2026-07-13).
    ("img", "assets/session_07/beat_7/the_party_parts.png",
     "The parting at Gearhaven's gates: three friends, three roads, one year.",
     5.8, {"crop": "3:2", "hmax": 3.9}),

    # ------------------------------------------------------------------
    # WARRIOR OF BREATHING: full text of warrior_of_breathing_v2.pdf
    # ------------------------------------------------------------------
    ("h1", "Warrior of Breathing (Stabby's Path)", {"hardbreak": True}),
    ("body", "A homebrew monk subclass taken at level 7 in place of Kensei. A Warrior of Breathing "
             "kindles an inner style, a visible breath that wreathes the blade. Three doors, three "
             "breathing styles; every road grants the **Nichirin Katana**, and every First Form "
             "replaces Flurry of Blows. The full text of all three follows."),
    ("lore", "What a Breathing Style Is",
     "The mountain monks say a breathing style is not a trick of the lungs but a way of "
     "remembering. Every warrior carries a wild thing, a still river, and a patch of honest "
     "dark somewhere inside them; a breathing style is simply the practice of calling one of "
     "them up on purpose, and setting it down again when the fight is done. The breath, the "
     "old masters warn, is easy to light and hard to quench, which is why they teach the "
     "quenching first."),

    ("h2", "Beast Breathing: the Bloodfang Form"),
    ("gold", "*“You think too much, little storm. The beast does not think. The beast moves, "
             "and the beast is already behind you.”* (the lesson Stabby finally understood)"),
    ("imgfloat", "assets/characters/stabby_breathing_style_red.png", 3.0),
    ("body", "Some warriors learn to still the storm inside them. The Warrior of Beast Breathing "
             "learns to ride it. Where other monks seek calm, this form reaches into the wild, "
             "animal heart of the fighter: the part that does not hesitate, does not flinch, and "
             "does not stop. Practitioners breathe in time with a racing heartbeat rather than a "
             "slow one, and when they ignite their breath, their blade glows blood-red and their "
             "body moves with the loping, unstoppable grace of a hunting beast."),
    ("body", "It is a form born of survival rather than discipline, favored by those who grew up "
             "where the strong eat and the slow are eaten. To master it is not to tame the beast, "
             "but to become it on command, and to remember how to set it down again afterward."),
    ("body", "**Features by Monk Level.** You gain Warrior of Beast Breathing features at Monk "
             "levels 3 (Beast Breathing), 6 (First Form: Devour), 11 (Advanced Beast Breathing), "
             "and 17 (Third Form: Apex Predator)."),
    ("stat", "Level 3: Beast Breathing", [
        "**Monk Weapons.** A katana, as well as any sword you adopt as your signature blade, "
        "counts as a Monk weapon for you. You can use your Martial Arts die with it, and you can "
        "use this subclass's features with it. You can still make an Unarmed Strike as a Bonus "
        "Action.",
        "**Beast Sense.** Your senses are sharp as a hunting animal's, even out of combat. You "
        "have Advantage on Wisdom (Survival) checks made to track creatures, on Wisdom "
        "(Perception) checks that rely on smell or hearing, and on Charisma (Intimidation) checks.",
        "**Igniting the Breath.** When you roll Initiative, you can expend 1 Focus Point to ignite "
        "your breath. It lasts until the combat ends, until you have the Incapacitated condition, "
        "or until you end it (no action required). While your breath is ignited, your weapon "
        "glows blood-red, and whenever you hit a target with it, the target takes an extra 2 "
        "Force damage.",
        "**Beast's Vigor.** While your breath is ignited, your Speed increases by 10 feet, and "
        "you have Advantage on Dexterity saving throws.",
    ]),
    ("stat", "Level 6: First Form: Devour", [
        "**First Form: Devour.** As a Bonus Action, you can expend 1 Focus Point to move up to 15 "
        "feet without provoking Opportunity Attacks and make one attack with your Monk weapon. On "
        "a hit, the target takes Force damage equal to 3d8 plus your Dexterity modifier instead "
        "of the weapon's normal damage. Bonuses to the weapon's damage rolls (such as the "
        "Nichirin katana's +2 bonus and the extra damage from your ignited breath) apply as "
        "normal. If the attack reduces the target to 0 Hit Points, you regain the expended Focus "
        "Point. This feature replaces Flurry of Blows for you.",
    ]),
    ("stat", "Level 11: Advanced Beast Breathing", [
        "**Advanced Breathing.** Your ignited breath grows fiercer. While your breath is ignited, "
        "you retain all its other benefits, you have Resistance to Bludgeoning, Piercing, and "
        "Slashing damage, and the extra Force damage your weapon deals increases from 2 to 3.",
        "**Sharpened Fang.** The damage of your First Form: Devour increases to 5d10 plus your "
        "Dexterity modifier.",
    ]),
    ("stat", "Level 17: Third Form: Apex Predator", [
        "**Third Form: Apex Predator.** You become a blur of fang and steel. As a Bonus Action, "
        "you can expend 3 Focus Points to move up to your Speed without provoking Opportunity "
        "Attacks and make one attack with your Monk weapon against each of up to three different "
        "creatures you move within reach of. On a hit, the target takes Force damage equal to "
        "5d10 plus your Dexterity modifier instead of the weapon's normal damage. Bonuses to the "
        "weapon's damage rolls (such as the Nichirin katana's +2 bonus and the extra damage from "
        "your ignited breath) apply as normal. Each creature hit must succeed on a Strength "
        "saving throw (DC 8 plus your Wisdom modifier and Proficiency Bonus) or have the Prone "
        "condition. You regain 1 expended Focus Point for each "
        "creature this feature reduces to 0 Hit Points.",
    ]),

    ("h2", "Water Breathing: the Monastery Form"),
    ("gold", "*“Be water. Water does not strike; it flows, and the rock is cut all the same. "
             "Now breathe, and begin again.”* (Master Kaelon Windstep)"),
    ("imgfloat", "assets/characters/stabby_breathing_style_water.png", 3.0),
    ("body", "The Warrior of Water Breathing is the form of the patient master, the discipline that "
             "other monks spend their whole lives chasing. Its practitioners learn to move like a "
             "river: never rigid, never still, every strike flowing into the next, every blow "
             "turned aside by giving way rather than resisting. When they ignite their breath, "
             "their blade runs pale blue and cold, and their guard becomes as fluid and unbroken "
             "as a current that cannot be grasped."),
    ("body", "It is the most traditional of the breathing forms, and the hardest to truly master, "
             "for it asks the warrior to be calm in the middle of chaos. Those who walk this path "
             "are as often menders as fighters, for the same stillness that turns a blade can also "
             "close a wound, and the same patience that wins a duel can sit a long vigil at a "
             "friend's side."),
    ("body", "**Features by Monk Level.** You gain Warrior of Water Breathing features at Monk "
             "levels 3 (Water Breathing), 6 (First Form: Flowing Strike and Healing Spring, First "
             "Water), 11 (Advanced Water Breathing and the full Healing Spring), and 17 (Third "
             "Form: Tidal Crash)."),
    ("stat", "Level 3: Water Breathing", [
        "**Monk Weapons.** A katana, as well as any sword you adopt as your signature blade, "
        "counts as a Monk weapon for you. You can use your Martial Arts die with it, and you can "
        "use this subclass's features with it. You can still make an Unarmed Strike as a Bonus "
        "Action.",
        "**Igniting the Breath.** When you roll Initiative, you can expend 1 Focus Point to ignite "
        "your breath. It lasts until the combat ends, until you have the Incapacitated condition, "
        "or until you end it (no action required). While your breath is ignited, your weapon "
        "glows pale blue, and whenever you hit a target with it, the target takes an extra 2 Cold "
        "damage.",
        "**Flowing Guard.** While your breath is ignited, you gain a +2 bonus to Armor Class "
        "against the first attack roll made against you before the start of each of your turns.",
    ]),
    ("stat", "Level 6: First Form: Flowing Strike", [
        "**First Form: Flowing Strike.** As a Bonus Action, you can expend 1 Focus Point to move "
        "up to 15 feet without provoking Opportunity Attacks and make one attack with your Monk "
        "weapon. On a hit, the target takes Cold damage equal to 3d8 plus your Dexterity modifier "
        "instead of the weapon's normal damage. Bonuses to the weapon's damage rolls (such as the "
        "Nichirin katana's +2 bonus and the extra damage from your ignited breath) apply as "
        "normal. If the attack hits, the target must also succeed on a Dexterity saving throw "
        "(DC 8 plus your Wisdom modifier and Proficiency Bonus) or have the Prone condition. "
        "This feature replaces Flurry of Blows for you.",
        "**Healing Spring (First Water).** As a Bonus Action, you can touch yourself or another "
        "creature, and the target regains a number of Hit Points equal to 2d8 plus your Wisdom "
        "modifier. Once you use this benefit, you can't use it again until you finish a Short or "
        "Long Rest. This benefit improves when you reach Monk level 11 (Healing Spring).",
    ]),
    ("stat", "Level 11: Advanced Water Breathing", [
        "**Advanced Breathing.** Your ignited breath deepens. While your breath is ignited, you "
        "retain all its other benefits, and whenever you hit a creature with your Monk weapon, "
        "that creature's Speed is reduced by 10 feet until the start of your next turn.",
        "**Sharpened Flow.** The damage of your First Form: Flowing Strike increases to 5d10 plus "
        "your Dexterity modifier.",
        "**Healing Spring.** When you use your Healing Spring, the target now regains a number "
        "of Hit Points equal to 4d8 plus your Wisdom modifier. Once you use this benefit, you "
        "can't use it again until you finish a Short or Long Rest.",
    ]),
    ("stat", "Level 17: Third Form: Tidal Crash", [
        "**Third Form: Tidal Crash.** As a Bonus Action, you can expend 3 Focus Points to move "
        "up to 20 feet and make one attack with your Monk weapon against each of up to three "
        "different creatures within your reach during that movement. On a hit, the target takes "
        "Cold damage equal to 5d10 plus your Dexterity modifier instead of the weapon's normal "
        "damage. Bonuses to the weapon's damage rolls (such as the Nichirin katana's +2 bonus "
        "and the extra damage from your ignited breath) apply as normal. Each creature hit must "
        "succeed on a Dexterity saving throw (DC 8 plus your Wisdom modifier and Proficiency "
        "Bonus) or have the Prone condition and a Speed of 0 until the end of its next turn.",
    ]),

    ("h2", "Shadow Breathing: the Idol Form"),
    ("gold", "*“Do not fear the dark. Breathe it in. Let it fill you, and then there is "
             "nothing left in the dark to fear you.”* (a whisper from the idol)"),
    ("imgfloat", "assets/characters/stabby_breathing_style_shadow.png", 3.0),
    ("body", "The Warrior of Shadow Breathing is the strangest and most secretive of the forms, a "
             "discipline touched by something older than any monastery. Its practitioners breathe "
             "in the gloom itself, drawing the dark into their lungs until it answers to them. "
             "When they ignite their breath, their blade runs violet-black, the shadows fold "
             "around them like a cloak, and they see clearly in darkness that blinds everyone "
             "else."),
    ("body", "Few teach this form openly, for it walks close to powers most monks are warned away "
             "from. Those who carry it often carry a question they cannot yet answer: why the dark "
             "heeds them, where the breath truly comes from, and what waits at the end of the path "
             "they have started down. Mastered well, it makes a warrior into something the night "
             "itself seems to bend around."),
    ("body", "**Features by Monk Level.** You gain Warrior of Shadow Breathing features at Monk "
             "levels 3 (Shadow Breathing), 6 (First Form: Umbral Slash), 11 (Advanced Shadow "
             "Breathing), and 17 (Third Form: Eclipse)."),
    ("stat", "Level 3: Shadow Breathing", [
        "**Monk Weapons.** A katana, as well as any sword you adopt as your signature blade, "
        "counts as a Monk weapon for you. You can use your Martial Arts die with it, and you can "
        "use this subclass's features with it. You can still make an Unarmed Strike as a Bonus "
        "Action.",
        "**Eyes of the Idol.** The idol's gift never fully leaves you. You have Darkvision with a "
        "range of 60 feet (if you already have Darkvision, its range increases by 60 feet), and "
        "you have Advantage on Dexterity (Stealth) checks.",
        "**Igniting the Breath.** When you roll Initiative, you can expend 1 Focus Point to ignite "
        "your breath. It lasts until the combat ends, until you have the Incapacitated condition, "
        "or until you end it (no action required). While your breath is ignited, your weapon "
        "glows violet-black, and whenever you hit a target with it, the target takes an extra 2 "
        "Necrotic damage.",
        "**One With the Gloom.** While your breath is ignited, you gain a +2 bonus to Armor "
        "Class against ranged attack rolls, and you can see normally in magical Darkness.",
    ]),
    ("stat", "Level 6: First Form: Umbral Slash", [
        "**First Form: Umbral Slash.** As a Bonus Action, you can expend 1 Focus Point to "
        "teleport up to 15 feet to an unoccupied space you can see within 5 feet of a creature. "
        "Magical Darkness then fills a 10-foot Cube of your choice, which must contain that "
        "creature's space. You then make one attack with your Monk weapon against that creature, "
        "and you have Advantage on the attack roll. On a hit, the target takes Necrotic damage "
        "equal to 3d8 plus your Dexterity modifier instead of the weapon's normal damage. "
        "Bonuses to the weapon's damage rolls (such as the Nichirin katana's +2 bonus and the "
        "extra damage from your ignited breath) apply as normal.",
        "You can see through Darkness created by this feature. The Darkness lasts until the end "
        "of your next turn, or you can end it early (no action required). This feature replaces "
        "Flurry of Blows for you.",
    ]),
    ("dm", "The gloom is his alone. Stabby sees through his own Darkness; his allies cannot. "
           "Allies make ranged attack rolls with Disadvantage against a creature wrapped in the "
           "gloom, and spells that require a visible target cannot reach it at all, so the party "
           "learns to pick different targets while the shadow does its work."),
    ("stat", "Level 11: Advanced Shadow Breathing", [
        "**Advanced Breathing.** Your ignited breath drinks deeper of the dark. While your "
        "breath is ignited, you retain all its other benefits. In addition, once per turn when "
        "you hit a creature with an attack roll that had Advantage, the target takes an extra "
        "2d6 Necrotic damage.",
        "**Sharpened Gloom.** The damage of your First Form: Umbral Slash increases to 5d10 plus "
        "your Dexterity modifier.",
    ]),
    ("stat", "Level 17: Third Form: Eclipse", [
        "**Third Form: Eclipse.** You vanish into the gloom and strike from everywhere at once. "
        "As a Bonus Action, you can expend 3 Focus Points to fill a 20-foot Cube centered on "
        "yourself with magical Darkness, which you can see through. For each of up to three "
        "different creatures in the Cube, you can teleport to an unoccupied space you can see "
        "within 5 feet of that creature and make one attack with your Monk weapon against it, "
        "and you have Advantage on each attack roll. On a hit, the target "
        "takes Necrotic damage equal to 5d10 plus your Dexterity modifier instead of the "
        "weapon's normal damage. Bonuses to the weapon's damage rolls (such as the Nichirin "
        "katana's +2 bonus and the extra damage from your ignited breath) apply as normal. Each "
        "creature hit has the Blinded condition until the end of your next turn, and creatures "
        "other than you can't see you until the Darkness ends.",
    ]),

    ("h2", "The Demon-Slayer's Blade: the Nichirin Katana"),
        ("body", "This sun-forged demon-slayer blade was made from crimson ore that drinks in "
             "dawnlight. While sheathed, the steel looks dark and almost ordinary, but when Stabby "
             "ignites his breathing, the blade catches that breath and burns with the color of his "
             "chosen form."),
    ("stat", "Nichirin Katana", [
        "*Weapon (Katana), Rare (Requires Attunement by Stabby)*",
        "**Weapon Statistics.** The Nichirin katana uses the statistics of a Longsword (1d8 "
        "Slashing damage) and has the Finesse and Versatile (1d10) properties, and it counts as "
        "a Monk weapon for you. Because the weapon has the Finesse property and is a Monk weapon "
        "for you, you can use your Dexterity modifier for its attack and damage rolls.",
        "**Magic Weapon.** You gain a +2 bonus to attack rolls and damage rolls made with this "
        "magic weapon.",
        "**Breath-Kindled Steel.** When you ignite your breathing, the blade glows with the "
        "color and nature of that form: blood-red for Beast Breathing, pale blue for Water "
        "Breathing, or violet-black for Shadow Breathing. This glow is magical but sheds only "
        "Dim Light unless you choose otherwise.",
        "**Cleansing Edge.** Once per turn when you hit a Fiend, an Undead, a shadow creature, "
        "or a creature empowered by planar corruption with this weapon, the blade burns away "
        "corruption until the start of your next turn. Until then, the target can't regain Hit "
        "Points and can't benefit from magical Darkness or shadowy concealment against you. Any "
        "visible corruption around the wound briefly burns, cracks, or peels away in sparks of "
        "purified light.",
        "The blade wounds the corruption, not the creature beneath; when a corrupted guardian "
        "falls to it, what breaks is the darkness.",
    ]),
    ("img", "assets/items/nichirin_katana.png",
     "The Nichirin Katana: dark steel waiting for dawnlight.", 5.6,
     {"crop": "3:2", "hmax": 3.8}),
    ("h2", "Lore of the Blade"),
    ("body", "They say the first Nichirin blades were quenched not in water or oil but in the "
             "light of dawn itself, folded by smiths who worked only in the hour before sunrise. "
             "The ore came from a single mountain that caught the morning sun before anywhere else "
             "in the world, and steel drawn from it never forgot that first warmth. A finished "
             "blade looks plain and dark in an idle hand; it is waiting. Only a warrior who can "
             "kindle their own breath can wake the color sleeping in the metal."),
    ("body", "For a creature of corruption, that waking light is a death sentence. Where an "
             "ordinary sword cuts flesh, a Nichirin blade cuts the rot itself: the shadow that "
             "hides a fiend, the dark magic that knits an undead back together, the planar taint "
             "that lets a horror shrug off honest steel. Stabby's blade chose its colors from his "
             "own breathing forms, and now it burns red, blue, or violet to match whichever beast, "
             "river, or shadow he calls upon."),
    ("gold", "**A whispered rumor.** Old hunters claim a Nichirin blade can never be truly stolen: "
             "carried by the wrong hand, the steel stays cold and dull and will not take an edge. "
             "No one in living memory has dared find out."),
    ("h2", "Setting Down the Kensei's Way"),
    ("body", "When Stabby takes up a breathing form at Level 7, the Kensei's tricks retire with "
             "his old teacher's lessons: Kensei's Shot and Agile Parry go, and the Repeating "
             "Longbow becomes simply a very good bow. In exchange he gains a stance he can ignite "
             "every single fight, a First Form that turns his Bonus Action into a 3d8 + 5 strike "
             "with 15 feet of free movement, and a road that grows with him to Level 17. He is "
             "trading a parry for a predator's gait. (And Candyfang remains: an heirloom at his "
             "belt, or one day a gift worthy of a Bloodfang.)"),

    # ------------------------------------------------------------------
    # PATHS OF THE STARS: full text of ursa_path_rewards_v2.pdf
    # ------------------------------------------------------------------
    ("h1", "Paths of the Stars (Ursa's Path)", {"hardbreak": True}),
    ("gold", "*For Ursa Catchum, Circle of the Stars Druid: the year apart, Level 5 to 7.* "
             "Ursa walked one of three roads during the year apart, and came back changed. Each "
             "road deepens something Ursa already does: his summons, his starry form, or his "
             "omens. Each "
             "road grants a feat (what he sought) and a keepsake (what found him): he gains the "
             "pair matching his road. These are special story feats: they grant no Ability Score "
             "Increase."),
    ("lore", "The Star-Paths of the Circle",
     "The Circle holds that no druid chooses the stars; the stars choose, and the druid only "
     "walks to meet them. Three roads are said to open before a sky-reader who has served the "
     "Circle well: one into the wild, where the living world answers; one into the sky, where "
     "the constellations lend their light; and one along a father's trail, where the omens stop "
     "coming at random and begin, at last, to obey. A druid walks one road and comes back "
     "changed, and the two roads not taken wait, patient as starlight, for whoever comes next."),

    ("h2", "Beast Handler: The Living World (the road into the wild)"),
    ("gold", "*“You went out to learn the speech of wild things. You came back, and three "
             "of them followed you home.”*"),
    ("stat", "Beast Handler (feat)", [
        "*Story Feat*",
        "You gain the following benefits.",
        "**Mightier Summons.** Whenever you cast the Summon Beast spell, the spell takes "
        "effect as if you had cast it using a spell slot of the highest level you can cast, "
        "without expending a slot of that level.",
        "**Signature Partners.** Your Summon Beast spell no longer conjures a nameless "
        "spirit. When you cast the spell, one of your three partners answers the call: "
        "Arcanine, Lapras, or Noctowl. The partner uses the Signature Partner stat block "
        "below, with the traits and actions marked for it.",
        "**Wild Speech.** You and any beast you summon can communicate simple ideas with "
        "each other telepathically.",
    ]),
    ("body", "*Ursa walked the wild year with three companions, and they answer his call "
             "still. These are not spirits wearing borrowed shapes; they are his friends, and "
             "he named each one the day it chose him.*"),
    ("imgrow", [("assets/characters/partner_arcanine.png",
                 "Arcanine, the Land partner."),
                ("assets/characters/partner_lapras.png",
                 "Lapras, the Water partner."),
                ("assets/characters/partner_noctowl.png",
                 "Noctowl, the Air partner.")], 2.05),
    ("ua_stat", {
        "name": "Signature Partner",
        "type_line": "Beast (Arcanine: Medium, Land. Lapras: Large, Water. Noctowl: Small, Air), Unaligned",
        "top": [
            ("Armor Class", "11 + the level of the spell (natural armor)"),
            ("Hit Points", "30 + 10 for each spell level above 2 (Noctowl: 20 + 10 for "
             "each spell level above 2nd)"),
            ("Speed", "40 ft., climb 40 ft. (Arcanine only); 30 ft., swim 40 ft. (Lapras "
             "only); 20 ft., fly 60 ft. (Noctowl only)"),
        ],
        "abilities": [("STR", "18 (+4)"), ("DEX", "11 (+0)"), ("CON", "16 (+3)"),
                      ("INT", "4 (−3)"), ("WIS", "14 (+2)"), ("CHA", "5 (−3)")],
        "meta": [
            ("Damage Vulnerabilities", "Cold (Arcanine only); Lightning (Lapras and Noctowl only)"),
            ("Damage Immunities", "Fire (Arcanine only); Cold (Lapras only); Necrotic (Noctowl only)"),
            ("Senses", "darkvision 60 ft., passive Perception 12"),
            ("Languages", "understands the languages you speak"),
            ("Challenge", "None"),
            ("Proficiency Bonus", "equals your bonus"),
        ],
        "sections": [
            ("Traits", [
                ("Intimidate (Arcanine Only)",
                 "When the partner appears, each enemy within 15 feet of it must succeed "
                 "on a Wisdom saving throw against your spell save DC or take a −2 penalty "
                 "to attack rolls until the end of its next turn."),
                ("Shell Armor (Lapras Only)",
                 "Attack rolls against the partner can't be Critical Hits."),
                ("Keen Eye (Noctowl Only)",
                 "The partner's attack rolls can't have Disadvantage, and its sight isn't "
                 "impeded by Dim Light or Darkness."),
                ("Flyby (Noctowl Only)",
                 "The partner doesn't provoke Opportunity Attacks when it flies out of an "
                 "enemy's reach."),
            ]),
            ("Actions", [
                ("Multiattack",
                 "The partner makes a number of Rend attacks equal to half this spell's "
                 "level (round down)."),
                ("Rend",
                 "*Melee Attack Roll:* your spell attack modifier, reach 5 ft. *Hit:* "
                 "1d8 + 4 + the spell's level Slashing damage."),
                ("Extreme Speed (Arcanine Only)",
                 "The partner moves up to its Speed without provoking Opportunity Attacks "
                 "and makes one Rend attack. On a hit, the target takes extra Fire damage "
                 "equal to twice the spell's level."),
                ("Ice Beam (Lapras Only)",
                 "When the partner uses Multiattack, it can replace any Rend with an Ice "
                 "Beam. *Ranged Attack Roll:* your spell attack modifier, range 60 ft. "
                 "*Hit:* 1d8 + 4 + the spell's level Cold damage, and the target's Speed "
                 "decreases by 10 feet until the start of the partner's next turn."),
                ("Hypnosis (Noctowl Only; Recharge 5–6)",
                 "One creature the partner can see within 30 feet must succeed on a Wisdom "
                 "saving throw against your spell save DC or have the Incapacitated "
                 "condition until the end of the partner's next turn or until it takes "
                 "damage."),
            ]),
        ],
    }),
    ("body", "**Arcanine.** *Legendary for its speed, it is said to run six thousand miles "
             "in a day and a night, driven by a flame that burns within. The old tales say "
             "folk stood entranced just watching it run.*"),
    ("body", "**Lapras.** *Intelligent enough to understand speech, it ferries travelers "
             "across cold water on its broad back, and it sings where sailors can hear.*"),
    ("body", "**Noctowl.** *Its eyes see by the faintest starlight, its head turns all the "
             "way around when it thinks, and its wings make no sound at all.*"),
    ("stat", "The Wildheart Token", [
        "*Wondrous Item (carved by his own hand)*",
        "Three small totems strung on one leather cord, one for each partner, whittled "
        "beside the wild year's campfires. When a partner you summoned would drop to 0 "
        "Hit Points, it drops to 1 Hit Point instead. Once this property is used, it "
        "can't be used again until the next dawn.",
    ]),
    ("dm", "Naming is a table ceremony: the player names each partner the first time Ursa "
           "calls it, exactly like a first catch, and the chosen names go into the printed "
           "book alongside the species. Base creatures locked by the DM 2026-07-13: "
           "Arcanine, Lapras, and Noctowl, played as realistic-fantasy reskins."),

    ("h2", "Starlit Channeler: The Circle of Stars (the road into the sky)"),
    ("gold", "*“You returned to the Circle, and every constellation answered: their light now "
             "runs down your arm and out through the staff. Whatever stars you wear, the "
             "Warden's spear sweeps between danger and the party.”*"),
    ("img", "assets/characters/starlit_warden_mantle.png",
     "The Warden stands guard in Ursa's starlight.", 5.6, {"crop": "3:2", "hmax": 3.8}),
    ("stat", "Starlit Channeler (feat)", [
        "*Story Feat (Prerequisite: Starry Form Feature)*",
        "You gain the following benefits.",
        "**The Warden's Mantle.** You learn the Shillelagh cantrip, and Wisdom is your "
        "spellcasting ability for it. When you assume your Starry Form, you cast Shillelagh "
        "through your Staff of Waking Constellations as part of the same Bonus Action, and the "
        "spell lasts until the form ends rather than for 1 minute. While your Starry Form is "
        "active, whichever constellation you chose: the Staff's Starlight kindles with the form "
        "(no action required) and reaches 20 feet, and each ally within that light gains a +1 "
        "bonus to attack rolls and saving throws; the kindled staff deals Radiant damage, and "
        "when you hit with it, the target takes an extra 1d6 Radiant damage (this extra damage "
        "increases to 2d6 at Druid level 11 and 3d6 at Druid level 17); and the Warden, a "
        "spear-bearing figure of starlight, stands guard in your glow.",
        "**Warden's Intercession.** While your Starry Form is active, when a creature you can "
        "see hits an ally within your Starlight, you can take a Reaction to reduce the damage "
        "the ally takes by 1d8 plus your Wisdom modifier.",
        "**Constellation Gifts.** While your Starry Form is active, you also gain the benefit "
        "below for the constellation you chose.",
        "**Archer.** When you hit a creature with the Archer's luminous arrow, the arrow's "
        "light clings to it, and the next attack roll made against that creature before the "
        "start of your next turn has Advantage.",
        "**Chalice.** When the Chalice's light restores Hit Points, you can divide those Hit "
        "Points between two creatures within 30 feet of yourself.",
        "**Dragon.** Allies within your Starlight can treat a d20 roll of 9 or lower as a 10 "
        "on Constitution saving throws to maintain Concentration.",
    ]),
    ("dm", "The kindled staff IS the Shillelagh spell, so Starseed (+1d4) rides its strikes "
           "once per turn (house rule 1; never the Archer's arrow), and its damage counts as "
           "cantrip damage (Potent Spellcasting applies from Druid level 7, once per turn, "
           "house rule 2). The Warden is no longer a fourth constellation to pick: the mantle "
           "rides every form (DM ruling 2026-07-13). Sheet note: the feat grants Shillelagh, "
           "so Ursa's known copy frees up for a swap."),
    ("stat", "The Staff Wakes Further", [
        "*The relic grows, as promised.* "
        "The Staff of Waking Constellations has always brightened a new star after every "
        "victory; on this road, it brightens for him. It is the vessel the Warden shines "
        "through: when the constellation widens its Starlight to 20 feet, it is this staff "
        "carrying the light, and the whole party fits inside it. The staff now has 6 charges "
        "and regains 1d4 + 2 expended charges daily at dawn.",
    ]),

    ("h2", "Reader of Omens: The Father's Trail (the road east)"),
    # The Dreamed Day plate (DM-approved 2026-07-13) replaces the generic
    # portrait from the 2026-07-09 whitespace pass: door-specific art wins.
    ("gold", "*“Your father read the sky the way other folk read a map. On his trail you "
             "learned his art: the omens no longer come at random, and you choose your "
             "moment.”*"),
    ("img", "assets/characters/reader_omen_dreams.png",
     "At dawn the stone dreams the day to come.", 5.6, {"crop": "3:2", "hmax": 3.8}),
    # [DM CHECK: Shared Tides says "a number of times equal to your Wisdom modifier" without
    # the SRD's "(minimum of once)". The PHB Cosmic Omen base feature carries the minimum, so
    # adding it would match the underlying feature, but it touches a floor mechanic, so it is
    # flagged for a DM decision rather than fixed silently.]
    ("stat", "Reader of Omens (feat)", [
        "*Story Feat (Prerequisite: Cosmic Omen Feature)*",
        "You gain the following benefits.",
        "**Omen Dreams.** When you finish a Long Rest, roll two d20s and record the numbers "
        "rolled. These are your omens for the day. When you or a creature you can see is about "
        "to make a D20 Test, you can replace the d20 roll with one of your omens (no action "
        "required). You must choose to do so before the roll, and you can use each omen only "
        "once. When you finish a Long Rest, you lose any unused omens.",
        "**Both Omens.** When you consult your Star Map after finishing a Long Rest, you don't "
        "roll for a single omen. Instead, you gain access to both Weal and Woe until your next "
        "Long Rest.",
        "**Read the Moment.** When you take the Reaction granted by your Cosmic Omen feature, "
        "you can wait until after the d20 is rolled but before you know whether the roll "
        "succeeds or fails. You then choose whether to apply Weal or Woe.",
        "**The Stronger Tide.** Your omens run deeper than an ordinary star-reader's. Weal now "
        "adds 1d6 + 2 to the roll, and Woe subtracts 1d6 + 2 from it.",
        "**Awakened Gifts.** The road east wakes what you already carry. Your Staff of Waking "
        "Constellations becomes a +2 quarterstaff and its Starseed rises from 1d4 to 1d8; your "
        "Amulet of Guiding Light sheds its bonus to every ally within 30 feet of you rather than "
        "only to those standing in its light.",
        "**Shared Tides.** Your uses of Cosmic Omen remain a single pool: you can use the "
        "feature a number of times equal to your Wisdom modifier, expending one use on either "
        "Weal or Woe, and you regain all expended uses when you finish a Long Rest.",
    ]),
    ("dm", "Cosmic Omen is the Circle of Stars feature Ursa gained at Druid level 6."),
    ("body", "Woe lands after the die is cast: turning an enemy's save into a failure at the "
             "perfect moment feels like fate itself."),
    ("body", "The dreamed day has its own table craft: when an omen is spent, Ursa's player "
             "speaks the dreamed number aloud before the die would fall. “I dreamed this. The "
             "arrow lands on a 3.” Watching the world obey the dream is the whole art."),
    ("stat", "Ash's Sigil-Stone", [
        "*Wondrous Item, Rare (Requires Attunement by Ursa)*",
        "A river-smooth stone etched with a half-finished sigil of Elaria, in Ash's own hand. "
        "Recovered on the trail, it sits warm in the palm whenever it is carried east. Cast "
        "between fights, it knits the party whole and kindles Ursa's Chalice splash besides. "
        "One day, when the sigil is finished, it may wake.",
        "While holding the stone, you can cast Aura of Vitality from it without expending a "
        "spell slot. Once this property is used, it can't be used again until you finish a "
        "Long Rest.",
        "**The Stone Looks Ahead.** The stone has 2 charges and regains all expended charges "
        "daily at dawn. As a Magic action, you can expend 1 charge to do one of the following.",
        "**Ask the Day.** Ask the DM one yes-or-no question about the day ahead. You receive a "
        "truthful “yes” or “no,” or silence if the answer cannot be known.",
        "**Glimpse the Trail.** Learn what waits on one unrevealed rift-board space within 1 "
        "mile.",
        "**Read the Heart.** Learn a visible creature's emotional state and attitude toward "
        "the party.",
        "With the Staff and the Amulet, the Stone closes Ursa's third and final attunement "
        "slot.",
    ]),
    ("dm", "The Session 12 clue rides here."),
    ("body", "Ursa gains the one road he walked, feat and keepsake together. The other two roads "
             "remain: the stars are patient, and the wild does not forget him."),

    # ------------------------------------------------------------------
    # GLIMMERSTONE ARTIFACTS: full text of glimmerstone_artifacts_v2.pdf
    # ------------------------------------------------------------------
    ("h1", "Glimmerstone Artifacts (Lilly's Path)", {"hardbreak": True}),
    ("gold", "One weapon and one mastery, forged for Lilly Glimmergear in the year apart. "
             "Wherever her road leads, Poots's parting work finds her: Boomstick, the sidearm no "
             "Level 7 Artillerist walks into the rifts without. On top of the gun, the year "
             "teaches her a single mastery of three: stay and build the portal (Sentinel "
             "Protocol), go home to Glimmerspire and Poots (Stormgunner), or give the year to "
             "mote research (Aether Channeler). The mastery is hers, learned into hand and mind, "
             "not an item on her belt, so her attunements stay free for the Pocket Dynamo and "
             "whatever the rifts yield. The Frostbite Shard retires to her belt, a keepsake and "
             "one day a gift."),

    ("h2", "Boomstick, Poots's Parting Work"),
    ("imgfloat", "assets/items/boomstick.png", 2.2),
    ("gold", "*“It doesn't jam. It doesn't misfire. It simply states its opinion, loudly.”*"),
    ("body", "Whichever road Lilly walks, a parcel finds her, wrapped in waxed paper and string, "
             "postmarked Glimmerspire. Boomstick becomes her spellcasting focus and her "
             "designated Arcane Firearm (an artificer designates only one). With her shield in "
             "the other hand, her hands are exactly full: pistol, shield, and nothing wasted. "
             "Its clockwork drum conjures its own rounds, so Lilly will never want for ammunition "
             "again."),
    ("stat", "Boomstick", [
        "*Weapon (Repeating Pistol), Very Rare*",
        "**Repeating Pistol, +2.** You gain a +2 bonus to attack rolls and damage rolls made "
        "with this magic weapon, which deals 1d10 Thunder damage on a hit. The weapon requires "
        "no ammunition and never needs reloading.",
        "**Spell Focus and Arcane Firearm.** While holding Boomstick, you can use it as a "
        "Spellcasting Focus for your Artificer spells, and it is your designated Arcane Firearm. "
        "When you cast an Artificer spell through Boomstick, you can add 1d8 to one of the "
        "spell's damage rolls; the extra damage is Thunder damage.",
        "*Forged by the masters of Glimmerstone.*",
    ]),

    ("h2", "Stormgunner (the Glimmerspire Road)"),
    ("gold", "*“Gearhaven runs on lightning. So does she, now.”*"),
    ("img", "assets/characters/lilly_stormcharged.png",
     "Poots's brightest student, and the bottled lightning of Glimmerspire.", 5.6,
     {"crop": "3:2", "hmax": 3.8}),
    ("body", "On this road Lilly goes home to Glimmerspire, and the masters open the deep "
             "workshops for Poots's brightest student. What she brings back is not a device but "
             "a way of shooting: Boomstick becomes an extension of her own hand, stormcharged."),
    ("stat", "Stormgunner", [
        "*Path Feat (chosen in the year apart; requires Boomstick)*",
        "**War-Trained.** You have Advantage on Constitution saving throws you make to maintain "
        "Concentration, and you can perform the Somatic components of your Artificer spells even "
        "when you have Boomstick or a Shield in one or both hands.",
        "**Storm-Arc.** When you hit a creature with Boomstick, that creature takes an extra 1d6 "
        "Lightning damage, and the lightning arcs from it to up to two other creatures of your "
        "choice within 15 feet of it. Each arced creature makes a Dexterity saving throw against "
        "your spell save DC, taking 2d6 Lightning damage on a failed save or half as much damage "
        "on a successful one.",
        "**Counter-Bolt (twice per Long Rest).** When a creature you can see within 60 feet of "
        "you makes an attack roll against one of your allies, you can take a Reaction to fire "
        "Boomstick into the attack. The triggering attack roll has Disadvantage, and you make "
        "one attack with Boomstick against the attacker; on a hit, the target takes an extra "
        "1d10 Lightning damage.",
        "**Overloaded Shot (twice per Long Rest).** When you hit a creature with Boomstick, you "
        "can overload the shot to deal an extra 1d10 Lightning damage; the target must succeed "
        "on a Constitution saving throw against your spell save DC or have the Stunned condition "
        "until the end of your next turn.",
        "*A way of shooting learned in the workshops of Glimmerstone.*",
    ]),

    ("h2", "Aether Channeler (the Mote-Research Road)", {"hardbreak": True}),
    ("imgfloat", "assets/items/awakened_essence_sphere.png", 2.4),
    ("gold", "*“It was never a keepsake. It was a key, and it is finally awake.”*"),
    ("body", "Lilly gives the year to the Sphere, and the Sphere gives it back. It has spent the "
             "whole journey quietly pulling loose motes from the air; now she learns to spend "
             "what it has gathered. It begins with Aether Ward alone, and as the party clears "
             "each elemental rift and installs its pure Mote, the Sphere learns that plane's "
             "mighty discharge: five distinct answers on a strict budget, each the size of a "
             "spell she has no slot to cast, two of them burning for a full minute while her "
             "hands stay free for the cannon."),
    ("stat", "Aether Channeler", [
        "*Path Feat (chosen in the year apart)*",
        "**Mote Channeling.** You awaken the Essence Sphere you carry. Its powers share a pool "
        "of 2 uses, and you regain all expended uses when you finish a Short Rest. You start "
        "with the Aether Ward power, and you gain one Elemental Discharge each time a rift's "
        "Mote is installed in the Sphere (Ignis, Unda, Aer, Terra, Umbra). If a power requires "
        "a saving throw, the DC equals your spell save DC.",
        "**Aether Ward.** As a Magic action, expend 1 use to release the gathered motes as a "
        "protective shell: you and each ally within 30 feet of you gain Temporary Hit Points "
        "equal to 2d8 plus your Intelligence modifier.",
        "**Lingering Discharges.** A discharge that lasts 1 minute is sustained by the Sphere "
        "and doesn't require Concentration. The Sphere sustains only one lingering discharge at "
        "a time; activating another ends the first, and you can end one early (no action "
        "required).",
        "**Fire / Ignis, Cinderstorm.** As a Magic action, expend 1 use to unleash a firestorm "
        "in a 40-foot-radius Sphere centered on a point within 120 feet of yourself. Each "
        "creature there makes a Dexterity saving throw, taking 8d6 Fire damage on a failed save "
        "or half as much on a success. Until the start of your next turn the area is Difficult "
        "Terrain, and a creature that enters it for the first time on a turn or starts its turn there takes 2d6 Fire damage.",
        "**Water / Unda, the Drowning Lull.** As a Magic action, expend 1 use to fill a "
        "20-foot-radius Sphere within 120 feet with the shimmer of deep water. Each creature "
        "there must succeed on a Wisdom saving throw or have the Incapacitated condition and a "
        "Speed of 0 for 1 minute, standing entranced. It ends early for a creature that takes "
        "damage or is shaken awake by an ally's action within 5 feet.",
        "**Air / Aer, Tailwind.** As a Magic action, expend 1 use to send a following wind about "
        "your allies. For 1 minute, you and any number of allies within 30 feet of you gain a "
        "+2 bonus to attack rolls and saving throws, and your Speeds increase by 10 feet.",
        "**Earth / Terra, Tectonic Slam.** As a Magic action, expend 1 use to erupt the ground "
        "in a 20-foot-radius Sphere within 120 feet. Each creature there must succeed on a "
        "Dexterity saving throw or take 7d8 Force damage and have the Prone condition. Until the "
        "start of your next turn the raised stone is Difficult Terrain, a creature takes 5 "
        "Piercing damage for every 5 feet it moves there, and you and your allies have Half "
        "Cover while in the area.",
        "**Shadow / Umbra, Soul Siphon.** As a Magic action, expend 1 use to target one creature "
        "within 60 feet. It makes a Constitution saving throw, taking 8d6 Necrotic damage on a "
        "failed save or half as much on a success. You, or an ally within 30 feet of you, "
        "regains Hit Points equal to half the Necrotic damage dealt.",
    ]),

    ("h2", "Sentinel Protocol (the Portal Road)"),
    ("gold", "*“An upgraded Eldritch Cannon, rebuilt at the bench into a faithful guardian.”*"),
    ("body", "On this road Lilly stays in Gearhaven and builds beside Vane, and her Eldritch "
             "Cannon grows up. It walks on its own, blasts or shields on her command, and never "
             "makes her choose just one mode again."),
    ("statblock", {
        "name": "The Sentinel",
        "type": "Medium Construct (your Eldritch Cannon, rebuilt; granted by the Sentinel Protocol feat)",
        "ac": "18",
        "hp": "5 + five times your Artificer level (40 at Level 7); it has a number of d8 Hit "
              "Dice equal to your Artificer level",
        "speed": "30 ft.",
        "abilities": {"STR": 14, "DEX": 10, "CON": 16, "INT": 4, "WIS": 12, "CHA": 6},
        "immunities": "Poison",
        "condition_immunities": "Charmed, Exhaustion, Poisoned",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "languages": "understands the languages you know",
        "img": "assets/items/upgraded_eldritch_cannon.png",
        "traits": [
            ("Rebuilt Cannon", "The Sentinel is your Eldritch Cannon in a new form: when you "
                               "would create your Eldritch Cannon, you can create the Sentinel "
                               "instead. Anything that improves your cannon still applies to it, "
                               "the Pocket Dynamo included, so you deploy or recall the Sentinel "
                               "as a Bonus Action for no spell slot, it has no maximum duration, "
                               "and its Force Blast and Electric Pulse gain the Dynamo's +2 "
                               "damage. Casting Mending on the Sentinel restores 2d6 Hit Points; "
                               "if it drops to 0 Hit Points, you can rebuild it by expending a "
                               "level 1+ spell slot."),
            ("Bound Construct", "Add your Proficiency Bonus to any ability check or saving throw "
                                "the Sentinel makes."),
        ],
        "actions": [
            ("Activate", "As a Bonus Action, you can activate the Sentinel; it moves up to 30 "
                         "feet and takes one of the following actions of your choice."),
            ("Force Blast", "Ranged Attack Roll: your spell attack modifier, range 120 ft. Hit: "
                            "2d8 + your Intelligence modifier Force damage (+2 from the Pocket "
                            "Dynamo while attuned)."),
            ("Electric Pulse", "Dexterity Saving Throw: your spell save DC, each creature of "
                               "your choice within 15 feet of the Sentinel. Failure: 2d8 + your "
                               "Intelligence modifier Lightning damage (+2 from the Pocket "
                               "Dynamo while attuned), and the target can't "
                               "take Reactions until the start of your next turn. Success: Half "
                               "damage."),
        ],
        "reactions": [
            ("Guardian Protocol (1/Round)", "Trigger: An ally within 15 feet of the Sentinel "
                                            "takes damage. Response: The ally gains 1d8 + your "
                                            "Intelligence modifier Temporary Hit Points."),
        ],
    }),
    ("body", "**Why this is an upgrade.** The old cannon made Lilly choose a mode; the Sentinel "
             "walks on its own 30 feet, then blasts or pulses on her Bonus Action (her pick "
             "every time), and shields her friends as a Reaction in the same round. Her old kit "
             "lives on inside it: the Force Ballista became the Force Blast, the Storm mode "
             "became the Electric Pulse, and the Protector stands watch as Guardian Protocol. "
             "The Flamethrower was traded for lightning, Gearhaven's own element. Rebuilt at the "
             "bench in Gearhaven, from the masters' own designs."),

    ("h1", "Marks & Mysteries"),
    ("body", "**Ursa's Mark of Handling.** A dragonmark that woke when he was six: it prickles near "
             "frightened animals, grants Speak with Animals and Animal Friendship, and has become "
             "the channel through which sleeping and possessed things speak to him (Pikachu, the "
             "Grand Custodian). It has never once stirred for a machine."),
    # Closing vignettes. Whitespace pass 2026-07: as the part's last block at
    # 3.05in the square pair overshot the page foot and jumped whole to a
    # nearly blank page (and at foot-fit sizes its trailing spacer paragraph
    # spilled and stranded a fully blank page ahead of the Part IV
    # hardbreak). Anchored mid-section, between the mark and the star it
    # depicts, the row sits safely and the closing text seals the page foot.
    # (2.4in: at 2.7in the closing paragraph's last line still spilled and
    # stranded a near-blank page before the Part IV opener.)
    ("imgfloat", "assets/characters/ursa_with_amulet.png", 3.0),
    ("body", "**The seven-point star.** Elaria's sigil, wrapped in a leafed vine (or cupped in "
             "wings, on the Sash), found on every gift along the Guardians' path. When you see it, "
             "she saw you coming."),
    ("lore", "The Warden's Price",
     "Elaria spent her power the way a candle spends itself: all at once, on purpose, so "
     "others could see. When Maldrith was sealed beyond the last wall, the Warden had nothing "
     "left but her name and her sign, the seven-pointed star wrapped in a leafed vine. She "
     "scattered what remained into small safeguards and lay down to sleep, trusting the kind "
     "to find them. So far, the old tellings say, her trust has held."),
    ("lore", "The Warden's Watch",
     "Ask the Circle what Elaria is warden OF, and the old druids only point: at the turning "
     "planes, at the anchor-stars strung between them like a lantern-line, at the small safe "
     "things of the world that have no other reason to be safe. The tellings do not agree on "
     "why she sleeps. Some say the sealing emptied her to the last drop. Some say the sleep is "
     "itself the seal, and that waking her would open a door best left shut. The very oldest "
     "telling says she is not asleep at all, only listening, on a scale too slow and too deep "
     "for waking folk to follow. On one point every telling closes ranks: the stars her enemy "
     "puts out, her gifts relight. A staff kindles. A sash carries. A small bright core "
     "remembers. And somewhere beneath the turning of all seven planes, something that loves "
     "the world very much is dreaming it safe passage."),
    ("gold", "*“She is not gone,” the first druids wrote. “She is holding. When you carry her "
             "sign, hold with her.”*"),
    # Part III closes on a full-width showpiece of the Warden herself; Part IV
    # opens on its own hardbreak, so this plate fills the section-end page.
    ("img", "assets/world/elaria_goddess.png",
     "Elaria, the sleeping goddess who lit the way.", 6.5, {"crop": "1:1", "hmax": 6.7}),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    for blocks, out in ((I, "compendium/treasures_and_relics.docx"),
                        (C, "compendium/custom_compendium.docx")):
        print("built", build_doc(blocks, out))
