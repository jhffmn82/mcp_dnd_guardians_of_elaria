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
    # Session opener: half-page landscape plate directly under the first
    # heading, cropped 3:2 so the square art spans the full text column
    # and dominates page 1.
    ("img", f"{A}/scenes/s1_eldridge_village.png",
     "Eldridge Village at dusk, where our story begins.", 6.0, {"crop": "3:2", "hmax": 4.6}),
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
           "session live in the compendium; a DM run sheet and bestiary close each session."),
    ("img", f"{A}/world/elaria_region_map.png",
     "Eldridge Vale and the lands of Elaria, as mapped by the cartographers of Gearhaven.", 6.5, {"hmax": 4.6}),

    # ------------------------------------------------------------------
    ("h1", "Part One: The Gilded Acorn", {"hardbreak": True}),
    ("gold", "The **Gilded Acorn Tavern** is the heart of Eldridge Village: a warm, golden room "
             "that smells of roasting meat and fresh bread. Wooden beams cross the ceiling, hunting "
             "trophies and faded banners line the walls, and a great stone hearth crackles against "
             "the evening chill. A minstrel strums a lute on the little stage in the corner. The "
             "tavern is crowded tonight, and every table hums with the same uneasy talk: the forest, "
             "the lights, the whispers."),
    # Tavern interior: promoted to a half-page landscape plate per DM review.
    # 5:4 crop keeps this plate tall as well as wide; the three heroes fill the frame.
    ("img", f"{A}/scenes/s1_gilded_acorn_meeting.png",
     "The Gilded Acorn Tavern, the heart of Eldridge Village.", 5.8, {"crop": "5:4", "hmax": 4.6}),
    # Portrait floats right beside the Osric paragraph and Lilly's arrival;
    # anchored above the h2 so it sits high enough to clear the bottom margin.
    ("imgfloat", f"{A}/characters/lilly_with_essence_sphere_dalle.webp", 2.7),
    ("gold", "Behind the bar stands **Osric the innkeeper**, broad shouldered and bushy bearded, "
             "his laugh booming over the noise. Between tables darts **Rhea the barmaid**, quick "
             "handed and quicker witted, hearing every rumor in the room twice before anyone "
             "finishes telling it."),
    ("dm", "**Eldridge Village.** Small but lively. Besides the Gilded Acorn, heroes can visit "
           "**Garrick's Forge** (blacksmith), **Evelyn's Remedies** (herbalist), **The Wandering "
           "Trinket** (general store), and the **Weary Wanderer Inn**. Osric and Rhea are the "
           "rumor sources; both point toward the Forest of Whispers."),

    ("h2", "Lilly's Arrival"),
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
    # Portrait floats left; the tavern meeting paragraphs wrap around it.
    ("imgfloat", f"{A}/npcs/s1_ursa_intro.png", 3.3, "left"),
    ("gold", "In the tavern, Ursa spots the silver haired gnome girl at once, and the strange "
             "contraption glowing faintly in her lap. He crosses the room, cautious and curious in "
             "equal measure."),
    ("gold", "**Ursa:** “Are you looking for me?”"),
    ("gold", "**Lilly:** “Yes! I am Lilly. And I believe you can help me with... this.” She "
             "lifts the Essence Sphere. As Ursa leans close, he feels the familiar pull of living "
             "magic, but unlike any creature or energy he has ever met. Something is in there. "
             "Something waiting."),

    ("h2", "Stabby's Grand Entrance"),
    ("gold", "**BANG.** The tavern door slams open hard enough to rattle the trophies on the walls. "
             "In struts a goblin boy with green skin, light green hair, sharp little teeth, and red "
             "eyes lit with pure mischief. **Stabby Sharpblade**, eight years old and afraid of "
             "absolutely nothing, surveys the room like a king inspecting his castle."),
    ("gold", "Stabby was born to the **Bloodfang Clan** in far off **Bloodthorn Hollow**, where "
             "goblin children learn to be quick or learn to be sorry. A wandering monk, **Master "
             "Kaelon Windstep** of the Whispering Breeze, taught him balance, patience (a little), "
             "and gave him his name. Then the road called, and Stabby followed it here, bored and "
             "hungry for excitement."),
    # Lore of Elaria: L3, placed at the mention of Master Kaelon and the
    # Whispering Breeze; the overflow lands in the brawl page's deep tail.
    ("lore", "The Whispering Breeze Monastery",
     "High in the passes stands a monastery whose monks study the oldest wind, the one that "
     "has been circling the world since the Weaving. They say every storm is just that wind "
     "remembering something. Their teaching is short: when the whole world is screaming, "
     "get still."),
    # Portrait floats right; anchored two paragraphs in so the section start
    # at a page foot cannot push the float over the bottom margin.
    ("imgfloat", f"{A}/npcs/s1_stabby_intro.png", 3.3),
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
    ("dm", "**The brawl.** Bren (AC 12, HP 8, unarmed strike +3 for 1d4 + 1) and two friends "
           "(AC 11, HP 6, unarmed +3 for 1d4): fists, chairs, and one regrettable mug, strictly "
           "non lethal. Heroes who try to wave Bren off only make him louder; soon he and his "
           "friends are standing over the table, and the fight comes to them. They rely on brute "
           "force, ganging up on one or two heroes at a time, and Osric steps in if things get "
           "too hot. Any hero knocked down wakes a minute later with a bruised ear and a mug of "
           "cider on the house. The three strangers fight together for the first time, and win."),
    # Brawl scene promoted to a half-page plate: it is a tavern interior
    # action scene, and the DM wants those big.
    ("img", f"{A}/scenes/s1_bar_brawl.png",
     "A little friendly brawl, and the first fight the three ever won together.", 6.2,
     {"crop": "3:2", "hmax": 4.6}),
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
    ("h1", "Part Two: The Whispering Pond", {"hardbreak": True}),
    ("bridge", "The new friends left the warm noise of the tavern behind and followed the path "
               "toward the forest, drawn by rumor and the glow of adventure."),
    ("gold", "Beyond the last cottages, the night turns soft and silver. Mist rolls in from the "
             "treeline, and the path bends past a small pond ringed with reeds and wildflowers. The "
             "water holds the starlight strangely, glowing faintly from below, and here the air "
             "shivers, as though the world's fabric is worn thin as old cloth."),
    ("dm", "Wisdom (Perception) DC 12 to spot a glimmering light moving in the reeds; on a "
           "failure the heroes hear only rustling reeds and frogs, and Lickgloom shows itself "
           "when they reach the water's edge."),
    ("gold", "Something small is moving at the water's edge. It is round bodied, about the size of a "
             "halfling, with faintly shimmering skin, enormous curious eyes, and a tongue longer than "
             "it is tall, which flicks out to taste the pond, then a wildflower, then the air in the "
             "party's direction. Around it the reeds sway toward it like friends leaning in, and the "
             "colors of the night seem brighter, dreamlike, wherever it goes."),
    # Pond establishing shot: half-page landscape plate per DM review.
    # 16:9 crop: a wide cinematic plate that lets Part Two close out its page.
    ("img", f"{A}/scenes/s1_lickgloom_pond.png",
     "The Whispering Pond, where the water holds the starlight strangely.", 5.5,
     {"crop": "16:9", "hmax": 4.6}),
    ("gold", "This is **Lickgloom**, a creature of the **Feywild**, a realm of wild wonder that "
             "presses close against our own. It did not break into the world. It simply wandered "
             "through a door that should not have been open."),
    ("dm", "**Meeting Lickgloom.** Wisdom (Insight) DC 10: curious and playful, not a threat. "
           "Wisdom (Animal Handling) DC 12 to befriend with food and patience; on a failure, or "
           "at any aggression, it darts into the pond and hides. Intelligence (Arcana) DC 14: "
           "creature and pond both hum with Feywild energy; the boundary between planes is worn "
           "thin here. If it flees, searching the bank finds wildflowers blooming out of season "
           "and strange ripples (same Arcana check to read them), and quiet patience plus a "
           "snack coaxes it back out. The party offered bread, and succeeded."),
    ("gold", "Lickgloom pads closer, tilting its head. When Ursa kneels and holds out a bit of bread, "
             "the long tongue snaps out, the bread vanishes, and a feeling arrives in everyone's "
             "minds at once, wordless and warm: *Food? Friend?*"),
    ("gold", "Friend. The little fey creature falls in beside the party, flicking its tongue at "
             "fireflies, and just like that the three heroes become four travelers. All around the "
             "pond, where Lickgloom passed, the wildflowers are blooming out of season."),
    ("dm", "**Lickgloom, companion.** Traveling with the party, Lickgloom can fetch small "
           "objects with its 10 foot tongue, and once per scene its tasting tongue grants one "
           "hero advantage on a Wisdom (Perception) or Intelligence (Investigation) check. "
           "Statistics in the appendix."),

    # ------------------------------------------------------------------
    # No hardbreak: Part Two ends high on its page, and the forest's eaves
    # follow straight on from the pond, keeping the page full.
    ("h1", "Part Three: The Forest of Whispers"),
    ("bridge", "With Lickgloom trotting alongside, the party stepped beneath the eaves of the "
               "forest everyone in Eldridge Vale had warned them about."),
    ("gold", "The Forest of Whispers earns its name at once. The canopy closes overhead until the "
             "starlight comes through in coins and slivers, and the wind moving in the leaves makes a "
             "long, low murmur, like a crowd whispering just out of sight. The mist thickens around "
             "your boots. The air feels charged, the way it does before a storm breaks."),
    # The DM flagged this one by name: landscapes go half-page big.
    ("img", f"{A}/scenes/s1_forest_of_whispers.png",
     "Beneath the eaves of the Forest of Whispers, where the starlight comes through in coins and slivers.",
     5.8, {"crop": "3:2", "hmax": 4.6}),
    # Lore of Elaria: W2, under the forest plate; the first druids and the
    # Circle of the Eternal Stars, on the Forest of Whispers page.
    ("lore", "The First Listeners",
     "Before there were villages there were listeners. The first druids did not learn magic; "
     "they learned quiet, and the forests, glad of the company, taught them the rest. The "
     "Circle of the Eternal Stars still opens every gathering with a full minute of silence, "
     "in honor of the age when that was the whole religion."),

    # The stone circle section starts on a fresh page: the forest plate fills
    # the rest of Part Three's opening page, and the Duckleaf float would
    # otherwise be pushed over the bottom margin.
    ("pagebreak",),
    # Duckleaf floats right beside the whole stone circle section; anchored
    # above the h2 and cropped 5:4 so it stays clear of the bottom margin.
    ("imgfloat", f"{A}/monsters/duckleaf_stone_circle.png", 3.3, {"crop": "5:4"}),
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
    ("dm", "**The stone circle.** Intelligence (Arcana) or Wisdom (Nature) DC 14: the five "
           "stones are amplifying elemental air energy; the creature draws its power from the "
           "**Elemental Plane of Air**. Damaging or disrupting one stone breaks that "
           "connection: Duckleaf loses its Winged Leap for the rest of the battle, and it "
           "defends the stones fiercely once it realizes what the heroes are doing. If the "
           "players are stuck, ladder the hints: first, wind visibly streams from the stones to "
           "the duck each time it leaps; then, any stray hit on a stone makes Duckleaf shriek "
           "and rush to defend it."),
    ("dm", "**Duckleaf's tactics.** Wisdom (Perception) DC 12 reads its style: it opens with "
           "Aerial Slash from range, uses Winged Leap to skip away from melee without "
           "provoking, and saves its Quack of Fury (15 feet, Wisdom DC 14 or frightened) for "
           "when the party bunches up. It is a guardian, not a hunter: heroes who heed the "
           "warning and withdraw are allowed to leave, and if the fight turns badly it lets "
           "them retreat into the trees rather than pursue beyond the stones."),
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
    ("dm", "**The motes.** Intelligence (Arcana) DC 14: each mote is a residue of another "
           "plane, left behind when a planar creature falls. Similar motes will rise from every "
           "such creature the party defeats; the pattern is the session's biggest clue to the "
           "doors opening between worlds."),

    ("h2", "The Grove of Elemental Waters"),
    ("gold", "Deeper still, the ground turns soft and the sound of water leads the party to a hidden "
             "grove, where a wide pond glows a gentle blue from beneath, and droplets of water hang "
             "in the air, suspended as if time forgot them. Nothing here feels quite of this world."),
    # Cognifin art floats left beside the grove paragraphs.
    ("imgfloat", f"{A}/monsters/cognifin_grove.png", 3.0, "left"),
    ("gold", "The water stirs. From the center of the pond rises a duck like creature wrapped in "
             "pale blue light, hovering above its own reflection, eyes gleaming with psychic energy. "
             "The ripples spread from it in perfect rings, and its voice arrives not in the ears but "
             "behind them, calm and stern."),
    ("gold", "**Cognifin:** “You stand upon sacred ground. Prove your strength, or the waters "
             "will judge you.”"),
    ("dm", "**The guardian's test.** Cognifin, CR 3 (appendix). Intelligence (Arcana) or Wisdom "
           "(Nature) DC 14: it draws its strength from the pond itself, and disturbing the "
           "water's surface (a spell, a splash, a well-thrown rock) breaks its focus, silencing "
           "its whirlpools and tidal waves for a round. Wisdom (Perception) DC 13: small "
           "whirlpools form and fade wherever it drifts, a telegraph of the water control to come."),
    ("dm", "**Tactics.** It opens with Water Pulse to knock the closest hero prone, peppers the "
           "back line with Headache Blasts, and looses its Confusion Pulse when the party "
           "groups up; between turns its legendary waters pull heroes into whirlpools or shove "
           "them back with small tidal waves, while Psychic Shield turns away the worst blows. "
           "The test is stern but never lethal: a hero who drops is washed gently to the bank, "
           "unconscious but stable, and a party that falls or yields wakes at the grove's edge, "
           "free to try again once rested."),
    ("gold", "This one is no invader; it is a **guardian**, bound to test all who enter, and it "
             "fights like a slow, patient tide. Waves crash from a still pond. Whirlpools open where "
             "heroes stand. Psychic pressure squeezes like deep water. But the party fights as one "
             "now: Ursa's starlight, Lilly's sparks, Stabby laughing on the slick stones, Lickgloom "
             "yanking a friend back from a whirlpool with one heroic tongue."),
    ("gold", "When the guardian finally folds its light and yields, there is no anger in it. It "
             "bows its head, and a **mote of water energy** rises from the pond, pulsing soft and "
             "blue, before it too fades into the mist. The test is passed. The question it leaves "
             "behind is bigger than the grove: *who is opening the doors between worlds?*"),
    # Lore of Elaria: D2, closing the grove page right after the second mote
    # rises; the chronicler explains what a mote is.
    ("lore", "Motes",
     "A mote is a crumb of another world, and the world it lands in treats it the way a pond "
     "treats a dropped lantern: strange light, strange ripples, and every fish in the pond "
     "suddenly having opinions. The wondrous creatures of the chronicle, the talking, glowing, "
     "impossible ones, are what happens when the ripples reach something alive."),

    # ------------------------------------------------------------------
    # Fresh page: keeps the Oakshade shop card whole and the closing plate
    # flush with the session's last page.
    ("h1", "Part Four: The Road to Oakshade", {"hardbreak": True}),
    ("bridge", "Carrying two mysteries and one new friend, the party pressed on through the "
               "forest's far side, toward the next village on the map."),
    ("gold", "The road to **Oakshade Village** winds through hills as the sun goes down, and with "
             "the dusk comes fog, thick and white and strange. Great gnarled roots have burst up "
             "through the packed earth of the road itself, as if something beneath the ground rolled "
             "over in its sleep. Shapes move in the murk."),
    ("dm", "**Road hazards.** Dexterity (Acrobatics) DC 12 across the erupted roots, 1d4 "
           "bludgeoning on a stumble; Wisdom (Perception) DC 13 to hold the path in fog, and a "
           "party that strays gets ambushed on ground of the Stalkers' choosing."),
    ("dm", "**The ambush.** Two **Mist Stalkers** (appendix). Each wraps itself in Fog Cloak to "
           "strike from heavy obscurement, and their Howl of the Mist rolls in from every "
           "direction at once, hunting for frightened, scattered prey. They will not leave "
           "their fog: heroes who regain the road and keep moving escape them, and a strong "
           "wind or a gust of magic that thins the mist steals their cover and their nerve."),
    # Mist Stalker scene floats right beside the ambush paragraphs.
    ("imgfloat", f"{A}/scenes/s1_mist_stalkers.png", 3.1),
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
    ("gold", "**Elder Merwin**, the village's gray streaked blacksmith and elder, meets the party "
             "by his forge, sizing them up with a smith's eye for good material. “New faces in "
             "Oakshade, eh? Have not seen travelers since the forest started acting strange. The "
             "wind carries whispers, and folk say they have seen creatures... things that do not "
             "belong here. The old stories talk of other realms, other planes. I never thought they "
             "would spill into our world.”"),
    ("gold", "Next door, **Nina the herbalist** watches from the doorway of a little shop whose "
             "windows are crowded with dried herbs and potion bottles, the air around it sweet "
             "with lavender and sage. “There is magic in the air, stronger than usual,” she "
             "tells the party softly. “I can feel it in the plants and the water. And I have "
             "seen creatures near the village that are not in any of my books.”"),
    ("game", "Provisions in Oakshade Village", [
        "**Merwin's Forge.** Simple weapons (spear, shortsword, handaxe), arrows and bolts, "
        "chain shirts and shields at standard prices. Special: Merwin will silver a weapon for "
        "**100 gp**, good against certain fey and shadowy things.",
        "**Nina's Herbs and Remedies.** Potion of Healing **50 gp**, antitoxin **25 gp**, herbal "
        "salves **5 gp**. Special: **Moonroot**, 75 gp, a rare herb Nina can brew into a potion "
        "that grants advantage on saving throws against being charmed.",
        "**The Old Oak Tavern.** Hot stew, fresh bread, and cider; a warm room for the night is "
        "**5 silver** per person. A night here is a long rest.",
    ]),
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
    # Closing vignette: the village establishing shot as a half-page plate,
    # placed here so Part Four ends flush on a full page.
    ("img", f"{A}/scenes/s1_oakshade_twilight.png",
     "Oakshade Village at twilight, nestled beneath the ancient oaks.", 6.0,
     {"crop": "5:4", "hmax": 4.6}),
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
    # APPENDIX I: the DM run sheet (Session 7 format).
    ("appendix_title", "APPENDIX", "DM Run Sheet: The Day at a Glance",
     "Every DC, dial, and spotlight, in play order. Keep this page at your elbow."),

    ("h1", "The Shape of the Session"),
    ("body", "▶ Four parts, four fights, one friend. P1 the Gilded Acorn (roleplay: three "
             "meetings, Osric and Rhea's rumors) → FIGHT 1, the brawl. P2 the Whispering Pond: "
             "Lickgloom (Perception DC 12 to spot it; Insight DC 10: playful, not a threat; Animal "
             "Handling DC 12 plus a snack = a companion). P3 the Forest of Whispers: FIGHT 2, "
             "Duckleaf at the stone circle → the first mote (Arcana DC 14) → FIGHT 3, "
             "Cognifin's test at the grove → the second mote. P4 the foggy road (roots: "
             "Acrobatics DC 12, 1d4 on a stumble; path: Perception DC 13 or ambushed on the "
             "Stalkers' ground): FIGHT 4, the Mist Stalkers → two fey motes → Oakshade "
             "(roleplay: Merwin, Nina, the shops) → the hook (missing villagers, 50 gp) → "
             "LONG REST at the Old Oak Tavern. Natural break point: the pond."),

    ("h1", "Fights at a Glance"),
    ("body", "**FIGHT 1: The Bar Brawl** (Easy; strictly non lethal). Bren (AC 12, HP 8, fists +3, "
             "1d4 + 1) + 2x Regulars (AC 11, HP 6, fists +3, 1d4): brute force, ganging up on one "
             "or two heroes with fists, chairs, and one regrettable mug. Osric steps in if it gets "
             "too hot; a downed hero wakes in a minute with cider on the house."),
    ("body", "**FIGHT 2: The Stone Circle** (Hard; the stones are the puzzle). Duckleaf (AC 15, "
             "HP 52, fly 30 ft; RESISTS slashing & bludgeoning): opens Aerial Slash +5 (3d6 + 3) at "
             "range, Winged Leap skips 30 ft out of melee without provoking, saves Quack of Fury "
             "(rech 5-6; 15 ft, DC 14 Wis, frightened) for a bunched party. THE RULE: disrupt one "
             "circle stone (Arcana or Nature DC 14 to see why) and Winged Leap is gone for the "
             "fight; ladder the hints if they stall. THE OUT: it is a guardian, not a hunter; "
             "heroes who withdraw are allowed to leave."),
    ("body", "**FIGHT 3: The Grove** (Medium; stern, never lethal). Cognifin (AC 14, HP 45, hover; "
             "RESISTS cold & psychic; Psychic Shield reaction +2 AC): Water Pulse +4 (2d6 + 2, "
             "DC 12 Str or prone) on the closest hero, Headache Blast +4 (2d6 + 2 psychic) on the "
             "back line, Confusion Pulse (rech 5-6; 15 ft, DC 13 Wis) when they bunch; legendary "
             "waters between turns (whirlpool: DC 12 Str, restrained / tidal wave: 2d4, push 5 ft). "
             "THE RULE: disturbing the pond's surface (spell, splash, thrown rock) silences the "
             "legendary waters for a round. THE OUT: a dropped hero washes gently to the bank, "
             "stable; a beaten party wakes at the grove's edge, free to try again once rested."),
    ("body", "**FIGHT 4: The Foggy Road** (Medium; fear is the weapon). 2x Mist Stalker (AC 13, "
             "HP 39, Speed 40 ft; Stealth +5): Fog Cloak (bonus action) for heavy obscurement, then "
             "bite +5 (1d8 + 3) and claw +5 (2d4 + 3); Howl of the Mist (rech 5-6; 30 ft, DC 13 "
             "Wis, frightened) rolls in from every direction at once. THE RULE: they will not leave "
             "their fog; a strong wind or a gust of magic thins the mist and steals their cover and "
             "their nerve. THE OUT: heroes who regain the road and keep moving escape them."),

    ("h1", "The Resource Picture"),
    ("body", "▶ Level 3, fresh, and no rest until Oakshade: the brawl costs nothing but pride, "
             "so the real spend is the forest. Duckleaf and Cognifin land back to back; watch "
             "Stabby's focus and Ursa's slots between them, and remember Cognifin's test cannot "
             "kill (a fallen hero washes ashore, stable). The Mist Stalkers hunt a tired party at "
             "dusk, and the frightened condition is the real drain in every fight, so celebrate "
             "the saves. The night at the Old Oak Tavern (5 silver a head) is a full long rest, "
             "and Oakshade sells the restock: Potion of Healing 50 gp, antitoxin 25 gp, Moonroot "
             "75 gp, a silvered weapon for 100 gp, with Merwin's 50 gp bounty there to pay for it."),

    ("h1", "Spotlights & Seeds: every kid shines, every door gets planted"),
    ("body", "**Lilly:** her arrival opens the whole chronicle: the Essence Sphere and the name "
             "Ursa Catchum (Door: wake Pikachu) → the brawl: gadgets that spark and startle "
             "→ the Duckleaf duel: she reads the rippling stones and shouts the secret "
             "(“the circle is feeding it!”) → after the mote, the session's thesis "
             "is hers: “Something is leaking into our world.”"),
    ("body", "**Stabby:** the BANG of the tavern door is his overture → the brawl is his "
             "stage: he fights like a rumor, everywhere and nowhere → faster than Duckleaf's "
             "wind, laughing on Cognifin's slick stones → seeds: the Bloodfang Clan and Master "
             "Kaelon in his introduction (Door: the clan catches up with him in Session 2)."),
    ("body", "**Ursa:** a stranger asking for him BY NAME pulls him in from the fields → one "
             "piece of bread wins the party its first friend → his starlight finds Duckleaf "
             "wherever it lands → seeds: Ash Catchum's disappearance and the three enchanted "
             "potatoes (Door: his father's trail), and the stars that have been waiting for this "
             "evening."),

    ("h1", "Foreshadow Tracker: say it, then say it again"),
    ("body", "▶ The tells, in order. Tavern hum x3 (Jarek's glow, strange winds, “the "
             "forest is waking up”) • Osric: “like they wandered in from... "
             "somewhere else” • Rhea: glowing eyes by the pond • wildflowers bloom "
             "out of season wherever Lickgloom walks • the MOTES, one per fallen planar "
             "creature: green wind (Duckleaf) → blue water (Cognifin) → twin fey glimmers "
             "(the Stalkers); Arcana DC 14 names the pattern • Merwin: “the planes are "
             "bleeding together” • the missing villagers: Session 2 walks in the door."),

    # ------------------------------------------------------------------
    # APPENDIX II: the bestiary (Session 7 format).
    ("appendix_title", "APPENDIX", "Bestiary: Enemy Stat Blocks",
     "All four encounters of Session 1, in the order the party meets them, plus one friend made "
     "along the way."),

    ("fight_header", "ENEMIES, Fight 1: The Bar Brawl",
     "The Gilded Acorn ✦ Difficulty: Easy ✦ 1x Bren + 2x Regulars"),
    ("enemy_cards", [
        {
            "name": "Bren, the Rowdy Local",
            "sub": "Medium humanoid ✦ bandit stats, softened for a friendly brawl",
            "img": "assets/npcs/bren_rowdy_local.png", "img_w": 2.6,
            "stats": [
                "**AC** 12  **HP** 8  **Speed** 30 ft",
            ],
            "traits": [
                ("Non Lethal Brawler", "All of Bren's damage is non lethal. A hero reduced to "
                 "0 HP wakes a minute later with a bruised ear and a mug of cider on the house."),
            ],
            "actions": [
                ("Unarmed Strike", "*Melee Attack:* +3 to hit, reach 5 ft. *Hit:* 1d4 + 1 "
                 "bludgeoning damage (a fist, a chair, or one regrettable mug)."),
            ],
        },
        {
            "name": "Tavern Regular",
            "sub": "Medium humanoid ✦ bandit stats, softened ✦ 2 in the brawl",
            "img": "assets/npcs/tavern_regular.png", "img_w": 2.6,
            "stats": [
                "**AC** 11  **HP** 6  **Speed** 30 ft",
            ],
            "traits": [
                ("Non Lethal Brawler", "All damage in the brawl is non lethal; a downed hero "
                 "wakes a minute later, embarrassed but unhurt."),
            ],
            "actions": [
                ("Unarmed Strike", "*Melee Attack:* +3 to hit, reach 5 ft. *Hit:* 1d4 "
                 "bludgeoning damage."),
            ],
        },
    ]),
    ("tactics", "Bren and his friends are not skilled fighters; they rely on brute force, ganging "
                "up on one or two heroes at a time. Strictly non lethal: fists, chairs, and one "
                "regrettable mug. Waving Bren off only makes him louder, so let the fight come to "
                "the table, and have Osric step in if things get too hot. The point of the scene "
                "is three strangers fighting together for the first time, and winning."),
    # Lore of Elaria: L10, filling the bar-brawl card page's deep tail; the
    # vale that builds its tavern first, under the tavern brawl stat blocks.
    ("lore", "The Vale Villages",
     "The villages of Eldridge Vale were founded by families who followed the Warden's star "
     "west until it set behind friendly hills, then stopped. Every village in the vale still "
     "builds its tavern first and its walls never, which tells you everything about the "
     "thousand years the vale has had."),

    ("fight_header", "ALLIES: Lickgloom",
     "The Whispering Pond ✦ Befriended with bread and patience ✦ Fey companion"),
    ("enemy_cards", [
        {
            "name": "Lickgloom",
            "sub": "Small fey (Feywild), neutral ✦ CR 1 (200 XP)",
            "img": f"{A}/monsters/lickgloom.png",
            "img_w": 3.0,
            "banner": "1F7A78",
            "stats": [
                "**AC** 13 (natural armor)  **HP** 27 (5d6 + 10)  **Speed** 30 ft",
                "**STR** 14  **DEX** 12  **CON** 14  **INT** 6  **WIS** 10  **CHA** 8",
                "**Saves** Dex +3  **Skills** Perception +2, Stealth +4",
                "**Resist** acid, poison",
                "**Senses** darkvision 60 ft, passive Perception 12",
                "**Languages** understands Common but cannot speak; telepathic impressions",
                "**Challenge** 1 (200 XP)",
            ],
            "traits": [
                ("Helpful Tongue", "Traveling with the party, Lickgloom can fetch small objects "
                 "with its 10 foot tongue, and once per scene its tasting tongue grants one hero "
                 "advantage on a Wisdom (Perception) or Intelligence (Investigation) check."),
            ],
            "actions": [
                ("Tongue Whip", "*Melee Attack:* +4 to hit, reach 10 ft. *Hit:* 1d6 + 2 "
                 "bludgeoning damage, and the target must succeed on a DC 12 Strength saving "
                 "throw or be grappled (escape DC 12)."),
                ("Sticky Lick (Recharge 5-6)", "One creature within 10 ft must succeed on a "
                 "DC 13 Dexterity saving throw or lose one small item (a weapon, potion, or "
                 "trinket), which Lickgloom pulls to itself."),
                ("Lick Attack", "*Melee Attack:* +4 to hit, reach 5 ft. *Hit:* 1d8 + 2 "
                 "bludgeoning damage, and the target must succeed on a DC 12 Constitution "
                 "saving throw or be stunned until the end of its next turn."),
            ],
        },
    ]),
    ("tactics", "Not an enemy: curious, playful, and hungry for new tastes. It meets aggression by "
                "darting into the pond, and it meets bread by joining the party. In a fight it "
                "stays behind its friends and helps how it can; at the grove it hauled a hero out "
                "of a whirlpool with one heroic tongue."),

    ("fight_header", "ENEMIES, Fight 2: The Stone Circle",
     "The Forest of Whispers ✦ Difficulty: Hard ✦ 1x Duckleaf, guardian of the circle"),
    ("enemy_cards", [
        {
            "name": "Duckleaf",
            "sub": "Small beast (Elemental Air), neutral ✦ CR 4 (1,100 XP)",
            "img": f"{A}/monsters/duckleaf_stone_circle.png",
            "img_w": 3.2,
            "stats": [
                "**AC** 15 (natural armor)  **HP** 52 (8d8 + 16)  **Speed** 30 ft, fly 30 ft",
                "**STR** 14  **DEX** 16  **CON** 14  **INT** 10  **WIS** 12  **CHA** 10",
                "**Saves** Dex +5, Wis +3  **Skills** Acrobatics +5, Perception +3",
                "**Resist** slashing, bludgeoning (wind sheath)",
                "**Senses** darkvision 60 ft, passive Perception 13",
                "**Languages** telepathy 30 ft (quacks)",
                "**Challenge** 4 (1,100 XP)",
            ],
            "traits": [
                ("Winged Leap", "Duckleaf can leap 30 ft in any direction without provoking "
                 "opportunity attacks, riding the wind to evade and reposition. If a stone of "
                 "the circle is damaged or disrupted, it loses this trait for the rest of the "
                 "battle."),
            ],
            "actions": [
                ("Leek Strike", "*Melee Attack:* +6 to hit, reach 5 ft. *Hit:* 2d8 + 4 slashing "
                 "damage, the wind guiding the blow with deadly accuracy."),
                ("Aerial Slash", "*Ranged Attack:* +5 to hit, range 20/60 ft. *Hit:* 3d6 + 3 "
                 "slashing damage from a blade of sharpened air."),
                ("Quack of Fury (Recharge 5-6)", "A telepathic quack reverberates through the "
                 "clearing. Each creature within 15 ft must succeed on a DC 14 Wisdom saving "
                 "throw or be frightened for 1 minute; a frightened creature repeats the save "
                 "at the end of each of its turns."),
            ],
        },
    ]),
    ("tactics", "It opens with Aerial Slash from range, uses Winged Leap to skip away from melee "
                "without provoking, and saves Quack of Fury for a bunched-up party. The circle is "
                "the fight: wind visibly streams from the stones to the duck each time it leaps, "
                "and disrupting one stone grounds it; it defends the stones fiercely once it "
                "realizes what the heroes are doing. A guardian, not a hunter: heroes who heed the "
                "warning may withdraw, and it never pursues beyond the stones."),
    # Lore of Elaria: W5, on the Duckleaf card page; why the stone rings
    # stand, and why they come with guardians.
    ("lore", "The Stone Rings",
     "The standing stones scattered across the vales are older than every road. Each ring "
     "was raised where a plane leans close to the world, and each was given a guardian, "
     "feathered, finned, or worse, to keep the leaning from becoming a fall."),

    ("fight_header", "ENEMIES, Fight 3: The Grove of Elemental Waters",
     "The Forest of Whispers ✦ Difficulty: Medium ✦ 1x Cognifin, the guardian's test"),
    ("enemy_cards", [
        {
            "name": "Cognifin",
            "sub": "Small beast (Elemental Water), neutral guardian ✦ CR 3 (700 XP)",
            "img": f"{A}/monsters/cognifin_grove.png",
            "img_w": 3.2,
            "stats": [
                "**AC** 14 (natural armor)  **HP** 45 (6d8 + 18)  **Speed** 0 ft, fly 30 ft (hover)",
                "**STR** 10  **DEX** 14  **CON** 16  **INT** 10  **WIS** 14  **CHA** 12",
                "**Saves** Dex +4, Wis +4  **Skills** Perception +4, Arcana +2",
                "**Resist** cold, psychic",
                "**Senses** darkvision 60 ft, passive Perception 14",
                "**Languages** telepathy 60 ft (images and feelings)",
                "**Challenge** 3 (700 XP)",
            ],
            "actions": [
                ("Headache Blast", "*Ranged Attack:* +4 to hit, range 30 ft. *Hit:* 2d6 + 2 "
                 "psychic damage, a crush of pressure inside the mind."),
                ("Water Pulse", "*Ranged Attack:* +4 to hit, range 30 ft. *Hit:* 2d6 + 2 "
                 "bludgeoning damage, and the target must succeed on a DC 12 Strength saving "
                 "throw or be knocked prone by the crashing wave."),
                ("Confusion Pulse (Recharge 5-6)", "A wave of psychic energy in a 15 ft radius. "
                 "Each creature in the area must succeed on a DC 13 Wisdom saving throw or be "
                 "confused (as the confusion spell) for 1 minute; repeat the save at the end of "
                 "each turn."),
            ],
            "reactions": [
                ("Psychic Shield", "When hit by an attack, Cognifin raises a shimmering barrier, "
                 "gaining +2 AC until the start of its next turn."),
            ],
            "legendary": [
                ("Waters of the Grove", "At the end of any hero's turn, Cognifin commands the "
                 "pond: **Whirlpool** (5 ft radius; DC 12 Strength save or be pulled 10 ft to "
                 "the center and restrained until the end of its next turn) or **Tidal Wave** "
                 "(10 ft line; DC 12 Dexterity save or take 2d4 bludgeoning damage and be "
                 "pushed back 5 ft)."),
            ],
        },
    ]),
    ("tactics", "It opens with Water Pulse to knock the closest hero prone, peppers the back line "
                "with Headache Blasts, and looses Confusion Pulse when the party groups up, while "
                "its legendary waters pull heroes into whirlpools or shove them back between "
                "turns. Disturbing the pond's surface (a spell, a splash, a well-thrown rock) "
                "breaks its focus and silences the waters for a round. The test is stern but never "
                "lethal: a hero who drops is washed gently to the bank, stable, and a party that "
                "falls or yields wakes at the grove's edge, free to try again once rested."),

    ("fight_header", "ENEMIES, Fight 4: The Foggy Road",
     "The Road to Oakshade ✦ Difficulty: Medium ✦ 2x Mist Stalker"),
    ("enemy_cards", [
        {
            "name": "Mist Stalker",
            "sub": "Medium fey (Feywild), unaligned ✦ CR 2 (450 XP) ✦ 2 in the ambush",
            "img": f"{A}/monsters/mist_stalker.png",
            "img_w": 3.2,
            "stats": [
                "**AC** 13  **HP** 39 (6d8 + 12)  **Speed** 40 ft",
                "**STR** 14  **DEX** 16  **CON** 14  **INT** 6  **WIS** 12  **CHA** 8",
                "**Skills** Perception +3, Stealth +5",
                "**Senses** darkvision 60 ft, passive Perception 13",
                "**Challenge** 2 (450 XP)",
            ],
            "traits": [
                ("Fog Cloak (Bonus Action)", "The stalker wraps itself in mist, becoming heavily "
                 "obscured until the start of its next turn."),
            ],
            "actions": [
                ("Multiattack", "The mist stalker makes one bite attack and one claw attack."),
                ("Bite", "*Melee Attack:* +5 to hit, reach 5 ft. *Hit:* 1d8 + 3 piercing damage."),
                ("Claw", "*Melee Attack:* +5 to hit, reach 5 ft. *Hit:* 2d4 + 3 slashing damage."),
                ("Howl of the Mist (Recharge 5-6)", "A howl rolls through the fog from every "
                 "direction at once. Each enemy within 30 ft must succeed on a DC 13 Wisdom "
                 "saving throw or be frightened until the end of the stalker's next turn."),
            ],
        },
    ]),
    ("tactics", "Each stalker wraps itself in Fog Cloak and strikes from heavy obscurement, and "
                "their howls hunt for frightened, scattered prey. They will not leave their fog: "
                "heroes who regain the road and keep moving escape them, and a strong wind or a "
                "gust of magic that thins the mist steals their cover and their nerve. Two motes "
                "of fey energy glimmer where they fall."),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    out = build_doc(BLOCKS, "sessions/session_01_gathering_of_friends.docx")
    print("built", out)
