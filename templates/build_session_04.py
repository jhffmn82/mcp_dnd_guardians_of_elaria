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

    # Dominant page-1 plate (DM request): the festival aerial leads the page
    # right under the title, Session-1 style; the recap flows after it.
    ("img", f"{A}/scenes/s4_havenmoor_town.png",
     "Havenmoor in its festival best, the Great Pine shining above the harbor.", 6.2,
     {"crop": "16:9", "hmax": 4.5}),

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
    ("h1", "Part One: The Morning the Music Changed"),
    ("gold", "The morning chill seeps through the windows of your rooms at the **Sugarplum Hearth**. "
             "Dawn is only a pale gray promise, and for a moment all seems calm. Then a sound "
             "threads through the silence: crying. Somewhere below, out in the snow, a woman is "
             "sobbing as if her heart has cracked in half."),
    # The singing children float right beside the rhyme itself (anchored high
    # so the image clears the bottom margin).
    ("imgfloat", f"{A}/scenes/s4_children_singing.png", 3.0),
    ("gold", "From the window, the scene outside chills you more than the frosted air. In the "
             "snow-covered street, a group of children stands huddled together, their eyes vacant "
             "and far away. Their small voices rise together in a quiet, sing-song rhyme:"),
    ("melody", "On the coldest night, when the stars don't shine, | "
               "The shadow creeps past the twisted pine. | "
               "A jingle, a rattle, a claw and a grin, | "
               "It takes the lost ones, then fades to the wind."),
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
             "Lighthouse**. Two bells wait at each, eight notes of one unfinished song. Greta "
             "presses the map into your hands. “Each bell holds a fragment of our hope. Find "
             "them all, and you may give us the light we need to face this darkness.”"),
    ("dm", "**The quest.** Find the eight holiday bells. Learn the truth behind the Krampusshade "
           "and the eerie song. Protect the village's children from being taken by the shadows."),
    ("gold", "Outside, the festive cheer of Havenmoor has become a brittle mask. The party looks "
             "at the empty mitten in the mother's hands, and the choice makes itself."),

    # ------------------------------------------------------------------
    ("h1", "Part Two: The Hunt for the Winter Bells"),
    ("bridge", "Map in hand, the four friends went bell hunting through a frightened town, and "
               "found that every bell came wrapped in a story."),

    ("h2", "The Sugarplum Hearth: C and D"),
    ("gold", "The search begins at home. The tavern is all warmth and cinnamon, garlands of holly "
             "on the rafters, a decorated tree glittering in the corner, and above the crackling "
             "hearth, gleaming quietly in plain sight, hangs an old brass bell: the **C Bell**. "
             "Greta lifts it down herself. “It has watched over this room longer than I have. "
             "Take it, and bring it back singing.”"),
    # Wintry establishing shot (DM request): the common room as a half-page
    # landscape plate instead of a small float.
    ("img", f"{A}/scenes/s4_sugarplum_hearth.png",
     "The Sugarplum Hearth, all warmth and cinnamon, the C Bell above the fire.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
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
    ("game", "The Hearth Bells: C and D", [
        "**The C Bell.** Hangs in plain sight above the crackling hearth, polished brass gleaming "
        "in the firelight. Greta gives it gladly to any hero who promises to help the village.",
        "**The D Bell.** Hidden deep in the ornate wreath above the bar. **Wisdom (Perception) "
        "DC 15** spots the glint of brass tucked within the pine branches.",
        "**Digging deeper.** **Wisdom (Insight) DC 14**: Greta's eyes keep flicking to the bell "
        "above the hearth, as if it holds more significance than decoration. **Intelligence "
        "(Investigation) DC 14**: a carved wooden plaque above the bar, centuries old, shows a "
        "shadowy figure lurking among pine trees while frightened children look on. "
        "**Intelligence (Arcana) DC 16**: a faint aura of abjuration magic clings to the C Bell. "
        "“That bell's older than it looks,” Elda says. “Maybe it's more than just decoration.”",
        "**Fireside stories.** **Intelligence (History) DC 15**: Elda recounts the full Lay of "
        "the Longest Night. **Wisdom (Survival) DC 13**: Captain Torren shares how to avoid the "
        "dangerous mists along the coast after dark.",
        "**Old lore.** The bells are said to have once belonged to a fey guardian who protected "
        "the village with music and light. Rung in harmony, they call down Elaria's protective "
        "light to banish the shadows. Greta has also heard whispers of planar rifts in the "
        "forest and strange creatures appearing, and Captain Torren swears the sea mists are "
        "no natural weather.",
    ]),

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
    # Wintry establishing shot (DM request): the market square as a half-page
    # landscape plate.
    ("img", f"{A}/scenes/s4_bell_hunt_market.png",
     "Bell hunting in Frostwind Market Square, under the towering festival pine.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "Around the square, the party gathers more than bells. **Ingrid Stonegale**, the "
             "blunt dwarf blacksmith, remembers the old tales: “Last time the bells were gathered, "
             "the village was spared a terrible fate. We have not seen them in years. Maybe that "
             "is why things are going wrong now.” And **Lora Thistledown**, the gnome baker, "
             "shows them the strangest thing: frost blooming on her gingerbread cookies overnight, "
             "in a warm stall, which no winter she knows has ever done."),
    ("game", "The Market Bells: E and F", [
        "**The E Bell.** Dangles from a low branch of the great festival pine, silver with stars "
        "and snowflakes. No check needed; it only wanted to be noticed. At a touch it chimes "
        "faintly, and for one breath the cold air feels warmer.",
        "**The F Bell.** Tucked in a box of festive decorations behind Eldric Bramblefoot's "
        "stall. **Charisma (Persuasion) DC 15** talks him into parting with it willingly, or "
        "**Dexterity (Sleight of Hand) DC 14** slips it free unnoticed. On a failure Eldric "
        "grows flustered and demands an explanation, and the party must reassure him before he "
        "will say another word.",
        "**Digging deeper.** **Wisdom (Insight) DC 13**: Eldric's fear is genuine; he has heard "
        "children's laughter at night where there should be none. **Intelligence (Investigation) "
        "DC 15**: footprints lead from the forest into the square and vanish mid-stride, and "
        "frost blooms overnight on Lora's cookies. **Intelligence (Arcana) DC 16**: a faint dark "
        "aura clings to the edges of the square, the sign of a thinning planar veil. "
        "**Intelligence (History) DC 14**: this square once hosted winter solstice rituals meant "
        "to guard the village from dark forces; on a 15 or higher, Ingrid's old tales surface "
        "too, of shadowy Krampus-like figures that snatch away the wicked on winter nights.",
    ]),

    # Page balance: the market plate + rules card fill their page; the
    # orphanage opens a fresh page (self-suppressing hardbreak, so
    # repagination can never strand a blank page).
    ("h2", "The Hollow Hearth Orphanage: G and A", {"hardbreak": True}),
    # The orphanage art leads the section and floats beside Merida and Milo.
    ("imgfloat", f"{A}/scenes/s4_orphanage_milo.png", 3.0),
    ("gold", "The orphanage stands at the town's edge, weathered but tidy, a creaking sign with a "
             "faded heart swinging in the wind. Inside, a small hearth crackles against a chill "
             "that never quite leaves, and the walls are covered in children's drawings. Some of "
             "the newest drawings show a dark, horned figure standing in doorways. **Sister "
             "Merida**, the caretaker, follows the party's eyes and lowers her voice. “They draw "
             "what they see. I wish they didn't. Something is wrong this winter. The nights feel "
             "colder. The shadows, longer.”"),
    ("gold", "She knows the old stories all too well. “They say the Krampusshade comes for "
             "children left alone in the cold. It whispers to them, offering twisted comforts, "
             "before it takes them away forever.” Her hand tightens on her shawl. “The bells, "
             "when rung together, were said to call down Elaria's light to protect us. Maybe... "
             "maybe they can do it again.”"),
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
    ("melody", "When the bells fall silent, the cold will creep, | "
               "Shadows gather, and children weep. | "
               "Ring the light, banish the shade, | "
               "Or into the night, we'll be afraid."),
    # Page balance: the verse ends the orphanage page well filled; the rules
    # card keeps together and jumps whole to the next page on its own.
    ("game", "The Orphanage Bells: G and A", [
        "**The G Bell.** **Intelligence (Investigation) DC 15** uncovers the forgotten toy chest "
        "in the dusty attic; the bell lies inside, etched with tiny snowflakes, nested among "
        "stuffed animals and broken dolls.",
        "**The A Bell.** In Milo's fist, and he will not let go. Calming him takes gentleness, "
        "not force: **Charisma (Persuasion) DC 14** or **Wisdom (Insight) DC 13**, with "
        "advantage for genuine kindness. On a failure Milo begins to cry, and Sister Merida "
        "gently asks the party to try again.",
        "**Once calmed.** Milo opens his hand, and the A Bell rings one soft, comforting chime "
        "that briefly pushes every shadow in the room away. Then he sings the verse the "
        "grown-ups have not heard.",
        "**Digging deeper.** **Wisdom (Insight) DC 14**: Sister Merida is far more afraid for "
        "the children than she lets show. **Intelligence (Arcana) DC 16**: the too-long shadows "
        "in the corners ripple with Shadowfell energy, leaking through a weakened planar "
        "barrier.",
    ]),

    ("h2", "The Wyrmgale Lighthouse: B and High C"),
    ("gold", "Last comes the lighthouse, tall and steadfast on the cliffs, battered by wind and "
             "salt spray, its beacon struggling against a mist that does not behave like mist. "
             "The keeper meets them at the door: **Master Doran Bramblebeard**, Havenmoor's "
             "shipwright, a tall, wiry man in an oilskin coat who tends the Wyrmgale light in "
             "winter because, as he puts it, nobody else has the stomach for it. “Storms rage "
             "out at sea, but sometimes the real danger comes from the shadows that walk these "
             "cliffs. Watch the light. Mind the dark.” He squints out at the mist beyond the "
             "breakers. “They say the sea swallows the lost and forgotten. But sometimes, the "
             "lost come back... twisted and hollow.”"),
    # Wintry establishing shot (DM request): the lighthouse as a half-page
    # landscape plate.
    ("img", f"{A}/scenes/s4_lighthouse.png",
     "The Wyrmgale Lighthouse, tall and steadfast on the cliffs.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
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
    ("game", "The Lighthouse Bells: B and High C", [
        "**The B Bell.** **Strength (Athletics) DC 15** to climb the last stretch of the tower, "
        "up a rickety ladder over footing slick with spray. Failure means a short slip and 1d6 "
        "bludgeoning damage, but the bell stays within reach.",
        "**The High C Bell.** **Intelligence (Arcana) DC 14** senses the faint magic humming "
        "inside the old ship's bell in the storeroom. Failure knocks something loose and "
        "startles a flock of gulls into a brief commotion, no harm done.",
        "**Digging deeper.** **Wisdom (Insight) DC 15**: Doran speaks in riddles to keep his own "
        "fear at arm's length. **Intelligence (History) DC 15**: ancient sailors believed the "
        "Krampusshade could walk on the mist itself, snatching children who wandered near the "
        "cliffs. **Intelligence (Arcana) DC 16**: the darkness pressing on the beacon is no "
        "natural gloom; it answers to the Shadowfell.",
        "**The chime completes.** With B and High C found, all **eight Winter Bells** are "
        "gathered: C, D, E, F, G, A, B, High C. One full octave, one unfinished song.",
    ]),
    # Lore of Elaria (F3): the bell hunt ends with eight odd little things
    # gathered from rafters, wreaths, and toy chests; the Circle's old rule
    # about scattered safeguards lands right here, filling the page tail
    # before the Frozen Roads open.
    ("lore", "The Scattered Safeguards",
     "No one has ever counted the safeguards, which is the point of scattering. Some hang in "
     "plain sight in tavern rafters. Some sleep in root cellars, humble as potatoes. The old "
     "rule of the Circle is: treat every odd little thing kindly, in case it is holding up "
     "the sky."),

    # ------------------------------------------------------------------
    # F1 (2026-07-27): the full "Frozen Roads" deck of chances moved to the
    # appendix (with its stat blocks) so the read-aloud story runs straight
    # from the bell hunt into the lorekeeper. A short bridge stays here.
    ("gold", "The roads around Havenmoor that week were thick with wonders and dangers. Not all "
             "of them crossed the heroes' path, but every one was out there, waiting in the white "
             "silence between the pines."),
    ("dm", "**The frozen roads.** Faelan's directions mark the three barriers only roughly, so "
           "whenever the party sets out from Havenmoor, to a barrier or back, roll on the winter "
           "travel table. The DM's full deck of chances, the d20 tables and every wandering "
           "wonder of the frozen roads, waits in the appendix at the back of this session."),

    # ------------------------------------------------------------------
    ("h1", "Part Three: The Lorekeeper's Tale"),
    ("gold", "As the last bell is collected, a strange hush falls over Havenmoor, and it is Greta "
             "who points the way. “Now that you've found the bells, there is one more person you "
             "need to speak with. **Faelan**, the village lorekeeper. He knows more about the "
             "darkness we face than anyone else.”"),
    ("bridge", "With eight bells wrapped warm in their packs, the heroes crossed town as the light "
               "failed, to a small cottage swallowed in ivy at the edge of Havenmoor."),
    ("gold", "The door creaks open before anyone can knock. **Faelan**, the village lorekeeper, "
             "is an elderly half-elf with long silver hair and piercing violet eyes, wrapped in a "
             "deep green cloak stitched with symbols of winter and renewal. “Welcome, brave ones. "
             "You have done well to gather the bells: relics of light and hope. Please, come in. "
             "We have much to discuss.”"),
    # The lorekeeper floats right beside his tale of the bells.
    ("imgfloat", f"{A}/npcs/faelan.png", 3.1),
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
             "for they carry the last remnants of Elaria's light here.” His eyes meet yours, "
             "somber and resolute. “The Krampusshade cannot be defeated by strength alone. You "
             "must use the bells to weaken him and break his hold over this land.”"),
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
    # Lore of Elaria (F5): Faelan has just told the table what the Winter
    # Bells are; the chronicler adds where they came from. Fills the deep
    # whitespace tail under the lorekeeper's page.
    ("lore", "The Bells of the Coast",
     "When the safeguards were scattered, eight fell along the southern coast as bells, each "
     "holding one clear note of the song Elaria sang while she worked. Havenmoor built its "
     "festival around them centuries before anyone remembered why the bells mattered. The "
     "town rang them every winter anyway. Traditions are how a town remembers what its "
     "people forget."),

    # ------------------------------------------------------------------
    ("h1", "Part Four: The Three Barriers of Darkness"),
    ("bridge", "Three marks on a map, eight bells, and one long winter day: the heroes went out "
               "into the white silence to take the Krampusshade's power apart, one song at a time."),

    ("dm", "**Any order.** The three barriers can be met in whatever order the party's exploring "
           "turns them up; the sites below are listed for convenience, not as a fixed sequence."),

    ("h2", "The Frostpine Glade: Jingle Bells"),
    ("gold", "The pines around the glade creak under armor of ice, and the mist between them "
             "curls as though alive. At the center stands a massive frozen pine, its trunk twisted "
             "and blackened, jagged chains of black ice wrapped around its roots. On the wind ride "
             "faint, mournful whispers: the far-off cries of taken children. The black ice pulses "
             "with a sickly blue light, humming a low, wrong-noted mockery of a holiday tune."),
    # The area shot leads the seal (DM request: show each place BEFORE the
    # song breaks its barrier); the carol scene floats beside the aftermath.
    ("img", f"{A}/scenes/s4_frostpine_glade.png",
     "The Frostpine Glade, its great pine bound in chains of black ice.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "The answer is the true song. The heroes line up their bells and play it the way it "
             "was always meant to sound, bright and defiant in the dead air."),
    ("game", "Seal the First: Jingle Bells", [
        "**The seal.** Chains of black ice around the corrupted pine pulse with a sickly blue "
        "light, humming a low, wrong-noted mockery of a holiday tune. Only the true song, rung "
        "on the Winter Bells, can break it.",
        "**Play it at the table.** Share the bells out among the players and ring the tune of "
        "**Jingle Bells** together, bright and defiant, every hero striking their notes in "
        "sequence. Humming along is encouraged; the glade will not judge. At this seal and the "
        "two to come, a stumbled tune never punishes: the seal flickers, holds, and waits for "
        "the party to take a breath and begin again.",
        "**The notes.** E E E | E E E | E G C D E | F F F F | F E E E",
        "**When the last note sounds.** A burst of warm, golden light erupts from the bells and "
        "ripples through the black ice; the chains shatter, and the first barrier of darkness "
        "falls. Then the mist fights back: **3 Frozen Wolves** (pack tactics, icy ground) rise "
        "to avenge the broken seal.",
    ]),
    ("gold", "On the last note, golden light bursts from the bells and rolls through the black "
             "ice, and the chains shatter with a crack that shakes snow from every branch."),
    ("imgfloat", f"{A}/scenes/s4_barrier_carol.png", 3.0),
    ("gold", "The mist answers back. It gathers itself into three snarling shapes: **Frozen "
             "Wolves**, frost-armored, eyes burning icy blue, guardians grown from the "
             "Krampusshade's own cold. The fight is knives and starlight on slick ground, wolf "
             "breath rolling white and freezing, until the last wolf comes apart into glittering "
             "mist, and the glade breathes again."),

    ("h2", "The Crystalbrook Stream: Deck the Halls"),
    ("gold", "The stream winds through a grove of silver-barked trees, its water glittering "
             "under a skin of ice. A rickety wooden bridge crosses at the narrows, and beneath "
             "it, dark tendrils snake along the underside of the planks, pulsing. Shadowy shapes "
             "flicker under the ice, faces twisted in silent song. Frost blooms across the "
             "boards as the party steps up."),
    # The area shot leads the seal (DM request: show each place BEFORE the
    # song breaks its barrier).
    ("img", f"{A}/scenes/s4_crystalbrook_stream.png",
     "The Crystalbrook Stream and the rickety bridge at the narrows.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "Eight bells ring out, lively and warm, the notes echoing down the frozen water "
             "like skaters."),
    ("game", "Seal the Second: Deck the Halls", [
        "**The seal.** Dark, icy tendrils snake along the underside of the bridge, pulsing with "
        "malevolent energy, and shadowy figures flicker beneath the ice, twisted in silent "
        "song. Only a lively, festive tune can drive the cold out of the water.",
        "**Play it at the table.** Ring the tune of **Deck the Halls** on the Winter Bells, "
        "lively and warm, the whole table keeping the beat together.",
        "**The notes.** C D E C D E | C E D C B A G | F G A F G A | G E F D C",
        "**When the last note sounds.** Defiant warmth pierces the oppressive cold; the tendrils "
        "hiss and dissipate like smoke in sunlight, and the second barrier of darkness falls. "
        "Then the treetops giggle: **4 Frostbite Pixies** (Ray of Frost, invisibility, slick "
        "ice underfoot) dart down to defend what is left of it.",
    ]),
    ("gold", "The tendrils hiss, thrash once, and dissipate like "
             "smoke in sunlight. And then the treetops giggle. Four tiny figures dart into view "
             "on frost-covered wings, faces fixed in mischievous grins, fingers glowing with "
             "cold magic: **Frostbite Pixies**, flinging rays of frost and turning invisible "
             "mid-cackle. It is the silliest, slipperiest fight of the winter, and the party "
             "wins it laughing."),

    ("h2", "The Whispering Hollow: Silent Night"),
    ("gold", "The last barrier waits between two snow-covered hills, in a hollow where the wind "
             "whistles words no one can quite make out. A ring of frost-covered standing stones "
             "rises at its heart, their old protective runes blackened and writhing. Above the "
             "stones churns a slow vortex of shadow, radiating waves of cold that sap warmth and "
             "hope together."),
    # Wintry establishing shot: the hollow's shadow vortex over the standing
    # stones, raised from a float to a half-page location plate.
    ("img", f"{A}/scenes/s4_whispering_hollow.png",
     "The Whispering Hollow: a vortex of shadow churning over the ring of standing stones.", 5.8,
     {"crop": "3:2", "hmax": 4.6}),
    ("gold", "This song cannot be loud. The heroes play it slow and gentle, each note held like "
             "a candle against the dark."),
    ("game", "Seal the Third: Silent Night", [
        "**The seal.** A swirling vortex of shadow churns above the standing stones, whispering "
        "twisted secrets of despair and radiating waves of cold that sap warmth and hope "
        "together. This one cannot be broken loudly.",
        "**Play it at the table.** Ring the tune of **Silent Night** on the Winter Bells, slow "
        "and solemn, each note held like a candle against the dark. Let the table hum the "
        "melody together, softly.",
        "**The notes.** G A G E | G A G E | D C D G | E G A",
        "**When the last note sounds.** A wave of gentle, radiant light washes over the standing "
        "stones; the vortex shrieks and dissolves, the blackened runes return to their old "
        "protective silver, and the third and final barrier of darkness falls. From the "
        "lingering shadows steps the **Icy Specter** (Wail of Despair, DC 14 Wisdom).",
        "**Rewards.** The **Shadow-Touched Rune Fragment**: a small corrupted shard of standing "
        "stone granting advantage on saving throws against fear for 1 hour while held. Then a "
        "roll on the Gift Box Table for defeating the Icy Specter.",
    ]),
    ("gold", "The melody threads through the hollow, and gentle, radiant light washes over the "
             "standing stones. The vortex shrieks and dissolves; the blackened runes flicker, "
             "then glow their old protective silver."),
    ("gold", "From the last rags of shadow steps an **Icy Specter**, translucent and wreathed "
             "in frost, hollow eyes fixed on the intruders. It fights in whispers and cold "
             "hands, wailing despair at the heroes until Ursa's starlight burns through its "
             "center and it unravels on the wind. Where it stood, half-buried in the snow, lies "
             "a small blackened shard of standing stone that hums against the palm: a "
             "**Shadow-Touched Rune Fragment**."),

    ("h2", "The Krampusshade Awakens"),
    # The gathering storm floats right beside the awakening.
    ("imgfloat", f"{A}/scenes/s4_krampusshade_over_havenmoor.png", 3.0),
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
    # Flows continuously: the awakening ends its page under half full, so the
    # part follows on the same page rather than stranding whitespace.
    ("h1", "Part Five: The Longest Night"),
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
    # Showpiece (DM request): the session's villain gets a big centered plate
    # (height tuned so the harmony lead-in paragraphs share his page).
    ("img", f"{A}/monsters/krampusshade.png",
     "The Krampusshade comes for Havenmoor.", 4.4, {"hmax": 4.1}),

    ("h2", "The Bells' Harmony"),
    ("gold", "He slams his claws together and freezing power rolls across the square; his "
             "chains lash out like serpents, and shadow imps come boiling up out of the fog "
             "around him, eyes burning. But the heroes did not come to be afraid. They came to "
             "finish a song."),
    ("gold", "While blade, bolt, claw, and starlight hold the imps back, bell after bell rings "
             "out through the fog, weaving into the one carol big enough for the moment, eight "
             "notes of Elaria's light striking through the dark like lantern beams."),
    # Page balance: the finale card keeps together and jumps whole on its own;
    # no explicit break, so the lead-in paragraphs fill the villain's page.
    ("game", "The Bells' Harmony: Carol of the Bells", [
        "**The last song.** To weaken the Krampusshade and banish him for good, all **eight "
        "Winter Bells** must ring in harmony while the battle rages: one haunting, hopeful "
        "rendition of **Carol of the Bells**.",
        "**Play it at the table.** Share the eight bells among the heroes: C, D, E, F, G, A, B, "
        "High C. While the fight goes on, ring the sequence together, over and over, letting it "
        "build. Hum the melody underneath; the bells carry the rest.",
        "**The notes.** E E E E | E G C D | E G D C",
        "**The battlefield.** The **Krampusshade** (statistics in the Appendix) rises with "
        "**four of his shadow imps**, and two more boil out of the fog at the start of the "
        "second round unless a phrase of the carol has already sounded. The frost-cracked "
        "ground within 10 feet of him is difficult terrain, and the villagers huddle at the "
        "Great Pine behind the heroes; keeping the imps away from them is worth Heroic "
        "Inspiration.",
        "**What the song unlocks.** A hero holding a bell can ring it as a Bonus Action. Each "
        "round in which all eight bells sound completes one phrase of the carol: beams of "
        "radiant light pierce the fog and sear the Krampusshade for 2d10 radiant damage, and "
        "he cannot use Shadow Step until the start of his next turn. Completing the third "
        "phrase finishes the carol and banishes him outright, whatever hit points he has "
        "left; dropping him to 0 hit points banishes him just the same. He is never slain, "
        "only unmade into wisps of shadow, and the sack of children bursts open.",
    ]),
    # Showpiece: the carol finale plate rides directly under the rules card,
    # keeping the song spread together and the page full.
    ("img", f"{A}/scenes/s4_carol_finale.png",
     "The Carol of the Bells rings out, and the Krampusshade comes apart into shadow above them.", 4.2, {"hmax": 4.0}),
    ("gold", "With every toll the Krampusshade flinches. Threads of shadow "
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
    ("dm", "The final battle: the **Krampusshade** (CR 5) with **four shadow imps** rising from "
           "the fog, while the party rang the eight bells into the Carol of the Bells. Each "
           "completed phrase of the carol seared him; the finished carol banished him."),

    # Flows continuously: the celebration follows the battle recap on the same
    # page, so no near-empty page strands between them.
    ("h2", "The Village Rejoices"),
    ("gold", "The villagers pour out of hiding, laughing and crying at once. The Great Pine "
             "blazes brighter than it has all festival, and clean, untroubled snow begins to "
             "drift down out of a clearing sky. Greta Frostbough reaches the party first, eyes "
             "shining. “You have saved us all. The darkness has lifted, and hope shines once "
             "more.” Somewhere behind her, Milo is showing the other orphans exactly how the "
             "bells went, loudly, and mostly in tune."),
    # Lore of Elaria (D4): the shadow is banished and the gifts come next;
    # the chronicler explains why it is always the kind ones. Placed here so
    # it absorbs the celebration page's tail instead of pushing the closing
    # spread past its last page.
    ("lore", "Why the Guardians",
     "The Warden's safeguards do not choose the strong. Every tale of the scattered gifts "
     "agrees on this one point: they choose the kind, because kindness is the only power "
     "Maldrith has never once predicted correctly."),

    ("h2", "Gifts of Gratitude"),
    # The reunion floats right beside the morning gifts (anchored on the page
    # after the finale plate so the image clears the bottom margin).
    ("imgfloat", f"{A}/scenes/s4_children_freed.png", 3.2),
    ("gold", "As dawn breaks over Havenmoor, Faelan comes through the celebrating crowd with "
             "three carefully wrapped packages. “Tokens of our eternal gratitude. May they aid "
             "you on the journey ahead.”"),
    ("gold", "For **Lilly**, the **Frostbite Shard Dagger**: a blade of crystalline ice that "
             "never melts, glowing with faint blue arcane light, hungry to channel her spells."),
    ("gold", "For **Ursa**, the **Amulet of Guiding Light**: a polished silver starburst with a "
             "blue gem at its heart that pulses softly, like a distant star keeping watch."),
    ("gold", "And for **Stabby**, the **Candyfang Katana**: a katana of impossible candy-striped "
             "steel, red and white and wickedly sharp, trailing a faint scent of sugar. Stabby "
             "licks it immediately. It is delicious."),
    ("reward_card", "Rewards: The Gifts of Faelan",
     "Havenmoor at dawn ✦ one gift for each hero ✦ full lore in the treasures compendium", [
        ("Frostbite Shard Dagger (Lilly)",
         "Rare, attunement by an Artificer. A blade of crystalline ice that never melts: "
         "1d4 piercing plus 1d4 cold, +1 to attack. *Spell focus and Arcane Firearm:* +1d8 "
         "frost to one spell damage roll cast through it, and +2 frost on spell damage."),
        ("Amulet of Guiding Light (Ursa)",
         "Rare, attunement by a Circle of Stars druid. *Guiding Light:* sheds light, and "
         "allies gain +1 to attacks and saves while Ursa is in Starry Form. *Starry Glow:* "
         "Reaction, 1/long rest: 2d8 radiant, DC 15 Con or blinded. *Celestial Resilience:* "
         "reroll natural 1s, 2/long rest."),
        ("Candyfang Katana (Stabby)",
         "Rare, attunement by a Monk. Impossible candy-striped steel: 1d8/1d10 slashing, +1 to "
         "attack and damage. *Sugar Rush:* Bonus Action lick, 1/long rest: 2d8 + Con "
         "temporary hit points. *Frostbite Infusion:* +2 frost on hit."),
    ]),
    ("gold", "Down at the harbor, the shipwright **Master Doran Bramblebeard**, lighthouse soot "
             "still on his sleeves, nods toward a trim vessel rocking at the dock. “The "
             "**Stormwind** is ready when you are. Gearhaven awaits.”"),
    # The two gift portraits open the final story page together with the
    # closing lines; the gifts page ends full, so no explicit break is needed
    # (one here would mint a blank page).
    ("imgrow", [(f"{A}/characters/lilly_session4.png",
                 "Lilly and the Frostbite Shard Dagger."),
                (f"{A}/characters/stabby_cane.png",
                 "Stabby and the Candyfang Katana. Yes, he licked it.")], 3.2),
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
    # APPENDIX 1: the DM run sheet (S7 gold-standard format).
    ("appendix_title", "APPENDIX", "DM Run Sheet: The Day at a Glance",
     "Every DC, dial, and spotlight, in play order. Keep this page at your elbow."),

    ("h1", "The Shape of the Session"),
    ("body", "Six beats, four fights, one long day into the longest night. B1 the morning: the "
             "crying mother, the children's rhyme, Greta's warning and the singed map (roleplay). "
             "B2 the bell hunt: four sites, eight bells, all skill beats, no fights (DCs below). "
             "B3 Faelan's cottage: the Krampusshade lore, the three barriers, the frosted "
             "cookies. B4 the three barriers, each one song then one fight: Frostpine Glade "
             "(FIGHT 1), Crystalbrook Stream (FIGHT 2), Whispering Hollow (FIGHT 3); roll the "
             "d20 travel table on every trek out or back. B5 the longest night: the BOSS in the "
             "market square, eight bells against the dark. B6 dawn: children freed, the Gifts "
             "of Faelan, the Stormwind at the dock."),

    ("h1", "The Bell Hunt at a Glance"),
    ("body", "**SUGARPLUM HEARTH (C + D).** C is free from Greta. D: Perception DC 15 in the "
             "wreath above the bar. Digging: Insight 14 (Greta and the hearth bell), "
             "Investigation 14 (the old plaque), Arcana 16 (abjuration on the C Bell), History "
             "15 (Elda's full Lay), Survival 13 (Torren's coast advice)."),
    ("body", "**FROSTWIND MARKET (E + F).** E is free on the festival pine; it only wanted to "
             "be noticed. F: Persuasion DC 15 or Sleight of Hand 14 at Eldric's stall; on a "
             "fail, reassure him before he says another word. Digging: Insight 13 (his fear is "
             "real), Investigation 15 (vanishing footprints, frosted gingerbread), Arcana 16 "
             "(thinning veil), History 14 (solstice rituals; 15+ adds Ingrid's Krampus tales)."),
    ("body", "**HOLLOW HEARTH ORPHANAGE (G + A).** G: Investigation DC 15 finds the attic toy "
             "chest. A is in Milo's fist: Persuasion 14 or Insight 13, ADVANTAGE for genuine "
             "kindness; on a fail he cries, and Sister Merida asks the party to try again "
             "gently. Calmed, he sings the verse the grown-ups have not heard. Arcana 16: "
             "Shadowfell energy in the too-long shadows."),
    ("body", "**WYRMGALE LIGHTHOUSE (B + High C).** B: Athletics DC 15 up the tower; a fail is "
             "a slip, 1d6 bludgeoning, bell still in reach. High C: Arcana DC 14 hears the hum "
             "inside the old ship's bell in the storeroom. Digging: Insight 15 (Doran's "
             "riddles), History 15 (the mist-walking Krampusshade), Arcana 16 (the gloom on the "
             "beacon answers to the Shadowfell). All eight found: one full octave, one "
             "unfinished song, then Faelan."),

    ("h1", "Fights at a Glance"),
    ("body", "**FIGHT 1: Frostpine Glade (Moderate; the seal breaks, the mist bites back).** "
             "3× Frozen Wolf (AC 15, HP 45; Pack Tactics; icy ground within 10 ft of each "
             "wolf; Bite +5, 2d6+3 plus 1d8 cold, DC 13 Con or speed -10; Frost Breath rech "
             "5-6: 15-ft cone, DC 13 Dex, 4d8 cold, slowed on a fail). The one rule: don't "
             "clump for the breath, don't scatter into Pack Tactics. The out: the last wolf "
             "comes apart into glittering mist, no chase."),
    ("body", "**FIGHT 2: Crystalbrook Stream (Easy and silly; play it for laughs).** 4× "
             "Frostbite Pixie (AC 15, HP 14; Ray of Frost +5, 60 ft, 2d8 cold plus speed -10; "
             "Invisibility between attacks; slick ice underfoot, DC 13 Dex to move fast). The "
             "one rule: they blink invisible mid-cackle, so reward readied actions and clever "
             "flushing. The out: the party should win this one laughing; it is the silliest, "
             "slipperiest fight of the winter."),
    ("body", "**FIGHT 3: Whispering Hollow (Moderate; a mood fight, not a slugfest).** 1× Icy "
             "Specter (AC 12, HP 45, fly 50 hover; resists cold, necrotic, nonmagical B/P/S; "
             "Chilling Touch +5, 3d6 cold; Wail of Despair rech 5-6: 30 ft, DC 14 Wis or "
             "frightened 1 minute, repeat save each turn). The one rule: the Wail scatters the "
             "brave; let Ursa's starlight land the ending. Drops the Shadow-Touched Rune "
             "Fragment (advantage vs fear, 1 hour) plus a Gift Box roll."),
    ("body", "**BOSS: The Longest Night (epic spectacle, never a meat grinder).** Krampusshade "
             "(AC 15, HP 102; Claw +7 reach 10 ft, 2d6+4 plus 1d10 cold; Chains +7 reach 15 "
             "ft, DC 14 Str or restrained; Gift of Despair rech 5-6: DC 14 Wis or frightened; "
             "Icy Retaliation reaction; Shadow Step 1/round in dim light) + 4× shadow imp "
             "(AC 14, HP 22), 2 more at the start of round 2 unless a carol phrase has already "
             "sounded. THE DIAL is the carol: ringing a bell is a Bonus Action; a round in "
             "which all eight sound completes one phrase, 2d10 radiant and no Shadow Step; the "
             "THIRD phrase banishes him outright, and 0 HP banishes him just the same. "
             "Difficult terrain within 10 ft of him; imps kept off the villagers at the Great "
             "Pine = Heroic Inspiration."),

    ("h1", "The Resource Picture"),
    ("body", "One long day, no long rest: the bell hunt is free, but the three barrier fights "
             "and the boss all come out of the same pool, and every trek out of town risks a "
             "d20 travel roll on top. The safety net is Faelan's three Frosted Cookies (2d8 "
             "HP, a short rest's benefit, and one spell slot each): let the party spend them "
             "between barriers, and remind them before the longest night if they forget. Gift "
             "Boxes drop from the Krampusshade's defeated creatures (d20 table mid-session). "
             "In the boss fight a rung bell is a Bonus Action, so turns stay full: attack, "
             "ring, move."),

    ("h1", "Spotlights & Seeds: every kid shines"),
    ("body", "**Lilly:** the G Bell in the attic toy chest → the High C Bell's magic hum in "
             "the storeroom, her Arcana find → her turret keeps time like a drummer through "
             "the carol → the Frostbite Shard Dagger (Door: Gearhaven's artificers ahead)."),
    ("body", "**Stabby:** silly faces that crack Milo open → the B Bell scramble up the "
             "lighthouse ladder before anyone can say be careful → ringing a bell one-handed "
             "while parrying chains → the Candyfang Katana, licked immediately, delicious."),
    ("body", "**Ursa:** the E Bell warms the air at his touch → \"bells are like stars: little "
             "lights the dark cannot put out,\" the line that wins Milo over → his starlight "
             "burns through the Icy Specter → the Amulet of Guiding Light, a distant star "
             "keeping watch."),

    ("h1", "Foreshadow Tracker: say it, then say it again"),
    ("body", "The tells, in order. The rhyme ×3: sung at dawn, hummed by Milo, and his unheard "
             "verse names the fix (ring the light, banish the shade) • frost where frost cannot "
             "be: Lora's gingerbread, footprints that vanish mid-stride • the thinning veil ×3 "
             "(Arcana): the square's edges, the orphanage shadows, the gloom on the beacon • "
             "the sea keeps its secrets: Torren's swallowed ships, Doran's \"the lost come "
             "back, twisted and hollow,\" Session 5's ghost ship knocking • \"something on the "
             "stocks\": the Stormwind, and the road to Gearhaven over water."),

    # ------------------------------------------------------------------
    # APPENDIX 2: the bestiary (S7 gold-standard format). Numbers transcribed
    # faithfully from the audited compact boxes; only the format is new.
    ("appendix_title", "APPENDIX", "Bestiary: Enemy Stat Blocks",
     "All four encounters of Session 4 in the order the party meets them, plus the "
     "wandering threats of the frozen roads."),

    ("fight_header", "ENEMIES, Fight 1: The First Barrier",
     "Frostpine Glade ✦ Difficulty: Moderate ✦ 3× Frozen Wolf"),
    ("enemy_cards", [{
        "name": "Frozen Wolf",
        "sub": "Medium beast, neutral evil ✦ CR 2 ✦ pack of 3",
        "img": f"{A}/monsters/frozen_wolf.png", "img_w": 3.0,
        "stats": [
            "**AC** 15 (natural armor)  **HP** 45 (6d10+12)  **Speed** 40 ft",
            "**STR** 16  **DEX** 15  **CON** 14  **INT** 3  **WIS** 12  **CHA** 6",
            "**Immune** cold",
            "**Senses** darkvision 60 ft",
            "**Challenge** 2 (450 XP)",
        ],
        "traits": [
            ("Pack Tactics", "The wolf has advantage on attack rolls against a creature if "
             "at least one of its allies is within 5 ft of the target."),
            ("Icy Terrain", "The ground within 10 ft of the wolf is difficult terrain, slick "
             "with spreading frost."),
        ],
        "actions": [
            ("Bite", "+5 to hit, reach 5 ft. Hit: 10 (2d6+3) piercing plus 4 (1d8) cold; "
             "DC 13 Con save or the target's speed is reduced by 10 ft."),
            ("Frost Breath (Recharge 5-6)", "15-ft cone, DC 13 Dex save; 18 (4d8) cold, half "
             "on a success, and slowed on a failure."),
        ],
    }]),
    ("tactics", "The wolves rise the moment the chains shatter and hunt as one: Pack Tactics "
                "rewards every flank, the icy ground herds heroes where the pack wants them, "
                "and Frost Breath punishes a clumped party. They are guardians grown from the "
                "Krampusshade's own cold; the last one falls apart into glittering mist, and "
                "the glade breathes again."),

    ("fight_header", "ENEMIES, Fight 2: The Second Barrier",
     "Crystalbrook Stream ✦ Difficulty: Easy and silly ✦ 4× Frostbite Pixie"),
    ("enemy_cards", [{
        "name": "Frostbite Pixie",
        "sub": "Tiny fey, chaotic neutral ✦ CR 1/4 ✦ giggling flight of 4",
        "img": f"{A}/monsters/frostbite_pixie.png", "img_w": 3.4,
        "stats": [
            "**AC** 15  **HP** 14 (4d4+4)  **Speed** 20 ft, fly 60 ft",
            "**STR** 3  **DEX** 20  **CON** 12  **INT** 14  **WIS** 11  **CHA** 16",
            "**Skills** Stealth +7",
            "**Immune** cold",
            "**Challenge** 1/4 (50 XP)",
        ],
        "actions": [
            ("Ray of Frost", "+5 to hit, range 60 ft. Hit: 9 (2d8) cold; the target's speed "
             "is reduced by 10 ft for one turn."),
            ("Invisibility", "The pixie turns invisible until it attacks or casts a spell."),
        ],
    }]),
    ("tactics", "Pure mischief. The pixies fling Ray of Frost from the treetops, turn "
                "invisible mid-cackle, and count on the slick ice underfoot (DC 13 Dex to "
                "move fast) to do half their work. Reward readied actions and clever "
                "flushing; the party should win this one laughing."),

    ("fight_header", "ENEMIES, Fight 3: The Third Barrier",
     "Whispering Hollow ✦ Difficulty: Moderate ✦ 1× Icy Specter"),
    ("enemy_cards", [{
        "name": "Icy Specter",
        "sub": "Medium undead, neutral evil ✦ CR 2 ✦ steps from the broken seal, alone",
        "img": f"{A}/monsters/icy_specter.png", "img_w": 3.3,
        "stats": [
            "**AC** 12  **HP** 45 (10d8)  **Speed** 0 ft, fly 50 ft (hover)",
            "**STR** 1  **DEX** 14  **CON** 11  **INT** 10  **WIS** 10  **CHA** 16",
            "**Resist** cold, necrotic; nonmagical B/P/S",
            "**Imm.** poison ✦ (cond) charmed, exhaustion, grappled, paralyzed, poisoned, "
            "prone, restrained",
            "**Challenge** 2 (450 XP)",
        ],
        "actions": [
            ("Chilling Touch", "+5 to hit, reach 5 ft. Hit: 10 (3d6) cold."),
            ("Wail of Despair (Recharge 5-6)", "Each creature within 30 ft makes a DC 14 Wis "
             "save or is frightened for 1 minute (repeat the save at the end of each turn)."),
        ],
    }]),
    ("tactics", "A mood fight, not a slugfest. The specter opens with Wail of Despair to "
                "scatter the party, then drifts through the frightened gaps with Chilling "
                "Touch, whispering all the while. Let Ursa's starlight land the ending. It "
                "guards the Shadow-Touched Rune Fragment and a Gift Box roll."),

    # ------------------------------------------------------------------
    ("h1", "The Frozen Roads: A Winter Bestiary of Chances"),
    ("gold", "The roads around Havenmoor that week were thick with wonders and dangers. Not all of "
             "them crossed the heroes' path, but every one of them was out there, waiting in the "
             "white silence between the pines. What follows is the DM's deck of chances, exactly "
             "as it hung over every journey out of town that winter."),
    # The winter overworld leads the deck of chances (DM request 2026-07-06):
    # the three barrier sites are found by exploring, and every trek rolls.
    ("img", f"{A}/world/havenmoor_wilds_map.png",
     "The frozen wilds around Havenmoor: the town and the Wyrmgale Lighthouse on the coast, and "
     "somewhere in the white silence, the three barriers waiting to be found.", 6.2,
     {"hmax": 4.6}),
    ("dm", "**Exploring the wilds.** Faelan's directions mark the three barriers only roughly; "
           "the party must range out into the frozen wilds and FIND each one (the map above is "
           "the shape of that search). Whenever the party sets out from Havenmoor, to a barrier "
           "or back again, roll a d20 on the table below. Notes on the most colorful entries "
           "follow; full statistics for every creature live in the bestiary compendium."),

    ("h2", "Travel Encounter Table (d20)"),
    ("body", "**1.** Krampusshade's Minion: a shadowy imp attacks, attempting to steal something "
             "from the party."),
    ("body", "**2.** Frozen Wolves: 2d4 frost-covered wolves stalk the party, their eyes glowing "
             "with cold malice."),
    ("body", "**3.** Frostbite Pixies: mischievous pixies cast Ray of Frost and try to confuse "
             "the party."),
    ("body", "**4.** Icy Specter: a ghostly figure whispers a chilling warning before attacking."),
    ("body", "**5.** Snowbound Bandits: desperate bandits, half-mad with cold, ambush the party."),
    ("body", "**6.** Frost Golems: two small frost golems rise from the snow and attack."),
    ("body", "**7.** Blizzard Trap: a sudden blizzard cuts visibility to a few feet; Wisdom "
             "(Survival) DC 14 to avoid becoming lost."),
    ("body", "**8.** Enchanted Snowmen: three animated snowmen with coal-black eyes hurl "
             "snowballs laced with Ray of Frost."),
    ("body", "**9.** Yule Cat: a huge predatory feline prowls near the party, looking for those "
             "who have not been good."),
    ("body", "**10.** Friendly Caribou: a lost, enchanted caribou offers the party a brief rest "
             "and warmth."),
    ("body", "**11.** The Sleeping Traveler: a traveler frozen beneath the snow, one hand still "
             "holding a cryptic note or map."),
    ("body", "**12.** Holiday Illusions: visions of a warm celebration that hide a dangerous "
             "snow drift."),
    ("body", "**13.** Frozen Will-o'-Wisps: malevolent lights lure the party toward a frozen "
             "pond."),
    ("body", "**14.** Frost Hag Ambush: a frost hag disguised as a kind old woman offers "
             "poisoned treats."),
    ("body", "**15.** Ice Spiders: 2d6 ice spiders drop from the trees and attack."),
    ("body", "**16.** Resting Reindeer: a magical reindeer grants the party Heroic Inspiration "
             "if treated kindly."),
    ("body", "**17.** Frozen Treasure: a chest sealed in a block of ice; Strength DC 15 or fire "
             "magic to open."),
    ("body", "**18.** Aurora Spirits: peaceful, glowing spirits offer a cryptic hint or "
             "prophecy."),
    ("body", "**19.** Fey Tricksters: playful fey challenge the party to a riddle contest or a "
             "harmless prank."),
    ("body", "**20.** Holiday Miracle: a warm breeze restores 1d4 hit points to each party "
             "member."),

    ("h2", "Gift Box Table (d20)"),
    ("dm", "**Gift Boxes.** When one of the Krampusshade's creatures is defeated, it leaves "
           "behind a wrapped gift box. Roll a d20 for its contents."),
    ("body", "**1.** Mimic in Disguise! The gift box is a tiny mimic (CR 1), and it immediately "
             "attacks."),
    ("body", "**2-4.** Lump of Coal: a mundane lump of coal. Slightly warm, but otherwise "
             "useless."),
    ("body", "**5-6.** Handful of Peppermint Shards: slightly refreshing. No mechanical effect."),
    ("body", "**7-9.** Gingerbread Cookie: a tasty treat that restores 1d4 hit points when "
             "eaten."),
    ("body", "**10-12.** Candy Cane Dagger: a simple weapon, 1d4 piercing damage. Melts after "
             "24 hours."),
    ("body", "**13-15.** Hot Cocoa Flask: when drunk, grants resistance to cold damage for "
             "1 hour."),
    ("body", "**16-17.** Sparkling Snow Globe: shaking it causes a harmless flurry of snow, and "
             "it sheds light for 30 feet."),
    ("body", "**18-19.** Frosted Cookie of Restoration: restores 2d8 hit points, grants the "
             "benefit of a short rest, and restores one spell slot."),
    ("body", "**20.** Holiday Miracle Charm: a small charm granting advantage on one saving "
             "throw within 24 hours."),

    # Page balance: the bestiary flows continuously after the tables; floats
    # sized at 2.7 so the wrapped sections pack without stranding.
    ("h2", "The Yule Cat"),
    ("imgfloat", f"{A}/monsters/yule_cat.png", 2.7),
    ("body", "A massive black feline with frost-covered fur and glowing yellow eyes, the Yule "
             "Cat is a creature of fey legend that judges those who lack generosity or "
             "kindness. It prowls the deep snow on silent paws, and a low growl through the "
             "cold air is the only warning before it pounces. Legends around Havenmoor say "
             "it circles the houses on festival nights, counting who has shared their "
             "supper and who has not."),
    ("dm", "**Yule Cat (CR 3).** Wisdom (Animal Handling) DC 15 calms it for a round; Wisdom "
           "(Insight) DC 14 reveals that it seeks acts of generosity, so offering food or "
           "gifts can delay its attack entirely. In a fight it relies on Frost Claw, a "
           "Frostbite Pounce that knocks heroes prone, and a Chilling Gaze (DC 14 "
           "Constitution) that paralyzes with cold. Win or appease it, and a roll on the "
           "Gift Box Table follows."),

    ("h2", "The Frost Hag"),
    ("imgfloat", f"{A}/monsters/frost_hag_disguised.png", 3.2),
    ("body", "In a lonely clearing, a kindly old woman tends a bubbling cauldron and waves "
             "travelers over to warm themselves and share pastries dusted with powdered "
             "sugar. Her voice is honey and her fire is warm, but her eyes glint far too "
             "coldly for the warmth of her smile. The wisest travelers notice that no snow "
             "melts anywhere near her fire."),
    ("dm", "**Frost Hag (CR 4).** Wisdom (Insight) DC 14 catches the malice behind the "
           "smile. Anyone who eats her treats must make a DC 13 Constitution save or be "
           "poisoned for 1 hour, taking 1d4 cold damage. Unmasked, she is ice-crusted skin "
           "and jagged teeth: Icy Claw, a 15-foot Frostbite Breath cone (DC 14 Constitution, "
           "4d6 cold, slowed on a failure), and Misty Step as a bonus action to keep out of "
           "reach."),

    ("h2", "Snowbound Bandits"),
    ("imgfloat", f"{A}/monsters/snowbound_bandits.png", 3.2),
    ("body", "On a narrow, snow-choked path, three desperate figures rise out of the drifts "
             "with weapons trembling in frostbitten hands, and a grizzled leader with a "
             "frost-crusted beard demands the party's packs. They are cold and hungry rather "
             "than wicked, and a warm meal buys more peace than a drawn blade. A DM with a "
             "soft heart may let a fed and warmed bandit whisper a useful rumor about the "
             "roads before the band slips away into the snow."),
    ("dm", "**3 Bandits and 1 Bandit Leader.** Wisdom (Insight) DC 14 shows they are driven "
           "by desperation, not malice. Charisma (Persuasion) DC 15 with an offer of food or "
           "warmth avoids the fight; Intimidation DC 14 scares them into retreat, but "
           "failure means combat on slippery ice (Dexterity DC 13 to move more than 15 feet "
           "without falling prone). The leader's Frostbite Strike adds 1d6 cold damage and "
           "can slow its target. Victory yields 1d4 healing potions, 10 gold, rations for "
           "two days, and a Gift Box."),

    # Hardbreak: started at a page bottom, the golems float sinks into the
    # margin; opening the page lets golems + snowmen + spiders fill it whole.
    ("h2", "Frost Golems", {"hardbreak": True}),
    ("imgfloat", f"{A}/monsters/frost_golems.png", 2.7),
    ("body", "On a serene snowfield, the powder suddenly trembles and pulls itself together, "
             "packing into two jagged shapes of snow and ice shard. Their eyes glow with an "
             "eerie blue light as they lumber forward, frost radiating from their bodies, "
             "without hurry and without mercy."),
    ("dm", "**2 Frost Golems (CR 2 each).** Icy Slam (2d6 + 3 bludgeoning plus 1d4 cold) and "
           "a Frost Aura that deals 2 cold damage at the start of each creature's turn "
           "within 5 feet. The snowfield itself is a hazard: Dexterity (Acrobatics) DC 14 "
           "to move quickly without falling prone. The golems trudge relentlessly and try "
           "to corner heroes on the worst of the ice."),

    ("h2", "Enchanted Snowmen"),
    ("imgfloat", f"{A}/monsters/enchanted_snowman.png", 2.5),
    ("body", "Three cheerful roadside snowmen with coal-black eyes and wicked twig grins "
             "shudder to life as travelers pass, stick arms lifting to pelt them with "
             "snowballs laced with ice magic. It would almost be funny, if the snowballs "
             "did not hit quite so hard."),
    ("dm", "**3 Enchanted Snowmen (CR 1 each).** Wisdom (Perception) DC 14 to act before "
           "the snowmen do. Frostball: +4 to hit, 2d4 cold damage, and a DC 12 Constitution "
           "save or the target's speed is halved until the end of its next turn. AC 13, "
           "HP 30, and they never stop grinning."),

    ("h2", "Ice Spiders"),
    # Anchored at the top of the section, floated LEFT so it cannot collide
    # with the snowman float on the right edge above it.
    ("imgfloat", f"{A}/monsters/ice_spider.png", 2.5, "left"),
    ("body", "In a grove of frost-covered trees, branches creak under an unnatural weight "
             "and a faint skittering echoes overhead. Then icy webs glisten in the dappled "
             "light, and frost-coated spiders the size of wolves drop from the canopy, "
             "mandibles glittering with rime."),
    ("dm", "**2d6 Ice Spiders (CR 1 each).** Wisdom (Perception) DC 15 spots them before "
           "they drop; Wisdom (Survival) DC 14 keeps the party out of the sticky web traps "
           "(DC 13 Strength to break free). Their bite carries a venomous chill (DC 13 "
           "Constitution or poisoned 1 minute), their frozen webbing stings for 1d4 cold "
           "damage if touched, and the ground beneath the grove is slick ice, Dexterity "
           "(Acrobatics) DC 14 to keep footing."),

    # Hardbreak: the wisps float needs a page's top half; anchored lower it
    # collides with the ice spider float and mangles the wrap.
    ("h2", "Frozen Will-o'-Wisps", {"hardbreak": True}),
    ("imgfloat", f"{A}/monsters/frozen_will_o_wisps.png", 2.7),
    ("body", "Above a frozen pond, ghostly blue lights flicker and bob, beckoning travelers "
             "out onto the ice with whispers of false promises. The scene looks tranquil, "
             "almost inviting, but the mist around the lights is far, far too cold."),
    ("dm", "**Frozen Will-o'-Wisps (CR 2 each).** Wisdom (Perception) DC 14 notices strange "
           "ripples beneath the ice; Intelligence (Arcana) DC 15 names the lights for what "
           "they are. The careless suffer a surprise round, slippery ice (Dexterity DC 13 "
           "each round or fall prone), and 1d4 cold damage per round of exposure. Icy Shock "
           "deals lightning and cold together, and the wisps blink invisible between "
           "attacks. They guard a Gift Box, and a whispered warning of the Krampusshade's "
           "icy influence."),

    ("h2", "Tricks of the Road"),
    ("dm", "**Blizzard Trap.** The wind rises and the world goes white. Wisdom (Survival) "
           "DC 14 finds the way through to a small sheltered grove where the party can rest "
           "and warm up; failure means an hour lost in the storm and 1d6 cold damage from "
           "exposure."),
    ("dm", "**Holiday Illusions.** A vision of a warmly lit cabin unfolds, all laughter, "
           "glowing lanterns, roasted chestnuts, and spiced cider. Intelligence (Arcana) or "
           "(Investigation) DC 15 spots the flickering seams. Those who walk in take 1d4 "
           "psychic damage as the vision shatters over a deep snow drift: DC 13 Dexterity "
           "save or become trapped and take 1d6 cold damage, then DC 14 Constitution save "
           "or gain a level of exhaustion. Seeing through the trick earns a brief warmth, "
           "a protective charm against illusions for the next hour."),
    ("dm", "**Mimic in Disguise.** The prettiest gift box on the road is sometimes a tiny "
           "mimic, all teeth and adhesive. Its bigger cousin (CR 2, AC 12, HP 58, bite plus "
           "1d8 acid, DC 13 Strength to escape its grip) waits in the bestiary compendium "
           "for DMs feeling festive."),

    ("h2", "Kindly Wonders"),
    ("body", "Not everything on the winter roads wished travelers ill. Some of it was "
             "watching, quietly, to see if they would be kind."),
    ("dm", "**Friendly Caribou.** An enchanted caribou with softly glowing antlers steps "
           "from the treeline into the moonlight. Offering food or kind words earns its "
           "aura of warmth: each party member regains 1d4 hit points, and Wisdom (Animal "
           "Handling) DC 13 earns one hero Heroic Inspiration. Hostility makes it dissolve "
           "sadly into mist."),
    ("dm", "**Resting Reindeer.** A majestic reindeer with antlers like polished silver "
           "rests beneath a frosted pine. Wisdom (Animal Handling) DC 14 to approach "
           "calmly; treated kindly, its nose glows softly and each hero gains Heroic "
           "Inspiration and temporary hit points equal to 1d6 + their level."),
    ("dm", "**Aurora Spirits.** Beneath dancing ribbons of blue, purple, and green, serene "
           "spirits descend, humming an ethereal tune. Wisdom (Insight) DC 14 or "
           "Intelligence (Religion) DC 15 understands them as messengers of Elaria; they "
           "impart a cryptic hint about the Krampusshade and grant advantage on the next "
           "Wisdom saving throw."),
    ("dm", "**Fey Tricksters.** Small winged pranksters flit between the trees and propose "
           "a riddle contest (Intelligence DC 15) or spring a prank to dodge (Dexterity "
           "DC 14). Winners receive a charm of luck, advantage on one roll of their choice; "
           "losers get a pie in the face and disadvantage on their next skill check."),
    ("dm", "**Holiday Miracle.** A sudden warm breeze carries the scent of pine, cinnamon, "
           "and fresh cookies, restoring 1d4 hit points to each party member. For a moment, "
           "the world feels kinder, and the shadows retreat just a little."),

    ("h2", "Treasures in the Ice"),
    ("dm", "**The Sleeping Traveler.** A traveler frozen beneath a drift, still and "
           "peaceful as a statue, one outstretched hand holding a crumpled note. "
           "Intelligence (Investigation) DC 12 preserves the brittle parchment: a warning "
           "about the Krampusshade's minions and, tucked beneath the traveler's coat, a "
           "**Map of Hidden Paths** granting advantage on the next Survival check to "
           "navigate the snowy wilderness."),
    ("dm", "**Frozen Treasure.** A sturdy chest sealed inside a block of ice carved with "
           "faintly glowing runes. Strength DC 15 breaks it open, Intelligence (Arcana) "
           "DC 14 finds the weak point, and fire magic melts it in a single round; a "
           "failed attempt stings for 2d6 cold damage. Inside wait 50 gold pieces and a "
           "Frosted Cookie of Restoration."),
    ("dm", "Full statistics for every creature of the frozen roads live in the bestiary "
           "compendium. The stat blocks for the ones the heroes actually fought follow on "
           "the next pages."),

    # ------------------------------------------------------------------
    # The travel mobs (DM directive 2026-07-07): every hostile creature type
    # on the d20 travel table gets its full block here, doubled up two or
    # three to a page so a DM can run the frozen roads from this book alone.
    # Numbers transcribed faithfully from templates/build_bestiary.py.
    ("fight_header", "THE FROZEN ROADS: Travel Encounters",
     "The wilds around Havenmoor ✦ roll a d20 per trek (tables in Part Two) ✦ "
     "the wandering threats", {"compact": True}),
    ("enemy_cards", [{
        "name": "Snowbound Bandit Leader",
        "sub": "Medium humanoid, neutral ✦ leads a band of 3",
        "img": f"{A}/monsters/snowbound_bandits.png", "img_w": 1.8,
        "stats": [
            "**AC** 14  **HP** 32  **Speed** 30 ft",
            "**STR** 14  **DEX** 13  **CON** 12  **INT** 10  **WIS** 11  **CHA** 11",
        ],
        "traits": [
            ("Desperate, Not Cruel", "Driven mad by the cold; kindness (food, "
             "warmth) or a DC 14 Intimidation check can end the fight before it "
             "begins."),
        ],
        "actions": [
            ("Scimitar", "+5 to hit, reach 5 ft. Hit: 7 (1d6+3) slashing."),
            ("Dagger", "+5 to hit, melee or ranged. Hit: 5 (1d4+3) piercing."),
            ("Frostbite Strike (Recharge 5-6)", "+5 to hit; an extra 1d6 cold, and "
             "a DC 13 Con save or speed reduced by 10 ft until its next turn."),
        ],
    }, {
        "name": "Snowbound Bandit",
        "sub": "Medium humanoid, neutral ✦ 3 rise from the drifts",
        "img": "assets/monsters/snowbound_bandit.png", "img_w": 2.2,
        "stats": [
            "**AC** 12  **HP** 20  **Speed** 30 ft",
        ],
        "traits": [
            ("Desperate, Not Cruel", "Like their leader, the bandits fight out of "
             "hunger and cold; kindness can end the fight before it begins."),
        ],
        "actions": [
            ("Scimitar", "+4 to hit, reach 5 ft. Hit: 5 (1d6+2) slashing."),
            ("Shortbow", "+4 to hit, ranged. Hit: 5 (1d6+2) piercing."),
        ],
    }, {
        "name": "Frost Golem",
        "sub": "Medium elemental, neutral ✦ CR 2 ✦ they rise in pairs",
        "img": f"{A}/monsters/frost_golems.png", "img_w": 1.8,
        "stats": [
            "**AC** 14 (natural armor)  **HP** 42 (5d10+15)  **Speed** 20 ft",
            "**STR** 16  **DEX** 10  **CON** 16  **INT** 6  **WIS** 10  **CHA** 5",
            "**Resist** cold; nonmagical B/P/S",
            "**Imm.** (cond) exhaustion, poisoned",
            "**Challenge** 2 (450 XP)",
        ],
        "traits": [
            ("Frost Aura", "At the start of each creature's turn within 5 ft of the "
             "golem, that creature takes 2 cold."),
        ],
        "actions": [
            ("Icy Slam", "+5 to hit, reach 5 ft. Hit: 7 (2d6+3) bludgeoning plus "
             "3 (1d4) cold."),
        ],
    }], {"pack": True}),
    ("enemy_cards", [{
        "name": "Yule Cat",
        "sub": "Large fey beast, neutral ✦ CR 3 ✦ prowls alone; generosity delays it",
        "img": f"{A}/monsters/yule_cat.png", "img_w": 2.75,
        "stats": [
            "**AC** 15 (natural armor)  **HP** 52 (7d10+14)  **Speed** 40 ft, "
            "climb 30 ft",
            "**STR** 18  **DEX** 16  **CON** 14  **INT** 6  **WIS** 14  **CHA** 10",
            "**Skills** Perception +4, Stealth +6",
            "**Resist** cold",
            "**Senses** darkvision 60 ft",
            "**Challenge** 3 (700 XP)",
        ],
        "actions": [
            ("Frost Claw", "+6 to hit, reach 5 ft. Hit: 10 (2d6+3) slashing plus "
             "3 (1d6) cold."),
            ("Frostbite Pounce", "If the cat moves 20 ft and hits with Frost Claw, "
             "the target makes a DC 14 Str save or is knocked prone; if prone, the "
             "cat makes another Frost Claw as a bonus action."),
            ("Chilling Gaze (Recharge 5-6)", "One target within 30 ft makes a DC 14 "
             "Con save or takes 9 (2d8) cold and is paralyzed until the end of its "
             "next turn."),
        ],
    }, {
        "name": "Frost Hag (disguised)",
        "sub": "Medium fey, neutral evil ✦ CR 4 ✦ alone at her roadside cauldron",
        "img": f"{A}/monsters/frost_hag_disguised.png", "img_w": 2.75,
        "stats": [
            "**AC** 15  **HP** 52  **Speed** 30 ft",
            "**STR** 14  **DEX** 14  **CON** 14  **INT** 13  **WIS** 12  **CHA** 14",
            "**Challenge** 4 (1,100 XP)",
        ],
        "traits": [
            ("Kindly Guise", "The hag appears as a sweet old woman offering sugared "
             "pastries; those who eat them make a DC 13 Con save or are poisoned for "
             "1 hour, taking 1d4 cold."),
        ],
        "actions": [
            ("Icy Claw", "+6 to hit, reach 5 ft. Hit: 10 (2d6+3) slashing plus "
             "4 (1d6) cold."),
            ("Frostbite Breath (Recharge 5-6)", "15-ft cone, DC 14 Con save; "
             "16 (4d6) cold, half on a success, and slowed until its next turn on a "
             "failure."),
            ("Misty Step (Bonus Action)", "The hag teleports 30 ft."),
        ],
    }], {"pack": True}),
    ("enemy_cards", [{
        "name": "Enchanted Snowman",
        "sub": "Small construct, unaligned ✦ CR 1 ✦ roadside trio",
        "img": f"{A}/monsters/enchanted_snowman.png", "img_w": 1.7,
        "stats": [
            "**AC** 13  **HP** 30 (4d8+12)  **Speed** 20 ft",
            "**STR** 12  **DEX** 10  **CON** 16  **INT** 3  **WIS** 10  **CHA** 6",
            "**Challenge** 1 (200 XP)",
        ],
        "actions": [
            ("Frostball", "+4 to hit, ranged. Hit: 2d4 cold, and a DC 12 Con save "
             "or speed halved until the end of its next turn."),
        ],
    }, {
        "name": "Ice Spider",
        "sub": "Medium beast, unaligned ✦ CR 1 ✦ 2d6 drop from the canopy",
        "img": f"{A}/monsters/ice_spider.png", "img_w": 1.7,
        "stats": [
            "**AC** 14 (natural armor)  **HP** 26 (4d10+4)  **Speed** 30 ft, "
            "climb 30 ft",
            "**STR** 12  **DEX** 14  **CON** 12  **INT** 2  **WIS** 11  **CHA** 4",
            "**Challenge** 1 (200 XP)",
        ],
        "actions": [
            ("Bite", "+5 to hit, reach 5 ft. Hit: 9 (1d8+1) piercing plus 4 (1d6) "
             "cold, and a DC 13 Con save or poisoned for 1 minute."),
            ("Web (Recharge 5-6)", "+4 to hit, range 30 ft. On a hit the target is "
             "restrained by webbing (DC 13 Str to escape)."),
        ],
    }, {
        "name": "Frozen Will-o'-Wisp",
        "sub": "Tiny undead, chaotic evil ✦ CR 2 ✦ lights over a frozen pond",
        "img": f"{A}/monsters/frozen_will_o_wisps.png", "img_w": 1.7,
        "stats": [
            "**AC** 15  **HP** 22 (5d8)  **Speed** 0 ft, fly 50 ft (hover)",
            "**STR** 1  **DEX** 18  **CON** 10  **INT** 10  **WIS** 12  **CHA** 11",
            "**Resist** cold, lightning; nonmagical B/P/S",
            "**Imm.** poison ✦ (cond) exhaustion, grappled, paralyzed, prone",
            "**Challenge** 2 (450 XP)",
        ],
        "actions": [
            ("Icy Shock", "+5 to hit (melee spell), reach 5 ft. Hit: 9 (2d8) "
             "lightning plus 4 (1d6) cold."),
            ("Invisibility", "The wisp turns invisible until it attacks."),
        ],
    }], {"pack": True}),
    ("tactics", "One roll per trek: whenever the party sets out from Havenmoor or "
                "heads back, roll once on the d20 travel table in Part Two. Not "
                "every threat must end in blows: the Yule Cat seeks generosity, so "
                "offering food or gifts can delay its attack entirely (Wisdom "
                "(Animal Handling) DC 15 calms it for a round), and Wisdom "
                "(Insight) DC 14 catches the malice behind the Frost Hag's smile "
                "before anyone touches her treats. The bandits are desperate, not "
                "wicked; Persuasion DC 15 with an offer of food or warmth avoids "
                "that fight altogether. And when one of the Krampusshade's "
                "creatures is defeated (win against the Yule Cat or appease it, "
                "either way), it leaves behind a wrapped gift box: roll on the "
                "Gift Box Table."),

    # Fills the travel-section closer page before the boss appendix begins.
    # D7 "The Longest Night" (world_history.md), placed here for the Krampusshade
    # "Longest Night" boss that follows; avoids duplicating the "Bells of the Coast"
    # box that already sits on Faelan's page in Part Three.
    ("lore", "The Longest Night",
     "The Circle marks one night a year when the dark leans hardest on the world, and teaches "
     "that it is not to be feared but outlasted. Kindle a light, share a warm meal, ring a true "
     "bell, and keep one another company until dawn, the old rule runs, for the longest night "
     "has never once failed to end, and the things that walk it are hungriest for the lonely."),

    ("fight_header", "BOSS: The Longest Night",
     "Havenmoor market square ✦ Difficulty: Boss ✦ Krampusshade + 4× shadow imp (2 more, round 2)"),
    ("enemy_cards", [{
        "name": "Krampusshade",
        "sub": "Large fiend, chaotic evil ✦ CR 5 ✦ never slain, only banished",
        "img": f"{A}/monsters/krampusshade.png", "img_w": 3.2,
        "stats": [
            "**AC** 15 (natural armor)  **HP** 102 (12d10+36)  **Speed** 40 ft",
            "**STR** 18  **DEX** 14  **CON** 16  **INT** 12  **WIS** 14  **CHA** 17",
            "**Saves** Wis +5, Cha +6",
            "**Resist** cold, necrotic; nonmagical B/P/S",
            "**Imm.** poison ✦ (cond) charmed, frightened, poisoned",
            "**Senses** darkvision 120 ft",
            "**Challenge** 5 (1,800 XP)",
        ],
        "traits": [
            ("The Bells Are His Undoing", "Each completed phrase of the carol (a round in "
             "which all eight Winter Bells sound) sears him for 2d10 radiant damage and locks "
             "Shadow Step until the start of his next turn. The finished carol banishes him "
             "outright, whatever hit points he has left; reduced to 0 HP, he is banished all "
             "the same, never slain, only unmade into wisps of shadow."),
        ],
        "actions": [
            ("Multiattack", "One Claw and one Chains of Despair."),
            ("Claw", "+7 to hit, reach 10 ft. Hit: 11 (2d6+4) slashing plus 5 (1d10) cold."),
            ("Chains of Despair", "+7 to hit, reach 15 ft. Hit: 11 (2d6+4) bludgeoning; "
             "DC 14 Str save or restrained for one turn."),
            ("Gift of Despair (Recharge 5-6)", "A cursed gift box appears within 30 ft; each "
             "nearby creature makes a DC 14 Wis save or is frightened for 1 minute."),
        ],
        "reactions": [
            ("Icy Retaliation", "When hit by a melee attack, the attacker makes a DC 14 Con "
             "save or takes 7 (2d6) cold and its speed drops by 10 ft."),
        ],
        "legendary": [
            ("Shadow Step (1/round)", "Teleports up to 20 ft to a space within dim light or "
             "darkness."),
        ],
    }]),
    ("enemy_cards", [{
        "name": "Krampusshade's Imp",
        "sub": "Small fiend (shadow), chaotic evil ✦ CR 2 ✦ 4 rise with him, 2 more in round 2",
        "img": f"{A}/monsters/krampus_imp.png", "img_w": 3.0,
        "stats": [
            "**AC** 14 (natural armor)  **HP** 22 (5d6+5)  **Speed** 30 ft, fly 40 ft",
            "**STR** 10  **DEX** 16  **CON** 12  **INT** 13  **WIS** 11  **CHA** 14",
            "**Skills** Stealth +6, Deception +4",
            "**Resist** cold, fire, necrotic; nonmagical B/P/S",
            "**Imm.** poison",
            "**Senses** darkvision 120 ft",
            "**Challenge** 2 (450 XP)",
        ],
        "traits": [
            ("Magic Resistance", "The imp has advantage on saving throws against spells and "
             "other magical effects."),
            ("Shadow Stealth", "Hides as a bonus action while in dim light or darkness."),
            ("Invisibility (3/short rest)", "Turns invisible until it attacks."),
        ],
        "actions": [
            ("Shadow Claws", "+5 to hit, reach 5 ft. Hit: 8 (2d4+3) slashing plus 3 (1d6) "
             "cold."),
            ("Shadowy Grasp (Recharge 5-6)", "One creature within 5 ft makes a DC 13 Dex "
             "save or is restrained for one turn, taking 5 (1d10) cold while held."),
        ],
    }]),
    ("tactics", "He opens big: freezing power across the square, chains lashing like "
                "serpents, imps boiling out of the fog. The frost-cracked ground within 10 ft "
                "of him is difficult terrain, and the villagers huddle at the Great Pine "
                "behind the heroes; keeping the imps away from them is worth Heroic "
                "Inspiration. The bells are the fight: each completed phrase sears him and "
                "locks his Shadow Step, the third banishes him outright, and dropping him to "
                "0 HP banishes him just the same. Spectacle, never a meat grinder: the sack "
                "of children bursts open the moment he comes apart."),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    out = build_doc(BLOCKS, "sessions/session_04_shadows_and_songs.docx")
    print("built", out)
