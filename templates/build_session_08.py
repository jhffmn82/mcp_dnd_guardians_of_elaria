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

    ("img", f"{S8}/A_the_finished_ring.png",
     "The Rift Hall at midnight: ten years of Vane's life, finished, and nobody has dared switch it on.",
     6.2, {"crop": "3:2", "hmax": 4.5}),

    ("h1", "Previously, on The Guardians of Elaria...", {"hardbreak": True}),
    ("gold", "In the clockwork city of **Gearhaven** the heroes freed the **Grand Custodian**, the "
             "great machine that makes the city's heartbeat, from the corruption twisting it. The "
             "city's wounds knitted shut behind them, and they learned the rule that governs "
             "everything since: **a crack cannot be sealed from our side, but free a world's "
             "guardian and its cracks close on their own.**"),
    ("gold", "**Guildmaster Vane** showed them his life's work, a ring of brass ten years in the "
             "building, waiting on the one thing it lacked: an anchor. The **Essence Sphere** is "
             "that anchor. Pikachu's spark spoke to them through Ursa's Mark, in dread-images "
             "rather than words, of a vast hunger and a herald-shadow, and of itself as *a key. To "
             "something.*"),
    ("gold", "And then, because the ring would not be ready for a year, the three of them went "
             "their separate ways. **This session opens on the day they come back.**"),
    ("dm", "The heroes return at **level 7**. Hand out the new sheets during **The Handover**, so "
           "the fiction and the paperwork land in the same beat. Part One is read like a chapter; "
           "Part Two is played on the Underroot board."),

    # ================================================================
    ("h1", "Part One: The Year Apart"),
    ("bridge", "Four arrivals, three stories, and a door that has never been opened."),

    ("h2", "Seven Days Early"),
    ("gold", "The Artificer's Guild never really sleeps, but at this hour it comes close. Down in "
             "the Underworks the furnaces are banked to a low orange mutter, and the great ring of "
             "the portal stands in the middle of the Rift Hall like something dreaming.\n"
             "It is finished. After ten years of Guildmaster Vane's life it is finished, and it has "
             "been finished for eleven days, and nobody has dared to switch it on.\n"
             "You have been here a week. You told yourself it was to check the anchor housing. It "
             "was really because you could not stand another night of waiting somewhere else."),
    ("dm", "**Three things to land this week.** **Vane has aged**: ten years of work ended eleven "
           "days ago and he does not know what to do with his hands, so he is louder than usual and "
           "sleeping less, and he will not say he is frightened. **Lilly is the expert now**, and "
           "the guild artificers ask her opinion and mean it. And **the cradle does not quite "
           "fit**, because Vane built it from drawings of a sphere he had only had described to "
           "him; when she finally sets the real thing in on the sixth night the brass closes around "
           "it as though it were cut for it. Play that quiet. It is the first hint of what she "
           "learned."),

    ("h2", "The Professor"),
    ("img", f"{S8}/B_aelwyn_arrives.png",
     "Professor Aelwyn Ravenstone arrives with three trunks and no help whatsoever, and Lickgloom "
     "rides the luggage.", 5.8, {"crop": "3:2", "hmax": 3.9}),
    ("gold", "He is exactly as you remember him and slightly worse: tall, silver haired, entirely "
             "certain, and delighted to be proven wrong about anything as long as he is the one "
             "doing the proving. He looks at the ring for a long moment, and then at the Sphere in "
             "its cradle, and then he says, to nobody in particular:\n"
             "\"Oh. That is much older than you think it is.\"\n"
             "He says it the way other people say good morning."),
    ("body", "**Lickgloom remembers them.** He stayed behind at Ravenstone Laboratory two years ago "
             "and has spent the time since licking a professor's equipment. He recognises the party "
             "instantly and is beside himself about it. Give this a beat: it is the only "
             "uncomplicated happy reunion in the whole session."),

    ("h2", "Dawn, and the Eastern Gate"),
    ("imgfloat", f"{S8}/C_ursa_at_the_eastern_gate.png", 2.9, {"hmax": 3.6}),
    ("gold", "He comes in with the dawn traffic, on foot, with road dust to his knees.\n"
             "He is taller. That is the first thing. The second is that he is quiet in a way he "
             "never used to be, and he waits half a beat before he answers you, as though he is "
             "listening to something a half second behind your voice. There is a stone in his left "
             "hand that he turns over and over without seeming to know he is doing it.\n"
             "He has been walking east for a year. He does not look like someone who found what he "
             "was looking for. He does not look like someone who failed, either."),

    ("h2", "Ten to Midnight"),
    ("gold", "The bell over the Rift Hall doors has not rung all evening. It does not ring now "
             "either, because the goblin coming through them does not touch them.\n"
             "He is on the rail above you before anybody thinks to look up. He is leaner, and there "
             "is a new sword across his back, dark and quiet, and when he drops down into the "
             "lamplight he lands without a sound, which he absolutely never used to do.\n"
             "\"I'm not late,\" says Stabby Sharpblade. \"It's still today.\""),
    ("img", f"{S8}/D_stabby_drops_from_the_rafters.png",
     "He has ten minutes in hand, and he has almost certainly been in Gearhaven since the afternoon.",
     4.6, {"crop": "1:1", "hmax": 3.6}),
    ("dm", "**The idol.** When Stabby swings his pack down, something inside knocks against the "
           "flagstones with a dull, wrong sound. It is the small carved idol that appeared in his "
           "bag after Wraithpine, which nobody has ever explained and no one saw put there. Here, "
           "forty feet from a portal that is not even lit, **it is cold enough to burn**. He has "
           "carried it a year and it has never done that. Do not explain it. Let it sit there."),

    # ---------------- the three chapters ----------------
    ("h1", "The Year Apart: Three Stories"),
    ("dm", "Give each player the floor and read their chapter in full. This order builds best: "
           "Lilly's is the most hopeful, Stabby's is the loudest, and Ursa's changes the shape of "
           "the campaign, so it goes last."),

    ("h2", "Lilly: The Year of Questions"),
    ("img", f"{S8}/L_poots_at_the_door.png",
     "Deepforge Hollow, and a mother with flour on her hands.", 5.6, {"crop": "3:2", "hmax": 3.6}),
    ("gold", "She went home first. That surprised everyone, including Lilly. She put the Essence "
             "Sphere on her mother's kitchen table and said: tell me everything.\n"
             "What followed was the least satisfying conversation of her life. Poots told her about "
             "the day she brought it home, about the long nights fitting the brass around it, about "
             "the sigil work along the equator that took eleven tries to get right. She talked like "
             "a craftsman describing a commission. And Lilly, who had grown up on her mother's "
             "stories, noticed the shape of the hole in this one: **Poots never once said where the "
             "thing inside the brass had come from.**"),
    ("img", f"{S8}/M_sparkwicks_verdict.png",
     "Master Droven Sparkwick studies it a long time. \"I taught your mother. I did not teach her this.\"",
     4.6, {"crop": "1:1", "hmax": 3.4}),
    ("gold", "So she went looking. She earned her answers out of Master Sparkwick at Glimmerspire, "
             "and then she followed the trade roads and paid a dozen artificers in the only "
             "currency she had, which was work. A season with a clockmaker who could not cast a "
             "single spell and whose escapements humbled her. Six weeks with a woman who built "
             "hands for injured miners. Two more passes through Gearhaven with Vane shouting about "
             "tolerances. Her craft went from clever to formidable."),
    ("imgfloat", f"{S8}/N_the_hands_workshop.png", 2.7, {"hmax": 3.2}),
    ("body", "Then she took it to wizards, who ask what a thing *is*, and one of them fainted, and "
             "another wrote her four increasingly frantic letters, and none of them knew."),
    ("gold", "The answer was in the brass. On the forty-first time she opened the housing she "
             "stopped admiring her mother's sigils and looked *underneath* them, and found older "
             "marks on a surface that should have been the inside of her mother's shell and was "
             "instead the outside of something else."),
    ("img", f"{S8}/E_the_marks_under_the_brass.png",
     "The brass was Glimmerspire. The brass was her mother, eleven tries and all. The thing inside "
     "the brass was old.", 5.6, {"crop": "1:1", "hmax": 3.8}),
    ("gold", "**Her mother did not make the Essence Sphere.** Poots Glimmergear found it, "
             "understood it was worth protecting, and spent a year of her own life building it a "
             "house.\n"
             "And the thing Lilly worked out on a workshop floor a long way from home: **it is a "
             "gatherer.** It was built to pull in loose planar essence and hold it. It held Pikachu "
             "because Pikachu's spark was loose, and the Sphere does not know the difference "
             "between a scrap of stray fire and somebody's friend. You cannot pick a gatherer's "
             "lock. You can only give it something to gather.\n"
             "So she stopped building at it and started listening to it."),
    ("dm", "**What she brings back.** *Aether Channeler*: she can draw the **Aether Ward** out of "
           "the Sphere, 2d8 + 5 temporary hit points to herself and every friend within 30 feet, "
           "twice per short rest. The five great discharges sleep until each plane's Mote comes "
           "home. **Her power now grows by going out**, which is the whole point. Also *Flash of "
           "Genius*: +5 to a failed check or save for her or any friend within 30 feet, five times "
           "a day."),

    ("h2", "Stabby: The Year He Went Back"),
    ("gold", "Every clan has one child who is a problem, and the Bloodfang had Stabby.\n"
             "He could not do any of it. Goblin children learn the clan's arts from the time they "
             "can stand, and the arts simply did not take with him. Every stance slid off. He was "
             "not lazy and he was not stupid. He was *unteachable*, in a clan that had exactly one "
             "measure of a person's worth, and by the time he was five everyone had quietly agreed "
             "what he was going to be.\n"
             "So he became the joke instead. If they were going to laugh anyway, he would decide "
             "what they laughed at."),
    ("body", "Then **Skitch** came. The young Bloodfang courier the party pulled half-dead out of "
             "the machinery under Gearhaven had been sent a very long way to find the only "
             "Bloodfang anyone could name who had gone out into the world and come back alive from "
             "anything. Stabby laughed at him, because the clan asking for him was the clan that "
             "had spent his whole childhood explaining he was not worth teaching. Then he stopped "
             "laughing, packed in about four minutes, and went."),
    ("gold", "**Bloodthorn Hollow was dying, and the blight took the strongest first.** The biggest "
             "hunter, then the second biggest, then down the list. The Bloodfang had one law, which "
             "was that the biggest goblin wins, and something in the woods was eating them in "
             "order. By the time Stabby walked back in, the clan was mostly the small ones. The "
             "overlooked ones. He knew every single one of them. He had been the smallest of them "
             "once."),
    ("body", "He saved them the way he does everything, fast and loud and extremely well: eleven "
             "weeks of hunting, the whole Hollow moved twice over furious objection, traps a "
             "cleverer person would not have thought of. By the end of summer the Bloodfang were "
             "not dying anymore. **But he had not fixed it. He had only outrun it.** Candyfang went "
             "through the corrupted things the way a knife goes through smoke."),
    ("img", f"{S8}/O_nokk_and_the_fourth.png",
     "Nokk tells him the truth nobody told him, because the ones who knew agreed it was kinder not to.",
     4.6, {"crop": "1:1", "hmax": 3.4}),
    ("gold", "**His father was the Fourth.** The fourth leader the Bloodfang ever named, and by "
             "every account the best of them. Nine years ago something came out of the deep woods, "
             "and the Fourth went to meet it alone, and he did not kill it, because it was not the "
             "kind of thing that can be killed. **He sealed it.** The only vessel to hand that night "
             "was his newborn son, and it cost him his life to do it.\n"
             "The clan is named Bloodfang for that thing. Not for their own teeth. **The Red Fang** "
             "is older than the Hollow.\n"
             "And that is why the arts never took. There was something enormous asleep behind "
             "Stabby's ribs, pushing back against every form they poured into him. **He was never "
             "unteachable. He was occupied.**"),
    ("img", f"{S8}/stabby_the_stillness_test.png",
     "Kettlecrown, above the cloud line: the Sunward Vigil turn out to be bullywugs, and the entire "
     "test is holding still.", 4.0, {"hmax": 4.6}),
    ("gold", "The sect on the mountain are frog-folk, enormous with age, and they cared about "
             "exactly one thing and tested it on the first morning. They asked him to be **still**. "
             "Not to sit quietly, which he could have faked: still, entirely, from the inside, in "
             "the moment before violence.\n"
             "He failed for eleven weeks. He nearly left twice. And then in the third month, in the "
             "dark, he heard Master Kaelon Windstep say the thing he had said years ago that Stabby "
             "had never once managed to do: *when the whole world is screaming, little storm, get "
             "still.*\n"
             "He had always heard it as an instruction to calm down. It was not. It was smaller and "
             "far more useful. **Be still for one second, at the one moment that matters.** One "
             "second, Stabby could do."),
    ("img", f"{S8}/P_the_bullywug_forge.png",
     "A Nichirin blade is a graduation, not a gift. He worked the bellows for eight days of it.",
     5.8, {"crop": "3:2", "hmax": 3.8}),
    ("img", f"{S8}/Q_the_purge.png",
     "He came home in deep winter and burned the thing out of the ground, root and all, exactly as "
     "he had promised.", 6.0, {"crop": "3:2", "hmax": 3.9}),
    ("gold", "The Bloodfang had watched their biggest and best taken one after another for two "
             "years, and the thing that finally walked out of the twisted woods with the blight "
             "dead behind it was **the runt**. The clan joke. The one they had all quietly agreed "
             "was not worth teaching.\n"
             "There is not a goblin in the Hollow who will hear a word against him now."),
    ("img", f"{S8}/R_teaching_the_count.png",
     "What made him something else was teaching it. The Vigil gave him the basics; his clan gave "
     "him the rest.", 5.8, {"crop": "3:2", "hmax": 3.6}),
    ("dm", "They offered him his father's seat and **he said not yet**, and Nokk was the only one "
           "who noticed he did not say never. He gave them Candyfang as the clan's heirloom, and by "
           "their new law the heirloom is carried by whoever the clan would follow, which is why it "
           "is still on his belt. It is not his anymore. It is theirs, and he is only wearing it."),

    ("h2", "Ursa: The Road East"),
    ("img", f"{S8}/T_selarin_and_the_cabinet.png",
     "Nine days of arguing, and then Elder Selarin unlocks the cabinet, because he knew from the "
     "first hour that he would.", 4.6, {"crop": "1:1", "hmax": 3.4}),
    ("gold", "The other two went home. Ursa went the other way.\n"
             "\"You are eight,\" Selarin said. \"I know how old I am,\" said Ursa. On the ninth day "
             "the old man handed over his father's field notes without a word, and then said one "
             "thing, which Ursa has repeated to nobody: *your father read the sky better than any "
             "of us. It did not save him. Read the ground too.*"),
    ("body", "The notes are the working papers of a man in the middle of a thought: sky charts with "
             "dates, the same constellation drawn eleven times over eleven months with one point of "
             "light getting fainter each time, and one word underlined twice and never explained. "
             "**Betelgeuse.** The first star to go out. The notes stop in the middle of a page. Not "
             "at the end of a thought. In the middle of one."),
    ("img", f"{S8}/U_the_cairn.png",
     "The Skyless Country: ordinary land under a sky that never breaks. For a druid who navigates "
     "by constellations, a blindfold.", 6.0, {"crop": "3:2", "hmax": 3.8}),
    ("gold", "He went east on foot and **alone**, because Ghostbloom stayed at the Guild and where "
             "he was going had no roads. Eleven months of walking. And when the maps ran out he "
             "came into a country where the cloud never breaks, and he lost eleven days in there, "
             "and he will not talk about the eleven days.\n"
             "What saved him was that his father had been there first. **A road of cairns**, each "
             "placed exactly at the edge of sight of the last, so a person could cross the blind "
             "land one stone at a time. Ash built it going out. Ursa walked it going in, and "
             "**repaired eleven of them on the way**, because there was no reason to assume he "
             "would be the last person to need the road."),
    ("img", f"{S8}/G_the_empty_camp.png",
     "The old shrine, far east beyond the maps. A camp in the condition of a place somebody meant "
     "to come back to.", 6.2, {"crop": "3:2", "hmax": 4.0}),
    ("gold", "He did not find his father. He found the camp his father made: a firepit long cold, a "
             "shelter of bent living branches still holding, split wood stacked dry and ready, a "
             "tin cup. Nothing packed. Nothing buried. **Nobody had said goodbye to this place.**\n"
             "And he found out how long ago by doing exactly what Selarin told him. The shelter was "
             "still alive and still growing, and the wood had closed over the bindings by an amount "
             "a druid can read like a page.\n"
             "Not fifteen years. **Three.**"),
    ("imgfloat", f"{S8}/V_the_half_carved_stone.png", 2.7, {"hmax": 3.2}),
    ("body", "Under the flat rock, wrapped in oilcloth against the weather, was a river stone "
             "carved with Elaria's seven-pointed star. **Half of it.** The line stops mid-stroke, "
             "the way a pen stops when somebody says your name. It is his father's hand. When Ursa "
             "closed his fingers around it the stone was warm, and it has been warm ever since."),
    ("img", f"{S8}/H_the_vision_in_the_stones.png",
     "On the eighth night the cloud broke, and the standing stones lit from the inside.",
     5.4, {"crop": "1:1", "hmax": 4.0}),
    ("gold", "**Elaria showed him three things.**\n"
             "The first was his father **walking**, deliberately, toward a light that was going "
             "out. Ursa has carried a small ugly question since he was old enough to understand the "
             "word *disappeared*: did my father choose to leave me? The answer is yes, and the "
             "reason is the best reason there has ever been. **Ash Catchum went east to save the "
             "stars.**\n"
             "The second was a wall at the bottom of everything, and behind it a hunger with "
             "patience, pressing. He knew the name from the Circle's old verses before the vision "
             "gave it to him. **Maldrith.**\n"
             "The third was a shadow that walks for her, on a high place with the sky dying behind "
             "it, putting out a light as calmly as a person pinching a candle. And the vision gave "
             "that one a name too, the way you hand somebody a weapon. **Nyxthid.**"),
    ("dm", "**This is the first time the name Nyxthid is spoken in this campaign.** Ursa has just "
           "sworn to hunt his own father and will spend four sessions doing it. Elaria did not lie "
           "to him: every single thing she showed him is true. She simply did not show him that the "
           "man walking east and the shadow in black are the same person. **Keep the figure "
           "featureless.** No face, no build, nothing that can be matched later. If a player asks "
           "what it looked like, it looked like a hole in the shape of a person."),

    # ---------------- handover ----------------
    ("h1", "The Handover"),
    ("img", f"{S8}/lilly_gifts_laid_out.png",
     "A cloth on the bench for each of them, which is a very Lilly way of doing things.",
     6.2, {"crop": "3:2", "hmax": 4.0}),
    ("gold", "Lilly has been awake since four. There is a cloth on the bench for each of you, and "
             "she has clearly rehearsed this speech, and she gets about six words into it before "
             "she gives up and just starts handing things over."),
    ("dm", "**Hand out the new character sheets here**, so the fiction and the paperwork happen in "
           "the same beat. Seven magic items land on three players at once and none of them work "
           "like a sword, so teach the traps now, in a quiet room, rather than on the far side of "
           "the ring."),
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

    # ---------------- briefing + lesson ----------------
    ("h1", "The Briefing"),
    ("img", f"{S8}/I_aelwyns_briefing.png",
     "Aelwyn talks, Vane interrupts, and Lickgloom licks something he should not.",
     6.2, {"crop": "3:2", "hmax": 4.0}),
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
     "He does this properly, with a chalkboard and far too much enthusiasm.",
     6.0, {"crop": "3:2", "hmax": 3.9}),
    ("gold", "\"Earth,\" says the professor, \"is not a cave. I want that out of your heads "
             "immediately. You are not going underground. You are going to a place that is *made* "
             "of ground, all the way through, in every direction, forever.\"\n"
             "\"It is called Underroot. There is no sun there and it has never needed one. There "
             "are roots down there the size of cathedrals, and they are alive, and they are older "
             "than your species. The soil breathes, slowly, about once an hour. And nothing there "
             "is in a hurry, which will be the strangest part for you three.\""),
    ("dm", "**Three facts the players need for Part Two.** It is **slow, not empty**: a rockfall "
           "there is a shrug. There is **no sky, so Ursa cannot navigate**, and his year of "
           "star-reading buys him nothing; what works is reading the ground, exactly as Selarin "
           "told him. And it is **indifferent, not hostile**."),
    ("gold", "\"Every world keeps something. Not a king and not a god. A *guardian*: one creature, "
             "very old, that is somehow the shape of that world's health. When Gearhaven was sick "
             "you found the Grand Custodian at the heart of it, twisted almost past recognition, "
             "and when you freed it the whole city knitted shut behind you. Do you remember?\"\n"
             "He taps the board. \"You did not do that by being clever. You did it by being *kind* "
             "to something that was hurting. I would like you to notice that, because you are about "
             "to do it again, and the thing you do it to this time is roughly the size of a hill.\"\n"
             "\"What if it fights us?\" says Stabby, delighted.\n"
             "\"Then I would prefer you not *lose*.\""),
    ("dm", "The Guardian of Underroot is **Groudon**. Aelwyn does not know its name and neither "
           "should the party: let them meet it as a shape in the dark and a sound in their teeth "
           "before it is ever a stat block."),

    ("h1", "The Threshold"),
    ("dm", "Last beats, in this order. **Ursa looks up** and sees that Antares is dimming, and says "
           "nothing; do not spend that, it pays off at the end of the night. **The idol goes cold** "
           "again in Stabby's pack, hard enough that he notices. **Lilly sets the Sphere in the "
           "cradle** and it fits like it was cut for it. And **Vane does not make a speech**: he "
           "had ten years to write one, and what he actually does is put a hand on Lilly's shoulder "
           "for a second and then go and stand at the lever."),
    ("gold", "The ring does not roar. That is the surprising part.\n"
             "The Sphere settles into the cradle with a small brass click, and the air inside the "
             "circle simply stops being air. What is on the other side is a red-brown dark, and "
             "warmth, and a smell like a garden turned over after rain, and a sound so low that you "
             "feel it in your teeth rather than hear it.\n"
             "Somewhere on the far side of that opening, something the size of a hill breathes in.\n"
             "Ghostbloom goes first, because of course she does."),
    ("img", f"{S8}/J_the_threshold.png",
     "The last picture before everything changes.", 6.2, {"crop": "3:2", "hmax": 4.2}),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    print("built", build_doc(BLOCKS, "sessions/session_08_underroot.docx"))
