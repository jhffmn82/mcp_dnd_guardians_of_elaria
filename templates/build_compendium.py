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

    ("h1", "The Great Mysteries", {"pagebreak": True}),
    ("h2", "The Essence Sphere"),
    ("imgfloat", "assets/items/essence_sphere.png", 2.6),
    ("body", "Brass and crystal, warm as a heartbeat, made by the deep-gnome masters of Glimmerspire "
             "BEFORE the cracks ever opened (how they knew is a question nobody has answered). It "
             "holds Pikachu's sleeping spark, and it is a GATHERER: it pulls loose planar motes to "
             "itself and survives holding them, which no other vessel can. It is the missing anchor "
             "of Vane's Rift Portal, and it never leaves the party's keeping. Gained **Planar "
             "Attunement** at the Whispering Glade (advantage on Arcana concerning planar magic)."),
    ("h2", "The Three Enchanted Potatoes"),
    ("imgfloat", "assets/items/three_potatoes.png", 2.6),
    ("body", "Ash Catchum's legacy to his son: three unassuming potatoes that are anything but. The "
             "goddess named them **remnants of a shattered covenant**, safeguards bound from her own "
             "essence in the old lore (Healing, Transformation, Insight). They pulse when the world "
             "thins. Their hour has not yet come."),
    # Refit note (0.9in bottom margin): the Idol's float straddled the page-1
    # foot at any size; break so the entry rides page 2 whole.
    ("pagebreak",),
    ("h2", "Stabby's Idol"),
    ("imgfloat", "assets/items/stabbys_doll.png", 2.2, "left"),
    ("body", "A small carved figure Stabby found tucked in his bag after Wraithpine, though nobody "
             "saw who put it there. It goes ice cold near rifts, and corruption recoils from it. It "
             "has dreams in it. That is all anyone knows, yet."),

    ("h1", "Relics of Elaria (the Wraithpine Chest)", {"pagebreak": True}),
    ("body", "One half-buried chest, bound in vines of silver and root, opened by Ghostbloom's song "
             "beneath the Old Theater. Inside, three gifts, each bearing the seven-point star."),
    ("img", "assets/items/wraithpine_chest.png", "The Wraithpine chest, bound in silver vines.", 3.4),
    ("h2", "Staff of Waking Constellations (Ursa)"),
    ("stat", "Staff of Waking Constellations", [
        "+1 quarterstaff, druidic focus. 5 charges, regain 1d4 + 1 at dawn: guiding bolt (1), faerie fire (1), moonbeam (2).",
        "**Starseed.** Once per turn, +1d4 radiant when Ursa deals radiant damage with a druid spell (house rule: druid spells only).",
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

    ("h1", "Gifts of Faelan (Havenmoor, Session 4)", {"pagebreak": True}),
    ("h2", "Frostbite Shard Dagger (Lilly)"),
    ("stat", "Frostbite Shard Dagger", [
        "Rare, attunement by an Artificer. Crystalline ice that never melts. 1d4 piercing + 1d4 cold, +1 to attack.",
        "**Spell focus and Arcane Firearm.** +1d8 frost to one spell damage roll cast through it; +2 frost on spell damage.",
    ]),
    ("h2", "Amulet of Guiding Light (Ursa)"),
    ("stat", "Amulet of Guiding Light", [
        "Rare, attunement by a Circle of Stars druid.",
        "**Guiding Light.** Sheds light; allies gain +1 to attacks and saves while Ursa is in Starry Form.",
        "**Starry Glow.** Reaction, 1/long rest: 2d8 radiant, DC 15 Con or blinded. **Celestial Resilience.** Reroll natural 1s, 2/long rest.",
    ]),
    ("h2", "Candyfang Katana (Stabby)"),
    ("stat", "Candyfang Katana", [
        "Rare, attunement by a Monk. A katana of impossible candy-cane steel. 1d8/1d10 slashing, +1 attack and damage.",
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
]

# ----------------------------------------------------------------------
# VOLUME III: CUSTOM CONTENT (feats, subclasses, house rules)
# ----------------------------------------------------------------------
C = [
    title("THE CUSTOM COMPENDIUM", "Subclasses, Paths & House Rules"),
    ("gold", "Homebrew and rulings of this table: the heroes as they stand at the table, the paths "
             "they may walk after the year apart, and the standing rules of the campaign. 2024 "
             "rules throughout; house rules override the books."),

    ("h1", "The Guardians at the Table"),
    ("body", "The chronicle's front matter tells you who the Guardians are; this page tells you "
             "what they roll. All three stand at level 5 at the close of the Gearhaven chapter."),
    ("h2", "Lilly Glimmergear"),
    ("dm", "**Level 5 Artificer (Artillerist).** Her Eldritch Cannon deploys as a free action via "
           "the Glimmerspire Pocket Dynamo Mk II and runs all day. Signature gear: the Essence "
           "Sphere, the Frostbite Shard Dagger.", {"size": 11}),
    ("slots", "lilly", [("Spell Slots, 1st Level", 4), ("Spell Slots, 2nd Level", 2)]),
    ("h2", "Stabby Sharpblade"),
    ("dm", "**Level 5 Monk (Kensei).** No spell slots; he runs on Focus Points, all back on a "
           "short rest (Flurry of Blows, Stunning Strike, Patient Defense, Step of the Wind). "
           "Signature gear: the Candyfang Katana, the Sash of the Swift Current.", {"size": 11}),
    ("slots", "stabby", [("Focus Points", 5)]),
    ("h2", "Ursa Catchum"),
    ("dm", "**Level 5 Druid (Circle of the Stars).** About eight free Guiding Bolts a day from the "
           "Star Map and the Staff of Waking Constellations' charges. Signature gear: the Staff, "
           "three enchanted potatoes.", {"size": 11}),
    ("slots", "ursa", [("Spell Slots, 1st Level", 4), ("Spell Slots, 2nd Level", 3), ("Spell Slots, 3rd Level", 2)]),

    ("h1", "House Rules & Standing Rulings", {"pagebreak": True}),
    ("body", "1. Ursa's Starseed +1d4 applies only to actual druid spells, never the Starry Form "
             "Archer's luminous arrow."),
    ("body", "2. Patient Defense grants a free Disengage (add Dodge by spending 1 Focus)."),
    ("body", "3. Shillelagh replaces Primal Savagery on Ursa's sheet (2024 rules)."),
    ("body", "4. Goodberry: eating a berry is a Bonus Action (2024)."),
    ("body", "5. Ursa's summoned Air spirit has 20 HP."),
    ("body", "6. Deep gnome uses the current 2024-era printing (Svirfneblin Camouflage, Disguise "
             "Self and Nondetection 1/long rest each)."),
    ("body", "7. Lilly's cannon picks its mode on EVERY activation (Forge of the Artificer rule)."),
    ("body", "8. Potent Spellcasting rides the kindled staff once per turn (Ursa, from level 7)."),

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

    # ------------------------------------------------------------------
    # WARRIOR OF BREATHING: full text of warrior_of_breathing_v2.pdf
    # ------------------------------------------------------------------
    ("h1", "Warrior of Breathing (Stabby's Path)", {"pagebreak": True}),
    ("body", "A homebrew monk subclass taken at level 7 in place of Kensei. A Warrior of Breathing "
             "kindles an inner style, a visible breath that wreathes the blade. Three doors, three "
             "breathing styles; every road grants the **Nichirin Katana**, and every First Form "
             "replaces Flurry of Blows. The full text of all three follows."),

    ("h2", "Beast Breathing: the Bloodfang Form"),
    ("gold", "*“You think too much, little storm. The beast does not think. The beast moves, "
             "and the beast is already behind you.”* (the lesson Stabby finally understood)"),
    ("imgfloat", "assets/characters/stabby_breathing_style_red.png", 2.4),
    ("body", "Some warriors learn to still the storm inside them. The Warrior of Beast Breathing "
             "learns to ride it. Where other monks seek calm, this form reaches into the wild, "
             "animal heart of the fighter: the part that does not hesitate, does not flinch, and "
             "does not stop. Practitioners breathe in time with a racing heartbeat rather than a "
             "slow one, and when they ignite their breath, their blade glows blood-red and their "
             "body moves with the loping, unstoppable grace of a hunting beast."),
    ("body", "It is a form born of survival rather than discipline, favored by those who grew up "
             "where the strong eat and the slow are eaten. To master it is not to tame the beast, "
             "but to become it on command, and to remember how to set it down again afterward."),
    ("body", "**Features by monk level:** 3rd, Beast Breathing; 6th, First Form: Devour; 11th, "
             "Advanced Beast Breathing; 17th, Third Form: Apex Predator."),
    ("stat", "Level 3: Beast Breathing", [
        "**Monk Weapons.** A katana (and any sword you take up as your signature blade) counts as "
        "a Monk weapon for you. You can use your Martial Arts die with it, make your Bonus Action "
        "Unarmed Strikes alongside it, and use this subclass's features through it.",
        "**Beast Sense.** Your senses are sharp as a hunting animal's, even out of combat. You "
        "have Advantage on Wisdom (Survival) checks made to track creatures, on Wisdom "
        "(Perception) checks that rely on smell or hearing, and on Charisma (Intimidation) checks.",
        "**Igniting the Breath.** When you roll Initiative, you can expend 1 Focus Point to ignite "
        "your breath for the rest of the combat. It lasts until the combat ends, you have the "
        "Incapacitated condition, or you end it (no action required). While your breath is "
        "ignited, your weapon glows blood-red and deals an extra 2 Force damage on every hit.",
        "**Beast's Vigor.** While your breath is ignited, your Speed increases by 10 feet and you "
        "have Advantage on Dexterity saving throws: the wild reflexes of a cornered animal.",
    ]),
    ("stat", "Level 6: First Form: Devour", [
        "**First Form: Devour.** As a Bonus Action, you can expend 1 Focus Point to move up to 15 "
        "feet without provoking Opportunity Attacks and make one attack with your Monk weapon. On "
        "a hit, the attack deals 3d8 plus your Dexterity modifier Force damage. If this attack "
        "reduces the target to 0 Hit Points, you regain the expended Focus Point. This feature "
        "replaces Flurry of Blows for you.",
    ]),
    ("stat", "Level 11: Advanced Beast Breathing", [
        "**Advanced Breathing.** Your ignited breath grows fiercer. While it is active you gain "
        "all its original benefits, and you also have Resistance to Bludgeoning, Piercing, and "
        "Slashing damage. In addition, your weapon's bonus damage increases from 2 to 3.",
        "**Sharpened Fang.** The damage of your First Form: Devour increases to 5d10 plus your "
        "Dexterity modifier.",
    ]),
    ("stat", "Level 17: Third Form: Apex Predator", [
        "**Third Form: Apex Predator.** As a Bonus Action, you can expend 3 Focus Points to "
        "become a blur of fang and steel. Move up to your Speed without provoking Opportunity "
        "Attacks and make one attack with your Monk weapon against each of up to three different "
        "creatures you move within reach of. Each attack deals 5d10 plus your Dexterity modifier "
        "Force damage on a hit, and each creature hit must succeed on a Strength saving throw or "
        "have the Prone condition. For each creature reduced to 0 Hit Points, you regain 1 "
        "expended Focus Point.",
    ]),
    ("body", "**At Level 7, Stabby has:** Beast Breathing (the Level 3 stance) + First Form: "
             "Devour (Level 6, 3d8 + Dex). The Level 11 and 17 features unlock as he grows."),

    ("h2", "Water Breathing: the Monastery Form"),
    ("gold", "*“Be water. Water does not strike; it flows, and the rock is cut all the same. "
             "Now breathe, and begin again.”* (Master Kaelon Windstep)"),
    ("imgfloat", "assets/characters/stabby_breathing_style_water.png", 2.4),
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
    ("body", "**Features by monk level:** 3rd, Water Breathing; 6th, First Form: Flowing Strike; "
             "11th, Advanced Water Breathing and Healing Spring; 17th, Third Form: Tidal Crash."),
    ("stat", "Level 3: Water Breathing", [
        "**Monk Weapons.** A katana (and any sword you take up as your signature blade) counts as "
        "a Monk weapon for you. You can use your Martial Arts die with it, make your Bonus Action "
        "Unarmed Strikes alongside it, and use this subclass's features through it.",
        "**Igniting the Breath.** When you roll Initiative, you can expend 1 Focus Point to ignite "
        "your breath for the rest of the combat. It lasts until the combat ends, you have the "
        "Incapacitated condition, or you end it (no action required). While your breath is "
        "ignited, your weapon glows pale blue and deals an extra 2 Cold damage on every hit.",
        "**Flowing Guard.** While your breath is ignited, you gain a +2 bonus to Armor Class "
        "against the first attack roll made against you before the start of each of your turns: "
        "an ever-moving guard that turns the first blow aside.",
    ]),
    ("stat", "Level 6: First Form: Flowing Strike", [
        "**First Form: Flowing Strike.** As a Bonus Action, you can expend 1 Focus Point to shift "
        "up to 15 feet without provoking Opportunity Attacks and make one attack with your Monk "
        "weapon. On a hit, the attack deals 3d8 plus your Dexterity modifier Cold damage, and the "
        "target must succeed on a Dexterity saving throw or have the Prone condition as the "
        "current sweeps its feet. This feature replaces Flurry of Blows for you.",
    ]),
    ("stat", "Level 11: Advanced Water Breathing", [
        "**Advanced Breathing.** Your ignited breath deepens. While it is active you gain all its "
        "original benefits, and also: whenever you hit a creature with your Monk weapon, that "
        "creature's Speed is reduced by 10 feet until the start of your next turn as the cold "
        "seeps into its limbs.",
        "**Sharpened Flow.** The damage of your First Form: Flowing Strike increases to 5d10 plus "
        "your Dexterity modifier.",
        "**Healing Spring.** Once per Long Rest, you can take a Bonus Action to touch a creature "
        "(or yourself) and channel the still water's mending. The target regains 4d8 plus your "
        "Wisdom modifier Hit Points.",
    ]),
    ("stat", "Level 17: Third Form: Tidal Crash", [
        "**Third Form: Tidal Crash.** As a Bonus Action, you can expend 3 Focus Points to shift "
        "up to 20 feet and make one attack with your Monk weapon against each of up to three "
        "different creatures within your reach as you flow among them. Each attack deals 5d10 "
        "plus your Dexterity modifier Cold damage on a hit, and each creature hit must succeed on "
        "a Dexterity saving throw or have the Prone condition and its Speed becomes 0 until the "
        "end of its next turn, frozen in place by the flood.",
    ]),
    ("body", "**At Level 7, Stabby has:** Water Breathing (the Level 3 stance) + First Form: "
             "Flowing Strike (Level 6, 3d8 + Dex). The Level 11 and 17 features unlock as he grows."),

    ("h2", "Shadow Breathing: the Idol Form"),
    ("gold", "*“Do not fear the dark. Breathe it in. Let it fill you, and then there is "
             "nothing left in the dark to fear you.”* (a whisper from the idol)"),
    ("imgfloat", "assets/characters/stabby_breathing_style_shadow.png", 2.4),
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
    ("body", "**Features by monk level:** 3rd, Shadow Breathing; 6th, First Form: Umbral Slash; "
             "11th, Advanced Shadow Breathing; 17th, Third Form: Eclipse."),
    ("stat", "Level 3: Shadow Breathing", [
        "**Monk Weapons.** A katana (and any sword you take up as your signature blade) counts as "
        "a Monk weapon for you. You can use your Martial Arts die with it, make your Bonus Action "
        "Unarmed Strikes alongside it, and use this subclass's features through it.",
        "**Eyes of the Idol.** The idol's gift never fully leaves you. You have Darkvision with a "
        "range of 60 feet (if you already have Darkvision, its range increases by 60 feet), and "
        "you have Advantage on Dexterity (Stealth) checks; the gloom favors you.",
        "**Igniting the Breath.** When you roll Initiative, you can expend 1 Focus Point to ignite "
        "your breath for the rest of the combat. It lasts until the combat ends, you have the "
        "Incapacitated condition, or you end it (no action required). While your breath is "
        "ignited, your weapon glows violet-black and deals an extra 2 Necrotic damage on every hit.",
        "**One With the Gloom.** While your breath is ignited, the dark wraps around you: you have "
        "Half Cover (a +2 bonus to AC) against ranged attacks (anywhere, not just in shadow), and "
        "you can see normally in magical Darkness.",
    ]),
    ("stat", "Level 6: First Form: Umbral Slash", [
        "**First Form: Umbral Slash.** As a Bonus Action, you can expend 1 Focus Point to "
        "teleport up to 15 feet to an unoccupied space you can see next to a creature, engulf "
        "that creature in a 10-foot Cube of magical Darkness, and make one attack with your Monk "
        "weapon against it, with Advantage. On a hit, the attack deals 3d8 plus your Dexterity "
        "modifier Necrotic damage. The Darkness lasts until the end of your next turn. This "
        "feature replaces Flurry of Blows for you.",
    ]),
    ("stat", "Level 11: Advanced Shadow Breathing", [
        "**Advanced Breathing.** Your ignited breath drinks deeper of the dark. While it is "
        "active you gain all its original benefits, and also: once per turn, when you hit a "
        "creature with an attack roll you made with Advantage, the attack deals an extra 2d6 "
        "Necrotic damage.",
        "**Sharpened Gloom.** The damage of your First Form: Umbral Slash increases to 5d10 plus "
        "your Dexterity modifier.",
    ]),
    ("dm", "The gloom is his alone. Stabby sees through his own Darkness; his allies can't. "
           "Creatures wrapped in his gloom are hidden from Ursa's bolts and Lilly's cannon until "
           "the dark lifts, so the party learns to pick different targets while the shadow does "
           "its work."),
    ("stat", "Level 17: Third Form: Eclipse", [
        "**Third Form: Eclipse.** As a Bonus Action, you can expend 3 Focus Points to vanish "
        "into the gloom and strike from everywhere at once. Create a 20-foot Cube of magical "
        "Darkness centered on yourself (you can see through it), then teleport to and make one "
        "attack with your Monk weapon against each of up to three different creatures within it, "
        "with Advantage. Each attack deals 5d10 plus your Dexterity modifier Necrotic damage on a "
        "hit. Each creature hit has the Blinded condition until the end of your next turn, and "
        "you remain effectively unseen by everyone but yourself until the Darkness ends.",
    ]),
    ("body", "**At Level 7, Stabby has:** Shadow Breathing (the Level 3 stance) + First Form: "
             "Umbral Slash (Level 6, 3d8 + Dex). The Level 11 and 17 features unlock as he grows."),

    ("h2", "The Demon-Slayer's Blade: the Nichirin Katana"),
    ("body", "This sun-forged demon-slayer blade was made from crimson ore that drinks in "
             "dawnlight. While sheathed, the steel looks dark and almost ordinary, but when Stabby "
             "ignites his breathing, the blade catches that breath and burns with the color of his "
             "chosen form."),
    ("stat", "Nichirin Katana", [
        "*Weapon (Katana), Rare (Requires Attunement by Stabby)*",
        "**Weapon Statistics.** The Nichirin katana uses the statistics of a Longsword (1d8 "
        "Slashing damage) with the Finesse and Versatile (1d10) properties, and it counts as a "
        "Monk weapon for Stabby. Because it has Finesse and is a Monk weapon, Stabby uses his "
        "Dexterity for its attack and damage rolls.",
        "**Magic Weapon.** You gain a +2 bonus to attack and damage rolls made with this magic "
        "weapon.",
        "**Breath-Kindled Steel.** When Stabby ignites his breathing, the blade glows with the "
        "color and nature of that form: blood-red for Beast Breathing, pale blue for Water "
        "Breathing, or violet-black for Shadow Breathing. This glow is magical but sheds only dim "
        "light unless Stabby chooses otherwise.",
        "**Cleansing Edge.** Once on each of your turns when you hit a Fiend, Undead, shadow "
        "creature, or creature empowered by planar corruption with this katana, the blade burns "
        "away corruption until the start of your next turn. While affected, the creature can't "
        "regain Hit Points, can't benefit from magical Darkness or shadowy concealment against "
        "Stabby, and any visible corruption around the wound briefly burns, cracks, or peels away "
        "in sparks of purified light.",
        "**Demon-Slayer's Mark.** The katana is especially dangerous to creatures twisted by "
        "darkness, undeath, or planar corruption. It leaves wounds that glow faintly like banked "
        "embers, revealing that the creature has been marked by cleansing sunlight. The blade "
        "wounds the corruption, not the creature beneath. When a corrupted guardian falls to it, "
        "what breaks is the darkness.",
    ]),
    ("h2", "Lore of the Blade"),
    ("body", "They say the first Nichirin blades were quenched not in water or oil but in the "
             "light of dawn itself, folded by smiths who worked only in the hour before sunrise. "
             "The ore came from a single mountain that caught the morning sun before anywhere else "
             "in the world, and steel drawn from it never forgot that first warmth. A finished "
             "blade looks plain and dark in an idle hand; it is waiting. Only a warrior who can "
             "kindle their own breath can wake the colour sleeping in the metal."),
    ("body", "For a creature of corruption, that waking light is a death sentence. Where an "
             "ordinary sword cuts flesh, a Nichirin blade cuts the rot itself: the shadow that "
             "hides a fiend, the dark magic that knits an undead back together, the planar taint "
             "that lets a horror shrug off honest steel. Stabby's blade chose its colours from his "
             "own breathing forms, and now it burns red, blue, or violet to match whichever beast, "
             "river, or shadow he calls upon."),
    ("gold", "**A whispered rumor.** Old hunters claim a Nichirin blade can never be truly stolen: "
             "carried by the wrong hand, the steel stays cold and dull and will not take an edge. "
             "Whether that is true, or simply a story told to keep thieves honest, no one in "
             "living memory has dared find out."),
    ("h2", "Setting Down the Kensei's Way"),
    ("body", "When Stabby takes up a breathing form at Level 7, the Kensei's tricks retire with "
             "his old teacher's lessons. He loses Kensei's Shot (the bow's bonus-action +1d4) and "
             "Agile Parry (his +2 AC after blade-and-fist turns), and the Repeating Longbow "
             "becomes simply a very good bow, no longer a Monk weapon. In exchange he gains a "
             "stance he can ignite every single fight, a First Form that turns his bonus action "
             "into a 3d8 + 5 strike with 15 feet of free movement, form gifts that work all day, "
             "and a road that grows with him to Level 17. He is trading a parry for a predator's "
             "gait, and he gains far more than he gives up. (And Candyfang, outshone by the "
             "Nichirin blade, needn't vanish: an heirloom at his belt, or one day, a gift worthy "
             "of a Bloodfang.)"),

    # ------------------------------------------------------------------
    # PATHS OF THE STARS: full text of ursa_path_rewards_v2.pdf
    # ------------------------------------------------------------------
    ("h1", "Paths of the Stars (Ursa's Path)"),
    ("gold", "*For Ursa Catchum, Circle of the Stars Druid: the year apart, Level 5 to 7.* "
             "Ursa walked one of three roads during the year apart, and came back changed. Each "
             "road grants a feat (what he sought) and a keepsake (what found him): he gains the "
             "pair matching his road. Special story feats: no ability score increase."),

    ("h2", "Beast Handler: The Living World (the road into the wild)"),
    ("gold", "*“You went out to learn the speech of wild things. You came back, and the wild "
             "things follow you home.”*"),
    ("stat", "Beast Handler (feat)", [
        "**Mightier Summons.** Whenever you cast the Summon Beast spell, you cast it as though "
        "using a spell slot of the highest level you can cast, without expending a higher-level "
        "slot. (The spell's effects scale to that level, 4th now, and growing as Ursa does, but "
        "it still uses only a 2nd-level slot.)",
        "**Wild Speech.** You and your summoned creatures share simple thoughts freely, no words "
        "needed. With ordinary Beasts, you understand their sounds and gestures even without your "
        "Mark's magic, and they understand yours.",
    ]),
    ("stat", "The Wildheart Token", [
        "*Carved by his own hand.*",
        "A totem of a beast Ursa befriended in the wild year: the player names it, and names the "
        "friend. His Bestial Spirit now always takes that companion's shape. Once per day, when "
        "the spirit would drop to 0 hit points, it drops to 1 instead: it refuses to leave him.",
    ]),

    ("h2", "Starlit Channeler: The Circle of Stars (the road into the sky)"),
    ("gold", "*“You returned to the Circle, and the constellations answered: their light now "
             "runs down your arm and out through the staff.”*"),
    ("stat", "Starlit Channeler (feat)", [
        "**The Warden.** You learn the Shillelagh cantrip (Wisdom is your spellcasting ability "
        "for it), and your Starry Form gains a fourth constellation: the Warden, a spear-bearing "
        "figure of starlight. When you assume your form, you can choose it. As part of the same "
        "Bonus Action, you cast Shillelagh through your staff, and the spell lasts as long as the "
        "form does (instead of 1 minute). While the Warden shines: the kindled staff's damage "
        "becomes Radiant, its strikes deal an extra 1d6 Radiant damage (2d6 at 11th level, 3d6 at "
        "17th), and as a Bonus Action on each of your later turns, you can make one strike with "
        "the kindled staff.",
    ]),
    ("dm", "The kindled staff IS the Shillelagh spell: Starseed (+1d4) rides its strikes (unlike "
           "the Archer's arrow, a form feature), and its damage counts as cantrip damage "
           "(Elemental Fury: Potent Spellcasting applies from 7th, once per turn, like Starseed). "
           "Sheet note: the feat grants Shillelagh, so Ursa's known copy frees up for a cantrip "
           "swap at his next level."),
    ("stat", "The Staff Wakes Further", [
        "*The relic grows, as promised.* "
        "The Staff of Waking Constellations has always brightened a new star after every victory: "
        "on this road, it brightens for him. Capacity rises to 6 charges (regain 1d4+2 at dawn), "
        "and its Starlight glow reaches 20 feet: the whole party fits inside his Starry Form's "
        "light, and inside the Amulet of Guiding Light's +1 to attacks and saves.",
    ]),

    ("h2", "Reader of Omens: The Father's Trail (the road east)"),
    ("gold", "*“Your father read the sky the way other folk read a map. On his trail you "
             "learned his art: the omens no longer come at random, and you choose your "
             "moment.”*"),
    ("stat", "Reader of Omens (feat)", [
        "**Both Omens.** When you consult your Star Map after a Long Rest, you do not roll for a "
        "single omen. Instead, you gain access to both Weal and Woe until your next Long Rest.",
        "**Read the Moment.** You can wait to use your Cosmic Omen reaction until after the d20 "
        "is rolled, but before you know the outcome. You then choose whether to apply Weal (add "
        "1d6 to the roll) or Woe (subtract 1d6).",
        "**Shared Tides.** Your uses of Cosmic Omen remain a single pool equal to your Wisdom "
        "modifier (regaining all uses on a Long Rest). Spend each use on either Weal or Woe.",
        "*Prerequisite: the Cosmic Omen feature (gained at druid level 6).*",
    ]),
    ("stat", "Ash's Sigil-Stone", [
        "*Recovered on the trail. Attunement.*",
        "A river-smooth stone etched with a half-finished sigil of Elaria, in Ash's own hand. It "
        "sits warm in the palm when carried east. 1/long rest: cast Aura of Vitality from it "
        "without a spell slot, healing between fights (triggers his Chalice splash). One day, "
        "when the sigil is finished, it may wake.",
    ]),
    ("dm", "The S13 clue rides here."),
    ("body", "Ursa gains the one road he walked, feat and keepsake together. The other two roads "
             "remain: the stars are patient, and the wild does not forget him."),

    # ------------------------------------------------------------------
    # GLIMMERSTONE ARTIFACTS: full text of glimmerstone_artifacts_v2.pdf
    # ------------------------------------------------------------------
    ("h1", "Glimmerstone Artifacts (Lilly's Path)"),
    ("gold", "Three masterworks of deep gnome artifice, forged for Lilly Glimmergear in the year "
             "apart. Three masterworks, one choice. Each door of Lilly's year apart leads to one "
             "of these treasures: stay and build the portal (the Sentinel), go home to "
             "Glimmerspire and Poots (Boomstick), or give the year to mote research (the Awakened "
             "Sphere). She walks one road and claims one masterwork. The attunement ledger closes "
             "on every road: her Frostbite Shard, her Pocket Dynamo, and the new artifact make "
             "exactly three, and on the Sentinel's road it is only two, for the Dynamo itself is "
             "rebuilt into the guardian."),

    ("h2", "Boomstick"),
    ("gold", "*“It doesn't jam. It doesn't misfire. It simply states its opinion, "
             "loudly.”*"),
    ("imgfloat", "assets/items/boomstick.png", 2.4),
    ("body", "On this road, Boomstick takes the dagger's watch. Boomstick becomes Lilly's "
             "spellcasting focus and her designated Arcane Firearm (an artificer designates only "
             "one). With her shield in the other hand, her hands are exactly full: pistol, shield, "
             "and nothing wasted. The Frostbite Shard retires to her belt as a keepsake, or one "
             "day, a gift."),
    ("stat", "Boomstick", [
        "*Weapon (Repeating Pistol), Rare (Requires Attunement by an Artificer)*",
        "**Repeating Pistol, +2.** You gain a +2 bonus to attack and damage rolls made with this "
        "magic firearm. It deals 1d10 Thunder damage and never needs reloading or ammunition; its "
        "clockwork drum conjures its own rounds.",
        "**Wand of the War Mage.** While holding Boomstick, you gain a +2 bonus to spell attack "
        "rolls, and you ignore Half Cover when making a spell attack. This also improves your "
        "Eldritch Cannon's attack rolls, since they use your spell attack modifier.",
        "**Spell Focus and Arcane Firearm.** Boomstick serves as your artificer spellcasting "
        "focus and as your Arcane Firearm: you can add 1d8 to one damage roll of an artificer "
        "spell you cast through it, dealt as Thunder damage.",
        "**Concussion Infusion.** When a creature takes damage from a spell you cast through "
        "Boomstick, it takes an additional 2 Thunder damage and can't take Reactions until the "
        "start of its next turn (the disorienting boom).",
        "**Made to Channel.** When you cast True Strike through Boomstick, the shot uses your "
        "Intelligence, counts as a spell attack (gaining the +2 and ignoring Half Cover), and "
        "deals Boomstick's Thunder plus True Strike's Radiant. A reliable scaling shot that "
        "leaves your Bonus Action free for your cannon.",
        "*Forged by the masters of Glimmerstone.*",
    ]),

    ("h2", "The Awakened Essence Sphere"),
    ("gold", "*“It was never a keepsake. It was a key, and it is finally awake.”*"),
    ("imgfloat", "assets/items/awakened_essence_sphere.png", 2.4),
    ("body", "The Sphere has spent the whole journey quietly pulling loose motes from the air. "
             "Now awakened, it holds a swirling jumble of collected aether that powers it from "
             "the start, and as the party clears each elemental rift and installs its pure Mote, "
             "the Sphere learns that plane's mighty discharge."),
    ("stat", "The Awakened Essence Sphere", [
        "*Wondrous Item, Rare (Requires Attunement). Mote Channeling.*",
        "**Mote Channeling.** You can use the Sphere's powers a total of 2 times per Short Rest "
        "(a shared pool). You start with the base Aether Ward and unlock one elemental discharge "
        "each time you install a rift's Mote. Where a save is called for, the DC is your spell "
        "save DC.",
        "**Base Power: Collected Aether. Aether Ward.** Action. You and each ally within 15 feet "
        "gain 2d8 + your Intelligence modifier Temporary Hit Points as the gathered motes form a "
        "protective shell. (Available from the start.)",
        "**Rift Tracker.** Mark each Mote as it comes home: Ignis, Unda, Aer, Terra, Umbra. Five "
        "rifts, five discharges, and a Sphere that remembers every one.",
    ]),
    ("stat", "Elemental Discharges", [
        "*Each unlocks when its rift is cleared and its Mote installed. The menu grows as the "
        "campaign goes.*",
        "**Fire / Ignis, Cinderstorm (LOCKED).** Action. A 40-foot-radius firestorm within 120 "
        "feet. Each creature in the area makes a Dexterity saving throw, taking 8d6 Fire damage "
        "on a failed save, or half as much on a success. The area becomes burning terrain until "
        "the start of your next turn: difficult terrain, and any creature that enters it or "
        "starts its turn there takes 2d6 Fire damage.",
        "**Water / Unda, Drowning Surge (LOCKED).** Action. A 30-foot Cone of crushing water. "
        "Each creature in the Cone makes a Constitution saving throw, taking 6d8 Cold damage on a "
        "failed save, or half as much on a success. On a failure, the creature also has the Prone "
        "condition and its Speed is halved until the end of its next turn.",
        "**Air / Aer, Cyclone (LOCKED).** Action. A 30-foot-radius whirlwind within 120 feet. "
        "Each creature in the area makes a Strength saving throw, taking 6d8 Thunder damage on a "
        "failed save, or half as much on a success. On a failure, the creature is also flung 20 "
        "feet and has the Prone condition.",
        "**Earth / Terra, Tectonic Slam (LOCKED).** Action. A 20-foot-radius eruption within 120 "
        "feet. Each creature in the area makes a Dexterity saving throw, taking 7d8 Force damage "
        "on a failed save; creatures that fail also have the Prone condition. The area becomes a "
        "Jagged Field until your next turn: difficult terrain that deals 5 Piercing damage for "
        "every 5 feet a creature travels through it, and you and your allies in the area have "
        "Half Cover from the raised stone.",
        "**Shadow / Umbra, Soul Siphon (LOCKED).** Action. One creature within 60 feet (or split "
        "the dice among up to three). Each target makes a Constitution saving throw, taking 8d6 "
        "Necrotic damage on a failed save, or half as much on a success. You regain Hit Points "
        "(or grant them to an ally within 30 feet) equal to half the Necrotic damage dealt.",
    ]),

    ("h2", "The Sentinel"),
    ("gold", "*“An upgraded Eldritch Cannon, rebuilt at the bench into a faithful "
             "guardian.”*"),
    ("statblock", {
        "name": "The Sentinel",
        "type": "Medium Construct (the Pocket Dynamo, rebuilt; Requires Attunement by Lilly)",
        "ac": "18",
        "hp": "5 + five times your artificer level (40 at Level 7); it has a number of d8 Hit "
              "Dice equal to your artificer level",
        "speed": "30 ft.",
        "abilities": {"STR": 14, "DEX": 10, "CON": 16, "INT": 4, "WIS": 12, "CHA": 6},
        "immunities": "Poison",
        "condition_immunities": "Charmed, Exhaustion, Poisoned",
        "senses": "Darkvision 60 ft., Passive Perception 11",
        "languages": "understands the languages you know",
        "img": "assets/items/upgraded_eldritch_cannon.png",
        "traits": [
            ("Duration", "None: it stays until it drops to 0 Hit Points or you dismiss it (no "
                         "action required); deploy or recall it as a Bonus Action."),
            ("Bound Construct", "Add your Proficiency Bonus to any ability check or saving throw "
                                "the Sentinel makes."),
            ("Rebuilt Dynamo", "The Sentinel is Lilly's Eldritch Cannon feature, rebuilt: while "
                               "attuned, she deploys the Sentinel instead of a cannon (never "
                               "both). The Dynamo's gifts live on inside it: free deployment, no "
                               "duration, and a hotter frame: the old cannon threw 2d8 flat, the "
                               "Dynamo warmed that to 2d8+2, and the Sentinel's blasts now carry "
                               "her full Intelligence (2d8+5). Mending repairs it 2d6, and if it "
                               "ever drops to 0 Hit Points, she reboots it with a spell slot of "
                               "1st level or higher, just as a cannon is rebuilt."),
        ],
        "actions": [
            ("Activate", "On your turn you can use a Bonus Action to activate the Sentinel. When "
                         "you do, it takes one of the following actions of your choice."),
            ("Force Blast", "Ranged Attack Roll: your spell attack modifier, range 120 feet. "
                            "Hit: 2d8 + your Intelligence modifier Force damage."),
            ("Electric Pulse", "Lightning arcs from the Sentinel's core. Each creature of your "
                               "choice within 15 feet of the Sentinel makes a Dexterity saving "
                               "throw (DC equals your spell save DC), taking 2d8 + your "
                               "Intelligence modifier Lightning damage on a failure, or half as "
                               "much on a success. A creature that fails is jolted: it can't "
                               "take Reactions until the start of your next turn."),
        ],
        "reactions": [
            ("Guardian Protocol (1/round)", "Trigger: an ally within 15 feet of the Sentinel "
                                            "takes damage. Response: that ally gains 1d8 + your "
                                            "Intelligence modifier Temporary Hit Points."),
        ],
    }),
    ("body", "**Why this is an upgrade.** The old cannon made Lilly choose a mode; the Sentinel "
             "walks on its own 30 feet, then blasts or pulses on her Bonus Action (her pick every "
             "time), and shields her friends as a Reaction in the same round. Her old kit lives "
             "on inside it: the Force Ballista became the Force Blast, the Storm mode became the "
             "Electric Pulse, and the Protector stands watch as Guardian Protocol. The "
             "Flamethrower was traded for lightning, Gearhaven's own element. Forged by the "
             "masters of Glimmerstone."),

    ("h1", "Marks & Mysteries"),
    ("body", "**Ursa's Mark of Handling.** A dragonmark that woke when he was six: it prickles near "
             "frightened animals, grants Speak with Animals and Animal Friendship, and has become "
             "the channel through which sleeping and possessed things speak to him (Pikachu, the "
             "Grand Custodian). It has never once stirred for a machine."),
    ("body", "**The seven-point star.** Elaria's sigil, wrapped in a leafed vine (or cupped in "
             "wings, on the Sash), found on every gift along the Guardians' path. When you see it, "
             "she saw you coming."),
    # Closing vignettes share one row on the final page.
    ("imgrow", [("assets/characters/ursa_with_amulet.png",
                 "The seven-point star of Elaria, held close."),
                ("assets/world/elaria_goddess.png",
                 "Elaria, the sleeping goddess who lit the way.")], 3.05),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    for blocks, out in ((I, "compendium/treasures_and_relics.docx"),
                        (C, "compendium/custom_compendium.docx")):
        print("built", build_doc(blocks, out))
