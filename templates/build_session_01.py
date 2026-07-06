# build_session_01.py
# The Guardians of Elaria, Session 1: The Gathering of Friends
# Publication build. Canon: memory/campaign_canon.md + CONTRADICTIONS.md rulings.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
BLOCKS = [
    ("titlepage", "THE GUARDIANS OF ELARIA", "SESSION 1",
     "The Gathering of Friends",
     "An illustrated adventure. Read the gold boxes aloud; the purple boxes are for the DM."),

    ("h1", "Our Story Begins"),
    ("gold", "Far to the west, in a land called **Eldridge Vale**, the hills roll green and soft, "
             "and the roads wind between hedgerows and sleepy farms. Folk here live quiet lives. "
             "They mend fences, bake bread, and tell stories by the fire. But lately the stories "
             "have changed. Travelers speak of glowing creatures slipping between the trees of the "
             "**Forest of Whispers**, of winds that seem to murmur words, of lights where no lantern burns."),
    ("gold", "The old tales say the world is only one of many: that other realms turn beside ours "
             "like the wheels of a great clock, close enough to touch in the thin places. For a "
             "thousand years the clock has kept perfect time. Tonight, in a little village at the "
             "edge of a whispering wood, something slips."),
    ("gold", "Three young heroes are about to meet. None of them knows it yet, but the stars "
             "themselves have been waiting for this evening."),
    ("dm", "The heroes begin this chronicle at **level 3**. Full creature statistics for every "
           "session live in the compendium; a compact appendix closes each session."),
    ("img", f"{A}/scenes/s1_eldridge_village.png",
     "Eldridge Village at dusk, where our story begins.", 2.9),
    ("img", f"{A}/world/elaria_region_map.png",
     "Eldridge Vale and the lands of Elaria, as mapped by the cartographers of Gearhaven.", 3.0),

    # ------------------------------------------------------------------
    ("h1", "Part One: The Gilded Acorn", {"pagebreak": True}),
    ("gold", "The **Gilded Acorn Tavern** is the heart of Eldridge Village: a warm, golden room "
             "that smells of roasting meat and fresh bread. Wooden beams cross the ceiling, hunting "
             "trophies and faded banners line the walls, and a great stone hearth crackles against "
             "the evening chill. A minstrel strums a lute on the little stage in the corner. The "
             "tavern is crowded tonight, and every table hums with the same uneasy talk: the forest, "
             "the lights, the whispers."),
    ("gold", "Behind the bar stands **Osric the innkeeper**, broad shouldered and bushy bearded, "
             "his laugh booming over the noise. Between tables darts **Rhea the barmaid**, quick "
             "handed and quicker witted, hearing every rumor in the room twice before anyone "
             "finishes telling it."),
    ("img", f"{A}/scenes/s1_gilded_acorn_meeting.png",
     "The Gilded Acorn on the night three strangers became a party.", 4.0),

    ("h2", "Lilly's Arrival"),
    # Portrait floats right; intro paragraphs wrap around it.
    ("imgfloat", f"{A}/characters/lilly_with_essence_sphere_dalle.webp", 2.3),
    ("gold", "The tavern door opens on a traveler unlike any Eldridge has seen: a deep gnome girl, "
             "small even for her folk, with skin like polished slate, long silver hair, and striking "
             "red eyes. **Lilly Glimmergear** has walked a long way from **Deepforge Hollow**, and the "
             "surface world is almost too much: too bright, too loud, too wonderfully strange. She "
             "clutches a brass and crystal device to her chest, a sphere that hums softly, like "
             "something inside it is dreaming."),
    ("gold", "Her mother, the tinkerer **Poots Glimmergear**, pressed the **Essence Sphere** into her "
             "hands before she left. Inside it sleeps the spark of a creature called **Pikachu**, an "
             "old friend trapped without a body. *Find Ursa Catchum*, her mother said. *The son of my "
             "old adventuring companion. If anyone can help you wake our friend, it is that family.*"),
    ("gold", "**Osric:** “Ursa, you say? Odd lad, that one. Can usually be found star gazing out "
             "in the fields, or else wandering the woods. If you are looking for him, best sit tight "
             "and wait. He comes around often enough.”"),
    ("gold", "So Lilly finds a small table by the fire, sets the Sphere gently in her lap, and waits, "
             "excited and nervous all at once, wondering what kind of person this Ursa will be."),

    ("h2", "Ursa's Curiosity"),
    ("gold", "Outside the village, a red haired boy lies back in the cool grass, tracing "
             "constellations as they wake in the darkening sky. **Ursa Catchum** knows the stars the "
             "way other children know their own street. His father, the renowned wildfire druid "
             "**Ash Catchum**, disappeared when Ursa was young, leaving behind three enchanted "
             "potatoes, a thousand questions, and a boy who watches the sky as if it might answer them. "
             "The **Circle of the Eternal Stars** raised him after that, and taught him to listen to "
             "the world's quiet voices."),
    ("gold", "Tonight the quiet voices are not quiet. There is a hum in the air, a shiver in the "
             "natural flow of things, and when word reaches him that a stranger is asking for him by "
             "name, Ursa is already walking toward the village. Some part of him, the part his father "
             "left him, knows: something is beginning."),
    # Portrait floats right; the tavern meeting paragraphs wrap around it.
    ("imgfloat", f"{A}/npcs/s1_ursa_intro.png", 2.3),
    ("gold", "In the tavern, Ursa spots the silver haired gnome girl at once, and the strange "
             "contraption glowing faintly in her lap. He crosses the room, cautious and curious in "
             "equal measure."),
    ("gold", "**Ursa:** “Are you looking for me?”"),
    ("gold", "**Lilly:** “Yes! I am Lilly. And I believe you can help me with... this.” She "
             "lifts the Essence Sphere. As Ursa leans close, he feels the familiar pull of living "
             "magic, but unlike any creature or energy he has ever met. Something is in there. "
             "Something waiting."),

    ("h2", "Stabby's Grand Entrance"),
    # Portrait floats right; intro paragraphs wrap around it.
    ("imgfloat", f"{A}/npcs/s1_stabby_intro.png", 2.3),
    ("gold", "**BANG.** The tavern door slams open hard enough to rattle the trophies on the walls. "
             "In struts a goblin boy with green skin, light green hair, sharp little teeth, and red "
             "eyes lit with pure mischief. **Stabby Sharpblade**, eight years old and afraid of "
             "absolutely nothing, surveys the room like a king inspecting his castle."),
    ("gold", "Stabby was born to the **Bloodfang Clan** in far off **Bloodthorn Hollow**, where "
             "goblin children learn to be quick or learn to be sorry. A wandering monk, **Master "
             "Kaelon Windstep** of the Whispering Breeze, taught him balance, patience (a little), "
             "and gave him his name. Then the road called, and Stabby followed it here, bored and "
             "hungry for excitement."),
    ("gold", "He notices the glowing sphere immediately. He notices the two interesting strangers "
             "around it immediately after. He invites himself to their table before either can say a word."),
    ("gold", "**Stabby:** “Oi! You two look like you are planning an adventure!” He plops "
             "down, grinning. Lilly startles; Ursa only raises an eyebrow. Lilly explains her quest, "
             "the Sphere, the sleeping spark inside. Stabby understands maybe half of it, and cares "
             "about exactly none of that half."),
    ("gold", "**Stabby:** “I do not know what that is. But it looks important. And if there is "
             "adventure involved, count me in!”"),

    ("h2", "Rumors and a Brawl"),
    ("gold", "Osric brings mugs and news to the new table of three. All around them the tavern "
             "murmurs: *old Jarek saw something glowing in the woods again... strange winds out "
             "there... the trees do not sound right... folk say the forest is waking up.*"),
    ("gold", "**Osric**, leaning in low: “There has been talk of creatures in the forest. "
             "Magical ones. Folk say they do not belong here, like they wandered in from... somewhere "
             "else.”"),
    ("gold", "**Rhea**, setting down a tray: “A traveler last night swore he saw something with "
             "glowing eyes by the pond. Did not stay to get a closer look. Cannot say I blame him.”"),
    ("gold", "Before the three can trade theories, a shadow falls across their table. **Bren**, a "
             "burly local several drinks past sensible, cracks his knuckles and grins down at them."),
    ("gold", "**Bren:** “Oi! You lot look like you think you are tough. How about you prove it? "
             "A little friendly brawl, eh?”"),
    ("dm", "**The brawl.** Bren and two friends, fists, chairs, and one regrettable mug. Strictly "
           "non lethal. The three strangers fight together for the first time, and win."),
    # Brawl scene floats right beside the fight paragraphs.
    ("imgfloat", f"{A}/scenes/s1_bar_brawl.png", 2.8),
    ("gold", "It is short, loud, and glorious. Stabby fights like a rumor: everywhere and nowhere. "
             "Lilly's gadgets spark and startle. Ursa never even stands up all the way. When Bren "
             "finally sits down hard, rubbing his jaw, the whole tavern is laughing, and so, almost, "
             "is he."),
    ("gold", "**Bren:** “Agh... fine. Maybe you are tougher than you look.”"),
    ("gold", "**Osric** claps his hands over the noise. “Alright, that is enough! Bren, leave "
             "these folks alone before I toss you out!” He sets a fresh round before the three "
             "young strangers, on the house. “Sorry about that. But I can see you lot handle "
             "yourselves. If you are heading into the forest, you will need that strength. There are "
             "more dangerous things out there than Bren, I promise you that. Something is stirring "
             "near the Forest of Whispers. And it is not just the wind.”"),
    ("gold", "Three strangers walked into the Gilded Acorn tonight. It is a party of adventurers "
             "that walks out, under a sky thick with watching stars."),

    # ------------------------------------------------------------------
    ("h1", "Part Two: The Whispering Pond", {"pagebreak": True}),
    ("bridge", "The new friends left the warm noise of the tavern behind and followed the path "
               "toward the forest, drawn by rumor and the glow of adventure."),
    ("gold", "Beyond the last cottages, the night turns soft and silver. Mist rolls in from the "
             "treeline, and the path bends past a small pond ringed with reeds and wildflowers. The "
             "water holds the starlight strangely, glowing faintly from below, and here the air "
             "shivers, as though the world's fabric is worn thin as old cloth."),
    ("dm", "Wisdom (Perception) DC 12 to spot a glimmering light moving in the reeds."),
    ("gold", "Something small is moving at the water's edge. It is round bodied, about the size of a "
             "halfling, with faintly shimmering skin, enormous curious eyes, and a tongue longer than "
             "it is tall, which flicks out to taste the pond, then a wildflower, then the air in the "
             "party's direction. Around it the reeds sway toward it like friends leaning in, and the "
             "colors of the night seem brighter, dreamlike, wherever it goes."),
    # Pond scene floats right beside the Lickgloom introduction.
    ("imgfloat", f"{A}/scenes/s1_lickgloom_pond.png", 2.8),
    ("gold", "This is **Lickgloom**, a creature of the **Feywild**, a realm of wild wonder that "
             "presses close against our own. It did not break into the world. It simply wandered "
             "through a door that should not have been open."),
    ("dm", "Wisdom (Animal Handling) DC 12 to befriend. The party offered food and gentle patience, "
           "and succeeded."),
    ("gold", "Lickgloom pads closer, tilting its head. When Ursa kneels and holds out a bit of bread, "
             "the long tongue snaps out, the bread vanishes, and a feeling arrives in everyone's "
             "minds at once, wordless and warm: *Food? Friend?*"),
    ("gold", "Friend. The little fey creature falls in beside the party, flicking its tongue at "
             "fireflies, and just like that the three heroes become four travelers. All around the "
             "pond, where Lickgloom passed, the wildflowers are blooming out of season."),

    # ------------------------------------------------------------------
    ("h1", "Part Three: The Forest of Whispers", {"pagebreak": True}),
    ("bridge", "With Lickgloom trotting alongside, the party stepped beneath the eaves of the "
               "forest everyone in Eldridge Vale had warned them about."),
    ("gold", "The Forest of Whispers earns its name at once. The canopy closes overhead until the "
             "starlight comes through in coins and slivers, and the wind moving in the leaves makes a "
             "long, low murmur, like a crowd whispering just out of sight. The mist thickens around "
             "your boots. The air feels charged, the way it does before a storm breaks."),
    ("img", f"{A}/scenes/s1_forest_of_whispers.png",
     "Beneath the eaves of the Forest of Whispers, where the starlight comes through in coins and slivers.", 3.7),

    ("h2", "The Stone Circle and the Duck with the Leek"),
    ("gold", "The trees open into a wide clearing where five towering stones stand in a rough ring, "
             "mossy and carved with runes too old to read. The air above them ripples like heat over "
             "a summer road. And perched atop the tallest stone, silhouetted against the sky, stands "
             "a bird."),
    ("gold", "It is a large, sturdy duck. It is holding a leek like a sword. Its eyes glow with a "
             "pale light, and the wind in the clearing moves when it moves, swirling leaves in slow "
             "spirals around the stones. A voice arrives in your minds, sharp as a whistle: a "
             "telepathic *quack*."),
    ("gold", "**Duckleaf:** “Intruders! Leave this place... or face the winds!”"),
    ("dm", "Intelligence (Arcana) DC 14: the stones are amplifying elemental air energy; the "
           "creature is drawing power from the **Elemental Plane of Air**. Disrupting a stone "
           "weakens its wind step."),
    # Duckleaf art floats right beside the duel paragraphs.
    ("imgfloat", f"{A}/monsters/duckleaf_stone_circle.png", 2.6),
    ("gold", "There is no talking their way past a guardian with a grudge and a leek. **Duckleaf** "
             "leaps from its stone and the wind leaps with it. It fights like a storm given feathers: "
             "riding gusts across the clearing, slashing with blades of sharpened air, loosing a "
             "*Quack of Fury* that rattles teeth and courage alike. But Stabby is faster than any "
             "wind, Ursa's magic finds it wherever it lands, and Lilly, watching the stones ripple, "
             "shouts the secret: *the circle is feeding it!* When the party disrupts one of the "
             "ancient stones, the gusts falter, and the duel turns."),
    ("gold", "Beaten at last, Duckleaf sinks to the grass with one final, dignified quack. And then "
             "something strange: as the creature fades, a small **mote of energy** rises from it, "
             "faintly green, crackling with wind and light. It hovers a moment, warm to the touch, "
             "then slips away like a breeze through fingers. The whole clearing goes still."),
    ("gold", "**Lilly**, quietly: “That came from somewhere else. Something is leaking into our "
             "world.”"),

    ("h2", "The Grove of Elemental Waters"),
    # Cognifin art floats right beside the grove paragraphs.
    ("imgfloat", f"{A}/monsters/cognifin_grove.png", 2.6),
    ("gold", "Deeper still, the ground turns soft and the sound of water leads the party to a hidden "
             "grove, where a wide pond glows a gentle blue from beneath, and droplets of water hang "
             "in the air, suspended as if time forgot them. Nothing here feels quite of this world."),
    ("gold", "The water stirs. From the center of the pond rises a duck like creature wrapped in "
             "pale blue light, hovering above its own reflection, eyes gleaming with psychic energy. "
             "The ripples spread from it in perfect rings, and its voice arrives not in the ears but "
             "behind them, calm and stern."),
    ("gold", "**Cognifin:** “You stand upon sacred ground. Prove your strength, or the waters "
             "will judge you.”"),
    ("gold", "This one is no invader; it is a **guardian**, bound to test all who enter, and it "
             "fights like a slow, patient tide. Waves crash from a still pond. Whirlpools open where "
             "heroes stand. Psychic pressure squeezes like deep water. But the party fights as one "
             "now: Ursa's starlight, Lilly's sparks, Stabby laughing on the slick stones, Lickgloom "
             "yanking a friend back from a whirlpool with one heroic tongue."),
    ("gold", "When the guardian finally folds its light and yields, there is no anger in it. It "
             "bows its head, and a **mote of water energy** rises from the pond, pulsing soft and "
             "blue, before it too fades into the mist. The test is passed. The question it leaves "
             "behind is bigger than the grove: *who is opening the doors between worlds?*"),

    # ------------------------------------------------------------------
    ("h1", "Part Four: The Road to Oakshade", {"pagebreak": True}),
    ("bridge", "Carrying two mysteries and one new friend, the party pressed on through the "
               "forest's far side, toward the next village on the map."),
    ("gold", "The road to **Oakshade Village** winds through hills as the sun goes down, and with "
             "the dusk comes fog, thick and white and strange. Great gnarled roots have burst up "
             "through the packed earth of the road itself, as if something beneath the ground rolled "
             "over in its sleep. Shapes move in the murk."),
    ("dm", "Dexterity (Acrobatics) DC 12 across the root falls; Wisdom (Perception) DC 13 to hold "
           "the path in fog. Then: two **Mist Stalkers**, ambushing from the white."),
    # Mist Stalker scene floats right beside the ambush paragraphs.
    ("imgfloat", f"{A}/scenes/s1_mist_stalkers.png", 2.6),
    ("gold", "They come with no sound at all: two sleek predators of fog and hunger, eyes like cold "
             "lamps, wearing the mist like a cloak. Their howls roll through the whiteness from "
             "every direction at once, hunting fear the way wolves hunt the slow. But this party "
             "does not scatter. Back to back around Lickgloom, blade and bolt and starlight answer "
             "the howling, until the mist runs thin and empties, and two motes of **fey energy** "
             "glimmer where the stalkers fell, swirling briefly before the fog swallows them."),
    ("gold", "The pattern is a pattern now. Every strange creature leaves a mote behind, a little "
             "piece of another plane, loose in the world. Somewhere, doors are opening. The party "
             "walks the last miles wondering what is on the other side."),

    ("h2", "Twilight at Oakshade"),
    ("gold", "Oakshade Village appears at last through the thinning fog, cottages nestled beneath "
             "oaks so old and vast the village seems built in their pockets. Lanterns glow gold in "
             "the windows. At the heart of the village square stands one ancient oak hung with faded "
             "ribbons and charms, an old well beside it, and the smell of woodsmoke and fresh bread "
             "on the air."),
    ("gold", "It should feel peaceful. It almost does. But the villagers walk quickly, and their "
             "eyes keep sliding to the forest's edge, as if the trees might follow them home."),
    ("img", f"{A}/scenes/s1_oakshade_twilight.png",
     "Oakshade at twilight, its cottages tucked in the pockets of ancient oaks.", 2.4),
    ("gold", "**Elder Merwin**, the village's gray streaked blacksmith and elder, meets the party "
             "by his forge, sizing them up with a smith's eye for good material. “New faces in "
             "Oakshade, eh? Have not seen travelers since the forest started acting strange. The "
             "wind carries whispers, and folk say they have seen creatures... things that do not "
             "belong here. The old stories talk of other realms, other planes. I never thought they "
             "would spill into our world.”"),
    ("gold", "In the warm little **Old Oak Tavern**, the keeper **Alwen** sets down bowls of hot "
             "stew unasked. “Well now, travelers! Made it just in time for dinner. Take a seat, "
             "and I will bring you a bowl.” Around the fire, villagers whisper of a glowing fox "
             "darting through the trees, and of old Merwin muttering that *the planes are bleeding "
             "together*."),

    ("h2", "The Missing Villagers"),
    ("gold", "As the party finishes eating, Merwin comes to their table, and the smith's steadiness "
             "in his face has a crack of worry in it."),
    ("gold", "**Merwin:** “There is something I did not mention earlier. A few of our young folk "
             "went into the forest to gather herbs, days ago now. They have not come back. I have "
             "sent search parties and found nothing. If you are willing to look, you will have fifty "
             "gold and my gratitude, and Oakshade's with it.”"),
    ("gold", "The party trades one look and agrees on the spot. But the search will wait for "
             "daylight. Tonight there are warm rooms above the tavern, and for the first time since "
             "three strangers collided at the Gilded Acorn, the new friends sleep under one roof: a "
             "gnome far from the deep places, a goblin far from his clan, a boy whose father watched "
             "these same stars, and one small fey creature dreaming, whatever fey creatures dream."),
    ("divider",),
    ("bridge", "Their first day together was done: a friendship, a brawl, two guardians bested, "
               "three motes of runaway magic, and a mystery with no bottom yet. In the morning, the "
               "search for the missing villagers would carry the Guardians of Elaria, though they "
               "did not yet know that name, deeper into the whispering wood, and toward a laboratory "
               "on the cliffs where an old elf kept watch on the doors between worlds."),
    ("gold", "*Next: Session 2, in which lost villagers come home, a rival clan finds Stabby, a "
             "goddess opens her eyes inside a vision, and a professor's laboratory turns out to be "
             "full of impossible creatures.*"),

    # ------------------------------------------------------------------
    ("h1", "Appendix: Creatures of Session One", {"pagebreak": True}),
    ("body", "Compact statistics for the table. The full bestiary, with lore and pictures, lives in "
             "the compendium."),
    ("stat", "Lickgloom", [
        "Small fey (Feywild), neutral. **CR 1**. AC 13 (natural armor), HP 27 (5d6 + 10), Speed 30 ft.",
        "STR 14, DEX 12, CON 14, INT 6, WIS 10, CHA 8. Saves Dex +3; Skills Perception +2, Stealth +4.",
        "Resistances acid, poison. Darkvision 60 ft. Understands Common; telepathic impressions.",
        "**Tongue Whip.** +4, reach 10 ft., 1d6 + 2 bludgeoning; DC 12 Strength save or grappled.",
        "**Sticky Lick (Recharge 5-6).** DC 13 Dexterity save or a small item is snatched.",
        "**Lick Attack.** +4, 1d8 + 2 bludgeoning; DC 12 Constitution save or stunned one turn.",
    ]),
    ("stat", "Duckleaf", [
        "Small beast (Elemental Air), neutral. **CR 4**. AC 15, HP 52 (8d8 + 16), Speed 30 ft., fly 30 ft.",
        "STR 14, DEX 16, CON 14, INT 10, WIS 12, CHA 10. Saves Dex +5, Wis +3; Acrobatics +5, Perception +3.",
        "Resistances slashing, bludgeoning (wind sheath). Darkvision 60 ft. Telepathy 30 ft. (quacks).",
        "**Leek Strike.** +6, reach 5 ft., 2d8 + 4 slashing.",
        "**Aerial Slash.** +5, range 20/60 ft., 3d6 + 3 slashing.",
        "**Quack of Fury (Recharge 5-6).** 15 ft., DC 14 Wisdom save or frightened 1 minute.",
        "**Winged Leap.** Leaps 30 ft. without provoking; lost if a circle stone is disrupted.",
    ]),
    ("stat", "Cognifin", [
        "Small beast (Elemental Water), neutral guardian. **CR 3**. AC 14, HP 45 (6d8 + 18), fly 30 ft. (hover).",
        "STR 10, DEX 14, CON 16, INT 10, WIS 14, CHA 12. Saves Dex +4, Wis +4; Perception +4, Arcana +2.",
        "Resistances cold, psychic. Darkvision 60 ft. Telepathy 60 ft. (images and feelings).",
        "**Headache Blast.** +4, range 30 ft., 2d6 + 2 psychic.",
        "**Water Pulse.** +4, range 30 ft., 2d6 + 2 bludgeoning; DC 12 Strength save or prone.",
        "**Confusion Pulse (Recharge 5-6).** 15 ft. radius, DC 13 Wisdom save or confused 1 minute.",
        "**Psychic Shield.** Reaction: +2 AC until its next turn.",
        "**Waters of the Grove (Legendary).** Whirlpool (restrain, DC 12 Str) or tidal wave (2d4, push 5 ft.).",
    ]),
    ("stat", "Mist Stalker", [
        "Medium fey (Feywild), unaligned. **CR 2**. AC 13, HP 39, Speed 40 ft.",
        "**Claw and Bite.** Pack hunters that strike from heavy fog.",
        "**Fog Cloak.** Wraps itself in mist, heavily obscured for 1 round.",
        "**Howl of the Mist.** Frightens prey within 30 ft. (Wisdom save).",
    ]),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    out = build_doc(BLOCKS, "sessions/session_01_gathering_of_friends.docx")
    print("built", out)
