# build_session_04.py
# The Guardians of Elaria, Session 4: Awakening to Shadows and Songs
# Publication build. Canon: memory/campaign_canon.md + CONTRADICTIONS.md rulings
# (C1 party at level 4; C7 the abducted Finn vs the orphan Milo, renamed;
# Doran Bramblebeard is one person; Faelan is the village lorekeeper in his
# ivy cottage; the Krampusshade is banished at the end).
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
BLOCKS = [
    ("titlepage", "THE GUARDIANS OF ELARIA", "SESSION 4",
     "Awakening to Shadows and Songs",
     "An illustrated adventure. Read the gold boxes aloud; the purple boxes are for the DM."),

    ("h1", "Previously, on The Guardians of Elaria..."),
    ("gold", "At **Ravenstone Laboratory**, Professor Aelwyn studied the Essence Sphere and gave "
             "the party a road: to **Gearhaven**, the clockwork city, where artificers might build "
             "what a sleeping spark needs. A leafy new friend, **Floraburst**, chose the party as "
             "much as they chose her, and gentle Lickgloom stayed behind with the professor, happily "
             "licking everything in the laboratory in farewell."),
    ("gold", "The road south was long and wild: a shadow with three false faces in Brambleshadow "
             "Thicket, displacer beasts that spoke when they should not, mushroom wardens guarding "
             "a glowing grove. And at **Stormwatch Cliffs**, an old puzzle opened an old door, and a "
             "vision poured out: a **Dark Figure** working at the walls of the world, wanting them "
             "broken. The party carried that cold picture down the last hill and into the warm "
             "lantern light of **Havenmoor**, a harbor town dressed head to toe for its winter "
             "festival, where they found beds at the Sugarplum Hearth and slept to the sound of "
             "carolers. And then, morning."),
    ("dm", "The heroes begin this session at **level 4**, grown by the long road south."),

    # ------------------------------------------------------------------
    ("h1", "Part One: The Morning the Music Changed", {"pagebreak": True}),
    ("gold", "The morning chill seeps through the windows of your rooms at the **Sugarplum Hearth**. "
             "Dawn is only a pale gray promise, and for a moment all seems calm. Then a sound "
             "threads through the silence: crying. Somewhere below, out in the snow, a woman is "
             "sobbing as if her heart has cracked in half."),
    ("gold", "From the window, the scene outside chills you more than the frosted air. In the "
             "snow-covered street, a group of children stands huddled together, their eyes vacant "
             "and far away. Their small voices rise together in a quiet, sing-song rhyme:"),
    ("gold", "*“On the coldest night, when the stars don't shine,*\n"
             "*The shadow creeps past the twisted pine.*\n"
             "*A jingle, a rattle, a claw and a grin,*\n"
             "*It takes the lost ones, then fades to the wind.”*"),
    ("gold", "The melody lingers, unsettling in its simplicity. The children are not playing. They "
             "are caught in something, like sleepwalkers singing in a dream."),
    ("gold", "Near them, a woman kneels in the snow, clutching a small, empty mitten. Her cry cuts "
             "the morning like a knife: **“They took him! My boy... he is gone! The shadows took "
             "my little Finn!”** Villagers gather, pale and hushed, their eyes darting to the dark "
             "line of the forest, as if even speaking of the shadows might call them back."),

    ("h2", "Greta's Warning"),
    ("gold", "**Greta Frostbough**, the stout dwarf keeper of the Sugarplum Hearth, draws the party "
             "inside to the warmth, her kind face lined with worry. “There is something terribly "
             "wrong this winter. The stories we tell to scare the young... they are becoming real. "
             "The children feel it. That song they are singing is an old rhyme about the "
             "**Krampusshade**, a shadow that takes children on the longest nights.”"),
    ("gold", "She reaches beneath the bar and pulls out a worn map of Havenmoor, its edges lightly "
             "singed. “There are **eight bells** hidden around this town, ancient holiday relics "
             "meant to keep the darkness away. Find them all and ring them together, and maybe, "
             "just maybe, we can drive back the shadows. Search these places, and talk to the "
             "people there. Hurry, before more children vanish into the night.”"),
    ("gold", "Four places are marked in vivid old ink: the **Sugarplum Hearth** itself, the "
             "**Frostwind Market Square**, the **Hollow Hearth Orphanage**, and the **Wyrmgale "
             "Lighthouse**. Two bells wait at each, eight notes of one unfinished song."),
    ("gold", "Outside, the festive cheer of Havenmoor has become a brittle mask. The party looks "
             "at the empty mitten in the mother's hands, and the choice makes itself."),

    # ------------------------------------------------------------------
    ("h1", "Part Two: The Hunt for the Winter Bells", {"pagebreak": True}),
    ("bridge", "Map in hand, the four friends went bell hunting through a frightened town, and "
               "found that every bell came wrapped in a story."),

    ("h2", "The Sugarplum Hearth: C and D"),
    ("gold", "The search begins at home. The tavern is all warmth and cinnamon, garlands of holly "
             "on the rafters, a decorated tree glittering in the corner, and above the crackling "
             "hearth, gleaming quietly in plain sight, hangs an old brass bell: the **C Bell**. "
             "Greta lifts it down herself. “It has watched over this room longer than I have. "
             "Take it, and bring it back singing.”"),
    ("gold", "By the fire, **Elda Merrywhistle**, a cheerful half-elf bard, strums her lute and "
             "hums. “The songs we sing tonight are meant to bring joy. But some songs are darker. "
             "You have heard the one the children sing?” She plays a few notes of an old ballad, "
             "the Lay of the Longest Night, about a shadow that steals children when joy turns to "
             "fear. At the corner table, **Captain Torren Windward**, a weathered sailor, stares "
             "into his mug. “Strange lights dance on the cliffs at night. I have seen ships "
             "swallowed by mist and shadow. Stay off the sea after dark, if you are smart.”"),
    ("gold", "It is Floraburst who finds the second bell, rustling her leaves at an ornate wreath "
             "above the bar until sharp eyes spot the glint of brass tucked deep in the pine "
             "branches: the **D Bell**. Greta blinks at it. “Huh. I thought we only had one.”"),
    ("dm", "Wisdom (Perception) DC 15 found the D Bell in the wreath. An old carved plaque above "
           "the bar, centuries old, shows a shadowy figure among pine trees and frightened "
           "children: the legend is far older than anyone living."),

    ("h2", "Frostwind Market Square: E and F"),
    ("gold", "The market square should be the happiest place in Havenmoor: stalls hung with snowy "
             "garland, the smell of roasted chestnuts and cinnamon pastries, and at the center a "
             "towering pine tree dressed in glass ornaments and golden ribbon. But the laughter "
             "here is forced, and every parent keeps one hand on a small shoulder."),
    ("gold", "The **E Bell** hangs from one of the pine's lower branches, silver, engraved with "
             "stars and snowflakes, chiming softly in the breeze as if it had been waiting to be "
             "noticed. When Ursa lifts it free, the cold air feels, for one breath, warmer."),
    ("gold", "The trail of the **F Bell** leads to the stall of **Eldric Bramblefoot**, a round "
             "little halfling merchant with a red woolen scarf and nervous eyes. “Festive cheer "
             "or not, there is something dark in those woods. I hear whispers at night. Not the "
             "wind. Something else.” Asked about bells, he digs through a box of decorations "
             "behind his stall and comes up holding a small brass bell patterned with holly. “A "
             "bell, you say? Well. If it helps bring back some peace, take it. Just... be careful "
             "out there.”"),
    ("gold", "Around the square, the party gathers more than bells. **Ingrid Stonegale**, the "
             "blunt dwarf blacksmith, remembers the old tales: “Last time the bells were gathered, "
             "the village was spared a terrible fate. We have not seen them in years. Maybe that "
             "is why things are going wrong now.” And **Lora Thistledown**, the gnome baker, "
             "shows them the strangest thing: frost blooming on her gingerbread cookies overnight, "
             "in a warm stall, which no winter she knows has ever done."),
    ("dm", "Charisma (Persuasion) DC 15 talked Eldric into parting with the F Bell willingly. "
           "Unnatural frost and vanishing footprints around the square hint that the shadow's "
           "reach is growing."),

    ("h2", "The Hollow Hearth Orphanage: G and A"),
    ("gold", "The orphanage stands at the town's edge, weathered but tidy, a creaking sign with a "
             "faded heart swinging in the wind. Inside, a small hearth crackles against a chill "
             "that never quite leaves, and the walls are covered in children's drawings. Some of "
             "the newest drawings show a dark, horned figure standing in doorways. **Sister "
             "Merida**, the caretaker, follows the party's eyes and lowers her voice. “They draw "
             "what they see. I wish they didn't. Something is wrong this winter. The nights feel "
             "colder. The shadows, longer.”"),
    ("gold", "In the attic, among old trunks and forgotten toys, a dusty toy chest holds the "
             "**G Bell**, brass etched with tiny snowflakes, nested between stuffed animals like "
             "a secret someone hid for safekeeping. As Lilly lifts it out, a whisper seems to "
             "drift through the rafters: *the bells keep us safe... don't lose them.*"),
    ("gold", "The last bell in the orphanage is not hidden at all. A small boy of about six, "
             "tousle-haired, sits in the corner clutching a threadbare teddy bear in one arm and "
             "a little silver bell in the other fist, humming the eerie rhyme under his breath. "
             "His name is **Milo**, and he will not let go. “He comes when it's dark,” Milo "
             "whispers. “With bells that jingle. I don't want to go with him.”"),
    ("gold", "So the heroes sit down on the floor with him. Stabby makes his very best silly "
             "faces. Floraburst produces a bright berry from her leaves. Ursa tells him, quietly, "
             "that bells are like stars: little lights the dark cannot put out, and that this one "
             "will fight better in brave hands. Milo looks at each of them for a long moment, "
             "then opens his fist. The **A Bell** chimes softly as it changes hands, and for a "
             "heartbeat every shadow in the room stands a little farther away. Milo sings them "
             "one more verse, the one the grown-ups have not heard:"),
    ("gold", "*“When the bells fall silent, the cold will creep,*\n"
             "*Shadows gather, and children weep.*\n"
             "*Ring the light, banish the shade,*\n"
             "*Or into the night, we'll be afraid.”*"),
    ("dm", "Calming Milo took gentleness, not dice: Charisma (Persuasion) DC 14 with advantage "
           "for kindness. Intelligence (Investigation) DC 15 found the G Bell in the attic toy "
           "chest."),

    ("h2", "The Wyrmgale Lighthouse: B and High C"),
    ("gold", "Last comes the lighthouse, tall and steadfast on the cliffs, battered by wind and "
             "salt spray, its beacon struggling against a mist that does not behave like mist. "
             "The keeper meets them at the door: **Old Doran Bramblebeard**, Havenmoor's "
             "shipwright, a tall, wiry man in an oilskin coat who tends the Wyrmgale light in "
             "winter because, as he puts it, nobody else has the stomach for it. “Storms rage "
             "out at sea, but sometimes the real danger comes from the shadows that walk these "
             "cliffs. Watch the light. Mind the dark.”"),
    ("gold", "The **B Bell** hangs from a rusted iron hook near the very top of the tower, past "
             "a rickety ladder and footing slick with spray, chiming a strangely mournful note "
             "in the wind. Stabby, naturally, is up and back before anyone can say *be careful*, "
             "the bell cold as the sea in his hand, engraved with swirling waves."),
    ("gold", "The eighth bell hides in the storeroom at the lighthouse's base, among old nets "
             "and salt-crusted rope. A faint hum of magic leads Lilly to a large tarnished "
             "ship's bell resting on a crate, and nestled inside it, like a pearl in an oyster, "
             "the **High C Bell**, etched all over with tiny stars. When she lifts it free it "
             "rings one pure, clear note, and light flickers across the old ship's bell as if "
             "the stars themselves acknowledged the find."),
    ("gold", "Doran walks them out, squinting at the horizon. “Eight bells, eh? Then it is real, "
             "and it is bad. Go see **Faelan**, the lorekeeper. And when this is over, come find "
             "me at the shipyard. I have something on the stocks you will want to see.”"),
    ("dm", "Strength (Athletics) DC 15 for the climb to the B Bell; Intelligence (Arcana) DC 14 "
           "sensed the magic hiding the High C Bell in the storeroom. All eight Winter Bells: "
           "C, D, E, F, G, A, B, High C."),

    # ------------------------------------------------------------------
    ("h1", "Part Three: The Lorekeeper's Tale", {"pagebreak": True}),
    ("bridge", "With eight bells wrapped warm in their packs, the heroes crossed town as the light "
               "failed, to a small cottage swallowed in ivy at the edge of Havenmoor."),
    ("gold", "The door creaks open before anyone can knock. **Faelan**, the village lorekeeper, "
             "is an elderly half-elf with long silver hair and piercing violet eyes, wrapped in a "
             "deep green cloak stitched with symbols of winter and renewal. “Welcome, brave ones. "
             "You have done well to gather the bells: relics of light and hope. Please, come in. "
             "We have much to discuss.”"),
    ("gold", "Inside, the cottage smells of herbs, pine, and old parchment. Shelves of ancient "
             "tomes and glowing crystals hum with stories. Faelan sets a wooden tray before the "
             "party: three **frosted cookies**, each shimmering faintly with magic. “Take these. "
             "They will warm your bodies and spirits in the trials ahead.”"),
    ("dm", "**Faelan's Frosted Cookies.** Each restores 2d8 HP, grants the benefit of a short "
           "rest, and restores one expended spell slot. Cookie-based healing: the finest kind."),
    ("gold", "Then the old lorekeeper settles into his chair, and his eyes darken. “Long ago, "
             "when winter nights seemed endless, the people of Havenmoor called on the light of "
             "the **Winter Bells**. The bells hold the blessing of **Elaria**, goddess of hope "
             "and protection. Rung in harmony, they drive back the shadows.” His fingers trace "
             "a symbol on his staff. “But there was one who thrived in the cold and dark. The "
             "**Krampusshade**. Once a guardian of winter, twisted by bitterness and envy, he "
             "turned against the light. He feasts on fear. He steals the joy of children and "
             "traps their laughter in a sack of shadows. The bells are the key to weakening him, "
             "for they carry the last remnants of Elaria's light here.”"),
    ("gold", "He spreads a weathered map and taps three places in the wilderness around "
             "Havenmoor, one, two, three. “His power is anchored by three **barriers of "
             "darkness**. The **Frostpine Glade**, where ancient pines have twisted under frost "
             "and shadow. The **Crystalbrook Stream**, where dark tendrils lurk beneath the ice. "
             "The **Whispering Hollow**, where the very stones whisper despair. Travel to each. "
             "Ring the bells. Shatter the barriers. Only then can the Krampusshade be banished "
             "for good. His minions will not let you pass easily. But I have faith in you. You "
             "carry the light of hope, even in the deepest winter.”"),
    ("gold", "Faelan raises his hands, and a soft silver light washes over each of you, warmth "
             "seeping into your bones. “Go now, brave souls. May the bells guide you, and may "
             "Elaria's light shield you from the shadows.”"),

    # ------------------------------------------------------------------
    ("h1", "Part Four: The Three Barriers of Darkness", {"pagebreak": True}),
    ("bridge", "Three marks on a map, eight bells, and one long winter day: the heroes went out "
               "into the white silence to take the Krampusshade's power apart, one song at a time."),

    ("h2", "The Frostpine Glade: Jingle Bells"),
    ("gold", "The pines around the glade creak under armor of ice, and the mist between them "
             "curls as though alive. At the center stands a massive frozen pine, its trunk twisted "
             "and blackened, jagged chains of black ice wrapped around its roots. On the wind ride "
             "faint, mournful whispers: the far-off cries of taken children. The black ice pulses "
             "with a sickly blue light, humming a low, wrong-noted mockery of a holiday tune."),
    ("gold", "The answer is the true song. The heroes line up their bells and play it the way it "
             "was always meant to sound: **Jingle Bells**, bright and defiant in the dead air. On "
             "the last note, golden light bursts from the bells and rolls through the black ice, "
             "and the chains shatter with a crack that shakes snow from every branch."),
    ("gold", "The mist answers back. It gathers itself into three snarling shapes: **Frozen "
             "Wolves**, frost-armored, eyes burning icy blue, guardians grown from the "
             "Krampusshade's own cold. The fight is knives and starlight on slick ground, wolf "
             "breath rolling white and freezing, until the last wolf comes apart into glittering "
             "mist, and the glade breathes again."),
    ("dm", "The carol lock: E E E, E E E, E G C D E, F F F F, F E E E. Then **3 Frozen Wolves** "
           "(pack tactics, icy ground). First barrier down."),

    ("h2", "The Crystalbrook Stream: Deck the Halls"),
    ("gold", "The stream winds through a grove of silver-barked trees, its water glittering "
             "under a skin of ice. A rickety wooden bridge crosses at the narrows, and beneath "
             "it, dark tendrils snake along the underside of the planks, pulsing. Shadowy shapes "
             "flicker under the ice, faces twisted in silent song. Frost blooms across the "
             "boards as the party steps up."),
    ("gold", "Eight bells ring out **Deck the Halls**, lively and warm, the notes echoing down "
             "the frozen water like skaters. The tendrils hiss, thrash once, and dissipate like "
             "smoke in sunlight. And then the treetops giggle. Four tiny figures dart into view "
             "on frost-covered wings, faces fixed in mischievous grins, fingers glowing with "
             "cold magic: **Frostbite Pixies**, flinging rays of frost and turning invisible "
             "mid-cackle. It is the silliest, slipperiest fight of the winter, and the party "
             "wins it laughing."),
    ("dm", "Second carol lock, then **4 Frostbite Pixies** (Ray of Frost, invisibility, slick "
           "ice underfoot). Second barrier down."),

    ("h2", "The Whispering Hollow: Silent Night"),
    ("gold", "The last barrier waits between two snow-covered hills, in a hollow where the wind "
             "whistles words no one can quite make out. A ring of frost-covered standing stones "
             "rises at its heart, their old protective runes blackened and writhing. Above the "
             "stones churns a slow vortex of shadow, radiating waves of cold that sap warmth and "
             "hope together."),
    ("gold", "This song cannot be loud. The heroes play **Silent Night**, slow and gentle, each "
             "note held like a candle against the dark. The melody threads through the hollow, "
             "and gentle, radiant light washes over the standing stones. The vortex shrieks and "
             "dissolves; the blackened runes flicker, then glow their old protective silver."),
    ("gold", "From the last rags of shadow steps an **Icy Specter**, translucent and wreathed "
             "in frost, hollow eyes fixed on the intruders. It fights in whispers and cold "
             "hands, wailing despair at the heroes until Ursa's starlight burns through its "
             "center and it unravels on the wind. Where it stood, half-buried in the snow, lies "
             "a small blackened shard of standing stone that hums against the palm: a "
             "**Shadow-Touched Rune Fragment**."),
    ("dm", "Third carol lock, then the **Icy Specter** (Wail of Despair, DC 14 Wisdom). Boon: "
           "the **Shadow-Touched Rune Fragment**, advantage on saves against fear for 1 hour "
           "while held. Third barrier down."),

    ("h2", "The Krampusshade Awakens"),
    ("gold", "As the last barrier shatters, an unnatural silence grips the land. The wind dies. "
             "The cold bites deeper, down past skin, down to the brave part of you. Far off over "
             "Havenmoor, dark clouds swirl into a slow vortex that swallows the stars, and the "
             "festival lights of the town flicker and dim, one street at a time. From the "
             "gathering dark, two fiery red eyes flare open, and a deep voice oozes across the "
             "snow, dripping with mockery."),
    ("gold", "**Krampusshade:** “So. You think your bells and lights can banish me? Fools! I "
             "feast on despair, and there is plenty yet to devour.”"),
    ("gold", "The heroes look at each other for exactly one heartbeat. Then they run."),

    # ------------------------------------------------------------------
    ("h1", "Part Five: The Longest Night", {"pagebreak": True}),
    ("bridge", "Down out of the hills and along the frozen road the four friends raced the "
               "darkness home, eight bells jangling in their packs like a heart beating."),
    ("gold", "A thick, unnatural fog rolls through Havenmoor's streets, muffling sound and "
             "smearing the lantern light. The villagers are huddled at the Great Pine in the "
             "market square, clutching one another, the tree's festive lights guttering weakly "
             "against the dark. Somewhere a child's cry echoes, far away and getting farther."),
    ("gold", "Then thunder cracks the sky, and the fog peels back like a curtain. Out of the "
             "mist steps a towering figure, **ten feet of shadow and frost**: goat-horned, "
             "black-furred, icicles dripping from his curved horns, chains swinging from his "
             "clawed hands with a sound like cruel sleigh bells. Over his shoulder writhes a "
             "burlap sack, and from inside it come the muffled cries of children. The ground "
             "cracks with frost where he walks."),
    ("gold", "**Krampusshade:** “Your defiance ends here. I will feast on your fear, and the "
             "children shall be mine forever!”"),

    ("h2", "The Bells' Harmony"),
    ("gold", "He slams his claws together and freezing power rolls across the square; his "
             "chains lash out like serpents, and shadow imps come boiling up out of the fog "
             "around him, eyes burning. But the heroes did not come to be afraid. They came to "
             "finish a song."),
    ("gold", "While blade, bolt, claw, and starlight hold the imps back, bell after bell rings "
             "out through the fog, weaving into the one carol big enough for the moment: the "
             "**Carol of the Bells**, eight notes of Elaria's light striking through the dark "
             "like lantern beams. With every toll the Krampusshade flinches. Threads of shadow "
             "peel from his shoulders like smoke from a dying fire. His chains crack. His "
             "outline gutters like a candle flame."),
    ("gold", "Stabby rings a bell in one hand and parries a chain with the other. Lilly's "
             "turret keeps time like a drummer. Floraburst shakes her petals and adds one small, "
             "clear chime of her own. And on the final note, sung by eight bells in perfect "
             "harmony, the fiend's roar breaks in the middle."),
    ("gold", "The Krampusshade's body **shatters into wisps of shadow**, spiraling up and up "
             "and dissolving into the night sky, banished from the world he had grown too "
             "bitter to guard. The frost gripping the village begins to melt. The fog lifts. "
             "And the burlap sack drops to the snow and bursts open."),
    ("gold", "Children tumble out, dazed, blinking, rubbing their eyes, **every single one of "
             "them safe**, and in the middle of them a small boy with one missing mitten. "
             "**Finn** hits his mother's arms at a dead run, and the sound she makes is the "
             "opposite of the one that woke the heroes that morning."),
    ("dm", "The final battle: the **Krampusshade** (CR 5) with **shadow imps** rising from the "
           "fog, while the party rang the eight bells into the Carol of the Bells. Each "
           "completed phrase of the carol seared him; the eighth harmony unmade him."),

    ("h2", "The Village Rejoices"),
    ("gold", "The villagers pour out of hiding, laughing and crying at once. The Great Pine "
             "blazes brighter than it has all festival, and clean, untroubled snow begins to "
             "drift down out of a clearing sky. Greta Frostbough reaches the party first, eyes "
             "shining. “You have saved us all. The darkness has lifted, and hope shines once "
             "more.” Somewhere behind her, Milo is showing the other orphans exactly how the "
             "bells went, loudly, and mostly in tune."),

    ("h2", "Gifts of Gratitude"),
    ("gold", "As dawn breaks over Havenmoor, Faelan comes through the celebrating crowd with "
             "three carefully wrapped packages. “Tokens of our eternal gratitude. May they aid "
             "you on the journey ahead.”"),
    ("gold", "For **Lilly**, the **Frostbite Shard Dagger**: a blade of crystalline ice that "
             "never melts, glowing with faint blue arcane light, hungry to channel her spells."),
    ("img", f"{A}/characters/lilly_session4.png",
     "Lilly Glimmergear and the Frostbite Shard Dagger, on the brightest morning of the festival.", 4.4),
    ("gold", "For **Ursa**, the **Amulet of Guiding Light**: a polished silver starburst with a "
             "blue gem at its heart that pulses softly, like a distant star keeping watch."),
    ("gold", "And for **Stabby**, the **Candyfang Katana**: a katana of impossible candy-cane "
             "steel, red and white and wickedly sharp, trailing a faint scent of sugar. Stabby "
             "licks it immediately. It is delicious."),
    ("img", f"{A}/characters/stabby_cane.png",
     "Stabby Sharpblade and the Candyfang Katana. Yes, he licked it.", 4.4),
    ("dm", "Full statistics for all three gifts live in the treasures compendium."),
    ("gold", "Down at the harbor, the shipwright **Master Doran Bramblebeard**, lighthouse soot "
             "still on his sleeves, nods toward a trim vessel rocking at the dock. “The "
             "**Stormwind** is ready when you are. Gearhaven awaits.”"),
    ("divider",),
    ("bridge", "Their fourth adventure was done: a stolen child brought home, eight bells rung "
               "into one great carol, a bitter old shadow banished into the dark between the "
               "stars, and a whole town's winter given back to it. The road to Gearhaven now ran "
               "over water, and the sea, as Captain Torren could have told them, keeps its own "
               "secrets."),
    ("gold", "*Next: Session 5, in which the Stormwind sails for Gearhaven, a storm has other "
             "plans, and a ghost ship rises from the deep with a captain who plays dice for "
             "souls.*"),

    # ------------------------------------------------------------------
    ("h1", "Appendix: Creatures of Session Four", {"pagebreak": True}),
    ("body", "Compact statistics for the table. The full bestiary, with lore and pictures, lives "
             "in the compendium."),
    ("stat", "Krampusshade", [
        "Large fiend, chaotic evil. **CR 5**. AC 15 (natural armor), HP 102 (12d10 + 36), Speed 40 ft.",
        "STR 18, DEX 14, CON 16, INT 12, WIS 14, CHA 17. Saves Wis +5, Cha +6.",
        "Resistances cold, necrotic, nonmagical weapons. Immunities poison; charmed, frightened, poisoned. Darkvision 120 ft.",
        "**Multiattack.** One Claw and one Chains of Despair.",
        "**Claw.** +7, reach 10 ft., 2d6 + 4 slashing plus 1d10 cold.",
        "**Chains of Despair.** +7, reach 15 ft., 2d6 + 4 bludgeoning; DC 14 Strength save or restrained one turn.",
        "**Gift of Despair (Recharge 5-6).** A cursed gift box, 30 ft.; DC 14 Wisdom save or frightened 1 minute.",
        "**Icy Retaliation (Reaction).** When hit in melee: DC 14 Constitution save or 2d6 cold, speed -10 ft.",
        "**Shadow Step (Legendary, 1/round).** Teleports up to 20 ft. within dim light or darkness.",
        "*Weakened by the eight Winter Bells rung in harmony; the completed Carol of the Bells unmade him.*",
    ]),
    ("stat", "Krampusshade's Imp", [
        "Small fiend (shadow), chaotic evil. **CR 2**. AC 14 (natural armor), HP 22 (5d6 + 5), Speed 30 ft., fly 40 ft.",
        "STR 10, DEX 16, CON 12, INT 13, WIS 11, CHA 14. Skills Stealth +6, Deception +4.",
        "Resistances cold, fire, necrotic, nonmagical weapons. Immunity poison. Magic Resistance. Darkvision 120 ft.",
        "**Shadow Stealth.** Hides as a bonus action in dim light or darkness. **Invisibility (3/short rest).**",
        "**Shadow Claws.** +5, reach 5 ft., 2d4 + 3 slashing plus 1d6 cold.",
        "**Shadowy Grasp (Recharge 5-6).** DC 13 Dexterity save or restrained one turn; 1d10 cold while held.",
    ]),
    ("stat", "Frozen Wolf", [
        "Medium beast, neutral evil. AC 15 (natural armor), HP 45 (6d10 + 12), Speed 40 ft.",
        "STR 16, DEX 15, CON 14, INT 3, WIS 12, CHA 6. Immune cold. Darkvision 60 ft.",
        "**Pack Tactics.** Advantage when an ally is within 5 ft. **Icy Terrain.** Difficult ground within 10 ft.",
        "**Bite.** +5, 2d6 + 3 piercing plus 1d8 cold; DC 13 Constitution save or speed -10 ft.",
        "**Frost Breath (Recharge 5-6).** 15 ft. cone, DC 13 Dexterity save; 4d8 cold, half on success, slowed on a failure.",
    ]),
    ("stat", "Frostbite Pixie", [
        "Tiny fey, chaotic neutral. **CR 1/4**. AC 15, HP 14 (4d4 + 4), Speed 20 ft., fly 60 ft.",
        "STR 3, DEX 20, CON 12, INT 14, WIS 11, CHA 16. Stealth +7. Immune cold.",
        "**Ray of Frost.** +5, range 60 ft., 2d8 cold; target's speed reduced 10 ft. one turn.",
        "**Invisibility.** Turns invisible until it attacks or casts a spell.",
    ]),
    ("stat", "Icy Specter", [
        "Medium undead, neutral evil. AC 12, HP 45 (10d8), Speed 0 ft., fly 50 ft. (hover).",
        "STR 1, DEX 14, CON 11, INT 10, WIS 10, CHA 16.",
        "Resistances cold, necrotic, nonmagical weapons. Immunity poison; charmed, exhaustion, grappled, paralyzed, poisoned, prone, restrained.",
        "**Chilling Touch.** +5, reach 5 ft., 3d6 cold.",
        "**Wail of Despair (Recharge 5-6).** 30 ft., DC 14 Wisdom save or frightened 1 minute (repeat save each turn).",
    ]),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    out = build_doc(BLOCKS, "sessions/session_04_shadows_and_songs.docx")
    print("built", out)
