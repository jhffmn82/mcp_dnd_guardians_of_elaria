# build_session_08.py
# The Guardians of Elaria, Session 8: Underroot
# Publication build, matching the Session 6/7 house format: gold boxes are read
# aloud, purple boxes are for the DM, enemy cards close each fight.
#
# Canon baked in (memory/campaign_canon.md, endgame locked 2026-08-17):
#   - Aelwyn Ravenstone returns from Session 3; Tamsin does NOT travel to
#     Gearhaven; Lickgloom rides the luggage and gets the reunion beat.
#   - Stabby's idol goes cold near the ring and colder in the Gallery. Never
#     explained: it seeds the Shadow road he did not take.
#   - Ursa's shrine vision names NYXTHID for the first time in the campaign.
#     Elaria shows him three true things and withholds that the man walking east
#     and the shadow in black are the same person.
#   - Groudon is FREED, not killed: the Grand Custodian rule at ten times scale.
#   - Antares relights; Ursa is the only one who understands what he is seeing.
#   - Homecoming: Ghostbloom steps into the Sphere as tether, Sandshrew
#     manifests, and the party learns the companion-swap rule.
#   - Terra's Mote wakes Lilly's first Elemental Discharge, Tectonic Slam.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
S8 = f"{A}/session_08"
M = f"{A}/monsters"

BLOCKS = [
    ("titlepage", "THE GUARDIANS OF ELARIA", "SESSION 8", "Underroot",
     "An illustrated adventure. Read the gold boxes aloud; the purple boxes are for the DM."),

    ("h1", "Previously, on The Guardians of Elaria...", {"hardbreak": True}),
    ("gold", "In the clockwork city of **Gearhaven** the heroes found the **Grand Custodian**, the "
             "great machine that makes the city's heartbeat, caught and corrupted almost to "
             "breaking. They freed it instead of destroying it, and the city's wounds closed "
             "behind them on their own. That is the rule that governs everything now: **a crack "
             "between worlds cannot be sealed from our side, but free a world's guardian and its "
             "cracks close themselves.**"),
    ("gold", "**Guildmaster Vane** showed them his life's work: a ring of brass, ten years in the "
             "building, that could open a door to another world. It lacked one thing, an anchor, "
             "and the **Essence Sphere** is that anchor. Through Ursa's Mark, Pikachu's spark "
             "warned them in pictures instead of words: a vast hunger, a shadow that walks ahead "
             "of it, and the spark's own dread that it is *a key. To something.*"),
    ("gold", "The ring needed a year to finish. So the three of them went their separate ways, "
             "each with a question only a year could answer. **This session opens on the day they "
             "come back.**"),
    ("dm", "The heroes return at **level 7**. Do not hand out the new sheets yet; they land during "
           "**The Handover**, so the fiction and the paperwork arrive in the same beat. Part One is "
           "read like a chapter. Part Two is played on the Underroot board."),

    ("h1", "Part One: The Year Apart"),
    ("bridge", "Four arrivals, one long dinner, and a door that has never been opened."),

    ("h2", "Seven Days Early"),
    ("gold", "The Artificer's Guild never quite sleeps, but at midnight it comes close. Down in the "
             "Underworks the furnaces are banked to a low orange mutter, and the great ring of the "
             "portal stands in the middle of the Rift Hall like something dreaming. The Rift Hall "
             "is the tall room at the head of the Underworks, galleried and railed the whole way "
             "around, and its clerestory windows sit above the roofline, so that even down here a "
             "person can look up and find a piece of the Gearhaven sky.\n"
             "Lilly Glimmergear has been here a week. She told herself it was to check the anchor "
             "housing. Really it was because she could not stand another night of waiting somewhere "
             "else.\n"
             "The ring is finished. Ten years of Guildmaster Vane's life, finished for eleven days "
             "now, and nobody has dared to switch it on."),
    ("img", f"{S8}/A_the_finished_ring.png",
     "The lamp at the foot of the ring has been burning all week.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("dm", "**Three things to land during Lilly's week.** **Vane has aged**: ten years of work "
           "ended eleven days ago and he does not know what to do with his hands, so he is louder "
           "than usual, sleeping less, and will not say he is frightened. **Lilly is the expert "
           "now**: the guild artificers ask her opinion and mean it. And **the cradle does not "
           "quite fit**, because Vane built it from drawings of a sphere he had only had described "
           "to him. When Lilly finally sets the real thing in on the sixth night, the brass closes "
           "around it as though it were cut for it. Play that quiet. It is the first hint of what "
           "she learned this year."),

    ("h2", "The Professor"),
    ("gold", "On the third morning of Lilly's week, three trunks arrive at the Guild gate, and "
             "behind them comes Professor Aelwyn Ravenstone. He is exactly as everyone remembers "
             "him and slightly worse: tall, silver haired, entirely certain, and delighted to be "
             "proven wrong about anything as long as he is the one doing the proving.\n"
             "He looks at the ring for a long moment. Then at the Sphere in its cradle. Then he "
             "says, to nobody in particular:\n"
             "\"Oh. That is much older than you think it is.\"\n"
             "He says it the way other people say good morning."),
    ("img", f"{S8}/B_aelwyn_arrives.png",
     "Three trunks, no porters, and one small green passenger who did not pay a fare.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("body", "**Lickgloom remembers them.** He stayed behind at Ravenstone Laboratory two years ago "
             "and has spent the time since licking a professor's equipment. He rode the luggage the "
             "whole way here. He recognises each hero on sight as they arrive through the week, and "
             "he is beside himself about it every single time. Give this a beat: it is the only "
             "uncomplicated happy reunion in the whole session."),

    ("h2", "Dawn, and the Eastern Gate"),
    ("gold", "Ursa Catchum comes in with the dawn traffic, on foot, with road dust to his knees.\n"
             "He is taller. That is the first thing anyone notices. The second is that he is quiet "
             "in a way he never used to be. He waits half a beat before he answers a question, as "
             "though he is listening to something a half second behind the voice. In his left hand "
             "is a stone that he turns over and over without seeming to know he is doing it.\n"
             "He has been walking east for a year. He does not look like someone who found what he "
             "was looking for. He does not look like someone who failed, either."),
    ("img", f"{S8}/C_ursa_at_the_eastern_gate.png",
     "First light on the Eastern Gate, and the guards wave through a traveler they do not "
     "recognize until he has already passed.", 6.2, {"crop": "3:2", "hmax": 4.3}),

    ("h2", "Ten to Midnight"),
    ("gold", "On the last night of the year apart, the bell over the Rift Hall doors has not rung "
             "all evening. It does not ring now either, because the goblin coming through them does "
             "not touch them.\n"
             "He is on the rail above everyone before anybody thinks to look up. He is leaner, and "
             "there is a new sword across his back, dark and quiet, and when he drops down into the "
             "lamplight he lands without a sound, which he absolutely never used to do.\n"
             "\"I'm not late,\" says Stabby Sharpblade. \"It's still today.\""),
    ("img", f"{S8}/D_stabby_drops_from_the_rafters.png",
     "Ten minutes in hand, and he has almost certainly been in Gearhaven since the afternoon.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("dm", "**The idol, lightly.** When Stabby swings his pack down, something inside knocks "
           "against the flagstones with a dull, wrong sound. It is the small carved idol that "
           "appeared in his bag after Wraithpine, which nobody has ever explained and no one saw "
           "put there. Tonight, forty feet from a portal that is not even lit, **it is cold enough "
           "to burn**. He has carried it a year and it has never done that. Do not explain it. Do "
           "not promise anything about it. Let it sit."),
    ("gold", "And then, for the first time in a year, all of you are standing in the same room.\n"
             "Nobody makes a speech. Stabby hugs Lilly hard enough to lift her off the floor, and "
             "Ursa puts a hand on each of their shoulders, and Lickgloom licks everyone whether "
             "they consent or not. Vane watches from the gallery rail and pretends he is checking "
             "a gauge.\n"
             "Tomorrow the ring opens. Tonight there is a year to account for."),

    ("h1", "One Long Dinner at the Gilded Gear"),
    ("bridge", "Three heroes, three stories, and a kitchen that has been told to keep the fire lit."),
    ("gold", "The Gilded Gear keeps its back room for guild business, and Vane has declared this "
             "guild business. The table is long, the food keeps coming, and nobody has to be "
             "anywhere until morning.\n"
             "Three of you have a year to tell. So you go around the table, and the telling takes "
             "most of the night, and nobody minds at all."),
    ("dm", "**Each chapter is a told tale.** The hero telling it is at the table; hand that "
           "player the floor before you begin, and read the chapter with them, letting them "
           "interrupt and add color. It is their year. This order builds best: Lilly's tale is the "
           "most hopeful, Stabby's is the loudest, and Ursa's changes the shape of the campaign, "
           "so it goes last."),

    ("h2", "Lilly Tells It: The Year of Questions"),
    ("gold", "Lilly goes first, because she has props. She lifts the Essence Sphere onto the table "
             "between the bread and the butter, which alarms everyone, and pats it like an old "
             "friend, and begins with the morning she carried it up her mother's lane."),
    ("dm", "**Hand Lilly's player the floor.** Everything below happened during her year, and she "
           "was there for all of it; invite her to tell parts of it in her own words."),
    ("img", f"{S8}/L_poots_at_the_door.png",
     "Deepforge Hollow, and a mother with flour on her hands.", 6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "She went home first. That surprised everyone, Lilly included. She set the Essence "
             "Sphere on her mother's kitchen table and said: tell me everything.\n"
             "It was the least satisfying conversation of her life. Poots told her about the day "
             "she brought the Sphere home, about the long nights fitting the brass around it, "
             "about the sigil work along the equator that took eleven tries to get right. She "
             "talked like a craftsman describing a commission.\n"
             "And Lilly, who had grown up on her mother's stories, noticed the one thing the story "
             "never touched. **Poots never once said where the thing inside the brass had come "
             "from.**"),

    ("h2", "The Trade Roads"),
    ("img", f"{S8}/M_sparkwicks_verdict.png",
     "The verdict at Glimmerspire took him most of a morning to say out loud.",
     6.2, {"crop": "4:3", "hmax": 4.4}),
    ("gold", "So she went looking.\n"
             "She earned her answers out of Master Sparkwick at Glimmerspire, one stubborn "
             "question at a time, and his verdict sent her down the trade roads. She paid a dozen "
             "artificers in the only currency she had, which was work.\n"
             "A season with a clockmaker who could not cast a single spell and whose escapements "
             "humbled her anyway. Weeks on the road between one workshop and the next, the Sphere "
             "wrapped in wool at the bottom of her pack. Two more passes through Gearhaven with "
             "Vane shouting about tolerances.\n"
             "By midwinter her craft had gone from clever to formidable, and she still did not "
             "have her answer."),

    ("h2", "The Hands Workshop"),
    ("img", f"{S8}/N_the_hands_workshop.png",
     "Every joint on the bench is for somebody waiting to go back to work.",
     6.2, {"crop": "4:3", "hmax": 4.4}),
    ("gold", "The best six weeks were with a woman who built hands for injured miners. Brass "
             "fingers, clever joints, work that had to be right because somebody's whole life "
             "would hang on it. Lilly learned more about listening to a mechanism in that "
             "workshop than in any year of her life.\n"
             "She took the Sphere to wizards too, because wizards ask what a thing *is*. One of "
             "them fainted. Another wrote her four increasingly frantic letters. None of them "
             "knew."),

    ("h2", "The Forty-First Opening"),
    ("gold", "The answer was in the brass the whole time.\n"
             "On the forty-first time she opened the housing, she stopped admiring her mother's "
             "sigils and looked *underneath* them. And there they were: older marks, in another "
             "hand, on a surface that should have been the inside of her mother's shell and was "
             "instead the outside of something else."),
    ("img", f"{S8}/E_the_marks_under_the_brass.png",
     "Lantern light and a loupe: forty openings were one too few.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "Lilly looks around the dinner table and says it plainly, because she has checked it "
             "forty-one times and it is proof, not theory.\n"
             "**Her mother did not make the Essence Sphere.** Poots Glimmergear found it, "
             "understood it was worth protecting, and spent a year of her own life building it a "
             "house.\n"
             "And the thing Lilly worked out on a workshop floor a long way from home: **it is a "
             "gatherer.** It was built to pull in loose planar essence and hold it. It held "
             "Pikachu because Pikachu's spark was loose, and the Sphere does not know the "
             "difference between a scrap of stray fire and somebody's friend. You cannot pick a "
             "gatherer's lock. You can only give it something to gather.\n"
             "So she stopped building at it, and started listening to it."),
    ("dm", "**What she brings back.** *Aether Channeler*: she can draw the **Aether Ward** out of "
           "the Sphere, **2d8 + 5 temporary hit points** to herself and every friend within 30 "
           "feet, **twice per short rest**. The five great discharges sleep until each plane's "
           "Mote comes home; **her power now grows by going out**, which is the whole point. Also "
           "*Flash of Genius*: **+5 to a failed check or save** for her or any friend within 30 "
           "feet, five times a day."),

    ("h2", "Stabby Tells It: The Year He Went Back"),
    ("gold", "Stabby waits until the plates are cleared, then climbs onto his chair, because his "
             "story requires standing up.\n"
             "It starts, he says, a long time before this year. It starts with a clan that had one "
             "joke, and the joke was him."),
    ("dm", "**Hand Stabby's player the floor.** This chapter runs from his childhood to the day "
           "he came back; let him act out as much of it as he wants."),
    ("gold", "Every clan has one child who is a problem, and the Bloodfang had Stabby.\n"
             "Goblin children learn the clan's arts from the time they can stand, and the arts "
             "simply did not take with him. Every stance slid off. He was not lazy and he was not "
             "stupid. He was *unteachable*, in a clan with exactly one measure of a person's "
             "worth, and by the time he was five everyone had quietly agreed what he was going to "
             "be.\n"
             "So he became the joke on purpose. If they were going to laugh anyway, he would "
             "decide what they laughed at."),
    ("body", "Then **Skitch** came. The young Bloodfang courier the party pulled half-dead out of "
             "the machinery under Gearhaven had been sent a very long way to find the only "
             "Bloodfang anyone could name who had gone out into the world and come back alive "
             "from anything. Stabby laughed at him, because the clan asking for help was the clan "
             "that had spent his whole childhood explaining he was not worth teaching. Then he "
             "stopped laughing, packed in about four minutes, and went."),
    ("gold", "**Bloodthorn Hollow was dying, and the blight took the strongest first.** The "
             "biggest hunter, then the second biggest, then on down the list. The Bloodfang had "
             "one law, which was that the biggest goblin wins, and something in the woods was "
             "eating them in order.\n"
             "By the time Stabby walked back in, the clan was mostly the small ones. The "
             "overlooked ones. He knew every single one of them. He had been the smallest of them "
             "once.\n"
             "He saved them the way he does everything, fast and loud and extremely well: eleven "
             "weeks of hunting, the whole Hollow moved twice over furious objection, traps a "
             "cleverer person would not have thought of. By the end of summer the Bloodfang were "
             "not dying anymore.\n"
             "But he had not fixed it. He had only outrun it. Candyfang went through the "
             "corrupted things the way a knife goes through smoke."),

    ("h2", "The Fourth"),
    ("img", f"{S8}/O_nokk_and_the_fourth.png",
     "Nokk waited nine years for somebody to ask the right question.",
     6.2, {"crop": "4:3", "hmax": 4.4}),
    ("gold", "It was old Nokk who finally told him why, by a banked fire, in the voice goblins "
             "save for things that must only be said once.\n"
             "**His father was the Fourth.** The fourth leader the Bloodfang ever named, and by "
             "every account the best of them. Nine years ago something came out of the deep "
             "woods, and the Fourth went to meet it alone, and he did not kill it, because it was "
             "not the kind of thing that can be killed. **He sealed it.** The only vessel to hand "
             "that night was his newborn son, and it cost him his life to do it.\n"
             "The clan is named Bloodfang for that thing. Not for their own teeth. **The Red "
             "Fang** is older than the Hollow.\n"
             "And that is why the arts never took. There was something enormous asleep behind "
             "Stabby's ribs, pushing back against every form they poured into him. **He was "
             "never unteachable. He was occupied.**"),

    ("h2", "The Vigil on Kettlecrown"),
    ("imgrow", [(f"{S8}/stabby_the_stillness_test.png",
                 "The entire test is holding still."),
                (f"{S8}/P_the_bullywug_forge.png",
                 "A Nichirin blade is a graduation, not a gift.")], 3.1),
    ("gold", "Nokk knew one more thing: where the Fourth had learned to seal what cannot be "
             "killed. A mountain called Kettlecrown, and a sect on it called the Vigil.\n"
             "The Vigil are frog-folk, bullywugs grown enormous with age, and they cared about "
             "exactly one thing, and they tested it on his first morning. They asked him to be "
             "**still**. Not to sit quietly, which he could have faked. Still, entirely, from the "
             "inside, in the moment before violence.\n"
             "He failed for eleven weeks. He nearly left twice. And then in the third month, in "
             "the dark, he finally heard the thing Master Kaelon Windstep had said to him years "
             "ago: *when the whole world is screaming, little storm, get still.*\n"
             "He had always heard it as an order to calm down. It was not. It was smaller and far "
             "more useful. **Be still for one second, at the one moment that matters.** One "
             "second, Stabby could do."),

    ("h2", "The Forge"),
    ("gold", "The sword came last, because among the Vigil a **Nichirin blade** is a graduation, "
             "not a gift. He worked the bellows for eight days of its making, and when it was "
             "done the masters put it in his hands and did not say congratulations, because the "
             "blade was the congratulations.\n"
             "It is the dark, quiet sword on his back right now. It cuts corruption out of a "
             "living thing without cutting the living thing. That is the whole art, and it took "
             "him a year."),

    ("h2", "Home in Winter"),
    ("img", f"{S8}/Q_the_purge.png",
     "The woods the Bloodfang stopped walking in two years ago.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "He came home in deep winter and did what he had promised: he went into the twisted "
             "woods and burned the blight out of the ground, root and all.\n"
             "The Bloodfang had watched their biggest and best taken one after another for two "
             "years, and the thing that finally walked out of those woods with the blight dead "
             "behind it was **the runt**. The clan joke. The one they had all quietly agreed was "
             "not worth teaching.\n"
             "There is not a goblin in the Hollow who will hear a word against him now."),

    ("h2", "Teaching the Count"),
    ("img", f"{S8}/R_teaching_the_count.png",
     "The first class in Bloodfang history where nobody is measured against anybody.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "The Vigil made him a monk. What made him something else was teaching it. Before he "
             "left, he lined up the smallest goblins in the Hollow, the overlooked ones, the ones "
             "he used to be, and taught them the count: one second of stillness, at the one "
             "moment that matters. The Vigil gave him the basics. His clan gave him the rest."),
    ("dm", "They offered him his father's seat and **he said not yet**, and Nokk was the only one "
           "who noticed he did not say never. He gave them Candyfang as the clan's heirloom, and "
           "by their new law the heirloom is carried by whoever the clan would follow, which is "
           "why it is still on his belt. It is not his anymore. It is theirs, and he is only "
           "wearing it."),
    ("gold", "Stabby sits back down, upside-down grin firmly in place.\n"
             "\"Anyway,\" he says. \"I got a sword.\""),

    ("h2", "Ursa Tells It: The Road East"),
    ("gold", "The fire has burned low by the time it is Ursa's turn, and he does not stand up. He "
             "sets both hands flat on the table, with the stone he carries between them, and for "
             "a moment he just looks at it.\n"
             "\"The two of you went home,\" he says. \"I went the other way.\""),
    ("dm", "**Hand Ursa's player the floor, and slow the room down.** This is the chapter that "
           "changes the shape of the campaign. Read it last, read it quietly, and do not rush "
           "the ending."),
    ("img", f"{S8}/T_selarin_and_the_cabinet.png",
     "Selarin knew from the first hour that he would unlock it.",
     6.2, {"crop": "4:3", "hmax": 4.4}),
    ("gold", "He went first to the Circle, to old Selarin, and asked for his father's papers.\n"
             "\"You are eight,\" Selarin said.\n"
             "\"I know how old I am,\" said Ursa.\n"
             "They argued for nine days, in the patient way druids argue, which mostly looks like "
             "silence. On the ninth day the old man unlocked the cabinet and handed over Ash "
             "Catchum's field notes without a word. Then he said one thing, which Ursa has "
             "repeated to nobody until tonight: *your father read the sky better than any of us. "
             "It did not save him. Read the ground too.*\n"
             "The notes are the working papers of a man in the middle of a thought. Sky charts "
             "with dates. The same constellation drawn eleven times over eleven months, one point "
             "of light fainter in each drawing. And one word, underlined twice and never "
             "explained: **Betelgeuse.** The first star to go out.\n"
             "The notes stop in the middle of a page. Not at the end of a thought. In the middle "
             "of one."),

    ("h2", "The Skyless Country"),
    ("img", f"{S8}/U_the_cairn.png",
     "The Skyless Country has no horizon; it has the next cairn instead.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "He went east on foot and **alone**, because Ghostbloom stayed at the Guild and "
             "where he was going had no roads. Eleven months of walking.\n"
             "When the maps ran out he came into a country where the cloud never breaks. No sun, "
             "no stars, no shadows to steer by. For a druid who navigates by constellations it "
             "was a blindfold, and he lost eleven days in there, and he will not talk about the "
             "eleven days.\n"
             "What saved him was that his father had been there first. **A road of cairns**, "
             "each placed exactly at the edge of sight of the last, so a person could cross the "
             "blind land one stone at a time. Ash built it going out. Ursa walked it going in, "
             "and **repaired eleven of them on the way**, because there was no reason to assume "
             "he would be the last person to need the road."),

    ("h2", "The Camp"),
    ("img", f"{S8}/G_the_empty_camp.png",
     "The tin cup is still where a hand last set it down.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "He did not find his father. He found the camp his father made.\n"
             "A firepit long cold. A shelter of bent living branches, still holding. Split wood "
             "stacked ready under cover. Nothing packed. Nothing buried. **Nobody had said "
             "goodbye to this place.**\n"
             "And he found out how long ago by doing exactly what Selarin told him: he read the "
             "ground. The shelter was still alive and still growing, and the wood had closed "
             "over the bindings by an amount a druid can read like a page.\n"
             "Not fifteen years. **Three.**"),

    ("h2", "The Half-Carved Stone"),
    ("img", f"{S8}/V_the_half_carved_stone.png",
     "The one thing in the whole camp his father thought to protect.",
     6.2, {"crop": "4:3", "hmax": 4.4}),
    ("gold", "Under the flat rock by the firepit, wrapped in oilcloth, was a river stone carved "
             "with Elaria's seven-pointed star. **Half of it.** The line stops mid-stroke, the "
             "way a pen stops when somebody says your name. It is his father's hand.\n"
             "When Ursa closed his fingers around it, the stone was warm. It has been warm ever "
             "since.\n"
             "He sets it on the dinner table now, and everyone understands at once that this is "
             "the stone he has been turning over since the Eastern Gate."),

    ("h2", "The Eighth Night"),
    ("img", f"{S8}/H_the_vision_in_the_stones.png",
     "The old shrine has been waiting a long time for somebody to keep an eighth night.",
     6.2, {"crop": "4:3", "hmax": 4.4}),
    ("gold", "He stayed at the old shrine eight nights. On the eighth, the cloud broke, the "
             "standing stones lit from the inside, and **Elaria showed him three things.**\n"
             "The first was his father, **walking**, deliberately, toward a light that was going "
             "out. Ursa has carried one small ugly question since he was old enough to understand "
             "the word *disappeared*: did my father choose to leave me? The answer is yes, and "
             "the reason is the best reason there has ever been. **Ash Catchum went east to save "
             "the stars.**\n"
             "The second was a wall at the bottom of everything, and behind it a hunger with "
             "patience, pressing. He knew the name from the Circle's old verses before the "
             "vision finished giving it to him. **Maldrith.**\n"
             "The third was a shadow that walks for her, on a high place with the sky dying "
             "behind it, putting out a light as calmly as a person pinching a candle. And the "
             "vision gave that one a name too, the way you hand somebody a weapon.\n"
             "**Nyxthid.**"),
    ("dm", "**This is the first time the name Nyxthid is spoken in this campaign.** Ursa has just "
           "sworn to hunt his own father and will spend four sessions doing it. Elaria did not "
           "lie to him: every single thing she showed him is true. She simply did not show him "
           "that the man walking east and the shadow in black are the same person. **Keep the "
           "figure featureless.** No face, no build, nothing that can be matched later. If a "
           "player asks what it looked like, it looked like a hole in the shape of a person."),
    ("gold", "\"I swore to hunt it,\" Ursa says. \"The shadow. Whatever it is.\"\n"
             "He picks the stone back up and closes his hand around it.\n"
             "Nobody speaks. The fire is down to embers, and out past the shutters the great "
             "city has gone quiet, and tomorrow the ring opens.\n"
             "It is Lickgloom who ends it, by falling asleep face-first in the butter."),

    ("h1", "The Handover"),
    ("bridge", "Three stories told, and one day left before the door opens."),
    ("img", f"{S8}/lilly_gifts_laid_out.png",
     "Puff supervised the polishing, and she will tell you so.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "Lilly has been awake since four in the morning. When the rest of you come down to "
             "the workshop the lamps are already lit, and there are four cloths laid out along "
             "the bench: one for each of you, and a fourth at the end for **Puff**, the small "
             "clay homunculus Lilly built and woke up herself. Puff is sitting beside her own "
             "cloth with her hands folded, plainly very proud, and she has been sitting that way "
             "for some time.\n"
             "Lilly has a speech prepared. You can tell, because she gets about six words into "
             "it, gives up, and just starts handing things over."),
    ("dm", "**Hand out the new character sheets here**, so the fiction and the paperwork land in "
           "the same beat. Six magic items arrive on three players at once and none of them "
           "works like a sword, so teach the traps now, in a quiet room, rather than on the far "
           "side of the ring."),
    ("reward_card", "What Lilly Built During the Year", "Sorted by whose cloth it is sitting on", [
        ("Wraps of Unarmed Power +2 (Stabby)",
         "No attunement, nothing to activate. +2 to hit and damage on every punch and kick, and "
         "they may deal Force. **The trap:** they do nothing at all for the katana."),
        ("Wand of the War Mage +2 (Ursa)",
         "While he is **holding** it, every spell attack gains +2 and he ignores Half Cover. Starry "
         "Wisp, his Guiding Bolts and the star-arrow all go to +10. **The trap:** it does not touch "
         "his save DC."),
        ("Wand of Web (Lilly)",
         "7 charges, 1 to cast Web. **The trap:** it casts at its own **DC 13**, not her DC 16."),
        ("Ring of Spell Storing (Puff)",
         "Holds 5 levels of spells and casts them at the original caster's DC and slot. **The "
         "trap:** it arrives EMPTY and does nothing until somebody casts into it."),
        ("Wand of Magic Missiles (Puff)",
         "1 charge for three darts that never miss, 1d4+1 force each, 120 ft. Up to 3 charges for "
         "five darts."),
        ("Pipes of Haunting (Puff)",
         "3 charges. Magic action: every creature she chooses within 30 ft. makes a DC 15 Wisdom "
         "save or is Frightened for a minute."),
    ]),
    ("dm", "**Puff has one action**, so she uses only one of her three items per turn. And "
           "**wands recharge at dawn, not on a rest**, which matters on the far side of a portal "
           "where nobody knows how time runs."),

    ("h1", "The Briefing"),
    ("img", f"{S8}/I_aelwyns_briefing.png",
     "The professor brought diagrams. Vane brought objections. Lickgloom found something to chew.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "After supper Aelwyn clears the long table, pins up a map of nothing anyone has ever "
             "mapped, and gives you the truth in his lecture voice, which is the kindest voice he "
             "owns."),
    ("body", "**One.** The rifts are not doors somebody opened; they are tears, and everything "
             "strange the party has fought for two years came through one. **Two.** You cannot sew "
             "a tear from this side: you go to the other side and bring back the plane's **Mote**, "
             "the piece of its heart caught here. **Three.** The Sphere is the anchor and the way "
             "home, and **if it is lost over there, they do not come back.** Say that once, "
             "plainly, and never repeat it. **Four.** Every Mote returned wakes a little more of "
             "the Sphere. **Five.** Something living may come back with them, and Aelwyn is "
             "carefully vague, because he is guessing."),
    ("gold", "\"I want you to understand that I am not sending you somewhere dangerous,\" Aelwyn "
             "says. \"I am sending you somewhere *indifferent*. A plane is not hostile to you any "
             "more than a mountain is hostile to you. It simply does not care whether you can "
             "breathe there. Everything that hurts you on the other side will hurt you the way "
             "weather does.\"\n"
             "Vane snorts. \"That is a terrible speech.\"\n"
             "\"It is an honest one.\""),

    ("h2", "The Lesson: Underroot, and the Thing That Lives There"),
    ("img", f"{S8}/K_the_lesson.png",
     "He has waited his whole career to give this lecture, and it shows.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "\"Earth,\" says Aelwyn, \"is not a cave. Get that out of your heads right now. You "
             "are not going underground. You are going to a place that is *made* of ground, all "
             "the way through, in every direction, forever.\n"
             "\"It is called Underroot. There is no sun there, and there has never needed to be "
             "one. There are roots down there the size of cathedrals. They are alive, and they "
             "are older than your species. The soil breathes, slowly, about once a minute, "
             "everywhere at once. And nothing down there is in a hurry, which will be the "
             "strangest part for you three.\""),
    ("dm", "**Three facts the players need for Part Two.** It is **slow, not empty**: a rockfall "
           "there is a shrug. There is **no sky, so Ursa cannot navigate**, and his year of "
           "star-reading buys him nothing; what works down there is reading the ground, exactly "
           "as Selarin told him. And it is **indifferent, not hostile**."),
    ("gold", "\"Every world keeps something. Not a king, and not a god. A *guardian*: one "
             "creature, very old, that is somehow the shape of that world's health. When "
             "Gearhaven was sick you found the Grand Custodian at the heart of it, twisted almost "
             "past recognition, and when you freed it the whole city knitted shut behind you. Do "
             "you remember?\"\n"
             "He taps the board. \"You did not do that by being clever. You did it by being "
             "*kind* to something that was hurting. I would like you to notice that, because you "
             "are about to do it again, and the thing you do it to this time is roughly the size "
             "of a hill.\"\n"
             "\"What if it fights us?\" says Stabby, delighted.\n"
             "\"Then I would prefer you not *lose*.\""),
    ("dm", "The Guardian of Underroot is **Groudon**, and the whole session is walking toward "
           "him. Aelwyn does not know his name and neither should the party: let them meet him "
           "as a shape in the dark and a sound in their teeth long before he is ever a stat "
           "block."),

    ("h1", "The Threshold"),
    ("dm", "Last beats before the crossing, in this order. **Ursa looks up** through the "
           "clerestory windows and sees that Antares is dimming, and says nothing; do not spend "
           "that, it pays off at the end of the night. **The idol goes cold** again in Stabby's "
           "pack, hard enough that he notices. **Lilly sets the Sphere in the cradle** and the "
           "brass takes it the way it did on the sixth night, without a hair of resistance. And "
           "**Vane does not make a speech**: he had ten years to write one, and what he actually "
           "does is put a hand on Lilly's shoulder for a second and then go and stand at the "
           "lever."),
    ("gold", "The ring does not roar.\n"
             "The Sphere settles into its cradle with one small brass click, and the air inside "
             "the circle simply stops being air. On the other side there is a red-brown dark, and "
             "warmth, and a smell like a garden turned over after rain, and a sound so low you "
             "feel it in your teeth instead of hearing it.\n"
             "Somewhere out in that dark, something the size of a hill breathes in.\n"
             "Ghostbloom goes first, because of course she does."),
    ("img", f"{S8}/J_the_threshold.png",
     "The first doorway between worlds ever opened on purpose.",
     6.2, {"crop": "3:2", "hmax": 4.3}),

    ("h1", "Part Two: Underroot", {"hardbreak": True}),
    ("bridge", "They stepped through a brass ring in a workshop in Gearhaven and came out "
               "the other side standing on something warm that was breathing."),

    ("h2", "How the Board Works"),
    ("img", f"{S8}/underroot_board.png",
     "The whole country between the ring and the Guardian, laid out one landing at a time.",
     6.4, {"hmax": 4.4}),
    ("dm", "**One token, everybody's hands.** The party moves as a single token. On their "
           "turn a player rolls **1d6** and moves that many spaces, and whoever holds the "
           "token rotates on every roll, so every player gets to move it. They land on a "
           "colour and it resolves at once."),
    ("dm", "**The die they moved with resolves the dot.** Each colour has two outcomes, and "
           "even or odd picks which one happens: no table to look up, no second roll, no "
           "pause. Slate blue is plain movement and does nothing on either result. All "
           "eight outcomes are written out in full in *The Road Between*."),
    ("dm", "**The four numbered locations are not dots.** They are fixed story stops. The "
           "token halts at each one no matter how much movement is left, the beat plays "
           "out, and movement resumes on the next turn. **The Rift Gate is the arrival and "
           "has no fight.**"),
    ("dm", "**They came here to fight.** Nothing in this session can be talked down, waited "
           "out, or avoided. Levers and objectives exist to turn a grinding fight into a "
           "satisfying one, never to skip it, and finding one is the reward."),
    ("dm", "**SHORT REST, immediately after the reef.** Call it out loud so nobody misses "
           "it: Hit Dice spent, Stabby's Focus back, Ursa's Wild Shape back, Lilly's "
           "Aether Ward back. Fight 3 assumes they took it."),
    ("dm", "**A note on the numbers.** Fights 2 and 3 sit deliberately above a \"deadly\" "
           "budget on paper, and both have a lever that collapses them: **thunder stuns a "
           "Chimestone and doubles all damage against it**, and **tending the roots strips "
           "the Weeper's regeneration**. A party that finds the lever wins comfortably. A "
           "party that ignores it is in a real fight. That gap is the fun, so do not "
           "soften either one before the players have had their chance to be clever."),

    ("h1", "The Road Between"),
    ("bridge", "Underroot is not empty between the landings, and the dark between them has "
               "its own weather."),
    ("gold", "The ground stays warm the whole way, and it goes on breathing under your "
             "boots, slow as something enormous asleep. There is no sky to measure your "
             "progress against, so the only way to know you are moving is the moss light "
             "going out behind you, patch by patch, as you leave it.\n"
             "Twice, something out in the dark keeps pace with you for a while. It is big "
             "enough to hear. It never arrives."),
    ("dm", "**How a dot resolves.** Read the die they moved with. **Garnet** is an "
           "Encounter (even: Thumpaw; odd: the Gleamoth). **Moss** is a Boon (even: the "
           "Deepwater Spring; odd: the Shortcut). **Ochre** is a Hazard (even: Sinkloam; "
           "odd: the Ceiling Lets Go). **Amethyst** is Wild (even: the Reef Answers; odd: "
           "the Guardian's Dream). Slate blue is simply movement: nothing happens, keep "
           "going."),
    ("imgrow", [(f"{A}/monsters/thumpaw.png",
                 "Thumpaw, the boulder that minds being prodded."),
                (f"{A}/monsters/gleamoth_swarm.png",
                 "The Gleamoth, hungry for the warmest thing in the tunnel.")], 3.1),
    ("dm", "**Garnet dots are small pressure, and that is all they are.** Two or three "
           "weak things that cost a little resource and no more. Never let a dot roll "
           "swell into a fifth big fight: the four scripted encounters are the session, "
           "and the dots are texture between them. Thumpaw and the Gleamoth appear "
           "nowhere else in Underroot, which is exactly what makes a garnet dot feel like "
           "luck instead of filler. Pace check: there are 22 dots between the gate and "
           "the Hollow, so if the evening is running long, hand-wave the dots between "
           "locations 3 and 4 and go straight to Groudon."),

    ("h2", "Thumpaw"),
    ("gold", "A shape unfolds out of what you took for a boulder. It is the size of a cart "
             "horse, round and shaggy with matted brown moss growing over stone-grey "
             "hide, and it has hands like shovels. It looks at you with small patient "
             "eyes and does not move, because you are standing in the tunnel it was going "
             "to use."),
    ("dm", "**Garnet dot, even. One Thumpaw.** It will not move, it is directly in the "
           "way, and when somebody inevitably prods it, it swings. This is a straight "
           "brawl and that is the point: **76 hit points**, two big slams a turn, no "
           "gimmick and no puzzle. Sometimes a table simply wants to hit something large "
           "until it stops, and this is that. It never pursues and it never finishes a "
           "downed hero; it is grumpy, not evil. If the party genuinely tries to befriend "
           "it rather than fight it, **DC 15 Animal Handling**, with advantage from "
           "Ursa's Mark of Handling, will move it aside. Do not offer that. Let them "
           "think of it."),

    ("h2", "The Gleamoth"),
    ("gold", "The lights come round the corner before the sound does: forty pale green "
             "sparks drifting like blown seeds. They are moths, each the size of a hand, "
             "and every one of them is glowing, and they want the warmest thing in the "
             "tunnel, which is you."),
    ("dm", "**Garnet dot, odd. Three Gleamoth Swarms**, not corrupted, just hungry for "
           "heat. They **blind and smother** rather than deal much damage, and they go "
           "for whoever is carrying light. **Fire and thunder scatter them fast**, so "
           "anything that hits an area is worth double here. The real cost is the Sphere: "
           "they are drawn to it hardest, which puts the swarm on Lilly for the whole "
           "fight and makes the rest of the party come to her."),

    ("h2", "The Deepwater Spring"),
    ("img", f"{S8}/events/D3_deepwater_spring.png",
     "The pool keeps its own light, a long way from any moss.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "A crack in the wall, and inside it a pool so still and so clear that the "
             "pale stones forty feet down look close enough to lift out. Nothing feeds "
             "it. Nothing drains it. And yet the surface keeps turning over, slow and "
             "patient, the way water moves when something a long way underneath it is "
             "still working. It is very cold, and it tastes like the air after "
             "lightning, and by the time you have all drunk, the ache has gone out of "
             "your legs and none of you can say when it left."),
    ("dm", "**Moss dot, even.** Everyone regains **1 Hit Die** and clears **one level of "
           "exhaustion**. Ghostbloom glows brighter for an hour and is insufferable "
           "about it."),

    ("h2", "The Shortcut"),
    ("img", f"{S8}/events/D4_sandshrew_shortcut.png",
     "A door where a minute ago there was wall.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "Something small and yellow-brown is waiting for you on a mound in the "
             "middle of the path, up on its back legs, and it does not run when your "
             "light finds it. It looks at you. Then it looks, very deliberately, at the "
             "blank wall on its left. Then back at you, and it keeps doing that until "
             "somebody understands. Then it drops and digs, and the packed earth goes "
             "soft in front of its claws like water, and the tunnel it opens runs "
             "straight and level and exactly the way you were trying to go. It is gone "
             "before any of you reach the far end. All it leaves behind is a scuffed "
             "patch of loose soil where it stood, and the distinct feeling of having "
             "been done a favour."),
    ("dm", "**Moss dot, odd. Advance the token 3 spaces free.** If the party was unkind "
           "to the Sandshrew at Mosslight Landing, it watches them take the long way "
           "round instead, and that should sting."),

    ("h2", "Sinkloam"),
    ("img", f"{S8}/events/D5_sinkloam.png",
     "Warm, wet, patient, and wearing the exact colour of the safe ground beside it.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "The floor stops being floor. There is no sound and no warning: one step is "
             "packed earth and the next is warm wet loam that takes your boot, then your "
             "shin, then your knee, and goes on politely taking. It is worst for the "
             "smallest of you: the loam does not care how clever anyone is, and whoever "
             "goes in deepest is suddenly fighting to keep their arms above the surface "
             "while the ground drinks the rest of them with terrible, unhurried "
             "patience."),
    ("dm", "**Ochre dot, even.** Everyone makes a **DC 13 Strength save** or is "
           "**restrained**, spending an action to pull free. Heavy armour has "
           "disadvantage on the save. If Lilly goes under, she holds the Sphere over "
           "her head with both hands the entire time, and somebody has to go back for "
           "her."),

    ("h2", "The Ceiling Lets Go"),
    ("img", f"{S8}/events/D6_rockfall.png",
     "You cannot outrun it. You can only be lucky.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "You feel it before you hear it: a low grinding roll somewhere far above, "
             "the sound a mountain would make turning over in its sleep. Then dust "
             "comes down in fine threads. Then the threads become gravel. You have "
             "exactly long enough to look up and understand what is about to happen, "
             "and nowhere near long enough to be somewhere else, and then the ceiling "
             "of the world lets go.\n"
             "When the roar stops and the air clears enough to breathe, the passage you "
             "came in by is not there. In its place is a wall of new stone, still warm, "
             "still shifting and settling against itself, and above you Underroot has "
             "already gone quiet again, as though it had shrugged in its sleep and "
             "thought nothing of it."),
    ("dm", "**Ochre dot, odd. DC 14 Dexterity save**, **2d10 bludgeoning** on a failure "
           "and half as much on a success. The passage behind them is now blocked, "
           "which matters a great deal if anyone was planning to run."),

    ("h2", "The Reef Answers"),
    ("img", f"{S8}/events/D7_the_reef_answers.png",
     "An invitation, sent through a mile of stone.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "Somewhere far off, a single crystal note. Then another underneath it, and "
             "another, until the whole tunnel is ringing in a slow enormous chord you "
             "can feel in your ribs, and the moss on the walls lights up in time with "
             "it."),
    ("dm", "**Amethyst dot, even.** Everyone gains **2d8 temporary hit points**, and "
           "Ghostbloom sings back, badly, at the top of her voice. **This is a good "
           "place for the short rest** if the party has not taken it yet."),

    ("h2", "The Guardian's Dream"),
    ("img", f"{S8}/events/D8_the_guardians_dream.png",
     "A memory that does not belong to any of them.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "For half a second the three of you see the same thing, and Ghostbloom sees "
             "it too, and none of you asked for it.\n"
             "An empty sea under an empty sky, going on forever. And something walking "
             "through it, huge and slow and patient, and where it walks the water "
             "shoulders aside and dry land comes up behind it, steaming, new.\n"
             "Then it is gone and you are standing in a tunnel again."),
    ("dm", "**Amethyst dot, odd. No mechanical effect.** They have just watched Groudon "
           "remember his own job, and they will not understand what they saw until they "
           "are standing in front of him. Ursa may **regain one spent Omen Dream**, "
           "because something has just spoken to him and he does not know what."),

    ("lore", "The Living Country",
     "The sky-readers teach that a plane is not a place but a creature: one living "
     "thing wearing a country for a body, with weather for moods and seasons for a "
     "pulse. Walk gently, the Circle says, for every step in another world is a step "
     "on somebody. The old verses go further still: each world keeps one guardian, "
     "very old, that is somehow the shape of that world's health, and to free a "
     "guardian is to heal the country it carries."),

    ("h1", "The Descent"),
    ("bridge", "Four stops between the ring and the Guardian: a doorway, a village of "
               "moss, a reef that sings, and a wound that will not stop spreading."),

    ("h2", "The Rift Gate: The First Breath"),
    ("img", f"{S8}/loc_rift_gate.png",
     "The first footprints anyone from Gearhaven has ever left in another world.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "You expected a cave.\n"
             "You are standing inside a root. One root, arched over you like the "
             "ceiling of a great hall, running away into the dark in both directions "
             "farther than your light can follow. The ground is warm under your boots, "
             "and soft, and it is breathing: a slow rise and settle, about once every "
             "minute, so gentle you have to stand still to be sure of it.\n"
             "There is no sky. There is no sun. There is light anyway, a low green-gold "
             "glow coming off the moss in patches, enough to see by, and the smell that "
             "came through the ring is everywhere now: turned earth after rain, warm, "
             "with no other air behind it.\n"
             "Behind you the ring hangs open, a bright coin of Gearhaven lamplight. "
             "Vane's shape is standing in it with his arms folded, getting smaller."),
    ("dm", "**Four beats to land here, one per hero and one for Ghostbloom.** **The "
           "Sphere is warm** in Lilly's hands, and it is *pulling*: she can feel it "
           "gathering, it has never done that before, and it does not stop for the rest "
           "of the session. **Ursa cannot navigate**, and say that to his player "
           "directly: no sky, no stars, and a year of star-reading buys him nothing. "
           "What does work is what Selarin told him, reading the ground, so give him "
           "**advantage on Survival** down here for root growth and soil. **Stabby's "
           "idol is cold**, colder than it was in the Rift Hall; he will keep checking "
           "it all session and it will keep getting worse. **Ghostbloom is delighted**, "
           "because she is a plant-spirit standing inside a plane made of growing "
           "things, and she has never been so happy. Let her chime read as joy all "
           "session, right up until the Hollow."),
    ("dm", "**No encounter here.** They get exactly one safe scene to be amazed. Do not "
           "spend it."),

    ("h2", "1. Mosslight Landing: The Friendly Face"),
    ("img", f"{S8}/loc_mosslight_landing.png",
     "The only place in Underroot that will seem glad to see them.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "The walk from the ring is the first walking any of you have done in "
             "another world. The ground gives a little under every step, warm as the "
             "flank of something asleep. The moss brightens ahead of you and dims "
             "behind, so the country opens the road one patch at a time and quietly "
             "puts it away again once you have used it. Ghostbloom rides at head "
             "height with every petal spread, chiming to herself. Nothing hurries you. "
             "Nothing follows. After an hour, that stops feeling like mercy and starts "
             "feeling like being noticed by something too big to be interested yet."),
    ("gold", "Then the root opens into a hollow the size of a village, and it is "
             "beautiful. Round mossy mounds rise out of the floor, each with a little "
             "round door of packed earth, though nobody built them and nobody lives in "
             "them; that is simply the shape moss grows in here. Threads of pale gold "
             "light drift up from the ground like slow sparks going the wrong way.\n"
             "Something is watching you from the top of the nearest mound. It is about "
             "the size of a badger, armoured in overlapping plates of yellow-brown "
             "hide, with small dark eyes and two enormous digging claws. It is holding "
             "absolutely still."),
    ("gold", "It is very bad at holding still. It is trembling slightly with the "
             "effort. One claw is still buried in the mound mid-dig, at an angle "
             "nothing would choose to stand at, and when Stabby waves at it, it does "
             "not wave back, because rocks do not wave. It has decided that it is a "
             "rock. It is going to be a rock until this crisis passes, and it commits "
             "to the performance with a dignity that would break your heart if it were "
             "not so funny.\n"
             "Here is the strange part: none of you reach for a weapon. It is not "
             "corrupted. You are all certain of that at once, without knowing why. It "
             "is just small, and you are new, and it got here first."),
    ("dm", "**This is the Sandshrew**, and unless a moss dot sends it back to dig them "
           "a shortcut, this is the only time they meet it in the flesh before the "
           "homecoming. **It cannot be caught, tamed, or bagged.** It watches them. If "
           "they are kind to it or feed it, it follows at a distance for the rest of "
           "the run and is present at the end. If they are aggressive, it vanishes and "
           "joins them at the homecoming anyway, which will feel like a gift they did "
           "not earn. **Ursa's Mark of Handling works on it**, and that should be the "
           "moment his player realises the plane's wildlife is not the enemy."),
    ("gold", "You could stay an hour in this place, and you nearly do. The mounds are "
             "warm to lean against. The gold threads rise slowly enough to pick one "
             "and follow it all the way up into the dark.\n"
             "It is Ghostbloom who notices. Her chime changes in the middle of a note, "
             "the way a voice changes when it sees something over your shoulder, and "
             "she goes very still in the air, pointing with her whole body at the far "
             "side of the hollow.\n"
             "The pretty part of Underroot has a wound in it. On the far mounds the "
             "moss is grey and wet and wrong, and standing in the grey, swaying, are "
             "six little flower-creatures.\n"
             "They were lovely a month ago. You can still see it: round soft bodies, "
             "stubby arms, big round flower-caps that used to be gold. The caps are "
             "grey now, and slack, and they leak. When they notice you they all turn "
             "at once, and their faces are still smiling, because their faces cannot "
             "do anything else."),
    ("dm", "**Let the players choose the moment.** The Rotblooms do not charge. They "
           "come on at a sway, slow as weather, leaking as they walk, and the grey "
           "spreads a hand's width behind them wherever they linger. Give the table a "
           "round of looking: some heroes will strike at once, some will try to talk "
           "to the smiling faces, and somebody may work out before a single swing "
           "that the flowers are not attacking, they are *spreading*. None of it "
           "changes what has to happen; this cannot be talked down, and left alone "
           "the grey takes the whole landing. But the party should walk into their "
           "first fight in Underroot knowing the enemy is the grey, never the flower "
           "wearing it. **The moment anyone engages, the instant the first cap is "
           "struck, read:**"),
    ("gold", "Then the moss itself comes apart. The instant the first cap is struck, "
             "the ground boils: tiny six-legged things, one enormous eye apiece, "
             "pouring out of the mounds in a wave and swarming up your boots.\n"
             "And Ghostbloom makes a sound you have never heard her make. She knows "
             "what these are. They are almost the same as her."),
    ("img", f"{S8}/fight1_the_landing.png",
     "Six that spread the grey, and a whole floor that rises to defend them.",
     6.2, {"crop": "3:2", "hmax": 4.3}),

    # ENEMY_CARDS_FIGHT_1
    ("dm", "**This fight exists to hand Stabby the session.** Rotblooms re-bloom every "
           "round, and ordinary steel keeps handing back ground it already won: leave "
           "one standing and part of that cap has swelled shut again before its next "
           "turn, so a good round of hits can end with the same six flowers swaying "
           "at them. **Cleansing Edge is the answer, and it is the only one the party "
           "has.** Let them flail for a round, let Lilly and Ursa watch pieces of "
           "their damage close up again, then let Stabby ignite, cut one, and have it "
           "*stay* cut. Say the reason out loud when it lands: he spent a year on a "
           "mountain learning to burn corruption out of the ground, and this is the "
           "first time anyone else has seen it work. His player has been carrying "
           "that backstory alone since the telling, so give him the beat."),
    ("dm", "**The Mossmites keep everyone honest.** Six of them, fast and cheap, "
           "swarming boots and climbing packs while the real problem re-blooms behind "
           "them. Spore Puff means the whole party is rolling saves, Puff and "
           "Ghostbloom are in the mix, and everybody gets three or four rounds of "
           "swinging. Nobody stands still and nobody is bored while they wait for the "
           "lever to reveal itself."),
    ("dm", "**The tell, for anyone watching closely:** the Rotblooms do not attack the "
           "Sandshrew and it does not run from them. It is hiding from the *party*. "
           "Corruption does not eat its own."),
    ("dm", "**The first time a Rotbloom goes down and stays down, read:**"),
    ("gold", "The grey goes first. It drains out of the cap the way muddy water wrings "
             "out of cloth, down and away into the soil, and the soil takes it and "
             "holds it, because that is what soil is for. And for one held breath the "
             "little creature is the colour it used to be: round and soft and gold, "
             "the loveliest thing on the landing, smiling because it wants to.\n"
             "Then it sighs, one long easy breath like a child finally put to bed, and "
             "folds down into the moss, and where it lay the grey does not come back."),
    ("gold", "It is over faster than it felt. The last of the mites pour back into "
             "their mounds like water finding its level, and the landing goes quiet, "
             "and then, patch by patch, the ground where the grey was cut away begins "
             "to light again: one faint thread of gold, then a slow scatter of them, "
             "rising past your faces the wrong way, exactly as before.\n"
             "The Sandshrew is back on its mound, at a careful distance, up on its "
             "hind legs. It is not pretending to be a rock anymore. It watched all of "
             "it, and it is watching you now the way you would watch somebody who "
             "just did a thing you did not know could be done.\n"
             "Ghostbloom says nothing at all, which from Ghostbloom is a great deal. "
             "She settles on Ursa's shoulder and stays there, ringing very softly, "
             "the same note the little flower sighed on.\n"
             "The road out of the hollow runs deeper and downward. The air coming up "
             "it is warmer than the air behind you, and somewhere a long way down, "
             "very faintly, something rings."),

    ("h2", "2. Chime Reef: The Beautiful Trap"),
    ("img", f"{S8}/loc_chime_reef.png",
     "A thousand years of patient growing, and none of it for visitors.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "The road out of the Landing runs uphill, and Underroot changes as you "
             "climb. The moss thins first, its glow guttering out until your own "
             "lamps are doing most of the work. Then the soil changes under it: "
             "drier, firmer, with a fine glitter worked all through it. Lilly stops "
             "and lifts a pinch to the light and finds tiny broken chips of crystal, "
             "blue and gold, more of them with every hundred feet, as though "
             "somewhere ahead something enormous were shedding.\n"
             "Then comes the sound, except it is not a sound yet. It is a pressure, "
             "low and sweet, somewhere underneath hearing, rising through the soles "
             "of your boots, and it grows with every step until you are leaning into "
             "it the way you lean into warmth."),
    ("gold", "The tunnel opens and you all stop at once, because the sound arrives "
             "before the sight does.\n"
             "Crystals. Thousands of them, growing up out of a shallow black pool in "
             "spires and fans and thickets, blue and gold and green, some of them "
             "taller than Vane's workshop. And the whole reef is ringing, very "
             "quietly, one slow shifting chord you feel in your back teeth. When the "
             "ground breathes, the note changes.\n"
             "Ghostbloom lifts off Ursa's shoulder and hangs in the middle of all "
             "that ringing with every petal spread. She is a spirit made of chime, "
             "and nothing has ever once answered her. She rings one small clear note "
             "out into the crystal, and the whole reef rings it back.\n"
             "Ursa, without deciding to, has taken his hand off his staff."),
    ("dm", "**Three beats before the boulders stand up.** **Loud carries:** anything "
           "loud makes the crystals ring louder, and a big enough noise brings a "
           "spire down, so reward the player who works that out and uses it. **Lilly "
           "can read the growth pattern** with an Arcana check: the crystals are "
           "growing *toward* something deeper in, the way plants grow toward light, "
           "and the whole reef is leaning on whatever that is. (It is Groudon.) "
           "**And there is a quiet gift here.** If anyone spends a turn simply "
           "listening, Elaria's presence is faintly in the chord; Ursa's player may "
           "notice it is the same seven-note shape as the Havenmoor bells."),
    ("gold", "The reef has been answering you the whole way in, and none of you "
             "noticed, because the answers were beautiful.\n"
             "Every footfall comes back off the crystal, tiny and bright. Lilly's "
             "pack clinks and a spire clinks back. Somebody laughs and the reef hums "
             "the shape of it half a second later. And the deeper you go, the more "
             "of the chord leans toward you, note after note bending in your "
             "direction, until the truth lands all at once: you are the loudest, "
             "warmest, fastest-moving thing this reef has ever held, and you have "
             "been ringing its doorbell with every single step.\n"
             "The chord drops. It goes low, and flat, and wide awake. The moss light "
             "dims in one slow pulse, and out in the pool the ripples stop."),
    ("gold", "Three boulders in the shallows unfold legs and stand up.\n"
             "They are squat and heavy and armoured in deep blue-black rock, with "
             "blunt jaws and small bright amber eyes, and jagged orange crystals "
             "grow out of their backs and shoulders like a struck chord frozen in "
             "place. Nothing about them is rotten or grey or wrong. They are simply "
             "enormous, and they are between you and the deep.\n"
             "Then the air is full of wings: pale crystal darts the size of hawks "
             "dropping out of the spires, banking once, and coming down at you fast "
             "enough to whistle."),
    ("dm", "**These are not corrupted.** The Chimestones are the reef's immune "
           "system, and the party is loud and warm and came in through a hole. That "
           "does not make them talkable: the reef has already decided. Play them as "
           "weather with legs."),
    ("img", f"{S8}/fight2_the_reef.png",
     "Every note in the cavern is now about you.",
     6.2, {"crop": "3:2", "hmax": 4.3}),

    # ENEMY_CARDS_FIGHT_2
    ("dm", "**This is a real fight and they are tough.** AC 16, they hit hard, and "
           "they resonate: every round the whole reef rings louder and everybody's "
           "ears hurt. The Shardwings are the reason nobody gets to stand still, "
           "diving in, spitting shards from sixty feet, and refusing to be pinned "
           "down."),
    ("dm", "**The clever play does not end the fight, it wins it.** Thunder damage "
           "makes a Chimestone ring itself apart: any thunder damage **stuns it "
           "until the end of its next turn**, and it takes **double damage** from "
           "every source while stunned. Lilly's Thunderwave and Shatter, Stabby's "
           "Nichirin against the crystal, and Ursa's Thunderwave all turn one of "
           "these from a wall into a free kill, and the Shardwings are **vulnerable "
           "to thunder** as well, so the same lever works on the whole encounter."),
    ("dm", "**The first time thunder damage lands on a Chimestone, read the "
           "following.** It is the turning point of the fight, and the whole table "
           "should hear it arrive."),
    ("gold", "The boom goes into the creature and does not come back out.\n"
             "For one heartbeat the Chimestone stands perfectly still. Then it "
             "begins to ring itself apart from the inside: the orange crystals "
             "along its back shiver into a blur, its own deep note climbing, "
             "cracking, splintering into wild harmonics, and the creature locks up "
             "mid-stride, stunned rigid by the one sound its armour cannot keep "
             "out, which is its own.\n"
             "And the reef takes up the note. Every spire, every fan, every thicket "
             "from the shallows to the dark edge of your light picks up the same "
             "stunned chord and sings it, the whole cavern ringing with the sound "
             "of the fight turning, and every one of you can hear that it has."),
    ("dm", "**The reef itself is a weapon too.** Anyone can spend an action to "
           "strike a big spire (**DC 13 Athletics**): the note rolls out and every "
           "Chimestone within **30 ft.** must make a **DC 14 Constitution save** or "
           "be stunned as above. Let them bring the roof down on the last one if "
           "they earn it. **The trade-off that keeps it honest:** the ringing hurts "
           "the party too, so anyone who uses the spire trick takes **1d6 thunder** "
           "themselves. Nobody minds."),
    ("dm", "**If a player strikes a spire and brings it down, read the following**, "
           "because they have just turned the terrain into a bell and they should "
           "feel it."),
    ("gold", "The spire goes over like a felled tree made of glass, and it does not "
             "crash. It **tolls**.\n"
             "One impossible note rolls out across the pool in a ring you can "
             "watch, bending the black water flat as it goes, and where it passes "
             "the Chimestones shudder and stagger and the slow heavy certainty "
             "goes out of them. It costs you a jolt of it yourselves, a boom "
             "straight through the breastbone, and not one of you would take it "
             "back."),
    ("dm", "**The fight can end without the last kill, and it is better if it "
           "does.** When the last Chimestone is stunned, or the win is no longer "
           "in doubt, put one beat of quiet on the table before anybody rolls "
           "again. If the party lowers their weapons and backs out of the "
           "shallows, the reef stands down: no check, no cost, it simply works, "
           "because an immune system does not chase what is already leaving. Do "
           "not offer this. Let a player think of it, exactly as with Thumpaw, and "
           "pay the idea in full when they do. In the Landing the kindness was the "
           "cut that set something free; here nothing is sick and nothing is "
           "bound, so the kindness is the strike withheld. If they finish the last "
           "one anyway, the fight was honest and nobody gets scolded; the chord is "
           "simply one note smaller on the way out, and Ghostbloom hears it."),
    ("gold", "You step back, and the reef notices that too.\n"
             "The last Chimestone stands in the shallows with its amber eyes on "
             "you, ringing softly, and does not follow. Then, joint by heavy "
             "joint, it folds its legs back under itself and settles into the "
             "water, and it is a boulder again, and you would swear it had never "
             "been anything else. Around you the ringing comes down slowly, wild "
             "harmonics settling back into the old patient chord, the moss light "
             "steadying, the pool remembering how to ripple.\n"
             "The reef has decided you are weather. Loud weather, strange weather, "
             "but the kind that passes, and it has stood through worse."),
    ("gold", "You take your rest inside a chord.\n"
             "There has never been a stranger campsite and there may never be a "
             "better one. You eat sitting on warm stone with music coming up "
             "through it, the reef's slow ringing folded around you like a roof, "
             "and the notes change when the ground breathes, so the whole meal "
             "happens inside something enormous and calm that is almost a song. "
             "Ghostbloom hums along, quietly, the entire time, and nobody asks her "
             "to stop.\n"
             "Years from now, when all of this is a story you tell, this is the "
             "note you will remember."),
    ("dm", "**SHORT REST, right here.** Take it the moment the last Chimestone "
           "goes quiet, and say so at the table: Hit Dice spent, Stabby's Focus "
           "back, Ursa's Wild Shape back, Lilly's Aether Ward back. The Glassed "
           "Gallery is built assuming they walk in full, and it is not kind if "
           "they do not."),

    ("h2", "3. The Glassed Gallery: The Wound"),
    ("img", f"{S8}/loc_glassed_gallery.png",
     "Black glass from wall to wall, and the shine of it is the worst part.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "You know something is wrong a hundred feet before you reach it, "
             "because the ground stops breathing.\n"
             "Ahead of you the roots are **black glass**. Not burned: glassed, "
             "smooth and shining and hard, frozen mid-growth in the middle of "
             "reaching for something. The whole gallery is silent in a way "
             "nothing else down here has been. There is no moss light. Your own "
             "lamps look small.\n"
             "And every surface, when you get close, is covered in fine cracks "
             "that are very slowly, very quietly, spreading."),
    ("dm", "**Let them feel the size of it.** This is not a monster's lair; it is "
           "a burn scar going outward at the speed of grass growing, and it has "
           "been going for two years. Nothing here needs a check to understand. "
           "The cracks all radiate from one direction, deeper in, toward the "
           "Hollow, and any hero who looks at them for ten seconds can say so "
           "out loud."),
    ("gold", "Stabby's idol has stopped being merely cold. It aches in the palm "
             "now, cold the way a nail left out in winter is cold, and after a "
             "minute of carrying it he has to wrap it in a fold of cloth and put "
             "it away. It has never once behaved like this."),
    ("dm", "**Explain nothing.** No check identifies it, no NPC has a theory, and "
           "nobody down here reacts to it. It got colder near the ring, it is "
           "colder here, and that is the entire beat. Let his player sit with "
           "it."),
    ("gold", "The Sphere is brighter here than it has been anywhere in Underroot, "
             "bright enough that Lilly is holding it a little away from her "
             "body, and it is drinking hardest exactly where the glass is "
             "thickest. Whatever is bleeding out of this wound, her Sphere was "
             "built to gather it."),
    ("dm", "**Give Lilly that deduction free**, no roll. It is the first hard "
           "evidence for the theory she spent her year building: the Sphere "
           "grows by going out, and a wound this size is a feast."),
    ("gold", "And then, from deeper in, past where the moss light died, you hear "
             "it: a sound of glass on glass, soft and patient and perfectly "
             "regular, like somebody sweeping a floor that will never come "
             "clean.\n"
             "It has been going a long time. It does not stop when you come "
             "closer."),
    ("dm", "**Let them approach that sound as slowly as they like.** It is the "
           "Weeper, still at its work, and it pays them no attention at all "
           "until light finds it. There is no ambush waiting in this gallery, "
           "only a job that never ends, so heroes who scout get the full reveal "
           "below before anything moves."),

    ("h2", "Fight 3: The Glass Weeper"),
    ("img", f"{S8}/mon_glass_weeper.png",
     "The Gallery's keeper, as the corruption remembers it.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "Something is still standing in the gallery.\n"
             "It has the shape of one of the big slow root-tenders: a long neck, "
             "a crown of fronds for combing the roots clean. It is far too tall "
             "to be one. It is black glass grown into the memory of a tender, a "
             "mimicry the corruption built up around something at its centre you "
             "cannot see, and the glass moves the way a hand moves a puppet. And "
             "the puppet is **still trying to do the job**, sweeping shattered "
             "glass fronds through glassed roots that cannot feel it, over and "
             "over, patiently, forever.\n"
             "Around its feet, rolling in fast, are lumps of black glassy coal "
             "the size of ripe pumpkins, each with one furious orange eye."),
    ("gold", "It does not notice you until your light touches it. Then the "
             "sweeping stops.\n"
             "The long neck comes around. The crown of broken fronds opens like "
             "a black glass fan, and from somewhere deep inside the mimicry a "
             "thin note begins to rise, and every crack in the gallery sings "
             "along with it. The tenders of Underroot were made to clean their "
             "roots of anything that does not belong, and the puppet wearing "
             "this one's shape has just decided that what does not belong is "
             "you."),
    ("img", f"{S8}/fight3_the_gallery.png",
     "Rolling coal, keening glass, and the hardest fight on the road down.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("dm", "**The Cinderolls arrive two at a time**, so the pressure never stops "
           "and never quite swamps the party. Do not open with all four. The "
           "Weeper does not chase and never leaves its roots; it does not have "
           "to, because it reaches fifteen feet and hits three times a turn."),

    # ENEMY_CARDS_FIGHT_3
    ("dm", "This one is meant to be hard, and it has a lever. The Weeper regains "
           "**10 hit points at the start of its turn** unless it took radiant or "
           "force damage, or was hit by **Cleansing Edge**, since its last turn, "
           "so with ordinary steel every wound they open is part closed again "
           "before their next turn and the fight reads as if it is going "
           "backwards. **Stabby is the answer, and everyone at the table should "
           "be able to see it.** The second lever is kindness: any hero can "
           "spend an action tending the glassed roots the Weeper is bound to "
           "(**DC 14 Nature or Medicine**, or any healing spell cast on the "
           "roots instead of a creature). On a success the Weeper **loses its "
           "regeneration until the end of its next turn** and every attack "
           "against it has **advantage** until the start of the helper's next "
           "turn. Two or three of those and the fight tips hard. It never ends "
           "the encounter; it makes the party feel brilliant while they finish "
           "it. Meanwhile the Cinderolls roll twenty feet and detonate: let the "
           "players work out that popping one next to three others is a chain "
           "reaction, and let them enjoy it. Watch the Weeper's **Keening** (its "
           "wail: a 30-ft cone, DC 15 Constitution, 21 psychic and frightened) "
           "landing on the same turn the roll-in pair arrives, and pull the "
           "fourth Cinderoll if the table is on the ropes."),
    ("dm", "**The first time a hero tends the glassed roots, read the "
           "following.** This is the session's thesis at its saddest, and it "
           "must not be missed at the table: the lever is mechanical, but what "
           "it shows them is not. Wait for the room to go quiet before you "
           "start."),
    ("gold", "Warmth. That is the first surprise: the glassed root under your "
             "hands is not cold at all, and where you tend it the black glass "
             "clouds over, greys, and lets go. For the width of one finger "
             "there is green underneath. Living green, soft and damp and "
             "stubborn, the first colour this gallery has held in two years.\n"
             "And across the gallery, the Weeper stops.\n"
             "Its frond hangs in the air, mid-sweep. Slowly, by inches, the "
             "whole tall broken shape of it leans toward what you are doing, "
             "the way a tired thing leans toward a fire. For one long breath it "
             "only watches the green, because somewhere inside the puppet, "
             "underneath the glass and the wrongness, something remembers this "
             "exact work, and remembers that it was worth doing."),
    ("dm", "**And when somebody pops a Cinderoll next to its friends, read this "
           "one with a grin.** The fight has earned exactly one laugh, and this "
           "is where it lives."),
    ("gold", "One furious orange eye goes very wide, and then the whole cluster "
             "goes up together, pop, pop, POP, a string of festival crackers in "
             "the dark, and for one glorious second the Glassed Gallery is lit "
             "up gold, as if it remembers what light is."),
    ("gold", "When it finally falls it does not crumple. It **shatters**, all at "
             "once, a whole creature's worth of black glass coming apart across "
             "the floor with a noise like a window breaking in another room. "
             "And in the middle of the wreckage, curled up small where its "
             "heart should have been, is an ordinary little animal. Grey fur. "
             "Four paws. It has been dead for two years, and something built a "
             "statue around it and kept it working."),
    ("dm", "**This is where the session stops being an adventure and becomes a "
           "rescue**, and it is the last beat before Groudon. Do not narrate it "
           "gruesomely and do not linger: one quiet image, then silence at the "
           "table, then let a player be the one to speak first."),
    ("gold", "Afterward, Stabby walks out into the gallery alone. He lights his "
             "breath, and sets the burning edge against the black glass."),
    ("dm", "**Stop there and hand the narration to Stabby's player.** This image "
           "is the whole point of his year, so let him be the one who says what "
           "the glass does. No check, no cost, no roll. If he stalls, offer him "
           "the picture and let him carry it from there: where the Nichirin "
           "passes, the black glass **flinches**, it greys, it dulls, it "
           "crumbles back into ordinary soil, exactly the way the blight "
           "recoiled from him on the mountain at home. The path stays clean "
           "behind them."),
    ("gold", "He cannot heal this place. It is a mile wide and he is very "
             "small. What he can do is burn a clean path straight through the "
             "middle of it, and that is the road you walk out on."),
    ("gold", "You are not fifty steps along that road when Ursa stops walking, "
             "and then all of you hear it. Behind you, faint as a sleeper "
             "turning over, at the very edge of feeling, the ground along the "
             "clean path has begun to breathe again: one narrow road's width of "
             "Underroot, remembering how. Nobody says anything for a while, and "
             "it is a good kind of quiet."),

    ("bridge", "Past the wound the tunnel narrows, then steepens, then simply ends, and everything "
               "they have felt underfoot all day turns out to have had a source."),

    ("h2", "4. Groudon's Hollow: The Guardian"),
    ("img", f"{S8}/loc_groudons_hollow.png",
     "The bottom of the world, where every road in Underroot has been leading.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "The tunnel ends at a ledge, and past the ledge there is no floor. Your light goes "
             "out into the dark and does not come back with a far side.\n"
             "Something down there is breathing.\n"
             "You have felt it all day, the slow rise and fall of the ground under your boots, "
             "once a minute, everywhere you went. You thought that was the plane. Standing on "
             "this ledge, you finally understand what you have been walking on top of since the "
             "gate.\n"
             "It was never the plane breathing.\n"
             "It was **him**."),
    ("img", f"{S8}/mon_groudon_corrupted.png",
     "The Continent-Maker. The glowing seams are his own. The black glass is not.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "He fills the hollow the way a mountain fills a valley. Red-brown plates the size of "
             "barn doors. Claws sunk deep into stone he has not moved from in a very long time. "
             "Seams of magma glow along his flanks like banked coals.\n"
             "And driven into his back, up near the shoulder where no claw of his can reach, is a "
             "**spike of black glass**. Every crack in this world runs outward from that one "
             "point.\n"
             "He is the reason there is dry land anywhere. He has been in pain for two years. "
             "And in all that time, he has not been able to tell a single living soul."),

    ("h2", "The Fight, and What It Is Actually About"),
    ("img", f"{S8}/boss_groudon_spike.png",
     "Everything in this room is enormous except the thing that matters.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("dm", "**Groudon is not the villain. The spike is.** This is the Grand Custodian rule from "
           "Gearhaven at ten times the scale: *free the guardian and the cracks close.* Say the "
           "rule out loud at the table if the players do not reach for it themselves, because the "
           "whole encounter is built on it. Nobody is killing a god tonight."),
    ("dm", "**Do not let the party win by damage.** Groudon has **AC 18 and 230 hit points** and "
           "hits hard enough to drop a level-7 hero in two turns. A straight brawl is a loss, and "
           "it is supposed to be. **The win condition is the spike**: a hard target on his back "
           "with **AC 17 and 60 hit points**, **immune to everything except radiant, force, and "
           "Cleansing Edge**. Reaching it means climbing him (Athletics or Acrobatics), flying "
           "(Stabby's Sash, Ursa's Starry Form), or a called shot at range with disadvantage. "
           "**When the spike breaks, the encounter ends instantly.** Not \"he has forty hit points "
           "left.\" It ends, whatever his total is. Do not run him to 0. He is not supposed to "
           "die, and nothing in this room is an execution."),
    ("dm", "**When someone first lays a hand on Groudon to climb**, read the following."),
    ("gold", "Your hand finds the edge of a plate the size of a barn door, and the first surprise "
             "is the heat. Not burning. Deep, like a hearth stone hours after the fire has died, "
             "warmth that comes from a very long way inside.\n"
             "The second surprise is the heartbeat. It rolls up through your palms, slow and "
             "enormous, and you feel it in your teeth and in the soles of your boots.\n"
             "You are climbing something alive. He is older than the land you were born on. He "
             "is in more pain than anything you have ever touched. And he does not know, he "
             "cannot know, that the small warm thing clinging to his shoulder is trying to help.\n"
             "Hold on. Keep climbing."),
    ("dm", "**The moment Ursa reaches out with the Mark**, the way Selarin taught him, read the "
           "following. He goes in expecting rage."),
    ("gold", "There is no rage in there at all.\n"
             "There is pain. It is old, and it is patient, and it goes on farther than the Mark "
             "can reach. And underneath it, very faint, is something that has been trying to say "
             "one word for two years, with no mouth to say it with.\n"
             "*Help.*"),
    ("dm", "**Only Ursa can feel this, and telling the others is the moment the fight becomes a "
           "rescue.** Give his player the line and let him deliver it in his own words. If nobody "
           "reaches for the Mark, let the Agony shockwave do the job instead: he screams when it "
           "hits him, and it hits him every single turn."),

    ("h2", "The Glasslings"),
    ("dm", "**The spike creates one Glassling at the start of each of Groudon's turns**: a "
           "cat-sized scuttling thing of black glass that drops off his back and goes straight for "
           "the nearest warm body. They are weak, they burst when killed (**DC 12 Dexterity, 5 "
           "slashing, 5 ft**), and they never stop coming. They exist to answer the obvious "
           "question, which is why not ignore the spike and whittle Groudon from range: because the "
           "longer the spike lives, the more little glass things are chewing on the party."),
    ("dm", "**When the spike breaks, every Glassling on the board collapses into ordinary sand at "
           "once**, wherever it is and whatever it was doing. Clear them off the map in one sweep "
           "of your hand and say nothing while you do it."),

    ("h2", "Groudon's Turns"),
    ("dm", "**Play him as a natural disaster with a wounded animal inside it**, never as a "
           "tactician. He does not aim, he does not focus fire, he does not plan. Alternate: "
           "**Continental Step** (he moves, the floor changes, DC 16 Dexterity within 30 ft of his "
           "path or knocked prone for 11 bludgeoning), **Magma Vent** (recharge 4-6, a 60-ft line "
           "10 ft wide, DC 17 Dexterity, 35 fire, half on a success), **Claw** (+12 to hit, reach "
           "15 ft, 24 slashing) if anything is in reach, and **Thrash** whenever the spike takes "
           "damage (once a round, no action: every creature climbing him makes a DC 15 Strength or "
           "Acrobatics check or falls for 3d6). Remember **Agony**: while the spike is intact, at "
           "the start of each of his turns he takes 10 damage himself and everything within 20 ft "
           "makes a DC 16 Dexterity save or takes 10 bludgeoning from the shockwave. He is being "
           "hurt in front of them, every round, and they can see it."),
    ("dm", "**Mercy rule, and it is not optional.** If a hero drops, Groudon immediately moves away "
           "from them. He does not finish anyone, ever. He does not know they are there in any "
           "meaningful way; he is swatting at pain, not hunting children. Tell the table that out "
           "loud the first time it happens."),

    # ENEMY_CARDS_BOSS
    ("dm", "The shape of this encounter is simple to say and hard to do: survive a very large "
           "angry mountain long enough for somebody to climb his back and cut the thing that "
           "is hurting him out of it. Every hero has a job. **Stabby is the one who ends "
           "this, and the entire session has been building to it**: speed 65 with his breath "
           "lit, Step of the Wind to close, and a Nichirin that is one of only three things "
           "in this world that can touch the spike at all. He climbs a mountain that is "
           "trying to shake him off and he cuts the corruption out of a god. **Do not let "
           "anybody else take that blow unless his player hands it over**; if the dice go "
           "badly, let Ursa's summon pin Groudon in place or Lilly's Flash of Genius rescue "
           "the climb check, so the last strike is still his. **Ursa** keeps everyone "
           "standing, drops a summon between Groudon and whoever is climbing, and is the only "
           "one who can feel that the creature is in pain. **Lilly** shoots the spike from "
           "range and holds the party together with Aether Ward; force damage from Puff's "
           "Wand of Magic Missiles hits the spike and never misses. When the sixty hit points "
           "are gone, stop rolling. Put the dice down, let the Glasslings fall to sand, and "
           "play what follows as a rescue landing rather than a victory lap: the party did "
           "not kill anything in this room, they took a splinter out of a mountain's "
           "shoulder, and the mountain is going to look at them."),
    ("dm", "**When the last hit is about to land on the spike**, pause the table before the roll, "
           "and read:"),
    ("gold", "The crack in the black glass widens. One bright hairline runs through the dark of "
             "it.\n"
             "The sick light inside the spike stutters. And for one breath, one single breath, "
             "the whole hollow goes quiet: the magma seams dim to embers, the Glasslings stop "
             "where they stand, and the mountain beneath you holds himself still, as if something "
             "in him, deeper down than two years of pain, knows what is coming and is waiting for "
             "it.\n"
             "One more hit. That is all it needs.\n"
             "Swing."),

    ("h1", "The Way Home"),

    ("h2", "When the Spike Breaks"),
    ("img", f"{S8}/the_spike_breaks.png",
     "The first thing he has felt in two years that is not pain.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "The black glass does not shatter.\n"
             "It comes apart all at once and quietly, like a held breath let go, into a spray of "
             "dark motes that hang in the air for a single heartbeat and then rush, every one of "
             "them together, into the Sphere in Lilly's hands.\n"
             "And the mountain stops.\n"
             "**Groudon goes absolutely still.** Then he lowers himself onto his belly on the "
             "stone with a sound like a hillside settling, and he breathes out, and the breath "
             "goes on so long that somebody laughs once out of pure nerves, and every root in the "
             "hollow shivers along its whole enormous length.\n"
             "Then he turns his head, slowly, and looks at the three of you properly for the "
             "first time.\n"
             "He is not angry. He is so tired."),
    ("dm", "Everything after the spike is the part they will remember. Slow down. This is not the "
           "end of a fight; it is the end of two years of somebody's pain, and the whole session "
           "has been walking toward it."),
    ("dm", "**The encounter ends the instant the spike drops, whatever his hit points are.** Do "
           "not roll another attack, do not finish the round, do not let anybody get one more hit "
           "in. And **every Glassling on the board collapses into ordinary sand where it "
           "stands**, mid-lunge, mid-bite, all of them at once. Clear the miniatures off the "
           "table with your hands while the players are still watching. That clatter is the "
           "applause line of the whole session."),
    ("gold", "As the last of the glass leaves him, something else comes loose from the wound in "
             "his shoulder. It is a fist-sized ember of packed red-brown light, dense as a river "
             "stone and warm as fresh bread, and it does not fall. It drifts across the hollow, "
             "unhurried, and settles against the Sphere like an animal finding the right place "
             "to sleep.\n"
             "This is the **Mote of Terra**: the piece of this world's heart that was caught "
             "here, come home to the only thing in the room built to carry it."),
    ("gold", "Groudon gathers himself, and the floor of the world moves with him. He reaches out "
             "one claw, a claw that has moved continents, and sets the very tip of it on the "
             "ground in front of **Ursa**, with a care that would not crack an egg.\n"
             "Nobody needs a Mark to understand that.\n"
             "Then he begins to walk. Where he walks, the cracks close behind him like a seam "
             "pulled shut, and far off in the dark you can hear the glassed gallery crumbling "
             "back into plain, ordinary, breathing soil."),
    ("dm", "**Give Ursa the line if his player wants it.** He is the only one who can feel what "
           "the creature is feeling, and what it is feeling is *relief*. Let him say it out loud "
           "to the other two. That sentence is what turns the boss fight into a rescue in "
           "everybody's memory, and it should come out of a player's mouth, not yours."),

    ("h2", "Antares"),
    ("img", f"{S8}/antares_relights.png",
     "The eastern sky over Gearhaven, carrying news only one person in the city can read.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "You come out of the ring into lamplight and noise, with Vane shouting three "
             "questions at once, and it is a long few minutes before anybody thinks to look up.\n"
             "**Ursa does.**\n"
             "Through the clerestory windows of the Rift Hall, over the wet slate roofs of "
             "Gearhaven, there is a star in the east that was dying.\n"
             "It is not dying now. It is the deep, steady red it is supposed to be, the red it is "
             "in every one of his father's charts. His father spent a year drawing that star "
             "getting fainter, month after month, and then he put the pen down and walked east to "
             "do something about it. In all the watching since, nobody has ever seen a star come "
             "back.\n"
             "This one has."),
    ("dm", "**Only Ursa understands what he is looking at, and that is the point.** He watched "
           "Antares dim on the night they left and said nothing to anybody; he has spent a year "
           "with those charts. Let his player be the one to explain it to the others, in his own "
           "words, at his own speed. Then let **Aelwyn** go very quiet, because a man who has "
           "been arguing a theory for thirty years has just watched it become a fact."),
    ("dm", "**The Staff of Waking Constellations answers.** One new star kindles on the haft and "
           "stays lit. That is what the staff was made for, and this is the first time anyone has "
           "seen it work."),

    ("h2", "The Sphere Will Not Settle"),
    ("img", f"{S8}/homecoming_sandshrew.png",
     "The brightest thing Vane's workshop has ever held, about to introduce itself.",
     6.2, {"crop": "3:2", "hmax": 4.3}),
    ("gold", "The Sphere has been getting brighter since Underroot, and now it is too bright to "
             "look at straight. It is warm as a stove top. It hums against Lilly's palms hard "
             "enough to make her teeth ache.\n"
             "Aelwyn takes one look at it and tells everybody to stand back, and for once he is "
             "not delighted. He is **nervous**, which is worse.\n"
             "\"It gathered more than it can hold,\" he says. \"It only keeps one shape at a "
             "time.\"\n"
             "\"So what happens?\" says Lilly.\n"
             "\"It is going to have to choose.\""),
    ("gold", "**Ghostbloom chooses first.**\n"
             "Nobody asks her to. Nobody gets the chance. She drifts around in front of Lilly so "
             "the two of them are eye to eye, and she chimes once, the small clear note she has "
             "been making since a foggy path above the sea two years ago.\n"
             "Then she steps into the light and is gone.\n"
             "The Sphere goes calm in Lilly's hands, and the room is very quiet."),
    ("dm", "**Play this straight and let it hurt for three or four seconds.** The kids will think "
           "they have just lost her. They have not: she is the tether, she is perfectly fine, she "
           "is aware in there and she can come back out tonight. Aelwyn explains all of that in a "
           "moment. Do not rush to reassure them before the moment lands, and do not stretch it "
           "past four seconds either. Count it in your head."),
    ("gold", "And then the light in Lilly's hands stands up.\n"
             "The gathered essence of a whole plane pulls itself into a shape, and what steps out "
             "of the glow, blinking in the lamplight and thoroughly unimpressed with all of you, "
             "is the small armoured digger from Mosslight Landing. Yellow-brown plates. Enormous "
             "claws. Very much solid, very much real. He shakes himself the way a dog does, and a "
             "little Underroot soil scatters across Vane's clean workshop floor."),
    ("dm", "**Where he goes matters.** If the party was kind to him at Mosslight Landing, or fed "
           "him, he walks straight to whoever did it. If they were unkind, he crosses the room to "
           "**Ursa** and settles against his boot, and on the way he goes right past the hero who "
           "chased him off without once looking up. **Then say nothing.** Do not explain it, do "
           "not soften it, do not offer that player a consolation line, and do not let Aelwyn "
           "talk over the silence. The table will work out what just happened on its own, and it "
           "should."),
    ("gold", "\"The Sphere gathers,\" Aelwyn says, crouching down to be polite about it. \"That "
             "is all it has ever done. Today it gathered an entire world's worth of loose "
             "essence, and essence gathers toward warmth, and toward company. So it brought "
             "somebody home.\""),
    ("dm", "**Teach the companion-swap rule right here, before anybody goes home.** The full "
           "script, in the words to say it, is in the run sheet appendix under **The Companion "
           "Swap**. Teach it, then hand Sandshrew over and let them run the first swap "
           "themselves, right there in the workshop, so Ghostbloom steps back out where they can "
           "all see her."),

    ("reward_card", "Rewards: What Underroot Gave Them",
     "The concrete gains, once the shouting in the Rift Hall dies down", [
        ("Sandshrew",
         "A companion, freely given, gathered out of the essence of a whole plane. He digs, he "
         "takes a hit, and he is made of the same stuff as the ground he stands on. **Second on "
         "the roster, and the first proof that the roster is real.**"),
        ("Ghostbloom, the Tether",
         "Unharmed and unchanged, riding inside the Sphere as its anchor and stepping back out "
         "on request. The Sphere holds **one** physical companion at a time; the swap is Lilly's "
         "Action."),
        ("The Mote of Terra",
         "The piece of Underroot's heart that was caught in this world, socketed into the "
         "Sphere. **The rift is closed.** Not patched, not held: closed, by a guardian walking "
         "home."),
        ("Tectonic Slam",
         "Lilly's **first Elemental Discharge**, woken by the Mote of Terra. Four sockets in the "
         "Sphere stay dark, and she can feel every one of them."),
        ("A New Star on the Staff",
         "**Antares is lit.** One new star kindles on the haft of the Staff of Waking "
         "Constellations and stays lit, which is precisely what the staff was made to do."),
    ]),

    ("h2", "What Each of Them Carries Home"),
    ("img", f"{A}/characters/sandshrew.png",
     "Sandshrew, with somebody else's dirt still on his claws.",
     6.2, {"crop": "4:3", "hmax": 4.4}),
    ("body", "**Lilly** gets the thing she spent a year arguing for: proof. Her power grows by "
             "going out, exactly as she worked it out alone at a bench in Gearhaven, and now "
             "there is a Mote in a socket and a discharge in her hands that nobody built for "
             "her."),
    ("gold", "Late that night Lilly has the Sphere open on the workbench, the Mote sitting in its "
             "new socket, and she is not looking at anybody.\n"
             "\"It isn't full. That's the thing. There's a whole *plane* in there and it barely "
             "moved the needle.\" She turns it over in her hands. \"I can feel where the other "
             "four go. The sockets are there, and they're empty, and when I put my hand flat on "
             "it I can almost hear what it would sound like with all five.\"\n"
             "\"I don't think it's a battery. I think it's an instrument. And I've only ever "
             "played one note on it.\""),
    ("dm", "**What that plants:** her ceiling is very high and entirely gated on rifts cleared. "
           "She has gone from one discharge to a promise of five in a single night, and she is "
           "the only person at this table who can feel the shape of the thing she is going to "
           "become. Let her player sit with that."),
    ("body", "**Ursa** carries home a relit star and the first hard evidence anybody has ever had "
             "that the damage can be *undone*. He also carries the beginning of a private worry, "
             "and he does not share it: the spike did not grow in Groudon's back. Somebody drove "
             "it in, on purpose, by hand. And he brought a name back from a shrine on a "
             "mountain."),
    ("body", "**Stabby** carries a katana that did something no other blade in the world could "
             "do, and one small fact he has told nobody. The idol went cold when they stepped "
             "through the ring, colder in the glassed gallery, and it warmed the instant they "
             "came back. He noticed exactly when. He has not mentioned it."),

    ("h2", "Threads to Leave Hanging"),
    ("dm", "**One: who drove the spike in?** Nobody says a name at the table tonight, and neither "
           "do you. But the party has now seen with their own eyes that the rifts are not "
           "weather. Somebody is doing this, by hand, one world at a time.\n"
           "**Two: the idol.** Cold at the threshold, colder at the gallery, warm at home. Where "
           "that thread finally goes is still yours to decide; until you decide it, explain "
           "nothing and promise nothing.\n"
           "**Three: four stars to go**, and two of them are still bright. Aelwyn will work out "
           "what that means before the next session is over: if the lights are being put out one "
           "by one, then somewhere out there is a star nobody has reached yet, and the party can "
           "get there **first**."),

    ("gold", "It is very late. Vane has finally stopped talking. Sandshrew has fallen asleep in a "
             "crate of brass fittings, and nobody has the heart to move him.\n"
             "Aelwyn stands at the high window with his hands behind his back, looking east, at a "
             "star that spent two years dying and is not dying anymore.\n"
             "He says it to nobody at all.\n"
             "**\"One.\"**"),

    ("lore", "The Second List",
     "The Circle has kept its list of stars for forty generations, and in all that time "
     "the scribes have only ever done one thing to it: cross names out. There is no mark "
     "in their book for a name coming back, because nobody ever needed one. The eldest "
     "sky-reader alive was asked, once, what the Circle would do if a dark star ever "
     "relit. She thought about it for a long while. Then she said: begin a second list."),

    # ================================================================
    # APPENDICES
    # ================================================================
# ------------------------------------------------------------------
    # APPENDIX I: the DM run sheet (Session 6/7 format).
    ("appendix_title", "APPENDIX", "The DM's Run Sheet",
     "Every DC, dial, and spotlight, in play order. Keep this page at your elbow."),

    ("h1", "The Shape of the Session"),
    ("body", "▶ **PART ONE is read, not rolled.** Seven days early: Lilly alone in the Rift Hall, "
             "Vane too loud and sleeping too little, and the cradle that does not quite fit until "
             "the sixth night, when it does → THE PROFESSOR: Aelwyn Ravenstone, three trunks, no "
             "help, and Lickgloom recognising the party (the only uncomplicated happy reunion all "
             "night) → DAWN AT THE EASTERN GATE: Ursa on foot, taller and quieter, turning a stone "
             "over in his left hand → TEN TO MIDNIGHT: Stabby off the rail without a sound, and "
             "**the idol knocks against the flagstones cold enough to burn** → THE THREE CHAPTERS, "
             "read in full, in this order: Lilly (the most hopeful), Stabby (the loudest), Ursa "
             "(NYXTHID, and it changes the campaign, so it goes last) → THE HANDOVER: hand out the "
             "level 7 sheets here, teach the traps in a quiet room → THE BRIEFING: five facts, and "
             "say the one about losing the Sphere exactly once → THE LESSON: slow, no sky, "
             "indifferent, and free the guardian → THE THRESHOLD."),
    ("body", "**PART TWO is played on the Underroot board.** The party moves as ONE token: a player "
             "rolls **1d6**, moves that many spaces, and the token passes to the next kid on the "
             "next roll. The colour they land on resolves at once, and **the die they just moved "
             "with picks the outcome: even or odd.** No table to look up, no second roll. The four "
             "numbered locations are not dots: the token stops at each one whatever movement is "
             "left, the beat plays, and movement resumes next turn. THE RIFT GATE (arrival, no "
             "fight, one safe scene to be amazed) → MOSSLIGHT LANDING and the Sandshrew (**FIGHT "
             "1**) → CHIME REEF (**FIGHT 2**) → **SHORT REST, immediately after the reef, called "
             "out loud** → THE GLASSED GALLERY (**FIGHT 3**), and the small creature curled inside "
             "the glass that turns the adventure into a rescue → GROUDON'S HOLLOW (**BOSS**): the "
             "spike breaks, the Mote of Terra comes home → back through the ring, and Ursa looks "
             "up at Antares → THE HOMECOMING: Ghostbloom steps into the Sphere, Sandshrew steps "
             "out, the swap rule gets taught, and Aelwyn says one word to nobody."),
    ("body", "**The natural break point is the Threshold.** Part One ends the moment the air inside "
             "the ring stops being air; if the evening has to stop somewhere, stop it there and "
             "start the next one on the far side. Inside Part Two the second-best pause is the "
             "short rest after the reef. **Pace check:** there are 22 dots between the gate and the "
             "Hollow, and they are texture, not the session. If the night is running long, "
             "hand-wave the dots between the Gallery and the Hollow and go straight to Groudon. "
             "Never let a garnet dot swell into a fifth big fight."),
    ("body", "**RUNS ALL SESSION.** **The Sphere is pulling**, warm in Lilly's hands from the first "
             "breath of Underroot, and it does not stop; it drinks fastest where the damage is "
             "worst. **Ursa cannot navigate**: no sky, no stars, and his year of star-reading buys "
             "him nothing, so give him advantage on Survival for reading root growth and soil, "
             "exactly as Selarin told him. **The idol gets colder the deeper they go**, and you "
             "never explain it. **Ghostbloom is delighted**, a plant-spirit inside a plane made of "
             "growing things, right up until the Hollow. And **nothing here can be talked down, "
             "waited out, or avoided**: the levers below turn grinding fights into satisfying ones, "
             "they are never an off-ramp."),

    ("h1", "Fights at a Glance"),
    ("body", "**FIGHT 1: Mosslight Landing** (warm-up, but it runs long; it teaches the session's "
             "rule). 6x Rotbloom (AC 12, HP 22; **Re-Bloom**: it regains 5 HP at the start of its "
             "turn if it took damage and is not at 0; Cap Slam +3 for 2d4+1; Spore Puff, recharge "
             "5-6, a 10-ft cone, DC 12 Constitution or 2d6 poison and poisoned) + 6x Mossmite (AC "
             "13, HP 7, Speed 40 ft and climb 40 ft; Skitter, no opportunity attacks; Pack Nerve; "
             "Nip +5 for 1d4+3), boiling out of the moss the moment the first Rotbloom is struck. "
             "**THE LEVER: Cleansing Edge.** A Rotbloom cannot re-bloom if it has taken radiant "
             "damage or been hit by Cleansing Edge since its last turn, and Stabby is the only "
             "reliable source at this table. Let the party flail for one round, let Lilly and Ursa "
             "watch their damage undo itself, then let him cut one and have it **stay** cut. "
             "**The tell:** the Rotblooms do not attack the Sandshrew and it does not run from "
             "them. Corruption does not eat its own."),
    ("body", "**FIGHT 2: Chime Reef** (hard on paper, easy the moment somebody thinks of thunder). "
             "3x Chimestone (AC 16, HP 52, **VULNERABLE THUNDER**, tremorsense 60 ft; Multiattack "
             "two Crystal Rams at +6 for 2d6+4; Shard Volley +6 for 2d8 at 40 ft) + 3x Shardwing "
             "(AC 14, HP 22, fly 50 ft, **VULNERABLE THUNDER**; Dive +6 for 2d6+2, plus 1d6 more "
             "if it came 30 ft straight in; Shard Spit +6 for 1d10+2 at 60 ft). **THE LEVER: "
             "Resonant Body.** Any thunder damage **stuns a Chimestone until the end of its next "
             "turn, and it takes DOUBLE damage from every source while stunned.** Thunderwave and "
             "Shatter turn a wall into a free kill. Better still, anyone can spend an action "
             "striking a big spire (**DC 13 Athletics**): every Chimestone within 30 ft makes a **DC "
             "14 Constitution save** or is stunned the same way, and the striker takes 1d6 thunder "
             "for standing that close. Nobody minds. Lilly's Arcana read: the crystals are growing "
             "toward something deeper in. It is Groudon."),
    ("body", "**FIGHT 3: The Glassed Gallery** (the hardest thing before the boss, and Stabby's "
             "proving ground). 1x Glass Weeper (AC 16, HP 115; **Glassbound**: regains 10 HP at the "
             "start of its turn unless it took radiant or force damage, or was hit by Cleansing "
             "Edge, since its last turn; Rooted, it never leaves its glassed roots by more than 15 "
             "ft; Multiattack three Frond Lashes at +7 for 2d6+5 with 15 ft of reach; Keening, "
             "recharge 5-6, a 30-ft cone, DC 15 Constitution for 6d6 psychic and frightened) + 4x "
             "Cinderoll (AC 15, HP 18, Speed 40 ft rolling, **arriving two at a time**; Rolling "
             "Charge adds 1d6 and a DC 12 Strength save or prone; **Burst** at 0 HP, DC 12 "
             "Dexterity within 10 ft or 2d6 fire; Slam +4 for 2d4+2 plus 1d6 fire). **THE LEVER: "
             "Tend the Roots.** An action clearing or healing the glassed roots (**DC 14 Nature or "
             "Medicine**, or any healing spell aimed at the roots rather than a creature) strips "
             "Glassbound until the end of the Weeper's next turn and gives everyone **advantage** "
             "on attacks against it until the start of the helper's next turn. Two or three of "
             "those and the fight tips hard. Let the kids chain a Cinderoll off its neighbours; "
             "that is what packs of them are for."),
    ("body", "**BOSS: Groudon's Hollow** (the rescue, not the kill). Groudon (AC 18, HP 230, "
             "tremorsense 120 ft, CR 11; **Continental Step**: he moves, and everything on the "
             "ground within 30 ft of his path makes a **DC 16 Dexterity save** or takes 2d10 and is "
             "knocked prone; **Magma Vent**, recharge 4-6, a 60-ft line 10 ft wide, **DC 17 "
             "Dexterity** for 10d6 fire, half on a success; **Claw** +12 for 3d10+8 at 15 ft; "
             "**Agony**: while the spike is intact he takes 10 damage at the start of each of his "
             "turns and everything within 20 ft makes a **DC 16 Dexterity save** or takes 3d6 from "
             "the shockwave) + Glasslings (AC 14, HP 10; Glass Bite +5 for 1d6+3; Shatterburst at 0 "
             "HP, DC 12 Dexterity within 5 ft for 2d4), **one spawned at the start of each of "
             "Groudon's turns**. **THE LEVER IS THE ONLY WIN CONDITION: THE SPIKE.** AC 17, 60 hit "
             "points, immune to everything except **radiant, force, and Cleansing Edge**, reached "
             "by climbing, by flight, or by a ranged attack at disadvantage. Damaging it triggers "
             "**Thrash** (once a round, no action): every climber makes a **DC 15 Strength or "
             "Acrobatics check** or falls for 3d6. **When the spike breaks the fight ends "
             "instantly**, whatever his hit points are, and every Glassling on the board collapses "
             "into sand in the same heartbeat. Do not run him to 0. He is not supposed to die, and "
             "**He Does Not Finish Them**: a hero who drops is left alone, because he is swatting "
             "at pain, not hunting children."),
    ("body", "**THE ROAD BETWEEN** (garnet dots only, small pressure, never a fifth big fight). "
             "**Even: Thumpaw** (1x, AC 14, HP 76; two Shovel Slams at +8 for 2d8+5; Immovable; Not "
             "Actually Angry, so it never starts it, never pursues, and never finishes a downed "
             "hero). A straight brawl with no gimmick, on purpose. Do not offer the way out; if "
             "they think of befriending it themselves, **DC 15 Animal Handling**, with advantage "
             "from Ursa's Mark, moves it aside. **Odd: the Gleamoth** (3x swarm, AC 12, HP 26, fly "
             "40 ft hover, resist bludgeoning, piercing and slashing, **VULNERABLE FIRE AND "
             "THUNDER**; Smother +4 for 4d4, or 2d4 at half HP, and blinded until the end of its "
             "next turn). They chase the warmest, brightest thing in the tunnel, which is the "
             "Sphere, so the swarm sits on Lilly all fight and the party has to come to her. "
             "**The other dots, even then odd:** moss gives the Deepwater Spring (1 Hit Die back, "
             "one level of exhaustion cleared) or the Shortcut (advance the token 3 spaces free, "
             "and only if they were kind at the Landing); ochre gives Sinkloam (**DC 13 Strength** "
             "or restrained, heavy armour at disadvantage, so somebody has to go back for Lilly) "
             "or the Ceiling Lets Go (**DC 14 Dexterity**, 2d10 bludgeoning, half on a success, and "
             "the way back is shut); amethyst gives the Reef Answers (**2d8 temporary hit points** "
             "for everyone, and a fine place for the short rest if they have not taken it) or the "
             "Guardian's Dream (no mechanical effect, and Ursa may regain one spent omen)."),

    ("h1", "The Resource Picture"),
    ("body", "▶ One evening, one long day underground, and **exactly one short rest inside it**: "
             "immediately after the Chime Reef. Call it by name at the table, because four things "
             "come back on it and the players need to see the shape of that: **Hit Dice**, **Stabby's "
             "Focus** (7, and Igniting the Breath costs 1 while Devour refunds its own on a kill), "
             "**one of Ursa's three Wild Shape uses** (Starry Form spends one and runs 10 minutes), "
             "and **both of Lilly's Aether Wards** (2d8 + 5 temporary hit points to her and every "
             "friend within 30 ft, twice per short rest). The Reef Answers dot hands out 2d8 "
             "temporary hit points and the Deepwater Spring gives back a Hit Die and a level of "
             "exhaustion, so the road can quietly pay for a rough fight. What to watch: **Stabby's "
             "Focus across four fights plus whatever the dots throw**, because he is the answer to "
             "three of them and cannot afford to arrive at the spike empty; **Ursa's "
             "concentration**, one thing at a time, and his Wild Shape, since Starry Form and a "
             "summon are competing for the same three uses; **Lilly's Aether Ward**, which is the "
             "party's only pre-emptive shield and wants spending before Magma Vent, not after; and "
             "**Ghostbloom's Guardian's Light** (a reaction within 30 ft, 2d8 + 3 and it ends "
             "charmed or frightened, three times a short rest), which is the safety net for the "
             "whole run. She carries it all night and only steps into the Sphere at the very end, "
             "so nothing about it changes until the homecoming. Lilly's **Flash of Genius** (+5 to "
             "a failed check or save for her or a friend within 30 ft, five times a day) is the "
             "spare: hold at least one for the climb up Groudon's back."),

    ("h1", "Spotlights & Seeds: every kid shines, every door gets planted"),
    ("body", "**Lilly:** she is on the ground seven days early because she cannot stand waiting "
             "anywhere else → the cradle Vane built from a description closes around the real "
             "Sphere as though it were cut for it → her chapter is the year of questions, ending on "
             "a workshop floor with the marks under the brass and the sentence that reframes "
             "everything: **her mother did not make it, her mother found it, and it is a gatherer** "
             "→ the Handover is hers, six gifts on three cloths and not one of them made for "
             "herself first → in Underroot the Sphere pulls from the first breath and she is the "
             "only one who can say why → her Arcana at the reef reads the crystals leaning toward "
             "something deeper in → in the Gallery the Sphere is visibly drinking, and she works "
             "out that the loose essence bleeding out of this wound is exactly what it was built "
             "to collect → at the Hollow she is the ranged answer to the spike, and **force damage "
             "from Puff's Wand of Magic Missiles never misses it** → the Mote of Terra comes home "
             "and **Tectonic Slam wakes**. (Doors: four empty sockets and a ceiling gated entirely "
             "on rifts cleared; and somebody, a very long time ago, built the thing her mother only "
             "housed. Give her the workbench beat that night: it is not a battery, it is an "
             "instrument, and she has only ever played one note on it.)"),
    ("body", "**Stabby:** he arrives ten minutes early and pretends otherwise, and the idol hits the "
             "flagstones cold enough to burn → his chapter is the loudest in the book: **he was "
             "never unteachable, he was occupied**, the Fourth was his father, the Red Fang is "
             "older than the Hollow, and the whole test on Kettlecrown was holding still for one "
             "second → he came home and burned the blight out of the ground, and the clan that "
             "agreed he was not worth teaching offered him his father's seat, and he said not yet "
             "→ **Fight 1 is built to hand him the session**: Cleansing Edge is the only thing at "
             "the table that makes a Rotbloom stay cut, and it is the first time anyone else has "
             "seen his year work. Say it out loud when it lands → **Fight 3 is his proving "
             "ground**: the Weeper claws back 10 a round, so every wound they open is part shut "
             "by the time it comes round to them again, and "
             "he is the reason it is winnable, and afterward let him walk the glassed roots with "
             "his breath lit and burn a clean road out of the wound for everyone else to walk "
             "→ **the boss is his**: Speed 65 ignited, Step of the Wind to close, and the Nichirin "
             "is one of only three things in the world that can touch the spike. He climbs a "
             "mountain that is trying to shake him off and he cuts the corruption out of a god. Do "
             "not let anybody else take that unless his player hands it over; if the dice go badly, "
             "rescue the climb with Ursa's summon or Lilly's Flash of Genius so the last blow is "
             "still his. (Doors: the idol he has told nobody about, and a seat he did not say never "
             "to.)"),
    ("body", "**Ursa:** he comes in with the dawn traffic, taller and half a beat slower to answer, "
             "turning his father's half-carved stone over and over → his chapter goes last because "
             "it moves the campaign: the cairn road Ash built going out and Ursa repaired going in, "
             "the camp nobody said goodbye to, wood growth that reads **three years, not fifteen**, "
             "and a vision that gives him **Maldrith** and then hands him **Nyxthid** the way you "
             "hand somebody a weapon → at the Rift Gate, tell his player directly that the sky is "
             "gone and his year of star-reading buys him nothing down here, then give him advantage "
             "on Survival for reading the ground, which is what Selarin actually told him → the "
             "**Mark of Handling works on the Sandshrew**, and that should be the moment his player "
             "understands the plane's wildlife is not the enemy → he is the party's engine room all "
             "run: healing, control, and a summon between Groudon and whoever is climbing → and he "
             "is the only creature in the Hollow who can **feel that the guardian is in pain**. "
             "Telling the others is the moment the fight stops being a boss and becomes a rescue "
             "→ afterward, in Gearhaven lamplight, he is the only one who looks up, and **Antares is "
             "the deep steady red it is supposed to be**, the first star in living memory to come "
             "back. One new star brightens on the Staff of Waking Constellations, which is exactly "
             "what it was made for. (Doors: a father who was alive three years ago, a name to hunt, "
             "and four stars still to go.)"),

    ("h1", "Foreshadow Tracker: say it, then say it again"),
    ("body", "▶ The tells, in order, and every one of them pays later. **ANTARES:** Ursa looks up at "
             "the Threshold, sees it dimming, and says nothing (do not spend that beat); he looks "
             "up again on the way home and it is burning steady, and he is the only person alive "
             "who understands what that means. Aelwyn goes very quiet, because a theory just became "
             "a fact, and his last line of the night is one word: One. • **THE IDOL:** it hits the "
             "flagstones cold enough to burn when Stabby drops his pack, forty feet from a portal "
             "that is not even lit; it goes cold **again** at the Threshold, hard enough that he "
             "notices; it is colder still at the Rift Gate and painful enough in the Glassed "
             "Gallery that he wraps it in cloth to carry it; and it is **warm** the instant they "
             "come back through, and he notices exactly when, and tells nobody. Never explain it. "
             "• **NYXTHID**, named aloud for the first time in this campaign, in Ursa's vision, "
             "with **Maldrith** pressing behind the last wall. Keep the figure featureless: no "
             "face, no build, nothing anybody can match to a person later. If a player asks, it "
             "looked like a hole in the shape of a person. • **THE HALF-CARVED STONE:** Elaria's "
             "seven-pointed star in his father's hand, the line stopping mid-stroke the way a pen "
             "stops when somebody says your name, warm since the day he picked it up. • **PIKACHU "
             "AS A KEY:** the spark spoke in dread-images through the Mark in Gearhaven, of a vast "
             "hunger, a herald-shadow, and itself as *a key. To something.* Nobody has asked to "
             "what, and this session quietly proves the Sphere gathers whatever is loose, friend or "
             "scrap alike. • **THE GUILD-STAMPED CRATES:** the essence-harvest crates in the "
             "Dutchman's hold wore the Gearhaven Artificers' Guild seal and were bound south, and "
             "this whole session is spent standing in that Guild's own Underworks, being helped, by "
             "people nobody has thought to ask about it. Do not resolve it. Let one crate in the "
             "background of the Rift Hall carry the same stamp, and say nothing at all."),

    ("h1", "The Companion Swap: the rule, and the words to say it"),
    ("dm", "**Teach this properly and teach it tonight.** It is the mechanic the rest of the "
           "campaign runs on, and this is its first outing. Say it in this order, in these words, "
           "small enough for the youngest player to repeat back:\n"
           "**One out at a time.** The Sphere holds one companion in the world. Everybody else "
           "rides inside it, safe and awake and perfectly fine.\n"
           "**Swapping is Lilly's Action.** She calls the name, the one outside steps into the "
           "light, and the one she called steps out. \"Sandshrew, I choose you!\" That is the "
           "whole ritual, and yes, she should get to say it out loud.\n"
           "**Nobody ever dies in there.** A companion knocked to **0 hit points faints**, the "
           "Sphere recalls it on the spot, and it is not lost, not hurt for keeps, not gone. "
           "Promise that once and never break it.\n"
           "**Choose before you go, not in the middle.** Ghostbloom heals and senses planar "
           "things; Sandshrew digs and takes hits and is made of the same stuff as the ground. "
           "Picking wrong for a plane is a real mistake and an entirely survivable one, which is "
           "exactly what makes it an interesting decision."),
    ("dm", "**The roster grows by one per rift. Say that out loud tonight.** Four more planes, "
           "four more companions. The kids should start arguing about who they want next before "
           "the dishes are done, and they will be right to. Then hand Sandshrew over and **let "
           "them run the first swap themselves**, right there in the workshop, just to prove it "
           "works and get Ghostbloom back out where they can see her."),

    ("appendix_title", "APPENDIX", "Bestiary: Enemy Stat Blocks",
     "Every creature of Underroot, in the order the party meets them."),

("fight_header", "ENEMIES, Fight 1: Mosslight Landing",
     "Mosslight Landing ✦ Difficulty: Warm-up ✦ 6x Rotbloom + 6x Mossmite"),
    ("enemy_cards", [
        {
            "name": "Rotbloom",
            "sub": "Small plant (corrupted), unaligned ✦ CR 1/2 (100 XP) ✦ 6 in the grey moss",
            "img": "assets/monsters/rotbloom.png", "img_w": 2.4,
            "stats": [
                "**AC** 12  **HP** 22 (4d6 + 8)  **Speed** 25 ft",
                "**STR** 10  **DEX** 12  **CON** 14  **INT** 4  **WIS** 8  **CHA** 6",
                "**Resist** poison  **Imm.** (cond) blinded, deafened, poisoned",
                "**Senses** blindsight 30 ft, passive Perception 9",
                "**Challenge** 1/2 (100 XP)",
            ],
            "traits": [
                ("Re-Bloom", "At the start of its turn, if it took damage since its last turn "
                 "and is not at 0 HP, it regains 5 hit points. It cannot re-bloom if it has "
                 "taken radiant damage, or been hit by Cleansing Edge, since its last turn."),
                ("Still Smiling", "It cannot be frightened, and its face never changes, whatever "
                 "is happening to it."),
            ],
            "actions": [
                ("Cap Slam", "*Melee Weapon Attack:* +3 to hit, reach 5 ft. *Hit:* 6 (2d4 + 1) "
                 "bludgeoning damage."),
                ("Spore Puff (Recharge 5-6)", "10-ft cone, DC 12 Constitution save: 7 (2d6) "
                 "poison damage and poisoned until the end of its next turn; half damage and no "
                 "poisoning on a success."),
            ],
        },
        {
            "name": "Mossmite",
            "sub": "Tiny beast (corrupted), unaligned ✦ CR 1/8 (25 XP) ✦ 6 boiling out of the moss",
            "img": "assets/monsters/mossmite.png", "img_w": 2.4,
            "stats": [
                "**AC** 13  **HP** 7 (2d4 + 2)  **Speed** 40 ft, climb 40 ft",
                "**STR** 6  **DEX** 16  **CON** 12  **INT** 2  **WIS** 10  **CHA** 4",
                "**Senses** blindsight 30 ft, passive Perception 10",
                "**Challenge** 1/8 (25 XP)",
            ],
            "traits": [
                ("Skitter", "It does not provoke opportunity attacks."),
                ("Pack Nerve", "It has advantage on attacks against a creature if another "
                 "Mossmite is within 5 ft of it."),
            ],
            "actions": [
                ("Nip", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 5 (1d4 + 3) "
                 "piercing damage."),
            ],
        },
    ]),
    ("tactics", "This fight exists to hand Stabby the session. The Rotblooms swell back up out "
                "of their own caps every round, and ordinary steel keeps handing that ground "
                "back: only radiant damage or Cleansing Edge shuts Re-Bloom off. Let the party "
                "flail for a round and let Lilly and Ursa watch pieces of their damage close up "
                "again, then let Stabby "
                "ignite, cut one, and have it stay cut. The Mossmites boil out of the moss the "
                "moment the first Rotbloom is struck, and they are there to keep everyone honest "
                "while the real problem regrows behind them: individually harmless, collectively "
                "a swarm that punishes anyone who stands still. Six Rotblooms hitting in a cloud "
                "means Spore Puff has the whole party rolling saves, so this is a proper scrap "
                "rather than a speed bump. The tell to plant quietly: nothing here attacks the "
                "little armoured digger watching from the mound, and it does not run from them. "
                "Corruption does not eat its own."),

    ("fight_header", "ENEMIES, Fight 2: Chime Reef",
     "The Chime Reef ✦ Difficulty: Hard, or easy the moment they use thunder ✦ 3x Chimestone + "
     "3x Shardwing"),
    ("enemy_cards", [
        {
            "name": "Chimestone",
            "sub": "Medium elemental (Plane of Earth), unaligned ✦ CR 3 (700 XP) ✦ 3 standing up "
                   "out of the shallows",
            "img": "assets/monsters/chimestone.png", "img_w": 2.4,
            "stats": [
                "**AC** 16 (rock plate)  **HP** 52 (7d8 + 21)  **Speed** 25 ft",
                "**STR** 18  **DEX** 8  **CON** 16  **INT** 5  **WIS** 12  **CHA** 6",
                "**Resist** piercing, slashing  **Vuln.** thunder",
                "**Imm.** poison ✦ (cond) charmed, exhaustion, frightened, poisoned",
                "**Senses** tremorsense 60 ft, passive Perception 11",
                "**Challenge** 3 (700 XP)",
            ],
            "traits": [
                ("Resonant Body", "Whenever it takes **thunder damage** it is **stunned** until "
                 "the end of its next turn, and it takes **double damage** from every source "
                 "while stunned."),
                ("Struck Chord", "A creature can use an action to strike one of the reef's large "
                 "spires (DC 13 Athletics). Every Chimestone within 30 ft makes a DC 14 "
                 "Constitution save or is stunned as above. The striker takes 1d6 thunder damage "
                 "from standing that close."),
            ],
            "actions": [
                ("Multiattack", "Two Crystal Rams."),
                ("Crystal Ram", "*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 11 "
                 "(2d6 + 4) bludgeoning damage."),
                ("Shard Volley", "*Ranged Weapon Attack:* +6 to hit, range 40 ft. *Hit:* 9 (2d8) "
                 "piercing damage."),
            ],
        },
        {
            "name": "Shardwing",
            "sub": "Small elemental, unaligned ✦ CR 1 (200 XP) ✦ 3 in the air above the reef",
            "img": "assets/monsters/shardwing.png", "img_w": 2.4,
            "stats": [
                "**AC** 14  **HP** 22 (5d6 + 5)  **Speed** 10 ft, **fly 50 ft**",
                "**STR** 8  **DEX** 18  **CON** 12  **INT** 4  **WIS** 12  **CHA** 6",
                "**Vuln.** thunder ✦ **Imm.** poison ✦ (cond) poisoned, prone",
                "**Senses** tremorsense 30 ft, passive Perception 11",
                "**Challenge** 1 (200 XP)",
            ],
            "traits": [
                ("Glide", "It can fly at full speed without provoking opportunity attacks from "
                 "creatures it starts its turn adjacent to."),
            ],
            "actions": [
                ("Dive", "*Melee Weapon Attack:* +6 to hit, reach 5 ft. *Hit:* 9 (2d6 + 2) "
                 "slashing damage. If it moved at least 30 ft straight toward the target first, "
                 "this deals an extra 1d6."),
                ("Shard Spit", "*Ranged Weapon Attack:* +6 to hit, range 60 ft. *Hit:* 7 "
                 "(1d10 + 2) piercing damage."),
            ],
        },
    ]),
    ("tactics", "These are not corrupted. They are the reef's immune system, and the party is "
                "loud and warm and came in through a hole. **The lever is thunder.** Any thunder "
                "damage stuns a Chimestone until the end of its next turn and doubles all damage "
                "against it while it is stunned, which turns a wall with AC 16 into a free kill: "
                "Lilly's Thunderwave and Shatter, Ursa's Thunderwave, and Stabby's Nichirin "
                "ringing off the crystal all do it, and the Shardwings are vulnerable to thunder "
                "too, so one lever answers the whole encounter. The reef itself is the second "
                "weapon: an action and a DC 13 Athletics check to strike a big spire sends the "
                "note rolling out, and every Chimestone within 30 ft saves or is stunned. The "
                "trade keeps it honest, because the striker takes 1d6 thunder from standing that "
                "close, and nobody has ever minded. Play the Chimestones as the wall and the "
                "Shardwings as the reason nobody gets to stand still: they dive, they spit from "
                "sixty feet, and they will not be pinned down. A party that never finds the "
                "lever is in a genuinely hard fight, so do not soften it before they have had "
                "their chance to be clever. Call the short rest out loud the moment the reef "
                "goes quiet: Hit Dice, Stabby's Focus, Ursa's Wild Shape, Lilly's Aether Ward."),

    ("fight_header", "ENEMIES, Fight 3: The Glassed Gallery",
     "The Glassed Gallery ✦ Difficulty: The hardest fight before the boss ✦ 1x Glass Weeper + "
     "4x Cinderoll"),
    ("enemy_cards", [
        {
            "name": "Glass Weeper",
            "sub": "Large plant (corrupted guardian-beast), unaligned ✦ CR 6 (2,300 XP) ✦ still "
                   "trying to do its job",
            "img": "assets/session_08/mon_glass_weeper.png", "img_w": 2.6,
            "stats": [
                "**AC** 16 (black glass)  **HP** 115 (11d10 + 55)  **Speed** 20 ft",
                "**STR** 18  **DEX** 8  **CON** 20  **INT** 4  **WIS** 12  **CHA** 5",
                "**Resist** bludgeoning, piercing, slashing from nonmagical weapons",
                "**Imm.** poison ✦ (cond) charmed, frightened, poisoned, prone",
                "**Senses** blindsight 60 ft, passive Perception 11",
                "**Challenge** 6 (2,300 XP)",
            ],
            "traits": [
                ("Glassbound", "It regains 10 hit points at the start of its turn unless it took "
                 "radiant or force damage, or was hit by Cleansing Edge, since its last turn."),
                ("Rooted", "It cannot move more than 15 ft from the glassed roots it is tending, "
                 "and it never tries to."),
                ("Tend the Roots", "A creature can use an action to clear or heal the roots near "
                 "it: DC 14 Nature or Medicine, or any healing spell cast on the roots rather "
                 "than a creature. On a success the Weeper **loses Glassbound until the end of "
                 "its next turn** and every attack against it has **advantage** until the start "
                 "of the helper's next turn."),
            ],
            "actions": [
                ("Multiattack", "Three Frond Lashes."),
                ("Frond Lash", "*Melee Weapon Attack:* +7 to hit, reach 15 ft. *Hit:* 12 "
                 "(2d6 + 5) slashing damage."),
                ("Keening (Recharge 5-6)", "30-ft cone, DC 15 Constitution save: 21 (6d6) "
                 "psychic damage and frightened until the end of its next turn; half damage and "
                 "no fear on a success."),
            ],
        },
        {
            "name": "Cinderoll",
            "sub": "Small elemental (corrupted), unaligned ✦ CR 1/2 (100 XP) ✦ 4 in the gallery, "
                   "arriving two at a time",
            "img": "assets/monsters/cinderoll.png", "img_w": 2.4,
            "stats": [
                "**AC** 15 (glassy coal)  **HP** 18 (4d6 + 4)  **Speed** 40 ft (rolling)",
                "**STR** 12  **DEX** 14  **CON** 12  **INT** 3  **WIS** 8  **CHA** 3",
                "**Imm.** fire, poison ✦ (cond) blinded, charmed, deafened, poisoned",
                "**Senses** blindsight 60 ft, passive Perception 9",
                "**Challenge** 1/2 (100 XP)",
            ],
            "traits": [
                ("Rolling Charge", "If it moves at least 20 ft straight toward a target before "
                 "hitting it, the attack deals an extra 3 (1d6) damage and the target makes a DC "
                 "12 Strength save or is knocked prone."),
                ("Burst", "When it drops to 0 hit points it cracks open: each creature within 10 "
                 "ft makes a DC 12 Dexterity save or takes 7 (2d6) fire damage."),
            ],
            "actions": [
                ("Slam", "*Melee Weapon Attack:* +4 to hit, reach 5 ft. *Hit:* 7 (2d4 + 2) "
                 "bludgeoning damage plus 3 (1d6) fire damage."),
            ],
        },
    ]),
    ("tactics", "This is the big fight of the run before the boss and it should be hard. The "
                "Weeper hits for real, it regenerates 10 a round, and the Cinderolls keep "
                "rolling in and detonating, two at a time so the pressure never stops but never "
                "quite swamps the party. **The lever is the roots.** The Weeper is bound to the "
                "glassed roots it is still trying to comb clean, so any hero who spends an "
                "action tending them (DC 14 Nature or Medicine, or any healing spell aimed at "
                "the roots rather than a creature) strips its regeneration for a round and hands "
                "everyone advantage against it. Two or three of those and the fight tips hard. "
                "It never ends the encounter: it makes the party feel brilliant while they "
                "finish it. This is also Stabby's proving ground, because 10 hit points a round "
                "means every wound they open is part closed before they swing again, and only "
                "radiant, force, or Cleansing Edge shuts Glassbound off. He is the reason this "
                "fight stops going backwards, and everyone at "
                "the table should be able to see it. Let the Cinderolls cluster: killing one "
                "next to three others is a chain reaction, and the players should be allowed to "
                "discover that and enjoy it. When the Weeper falls it shatters, and curled up "
                "where its heart would be is a small ordinary creature that has been dead for "
                "two years. That is the beat that turns the session from an adventure into a "
                "rescue, so let the table sit with it before anyone moves on."),

    ("fight_header", "ENEMIES, BOSS: Groudon's Hollow",
     "Groudon's Hollow ✦ Difficulty: Boss, but the spike is the whole fight ✦ 1x Groudon + one "
     "Glassling every round"),
    ("enemy_cards", [
        {
            "name": "Groudon, the Continent-Maker",
            "sub": "Gargantuan elemental (Plane of Earth, Guardian), unaligned ✦ CR 11 (7,200 "
                   "XP) as run here ✦ he is not the villain, the spike is",
            "img": "assets/session_08/mon_groudon_corrupted.png", "img_w": 3.0,
            "stats": [
                "**AC** 18 (mountain plate)  **HP** 230 (but see The Spike)  **Speed** 40 ft, "
                "burrow 40 ft",
                "**STR** 26  **DEX** 6  **CON** 24  **INT** 8  **WIS** 14  **CHA** 12",
                "**Resist** all damage from nonmagical weapons",
                "**Imm.** fire, poison ✦ (cond) most",
                "**Senses** tremorsense 120 ft, passive Perception 12",
                "**Challenge** 11 (7,200 XP)",
            ],
            "traits": [
                ("THE SPIKE (this is the encounter)", "A shard of black glass is driven into his "
                 "back at the shoulder. **AC 17, 60 hit points**, immune to all damage except "
                 "**radiant, force, and Cleansing Edge**. Reaching it requires climbing him, "
                 "flying, or a ranged attack at disadvantage. **When the spike is destroyed the "
                 "encounter ends immediately**, whatever Groudon's hit points are. Do not run "
                 "him to 0. He is not supposed to die."),
                ("Unstoppable", "He cannot be frightened, charmed, restrained, or knocked prone, "
                 "and he ignores difficult terrain."),
                ("Agony", "While the spike is intact, at the start of each of his turns he takes "
                 "10 damage and everything within 20 ft makes a DC 16 Dexterity save or takes 10 "
                 "(3d6) bludgeoning damage from the shockwave."),
                ("He Does Not Finish Them", "When Groudon reduces a creature to 0 hit points, he "
                 "immediately moves away from it. He is swatting at pain, not hunting children."),
            ],
            "actions": [
                ("Continental Step", "He moves up to his speed. Every creature on the ground "
                 "within 30 ft of his path makes a DC 16 Dexterity save or is knocked prone and "
                 "takes 11 (2d10) bludgeoning damage."),
                ("Magma Vent (Recharge 4-6)", "A 60-ft line, 10 ft wide. DC 17 Dexterity save: "
                 "35 (10d6) fire damage, half on a success."),
                ("Claw", "*Melee Weapon Attack:* +12 to hit, reach 15 ft. *Hit:* 24 (3d10 + 8) "
                 "slashing damage."),
                ("Thrash (when the spike takes damage, 1/round, no action)", "Every creature "
                 "climbing him makes a DC 15 Strength or Acrobatics check or falls, taking 3d6 "
                 "bludgeoning damage."),
            ],
        },
        {
            "name": "Glassling",
            "sub": "Tiny construct (spawned by the spike), unaligned ✦ CR 1/4 (50 XP) ✦ one new "
                   "one every round the spike lives",
            "img": "assets/monsters/glassling.png", "img_w": 2.4,
            "stats": [
                "**AC** 14  **HP** 10 (3d4 + 3)  **Speed** 30 ft, climb 30 ft",
                "**STR** 8  **DEX** 16  **CON** 12  **INT** 1  **WIS** 6  **CHA** 1",
                "**Imm.** poison, psychic ✦ (cond) blinded, charmed, deafened, frightened, "
                "poisoned",
                "**Senses** blindsight 30 ft, passive Perception 8",
                "**Challenge** 1/4 (50 XP)",
            ],
            "traits": [
                ("Spike-Born", "**The spike creates one Glassling at the start of each of "
                 "Groudon's turns.** When the spike is destroyed, every Glassling collapses into "
                 "ordinary sand immediately, wherever it is and whatever it was doing."),
                ("Shatterburst", "At 0 hit points, each creature within 5 ft makes a DC 12 "
                 "Dexterity save or takes 5 (2d4) slashing damage."),
            ],
            "actions": [
                ("Glass Bite", "*Melee Weapon Attack:* +5 to hit, reach 5 ft. *Hit:* 6 (1d6 + 3) "
                 "slashing damage."),
            ],
        },
    ]),
    ("tactics", "Do not let the party win by damage. Groudon has more hit points than they can "
                "chew through and hits hard enough to drop a hero in two turns, so a straight "
                "brawl is a loss. The win condition is the spike: AC 17, 60 hit points, immune "
                "to everything except radiant, force, and Cleansing Edge, reached by climbing "
                "him, by flight (Stabby's Sash, Ursa's Starry Form), or by a called shot at "
                "range with disadvantage. Break it and the fight is over on the spot, not "
                "whittled down. The Glasslings are the answer to the obvious question, which is "
                "why not ignore the spike and whittle Groudon from range: one more of them drops off his "
                "back at the start of every one of his turns, so the longer the spike lives the "
                "more little glass things are chewing on the party, and the instant the spike "
                "goes every one of them collapses into sand at once and the whole board clears "
                "in a heartbeat. Play Groudon as a natural disaster with a wounded animal inside "
                "it rather than a tactician, alternating Continental Step, Magma Vent, Claw, and "
                "Thrash when the spike is struck. Every hero has a role: Stabby climbs a "
                "mountain that is trying to shake him off and cuts the corruption out of a god, "
                "and this is his moment, so do not let anyone else take it unless his player "
                "hands it over; Ursa keeps people standing and can put a summon between Groudon "
                "and the climber, and his Mark of Handling lets him feel that the creature is in "
                "pain, which is the line that turns the fight into a rescue; Lilly shoots the "
                "spike from range, holds the party together with Aether Ward, and Puff's Wand of "
                "Magic Missiles is force damage that never misses. If the dice go badly, let a "
                "summon pin Groudon or let Flash of Genius rescue the climb check so the last "
                "blow is still Stabby's. Mercy rule for the table: if a hero drops, Groudon does "
                "not finish them. He is not killed here. He is freed."),

    ("fight_header", "ENEMIES: The Road Between",
     "Anywhere on the board ✦ Difficulty: Small pressure ✦ dot encounters only"),
    ("enemy_cards", [
        {
            "name": "Thumpaw",
            "sub": "Large beast (Plane of Earth), unaligned ✦ CR 3 (700 XP) ✦ random encounters "
                   "only ✦ 1, and it was there first",
            "img": "assets/monsters/thumpaw.png", "img_w": 2.4,
            "stats": [
                "**AC** 14 (mossy hide)  **HP** 76 (8d10 + 32)  **Speed** 30 ft, burrow 30 ft",
                "**STR** 20  **DEX** 8  **CON** 18  **INT** 3  **WIS** 12  **CHA** 6",
                "**Senses** tremorsense 60 ft, passive Perception 13",
                "**Challenge** 3 (700 XP)",
            ],
            "traits": [
                ("Not Actually Angry", "It does not attack until attacked, and it never pursues. "
                 "It is in the way and it was there first."),
                ("Immovable", "It has advantage on saves and checks against being moved, and it "
                 "cannot be knocked prone."),
            ],
            "actions": [
                ("Multiattack", "Two Shovel Slams."),
                ("Shovel Slam", "*Melee Weapon Attack:* +8 to hit, reach 10 ft. *Hit:* 14 "
                 "(2d8 + 5) bludgeoning damage."),
            ],
        },
        {
            "name": "Gleamoth Swarm",
            "sub": "Medium swarm of Tiny beasts, unaligned ✦ CR 1 (200 XP) ✦ random encounters "
                   "only ✦ 3 swarms, and they want the warmest thing in the tunnel",
            "img": "assets/monsters/gleamoth_swarm.png", "img_w": 2.4,
            "stats": [
                "**AC** 12  **HP** 26 (4d8 + 8)  **Speed** 5 ft, **fly 40 ft** (hover)",
                "**STR** 4  **DEX** 14  **CON** 14  **INT** 1  **WIS** 10  **CHA** 4",
                "**Resist** bludgeoning, piercing, slashing  **Vuln.** fire, thunder",
                "**Imm.** (cond) charmed, frightened, grappled, prone, restrained, stunned",
                "**Senses** blindsight 20 ft, passive Perception 10",
                "**Challenge** 1 (200 XP)",
            ],
            "traits": [
                ("Drawn to Warmth", "It always moves toward the warmest or brightest thing it "
                 "can sense, which is the Essence Sphere. If Lilly is carrying it, the swarm "
                 "goes for her every turn."),
                ("Swarm", "It can occupy another creature's space and move through any opening "
                 "large enough for a single moth."),
            ],
            "actions": [
                ("Smother", "*Melee Weapon Attack:* +4 to hit, reach 0 ft, one creature in its "
                 "space. *Hit:* 10 (4d4) piercing damage, or 5 (2d4) if the swarm is at half its "
                 "hit points or fewer, and the target is **blinded** until the end of its next "
                 "turn."),
            ],
        },
    ]),
    ("tactics", "These two never appear at a scripted fight. They are what a garnet dot means, "
                "and they are the only creatures the party meets purely by luck, which is what "
                "keeps a dot roll feeling different from a story beat instead of feeling like "
                "filler. Keep them small: a little pressure, a little resource, and no more. Do "
                "not let a dot roll swell into a fifth big fight, because the four scripted "
                "encounters are the session. Thumpaw is a straight brawl with no gimmick and no "
                "puzzle, 76 hit points and two big slams a turn, for the moments when the table "
                "simply wants to hit something large until it stops; it never pursues and it "
                "never finishes a downed hero, because it is grumpy, not evil. (If the players "
                "think of befriending it instead, a DC 15 Animal Handling check with advantage "
                "from Ursa's Mark moves it aside. Do not offer this. Let them find it.) The "
                "Gleamoths are not corrupted either, just hungry for heat: they blind and "
                "smother rather than deal much damage, fire and thunder scatter them fast, and "
                "anything that hits an area is worth double. The cost is the Sphere, which pulls "
                "them hardest, so the swarm sits on Lilly the whole fight and the rest of the "
                "party has to come to her."),

    ("lore", "The Two Lists",
     "The Circle's bestiary of the Darkening keeps two lists. The frightening one is "
     "long: the twisted, the glassed, the re-blooming, every creature the leaking dark "
     "has worn like a glove. The kind one is longer, and it is the same list, written "
     "again after somebody set them free. Corruption, the sky-readers say, is a thing "
     "that happens to a creature, never a thing that it is. Strike to free, not to "
     "punish, and a world will hand you back more friends than enemies."),

]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    print("built", build_doc(BLOCKS, "sessions/session_08_underroot.docx"))
