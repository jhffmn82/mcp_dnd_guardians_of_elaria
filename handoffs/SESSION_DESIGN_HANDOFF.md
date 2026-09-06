# Session Design Handoff

**The operator's manual for designing and producing one session of The Guardians of Elaria, from a blank chat to a numbered PDF in the book.**

Written 2026-09-06, after a session that ran long and made a string of expensive, avoidable mistakes. Every one of them was a documentation failure: the file that would have prevented it already existed and nobody had said to read it. This manual exists so the next agent cannot repeat them.

Repo root: `C:/Users/jhffm/dnd-campaign`. All paths below are relative to it unless written absolute.

**Verified against the working tree at commit `51b1553` on 2026-09-06.** Where this manual states repo state (what exists, what is approved, what is blocked), that state was checked on that date and is dated in the text. When this manual and a repo file disagree, the repo file wins and this manual should be corrected in the same work session.

If you read nothing else, read section 1 (READ THIS FIRST) and section 10 (THE TRAPS).

---

## 0. What you are being asked to do, and the shape of the job

The DM (Justin) runs a family D&D campaign for his kids and is building it into a printed keepsake book. One session is designed per chat. The finished artifact of a session-design chat is:

1. An enemy roster file at `reference/campaign/session_NN_enemies.md`.
2. A validated simulator at `templates/playthrough_session_NN.py`.
3. A document builder at `templates/build_session_NN.py` that writes `sessions/session_NN_title.docx`.
4. An approved set of illustrations in `assets/session_NN/`.
5. Two edits to `templates/publish.py`, one row in `README.md`, and a numbered PDF at the repo root.
6. Canon written back into `memory/campaign_canon.md`.

Six stages, in order, with hard gates between them. The gates exist because skipping one has already cost real money or a full rebuild:

| Stage | Work | Gate before you may leave it |
|---|---|---|
| 1 | Canon check (read only) | You can state the party's level, kit, companion, and the session's beat in the endgame table without looking |
| 2 | Encounter design, written into the roster file | Every enemy card has an Actions block with attack bonus, dice, damage type, recharge and arrival timing, and every fight total re-derives from `sum(Count x HP)` |
| 3 | Simulation | A sweep lands on target: 3 to 4 knockdowns, zero deaths, zero wipes |
| 4 | The document | The QA loop (section 7.6) is clean AND you have looked at every page PNG |
| 5 | The art | The DM has approved every plate by letter; nothing moves into `assets/` any other way |
| 6 | Publish and write back | The numbered PDF exists at the repo root and canon carries the settled decisions |

Stages 4 and 5 may overlap once the roster is frozen, because the document can reference image paths that do not exist yet. Stages 1 to 3 cannot overlap with anything.

---

## 1. READ THIS FIRST

Read these before you touch anything. In this order. None of them is long. Today's failures were all "did not open the file that already had the answer."

| # | File | Why, in one line |
|---|---|---|
| 1 | `CLAUDE.md` (repo root) | The constitution: session numbering, party level, no em dashes, recency wins, never invent table events, never state a 2024 rule from memory |
| 2 | `memory/campaign_canon.md` | The document of record. Read lines 3 to 9 first (the lockdown protocol, which is the precedence rule), then the whole file |
| 3 | `memory/house_rules.md` | Six true house rules, the 2024 migration notes, and dated document rulings. The newest and most volatile file in the repo; it overrides the hero kits |
| 4 | `memory/session_log.md` | One paragraph per PLAYED session. It ends at Session 7, and that stopping point is how you tell table history from published plan |
| 5 | `templates/session_template.md` | The 53-line written spec of the house style, extracted from Session 7, including the 2026-08-18 combat-section directive |
| 6 | `assets/character_refs.md` | The character reference registry AND the standing art rules. Line 12 is the rule that cost 41 plates. Read it before writing a single art prompt |
| 7 | `assets/art_production_guide.md` | The era-split reference rule and the HARD-WON GENERATION LESSONS block |
| 8 | `reference/README.md` | The map of the rules layer, the order to consult sources in, and the wiki-through-the-browser procedure |
| 9 | `reference/campaign/lilly_kit.md`, `stabby_kit.md`, `ursa_kit.md` | What the party can actually do at level 7. Read the hero you are about to build a fight for, including the "Easy-to-forget checklist" at the bottom |
| 10 | `reference/campaign/session_09_enemies.md` | If you are on Session 9: the declared source of truth for every enemy. **Read the RECONCILER ADJUSTMENTS block at line 18 before any stat block**, because it overrides the counts and timings printed in the cards. If you are on a later session, read the whole file as the template for your own roster |
| 11 | `simulation/ENCOUNTER_VALIDATION.md` | The validation METHOD: what the metrics mean, what "right" looks like, and section 4, the ways this has gone wrong before. Read before running a sweep |
| 12 | `reference/campaign/sim_standing_rulings.md` | The ten rulings a combat sim must declare, and the arithmetic traps the audits keep catching |
| 13 | `templates/book_style.py` | The only rendering engine. 949 lines. Read it once, in full; it is the authority on every block signature, default size, page-break rule and colour |
| 14 | `templates/build_session_08.py` | The gold-standard builder. Read the head (lines 1 to 130), the Part Two opener (around line 727), the Running the Fight pattern (around line 1244), and each appendix opener (1552, 1818, 2012) |
| 15 | `templates/s9_art_plan.py` | The corrected art architecture: where each plate happens, who is in it, and `refs_for_plate()`. Its header is the post-mortem of the failure it prevents |
| 16 | `templates/s9_locations.py` | The best worked example of prompt discipline in the repo. Lines 13 to 30 record the DM's rejection of the second location pass and both of its causes |
| 17 | `templates/publish.py` | The `BOOK` list, the `BUILDERS` list, and the character-sheet merge |

Also read, from outside the repo (these are user-level memory files, not repo files):

- `C:/Users/jhffm/.claude/projects/C--Users-jhffm-dnd-campaign/memory/book-layout-standards.md` : the single most load-bearing document for layout decisions. Every sizing rule, the no-cropping ruling, the whitespace campaign, the railrow rule, and the DM's own words for each complaint.
- `C:/Users/jhffm/.claude/projects/C--Users-jhffm-dnd-campaign/memory/combat-objectives-not-rp-hooks.md` : why in-combat objectives land at this table and roleplaying hooks fall flat.
- `C:/Users/jhffm/.claude/projects/C--Users-jhffm-dnd-campaign/memory/art-requires-dm-approval.md` : the approval gate and the do-not-curate-the-queue rule.

Read when the topic comes up, not up front: `reference/expansions/artificer.md` and `druid-circle-of-stars.md` (the two subclasses not in the SRD), `lore/world_history.md` (additive world lore, safe to draw on, never table events), `reference/campaign/session_08_draft.md` and `session_08_part_two.md` (the model working-notes files), `simulation/README.md` and `simulation/HANDOFF.md` (the simulator's own orientation and open questions).

---

## 2. The quality bar

**Sessions 7 and 8 are the standard.** Session 7 (`sessions/session_07_gearhaven.docx`, published as `09_Session_7_Gearhaven_the_Clockwork_City.pdf`) is 54 pages and is where the house style was extracted from. Session 8 (`sessions/session_08_underroot.docx`, published as `10_Session_8_Underroot.pdf`) is 66 pages, 337 blocks and 64 distinct art assets, and is the file you copy.

A session of that ambition budgets roughly like this, from Session 8's actual pagination:

| Pages | Section |
|---|---|
| 1 | Title page and frontispiece |
| 2 to 24 | The recap and Part One, the read chapter |
| 25 to 39 | Part Two, the played chapter: the arrival scene and four numbered locations |
| 40 to 46 | The homecoming, rewards, threads left hanging |
| 47 to 51 | Appendix: the DM's Run Sheet |
| 52 to 59 | Appendix: the Board, the road events, and two full-page printable board halves |
| 60 to 66 | Appendix: Bestiary, every creature in play order |

What actually makes them good, stated so you can aim at it:

- **The prose is young-adult, not simplified.** Kid-safe content, adventurous tone, real stakes, never gruesome, but rich vocabulary and real sentence complexity. The youngest player already reads chapter books. `CLAUDE.md` is explicit that the content rating governs CONTENT and TONE, not reading level.
- **Natural storytelling voice.** `templates/session_template.md` closing line: "no aphorism chains, no trailer fragments; at most one turned phrase per section."
- **The page supports the DM; it does not script him.** Combat gets ambiance in, one terse Running the Fight pointer block, and a short exit read-aloud. Never a branching tree, never "if the party..." conditionals, never a tactics essay in a purple box.
- **Every creature the session names gets a card in the bestiary appendix.** The appendix is self-sufficient, including random-encounter mobs.
- **The art is on-model and it is of the place the players can see on the board.** Every hero in the frame has their reference attached; every location plate was written with the board map open and attached.
- **The document, the canon and the simulator agree.** They all read the same numbers and none of them validates the others, so drift is invisible until it is expensive.
- **Nothing touches text, page edges or the bottom margin, and there is never a blank or near-blank page.**

---

## 3. Which file wins: the precedence ladder

`memory/campaign_canon.md:6` states it, and it is binding:

1. Dated DM rulings in `memory/campaign_canon.md` (newest first).
2. The published volumes at the repo root.
3. `reference/campaign/*.md` working docs.
4. Anything older.

Four refinements that matter more in practice than the ladder itself:

**Recency wins inside a tier.** `CLAUDE.md` and `memory/house_rules.md` (DM 2026-07-05): the newer document is canon when two conflict, and clear inconsistencies get fixed silently rather than escalated. A dated bullet added to `house_rules.md` on 2026-09-05 overrides a kit file written 2026-07-25, even though the kit file is more specific.

**Canon deliberately delegates the numbers.** `campaign_canon.md:122` says outright that campaign_canon does not carry attack routines and that `reference/campaign/session_09_enemies.md` is the source of truth for the simulator and the session document alike. That is a delegation, not a demotion: for Session 9 stat blocks the working doc outranks canon by canon's own instruction. Apply the same pattern to any future session that gets its own roster file.

**A roster file can outrank itself.** `session_09_enemies.md` carries a **RECONCILER ADJUSTMENTS** block at line 18, dated 2026-09-05, which says in its own first sentence that it "override[s] the counts and timings in the stat blocks above". The stat blocks were written by five designers in parallel and the reconciliation pass that followed was recorded in the totals table but never carried back into the cards. **Read the reconciler block before you read a single card.** Its four overrides are in section 5.3.

**Plans versus history.** `campaign_canon.md:8`: session plans are canon-of-plan until played; table events are canon forever. Sessions 1 to 7 are history. Session 8 is a published plan that binds design but not history. Never write a Session 9 document that assumes a Session 8 table outcome; write it assuming the published Session 8 plan, which is what the DM will run.

**What is settled versus open.** `campaign_canon.md:9`: the complete list of genuinely open questions is the "Open DM decisions" section at the bottom of that file, plus the "Open threads" ledger above it. If a question is not in one of those two places, it is settled, and your job is to find the dated ruling, not to reopen it.

**Known live drift, verified 2026-09-06.** Do not be caught by these:

- `memory/campaign_canon.md` lines 123 to 126 still carry the pre-difficulty-bump Session 9 rosters and the superseded Kyogre 250 / Quiet Hand 120 numbers. The paragraph two lines above already names `session_09_enemies.md` as the source of truth. The real numbers are **280 and 150**.
- `templates/playthrough_session_09.py` carries a `[DM CHECK]` in its docstring saying Fight 2 reconciles to 580 with five Needlemaws. **That flag is now STALE.** The reconciler block settled it at four, holding 552. The simulator still runs five. See section 6.5.
- `reference/campaign/lilly_kit.md:29` says Lilly has two attunement slots free. The 2026-09-04 ruling and her live sheet both put her at 3 of 3 attuned (Pocket Dynamo, Wand of Web, Spell-Refueling Ring).
- `reference/expansions/druid-circle-of-stars.md` still prints the Cosmic Omen self-target question as an open `[DM CHECK]`. House rule 3, dated 2026-09-05, settled it: self-target is allowed.
- `characters/builders/PROVENANCE.md` and `characters/builders/README.md` both predate the timeskip and say the party is level 5. Trust the three `build_<hero>.py` files instead.
- The Drowning Lull SYNC LIST at the end of `session_09_enemies.md` is unapplied: `templates/build_compendium.py` lines 822 to 826 still hold the superseded sketch.
- `templates/playthrough_session_08.py`'s "Sources of record" docstring block (lines 10 to 14) still lists the PRE-retune numbers while the code runs the retuned ones.

---

## 4. Stage 1: Understand the campaign

Read only. Change nothing. You are confirming facts, not designing yet.

### 4.1 The party, at level 7

All three started at level 3 in Session 1, reached 4 after Session 3, 5 after Session 5, stayed 5 through Session 7 (Gearhaven), and returned at 7 after the one-year timeskip (`campaign_canon.md:39`). Session 8 onward is played at level 7. **Their path-reward doors are LOCKED. Do not present them as choices.**

**Lilly Glimmergear**, deep gnome Artificer (Artillerist), accent frost-blue `#1F6FB8`, Door C (Aether Channeler). HP 52, AC 20 (25 under Shield), Speed 25, INT 20, spell save DC 16, spell attack +8, slots 4x1st and 3x2nd, Flash of Genius x5, darkvision 120 ft. Signature weapon: Boomstick, a repeating pistol in brass and electric blue, built with her mother Poots during the year at home. True Strike through Boomstick is +10 to hit and uses INT for damage as well; her kit calls this the single most-dropped number. Her Eldritch Cannon fires on a Bonus Action, so she keeps her full Action every turn. Authority: `reference/campaign/lilly_kit.md` for the kit, `characters/builders/build_lilly.py` for her live prepared spell list.

**Stabby Sharpblade**, goblin Monk (Kensei through 5, Warrior of Beast Breathing from 7), accent candy-red `#A32B2B`, Door B. HP 59, AC 18, feature save DC 13, Nichirin katana +10 for 1d10+7, base Speed 45 (55 with the Sash, 65 while ignited), 7 Focus, Martial Arts d8, Extra Attack plus a Bonus Action unarmed strike, Evasion new at 7, Deflect Attacks 1d10+12. Cleansing Edge is his signature rider against corrupted enemies. **He has NO ranged attack at level 7, deliberately** (DM 2026-09-04): Lilly reclaimed his Repeating Longbow and reshaped it into a Spell-Refueling Ring. Authority: `reference/campaign/stabby_kit.md`.

**Ursa Catchum**, human Druid (Circle of the Stars), accent starlight-purple `#5B2A86`, Door B (Reader of Omens). HP 52, AC 18, Speed 30, WIS 20, spell save DC 16, spell attack +10 holding the Wand of the War Mage +2, Wild Shape 3/rest, slots 4/3/3/1, Staff 5 charges, Cosmic Omen 5 uses, Star Map 5 free Guiding Bolts. His combat doctrine is DM-fixed (2026-08-21): round one Bonus Action Starry Form Archer plus Action Conjure Animals; every round after, Bonus Action star-arrow plus Action Starry Wisp or a free Guiding Bolt; the pack rides his 30 ft movement for free. **He is the only hero with no darkvision**, which is why Daylight is prepared and why the Blackwater Seam is dim light rather than Darkness. Authority: `reference/campaign/ursa_kit.md`, Always-on section plus Door B only. Its Door C material is dead: Ursa has no Signature Partners, and Arcanine, Lapras and Noctowl remain free for companion design.

**Companions.** Ghostbloom (she), the fey companion, on her Level 7 card from Session 8 (AC 16, HP 62, Guardian's Light 2d8+3, DC 16). Puff, Lilly's fairy-sized homunculus, is permanent, shares Lilly's initiative and acts right after her, and sits outside the Sphere roster. Sandshrew, the Earth tank, joins at the Session 8 homecoming and is the companion FIELDED during Session 9. Piplup, the Water healer, arrives at the Session 9 homecoming; his statblock is at `reference/campaign/session_09_enemies.md:679`.

At the table: Jessica plays Lilly, the younger kid (6 almost 7) plays Stabby, the older kid (11) plays Ursa. Hero ages at Session 8: Ursa 9, Stabby 9, Lilly 8.

### 4.2 The campaign spine

Five planes (Fire, Water, Air, Earth, Shadow) turn like the gears of a clock, held in alignment by ANCHOR-STARS. Put a star out and the plane slips, a crack opens, and elemental Motes leak through that madden machines and mutate creatures. The home world is the hub and has no anchor of its own. Each fraying world has a corrupted GUARDIAN, its legendary creature. **Freeing rather than killing the Guardian closes that world's cracks**, and Ursa's Staff of Waking Constellations relights the anchor-star afterward. One designed companion comes home per elemental rift; one Mote is socketed into the Essence Sphere per plane (five sockets, one lit as of Session 8).

Star map (must match the Session 7 orrery plate at `assets/session_07/beat_3/orrery_reacts.png`): Fire/Ignis is Aldebaran, Water/Unda is Fomalhaut, Air/Aer is Vega, Earth/Terra is Antares (relit in Session 8), Shadow/Umbra is Algol (dark). Betelgeuse is the keystone, the lock on Maldrith's prison, not one of the five elemental anchors. Achernar is the reserve anchor, holding nothing. THE NAMELESS is a star crossed off the Circle's list so long ago nobody knows what world it held. The map is a scoreboard, not scenery.

Villains: Nyxthid, the Harbinger of Decay (he), is putting the stars out. Maldrith, the Weaver of Fractures (she), is imprisoned primordial entropy who put Elaria to sleep. Marked DM ONLY and LOCKED in canon: **Nyxthid is Ash Catchum**, Ursa's father, corrupted at the failing keystone about three years ago. The reveal is Session 12; he dies in Session 14 when Maldrith takes his body. The players already know the name Maldrith from the in-world verses; the name Nyxthid is first spoken in-fiction in Session 8's shrine vision.

Timeline: 1 to 7 played (level 3 rising to 5). 8 Underroot / Earth / Antares at 7. 9 Water / Fomalhaut at 7. 10 Fire / Aldebaran at 7 to 8. 11 Air / Vega at 8. 12 Shadow / Algol, the reveal battle, at 8 to 9. 13 the Sack of Gearhaven at 9. 14 the finale at Betelgeuse at 9 to 10. Sessions 9 and 10 are RACES, because both remaining lit anchors are already under attack; 11 and 12 are salvage.

**Session numbering is adjudicated and must not drift.** Gearhaven is Session 7. The chronicle runs 1 through 7 continuously with no gap. Never reintroduce a "Session 8 = Gearhaven" label (DM 2026-07-06, superseding a 07-05 call).

Two in-world years elapse between Session 1 and Session 8.

### 4.3 Rules discipline

**Never state a 2024 rule from memory.** `CLAUDE.md` and `reference/README.md` both say it; `reference/ATTRIBUTION.md` records why the folder exists at all: "Claude was stating 2024 rules from unreliable memory and getting them wrong." Named past failures: True Strike, Divine Order, Origin feats, firearm proficiency.

Consult in this order:

1. `reference/srd/` (14 files, 13,405 lines, a faithful CC-BY transcription of SRD 5.2.1). Grep it first. `reference/SRD_CC_v5.2.1.pdf` is authoritative if the markdown ever disagrees. Conditions and defined terms are in `14_rules_glossary.md`; core action and combat rules are in `01_playing_the_game.md`.
2. `reference/expansions/` for the non-SRD content this campaign uses: `artificer.md`, `druid-circle-of-stars.md`, `homunculus_servant.md`, `ring_of_spell_storing.md`, `wither_and_bloom.md`.
3. Anything not in either: read the actual page at dnd2024.wikidot.com. **WebFetch cannot reach that site**; it loops on the HTTP-to-HTTPS redirect. Use the in-app browser: `mcp__Claude_Browser__preview_start` with the url, then `navigate`, then `get_page_text`.

**Then cite what you used, with a date, inline.** The standard to meet is `session_09_enemies.md:513` ("verified 2026-09-05, dnd2024.wikidot.com/spell:thorn-whip") and `:743` ("read at dnd2024.wikidot.com/spell:slow on 2026-09-05 via the in-app browser... Slow does not appear in SRD 5.2.1, so cite the wiki and never the SRD for it").

**If you cannot verify it, write "unverified, check your PHB".** Do not fill the gap with recall.

Known SRD coverage gaps: the Artificer, most subclasses beyond the SRD samples, firearms, and the 2014-only Peace Domain. The wiki's UA and HB sections are off by default; only pull Unearthed Arcana when the DM asks.

**House rules override RAW and must never regress** (`memory/house_rules.md`): Starseed applies only to actual druid spells, never the Starry Form Archer arrow (it is +1d8 now that the Staff is awakened, and it is radiant-only, so it rides Guiding Bolt, Moonbeam and Starry Wisp but not Conjure Animals or Thorn Whip); Potent Spellcasting rides the kindled staff once per turn; Cosmic Omen may target Ursa himself; Cleansing Edge fires on a hit Stabby CHOOSES; Arcane Firearm's die attaches to one damage roll of the spell whenever that roll happens; burning webs deal 2d4 per creature per round, not per cube. And the 2024 migration notes: Patient Defense's free tier is Disengage (Dodge costs 1 Focus), eating a Goodberry is a Bonus Action, Shillelagh replaced Primal Savagery, deep gnome uses the current printing, the Eldritch Cannon picks its mode on every activation, the Air Bestial Spirit has 20 HP by its own stat block.

**Rules checking is part of encounter design, not a review step.** Two Session 9 decisions were made by a rules check and are recorded with their reasoning: Kyogre's Undertow uses a DEX save, not Strength, because Strength "would have failed ~85% of the time and bypassed Stabby's new Evasion"; and the Blackwater Seam is DIM light, not Darkness, because "Darkness would have Blinded the one hero without darkvision and switched off his whole kit" (`campaign_canon.md:122`).

---

## 5. Stage 2: Design the encounters

### 5.1 The design law, in the DM's own words

These are recorded rulings, not style suggestions. Violating one means the work gets thrown out.

**1. Fights are combat-first. Terrain is flavour, never the win condition.** `campaign_canon.md:122`, quoting him: "the combats should all be more combat focused and less environmental or surviving the terrain, especially the boss fight." An environmental and puzzle-led Session 9 draft was rejected outright. The rebuilt fights are "enemies with real attack routines, beaten in initiative, with terrain demoted to flavor and at most a small modifier." The Session 9 air-bells are the model of an allowed terrain feature: they exist so that combat happens on **standard footing**, because RAW underwater combat would gut the party's kits (SRD Underwater Combat, `reference/srd/01_playing_the_game.md:691`, checked 2026-08-18). Terrain that makes the fight possible is fine. Terrain that IS the fight is not.

**2. In-combat OBJECTIVES land. Roleplaying hooks fall flat. Keep roleplay out of initiative.** The governing note is `memory/combat-objectives-not-rp-hooks.md` (DM 2026-09-05, from watching the actual games). The clever line has to be something a player **does with a turn and can see working**: hit the right target with the right weapon, break the thing making the fight worse, take the enemy's hands off the job, free a captive so it leaves the board. An objective is legible on the board and pays off the same round; a social out asks a kid to invent dialogue under pressure and then wait to find out whether it worked.

Design smells to cut on sight: "Ursa uses Speak with Animals and the fight ends", "a successful Persuasion calms the herd", "the party can choose not to fight". **Close the off-ramp on the monster card, not in a DM note.** The Surgehorn's Blind Panic trait names Animal Handling, Animal Friendship, Speak with Animals and the Mark of Handling and says they all fail automatically (`session_09_enemies.md:60`). Roleplay is not cut from the session, it is moved: the advice scene, the day of rest, the epilogue.

Good worked examples, both Session 9: Stabby's Cleansing Edge frees a Bloodied Hollowsong, which leaves the fight alive and is still an attack roll in initiative; and taking the Quiet Hand's hands off the spike.

**3. Every fight fields FOUR OR FIVE enemy TYPES with distinct roles.** Session 8 shipped two per fight; the DM asked for more variety. Every card in `session_09_enemies.md` carries an explicit **Role:** line naming its job (skirmisher, anchor, ranged controller, chaff, the objective). Write that line before you write the stat block. If two cards' Role lines say the same thing, you have two types, not four.

**4. Guardians are FREED, not killed.** Kyogre's 280 is **Black Water**, not hit points: "The 280 is the corruption riding it, not its life. At 0 the corruption is gone and Kyogre is FREE. It is never killed, it never dies, no death saves are rolled for it, and no wound is ever described" (`session_09_enemies.md:415`). The rule reaches down the roster: Surgehorn "It Breaks Past" (at 0 it stumbles off alive, and you say so out loud), Blackfroth "Blackwash", Quiet Hand "It Does Not Die" (it comes apart into cold seawater and empty leather).

**5. Content kid-safe, prose young-adult, and no em dashes anywhere including code comments.**

**6. Balance is table-relative, and the DM prefers watch-and-see to pre-nerfing.** `memory/table-relative-balance.md`: score what these players will actually do, not RAW ceilings under optimal piloting. Flag only exploits that fire WITHOUT optimization; anything needing coordination or system mastery goes on a watch list.

**7. Every image needs the DM's yes, and you do not curate the queue down on his behalf.**

### 5.2 Where the design lives while you work on it

Write the roster into its own file: `reference/campaign/session_NN_enemies.md`. Its header states the contract, and the Session 9 wording is the model: "This file is the source of truth for every Session NN enemy, including the attack routines, which `memory/campaign_canon.md` deliberately does not carry. The simulator and `templates/build_session_NN.py` must both read from here so they cannot drift."

One card per enemy: a line of flavour, **Count**, **Role**, AC / HP / Speed, ability scores, resistances and immunities, senses, CR, Traits, Actions, Reactions, and an **Art brief** paragraph. Putting the art brief on the same card as the stat block is deliberate: it is what stops the art pass from inventing a creature.

**If a reconciliation pass changes counts or timings after the cards are written, carry the change back into the cards in the same edit.** Session 9 did not, and the result is the RECONCILER ADJUSTMENTS block: an authoritative override sitting above cards that still print the old numbers, which is exactly the drift shape the repo keeps paying for. If you cannot carry it back immediately, write the override block the way Session 9 did (stating in its first sentence that it overrides the blocks above) and fix the cards before the document is built.

Narrative working notes go alongside, on the `session_08_draft.md` / `session_08_part_two.md` pattern: an HTML comment header stating what the file is, which board it is played on, its CANON OBLIGATIONS as a bulleted list, and the house style reminder. When the builder overtakes a working note, put a SUPERSEDED banner on line 1 naming the date, the file that supersedes it, every number that changed, and "Do not cite this file for play." Nothing is ever deleted; superseded material moves to `_triage/` with `git mv`.

**Do not leave design source in `art_review/`.** That directory is gitignored (`.gitignore` line 7). The reconciled Session 9 art list, 15 KB of real design work, currently lives only at `art_review/_s9_art_list.txt` and is one clean checkout away from gone.

### 5.3 The difficulty method

**The anchor.** Session 8's retuned per-fight enemy hit point totals are the reference standard for a level-7 night. They were adopted 2026-08-18 off a 60-day playthrough sweep and are recorded in `reference/campaign/sim_standing_rulings.md`:

| Slot | Session 8 fight | Total | Composition (verified in `templates/playthrough_session_08.py`) |
|---|---|---|---|
| 1 | Mosslight Landing | 320 | 8 Rotbloom at 33 + 8 Mossmite at 7 |
| 2 | Chime Reef | 444 | 4 Chimestone at 78 + 4 Shardwing at 33 |
| 3 | The Glassed Gallery | 412 | Glass Weeper 340 + 4 Cinderoll at 18 |
| 4 | Groudon's Hollow | 430 | Groudon 230 + the Spike 160 + 4 Glasslings at 10 |

**The target.** Session 9 sits 20 to 30 percent above the anchor, slot for slot (`session_09_enemies.md:5-12`): 404 (+26%), 552 (+24%), 530 (+29%), 558 on the board (+30%).

**The Session 9 RECONCILER ADJUSTMENTS, authoritative over every stat block in that file** (`session_09_enemies.md:18-23`, 2026-09-05):

1. **Fight 2, Needlemaw: 4, not 5.** Five put the fight at 580 (+30.6%, outside the band) and twelve enemy bodies into the longest fight of the night in front of an eight-year-old. **Four holds the printed total of 552.** This SETTLES the discrepancy the surveys and `playthrough_session_09.py` both flag as open.
2. **The Kept collapse at the end of the SECOND round after they rise, not the third.** Removes three enemy turns and one Glassfall from the peak window.
3. **The second Drownbell arrives at the start of round FOUR, not round three**, so Hush and the Kept never stack.
4. **Kyogre's Legendary Action uses run 1 / 2 / 2 by phase, not 1 / 2 / 3**, and The Undertow Turns costs 2 of them, so phase one cannot buy one at all.

**Computing the total.** Sum `Count x HP` over every card in the fight, and print the working. With the reconciler applied, all four now re-derive:

- Fight 1: 8x13 + 3x68 + 2x28 + 1x40 = **404**.
- Fight 2: 2x126 + 4x28 + 3x32 + 2x46 = **552**.
- Fight 3: 152 + 4x38 + 3x22 + 2x40 + 80 = **530**.
- Fight 4 on the board: 280 + 150 + 4x22 + 40 = **558**.

**State your accounting convention every time.** The four Session 9 totals are not all counted the same way, and this IS still open (section 13). Fight 1's 404 includes the Blackfroth, which arrives at the top of round three. Fight 2's total includes the two Gullet Bells that also drop on round three. Fight 4 is labelled "558 on the board" and EXCLUDES the second Drownbell and the three Kept that rise later; counting everything that ever appears gives 748. Prefer "on the board at initiative" plus a separate "total that ever appears", and use the same convention for all four slots, or the deltas against Session 8 mean nothing.

**Computing incoming damage per round.** For each card, take the MAXIMUM of its damage line (not the average in parentheses), multiply by its Multiattack count, multiply by Count. Then subtract everything the card itself forbids on round one. The Session 9 roster front-loads those restrictions deliberately, and they are the actual balance mechanism:

- Surgehorn Blind Charge: "Recharge 5-6, never on round one".
- Inkmantle Ink Sting: never on round one, and "one lashes and one stings, never both stinging in the same round".
- Quillfrond Multiattack: "Two Quills. On round one it fires only one, because it is waking".
- Blackcask Pouring: "It takes no actions on round one".
- Quiet Hand At Work: no actions, no Reactions, rounds one and two; every attack against it has Advantage and it auto-fails saves.
- Kyogre Undertow and Drownbell Hush: UNCHARGED at initiative, first roll at the start of the second turn.
- Gullet Bells: they do not arrive until round three.

**The round-one worst case check.** Its purpose is one guarantee: **nobody is dropped before taking two turns.** Method:

1. Take each hero's maximum hit points from the simulator's `State.__init__` (`templates/playthrough_session_08.py:277-289`), which is the numeric authority for the party: Lilly 52 / AC 20, Stabby 59 / AC 18, Ursa 52 / AC 18, Puff 15 / AC 13, the Cannon 35 / AC 18, companion Sandshrew 78 / AC 17 or Piplup 45 / AC 13 or Ghostbloom 62 / AC 16. Add the standing temporary hit points the party walks in with; for Session 9 that is 13, because the Eldritch Cannon's Protector mode is re-picked on every activation and has no daily limit, so out of combat Lilly tops everyone up to the maximum roll. The floor is therefore 52 + 13 = 65.
2. Enumerate every enemy that can physically reach that hero on round one, given Speed, reach, and starting positions.
3. Assume every attack hits, every damage die rolls maximum, every save fails.
4. If the sum exceeds the floor, **do not lower hit points.** Add a targeting rule to a card so the damage cannot all land on one body.

Step 4 is the pattern to copy, and the Session 9 roster does it three times, saying so in the trait text:

- Brine-Thing **They Share**: "Two Brine-Things never grip the same creature. Each one goes for a different warm body. This is a hard rule, not a preference, and it is the structural reason no hero can be swarmed to 0 in a single round."
- Drownbell **It Lamps the Far Ones**: "It attacks the creature FARTHEST from Kyogre that it can see. This is a hard rule and it is why the round-one arithmetic works: it never piles onto the hero already in melee."
- Kyogre **It Is Not Aiming** (phase one): its Flukes strike the two creatures NEAREST it that it can reach, never the same creature twice in a round.

Worked example, the trench at round one (this arithmetic is a reconstruction from the cards, not a table recorded anywhere in the repo, and see OPEN item 12): one Fluke at max 3d8+5 = 29 on the nearest hero; the Drownbell is aimed at the farthest hero so it cannot stack; at most one Brine-Thing grips that same hero for max 1d8+3 = 11; with the reconciler's 1 / 2 / 2 legendary schedule, phase one cannot buy a Cold Squall at all. Peak on one body is 40 against a floor of 65. Undertow is uncharged and the Quiet Hand is At Work, so neither contributes.

**The standing rule: no enemy ever finishes a downed hero.** Every Session 9 card carries a flavoured version: Glimmerfin "Not Hunting", Surgehorn "It Does Not Finish", Pillarback "It Does Not Finish", Tanglehand "It Lets Go", Brine-Thing "Cold, Not Cruel", the Kept "Only What Fights Back", Kyogre "It Does Not Finish Them", the Quiet Hand "It Steps Over Them" ("It never attacks or targets a creature at 0 hit points. It steps over them and goes back to work. Say that out loud, flatly, the first time it happens"). Several cards tell the DM to say the rule aloud, because otherwise the kids assume the worst. Implement it once centrally in the simulator (`playthrough_session_09.py:272`, `_marks()`), and still write the flavoured line on each card so the DM has something to read.

**The expected outcome for a night** (`campaign_canon.md:122`): 3 to 4 hero knockdowns, zero deaths, and two moments where the table should believe it might lose. One short rest, after Fight 2, matching Session 8.

---

## 6. Stage 3: Validate with the simulator

### 6.1 What it is

`templates/playthrough_session_08.py` is the ENGINE: a 30x30 grid of 5 ft squares, Chebyshev distance, with real positions, initiative, movement, action economy and resource carryover across a whole night (long rest, four fights, one short rest after fight two). It defines `Actor`, `State`, `deal()`, `attack_roll()`, and every hero, companion, cannon, Puff and item routine. Roughly 4,600 lines.

`templates/playthrough_session_09.py` imports that engine wholesale by file path and defines **only what Session 9 changes**, in roughly 950 lines. Its docstring: "Nothing about the party's kit is re-implemented here, so any fix made to the Session 8 sim is inherited automatically." **That is the pattern for every future session: never fork the engine, extend it.**

The simulator now has its own documentation folder: `simulation/README.md` (orientation), `simulation/ENCOUNTER_VALIDATION.md` (**the method**, and section 4 is the catalogue of ways this has gone wrong before), `simulation/HANDOFF.md` (state of the work and open questions). Read ENCOUNTER_VALIDATION before your first sweep.

The archived Monte Carlo scripts `sim_session_07.py` and `sim_session_08.py` are superseded by the playthrough engine. Read them only for the pattern.

### 6.2 What it is for

Validating a session BEFORE it is written. It answers: does the difficulty curve run in the right direction, do fights take the right number of rounds, how many times does a hero go down, does anybody die, does the party ever wipe.

Its evidence has repeatedly overturned design decisions. From `sim_standing_rulings.md`: the Session 8 curve "ran backwards", the Gallery billed as hardest measured second easiest at 2.8 rounds and the boss at 1.6, with zero deaths in 60 simulated days and the spike broken 60 times out of 60. Root cause found by the sim: 52 percent of party damage is radiant or force, so every regeneration clause was auto-satisfied and the Weeper's Glassbound fired 0.00 times per day. That produced the retune this repo now treats as the anchor.

### 6.3 Running it

```
python templates/playthrough_session_09.py 1
```
One seeded day, full turn-by-turn log plus a contribution tally. Output is thousands of lines; pipe through `head`, `tail` or `grep` rather than reading it whole. The integer is the RNG seed.

```
python templates/playthrough_session_09.py sweep 200
```
200 seeded days, one summary line: net damage taken minus healed with a 95 percent confidence interval, mean total rounds, mean knockdowns, wipes. A verified `sweep 5` returned: `SESSION 9  n=5  taken-heal  634.6 +/-84.1  rounds 21.80  knockdowns 4.400  wipes 0`. Budget roughly a minute per 5 seeds.

```
S8_HPX=1.5 python templates/playthrough_session_09.py sweep 200
```
Scaling stress test (Bash tool only; PowerShell needs `$env:S8_HPX='1.5'` first). This is the knob that exposed the Chimchar companion trap: wipes per 200 days at 1.5x enemy HP were 15 for Chimchar and 0 for Piplup. Other knobs: `S8_DMGX`, `S8_SPIKE_HP`, `S8_SPIKE_REKNIT`, `S8_BODIES`, `S8_COMPANION`, and Session 9's own `S9_TEMP` (starting temp HP, 0 disables), `S9_SLAM` and `S9_WARD` (an A/B on what Lilly spends her shared pool on).

Session 8 has no sweep entry point of its own; drive it from a short script that imports it and calls `run_day(seed)` in a loop.

### 6.4 Declare the standing rulings

`reference/campaign/sim_standing_rulings.md` exists because the same errors kept recurring. A harness MUST declare them in its setup: Guardian Protocol is the Sentinel's own reaction so Lilly keeps hers; Evasion applies only to half-on-success effects; save-based damage ignores nonmagical-attack resistance; Ursa's +1 aura never applies to the Sentinel and never to Ursa himself; log stands-from-Prone; exactly one d20 per attack roll; opportunity attacks require sight; rider windows expire and are not banked across rounds; position tracking is mandatory or aura and reaction claims cannot be verified. The arithmetic trap worth memorising: **on a crit, double the dice then add the modifier ONCE.** That was dropped three separate times across the sim series.

### 6.5 The simulator traps

**The simulator can only simulate what canon actually records.** If an attack routine is not written down, the sim invents a placeholder and the results are meaningless while looking authoritative, confidence interval and all. Before a sweep, walk every card in the fight and confirm it has an Actions block with an attack bonus, dice, damage type, and stated recharge and arrival timing.

**Canon drift feeds the simulator.** Canon carried stale encounter numbers for a day and a separate simulator session faithfully simulated them. What caught the last one was arithmetic, not the sim: the roster's own correction note says "The 458 in particular never added up (Kyogre 250 + the Quiet Hand 120 = 370), which is what the simulator caught." Add the components; if they do not sum to the header total, stop and reconcile before running anything.

**The simulator can go stale against a settled ruling, and it currently is.** `playthrough_session_09.py` carries a `[DM CHECK]` saying Fight 2 reconciles to 580 because "the Needlemaw card's own Count line says five, and five is what runs here." The RECONCILER ADJUSTMENTS block settled that at four on 2026-09-05, holding the printed 552. **The flag is stale and the code is wrong by one Needlemaw (28 points).** Fix the count, delete the `[DM CHECK]`, and re-run the sweep before quoting any Session 9 balance number. Check the other three reconciler overrides (Kept collapse timing, second Drownbell arrival, Kyogre legendary schedule) against the code in the same pass.

**Implement from the cards, not from imagination**, and make the simulator's docstring list every trait it implements, the way `playthrough_session_09.py` does under "Implemented from the cards, not invented". That docstring is the audit trail that lets the next agent check the sim against the roster without reading a thousand lines of code. **Trust the code over its own header comments**: `playthrough_session_08.py`'s "Sources of record" block (lines 10 to 14) still lists the pre-retune numbers (Rotbloom 22 x6, Chimestone 52 x3, Weeper 115, spike 60) while the code runs 33 x8, 78 x4, 340 and 160.

---

## 7. Stage 4: Write the document

### 7.1 The mental model

A session document is not prose. It is a Python list named `BLOCKS` in `templates/build_session_NN.py`, where every element is a typed tuple, fed to `build_doc(BLOCKS, out_path)` from `templates/book_style.py`, which emits a .docx. **You never set a font, never set a colour, never open Word.** The engine owns every font, border, spacing value and page-break rule.

The .docx is then rendered to PDF through Microsoft Word COM (there is no LibreOffice on this machine and no fallback; `C:/Program Files/Microsoft Office/root/Office16/WINWORD.EXE` exists) and scanned by the committed instruments before anyone looks at it.

Python here is 3.14.3 at `C:/Users/jhffm/AppData/Local/Microsoft/WindowsApps/python`, with python-docx, Pillow, PyMuPDF (`fitz`), pypdf and reportlab importable. No virtualenv.

### 7.2 Complete block reference

Every kind `build_doc` dispatches on. A trailing `[, opts]` means an optional dict as the last element. An unrecognized kind raises `ValueError(f"unknown block kind {kind}")` at `book_style.py:945`, so a typo fails loudly.

**Structure and headings**

- `("titlepage", kicker, title, subtitle, note)` : centered star row, kicker 15pt bold ink, title 30pt bold goldenrod, subtitle 17pt bold sienna, note 9.5pt gray italic (a falsy note skips the paragraph). Always block 0. It does not force a page break of its own.
- `("h1", title[, opts])` : 16pt bold goldenrod with a thin goldenrod bottom rule, `space_before` 20pt, `keep_with_next`. Page-breaks before ONLY if the title starts with "Appendix" or `opts` carries `{"hardbreak": True}` (lines 298 to 302). **The key is literally `hardbreak`. `{"pagebreak": True}` on an h1 is read by nothing and is a silent no-op.**
- `("h2", title[, opts])` : 13pt bold sienna, `space_before` 11pt, `keep_with_next`. Supports `{"hardbreak": True}`, suppressed automatically when the heading already opens a page, so it can never mint a blank page.
- `("appendix_title", kicker, title, subtitle)` : always page-breaks. Centered gold kicker 10.5pt, crimson title 16pt, sienna subtitle 10.5pt. How every appendix opens.
- `("divider",)` : centered goldenrod star row, 10pt of air either side.
- `("pagebreak",)` : an explicit break run. Prefer `hardbreak` on a heading; an explicit break paragraph strands blank pages when repagination moves it.

**Voice boxes**

- `("gold", text)` : the read-aloud box. Fill `#FBF6EA`, 2.25pt goldenrod left rule, 10.5pt Georgia, indented 340 twips both sides. THIS IS THE STORY. A `\n` inside `text` becomes a soft break, so one gold block holds several paragraphs under one continuous parchment fill. That is how Session 8 writes multi-paragraph read-alouds.
- `("dm", text[, {"size": 9.5}])` : the DM box. Fill `#F4F0FA`, purple left rule, prefixed with a right-pointing triangle glyph. Table notes only.
- `("body", text)` : plain paragraph, 10.5pt, `space_after` 4pt. Used for run-sheet prose.
- `("bridge", text)` : italic connective paragraph, `space_before` 6 / `space_after` 10.
- `("hero", who, line)` : a suggested player line in a gold box, accent-coloured by `who.split(' ')[0].lower()` against `ACCENTS`, so both "Stabby" and "Stabby Sharpblade" resolve. The line is curly-quoted and italicized.
- `("lore", title, text)` : the deep-blue margin fragment, double-ruled, indented 500 twips, 9.5pt italic, small-caps kicker LORE OF ELARIA. Its declared source is `lore/world_history.md` only. **This is the designated page-tail filler.**
- `("melody", text)` : a sung verse, lines separated by `|` inside one string, each centered 12pt italic goldenrod, with a music note on the first and last. Campaign-original verses only; real carols are referenced by title plus performance directions, never lyrics.
- `("game", title, [lines])` : the teal double-ruled SET PIECE card (`#EAF4F3` fill, `#1F7A78` edge) for dice games, storm sequences, song seals, anything the table puts the book down and plays. Zero internal spacing, every line `keep_together` and chained `keep_with_next`, so it can never split across a page turn. An empty string in `lines` is an internal spacer.

**Images**

- `("img", path, caption, width_in[, opts])` : centered plate. `opts` supports `{"crop": "W:H"}` and `{"hmax": float}`. `hmax` defaults to 4.2 inches; the engine recomputes `w = hmax / aspect` whenever `w * aspect > hmax`, so asking for 6.5in on a tall image silently gives you something narrower. Pass `""` for no caption. The full-page printable board halves are `("img", path, "", 6.5, {"hmax": 8.7})`.
- `("imgrow", [(path, label), ...], width_each)` : a 2-row table, images on row 0 and captions on row 1. Per-image height hard-capped at 3.6in, side cell margins zeroed (Word's default 0.08in per side pushed wide rows past the right margin), captions given an 8pt gutter so two captions cannot read as one sentence. **This block cannot overflow the bottom of a page by construction**, which is why it is the recommended repair for a float that overflows.
- `("imgfloat", path, width_in[, "left"/"right"][, opts])` : an anchored square-wrap float with no caption; text AFTER the block wraps around it. Float default `hmax` 3.4in. Pinned to the anchor paragraph with no bottom clamp. Session 8 uses ZERO of these.
- `("railrow", rail_path, rail_w_in, [inner_blocks])` : ONE table row, text cell left and a stacked image rail right. Text cell width is `6.5 - rail_w - 0.22` inches. Carries `w:cantSplit`, so it moves to the next page whole. **Inner block kinds actually handled: `h2`, `gold`, `dm`. Any other kind falls through and renders `ib[1]` as plain body text.** No images, no cards, no nesting.

**Statblocks and cards**

- `("stat", title, [lines])` : the compact crimson box, title 11pt bold crimson then 9pt lines. Appendix quick reference.
- `("statblock", dict)` : a full 5e block with the portrait floated right and text wrapping around it. Keys: `name`, `type`, `ac`, `hp`, `speed`, `abilities` (dict keyed STR DEX CON INT WIS CHA with integer scores; modifiers computed), `cr`, `saves`, `skills`, `resistances`, `vulnerabilities`, `immunities`, `condition_immunities`, `senses`, `languages`, `traits` / `actions` / `reactions` / `legendary` as `[(name, text)]`, `img`, `img_w` (default 2.35, height capped 2.6in). The first 8 paragraphs are chained `keep_with_next` so a block cannot start in the last sliver of a page and sink its portrait off the edge.
- `("ua_stat", spec)` : the official summon-spell block anatomy (DM directive 2026-07-13). Keys: `name`, `type_line`, `top` as `[(label, text)]`, `abilities` as `[(ab, score_string)]` rendered as a six-column table with goldenrod header cells, `meta`, `sections` as `[(header, [(entry, text)])]`.
- `("fight_header", title, subline[, opts])` : centered crimson 13pt title over a centered gray 9pt subline. `{"compact": True}` lowers `space_before` from 16 to 10pt and drops the subline's `keep_with_next` so a fight can begin low on a page; `{"hardbreak": True}` forces a page break. Session 8's subline convention: `"<location> [star] Difficulty: <one phrase> [star] <roster>"`.
- `("enemy_cards", [card, ...][, {"pack": True}])` : 1 to 3 bestiary cards side by side, column width `6.3 / ncols` inches. Card keys: `name` (uppercased into the banner), `sub`, `img`, `img_w`, `crop`, `banner` (hex fill, default crimson `8B2020`; allies use teal `1F7A78`), `plate` (bool), `plate_w`, `stats` (rich-markup lines), `traits` / `actions` / `reactions` / `legendary` as `[(name, text)]`. A SOLO card with an image and `plate` not False renders the portrait as a big centered plate BELOW the statblock (landscape capped 5.7in wide and 3.5in tall; square or portrait floored at 3.0 and capped at 4.1). `plate=False` reverts to a right float capped at 3.4in. Multi-card rows center the image above the stats at `col_in - 0.15`, or `col_in * 0.5` with `pack=True`. The row is `cantSplit` UNLESS it is a solo plate card of 22 lines or more, in which case it may split and fill two pages instead of jumping wholesale. There is deliberately NO trailing spacer paragraph after the table.
- `("tactics", text)` : the line under a fight's cards. Bold crimson label then 9pt italic prose.
- `("reward_card", title, sub, [(item, desc), ...][, img])` : the gold sibling of an enemy card. Full width 6.3in, goldenrod banner and border, `cantSplit`, item names bold crimson. Optional trailing image capped 4.6in wide and 3.2in tall.

**Character-sheet blocks** (used by `build_sheets.py`, not by sessions): `("slots", accent_key, [(label, count), ...])` renders big filled pips, one row per slot level; `("spellref", accent_key, {"note": str, "levels": [(label, slots, [names]), ...]})` renders the Spells at a Glance tracker, with `slots` of 0 printing "at will".

`accent_key` indexes `ACCENTS` (`book_style.py:28`): `lilly` `#1F6FB8`, `stabby` `#A32B2B`, `ursa` `#5B2A86`, `ghostbloom` `#1F7A78`, `gold` `#B8860B`.

### 7.3 Inline markup

`_rich()` (`book_style.py:64`) splits on one regex and supports exactly three markups. Nothing else works and there is no escape syntax.

- `**bold**`
- `*italic*` (requires more than two characters between the asterisks)
- `{color:name}text{/}` where `name` is an `ACCENTS` key; renders bold in that accent colour
- `\n` becomes a soft line break

No markdown links, no headings, no lists, no tables. A literal asterisk in prose will be eaten. The house separator inside a `sub` or a `fight_header` subline is the four-pointed star glyph U+2726.

### 7.4 The document skeleton, as Session 8 orders it

- **Title page and frontispiece.** `titlepage` with kicker THE GUARDIANS OF ELARIA, title SESSION N, subtitle the session name, and the standing note "An illustrated adventure. Read the gold boxes aloud; the purple boxes are for the DM." Immediately followed by `("img", f"{S9}/frontispiece.png", <caption>, 6.2, {"hmax": 4.2})`.
- **The recap.** `("h1", "Previously, on The Guardians of Elaria...", {"hardbreak": True})`, three `gold` blocks recapping the previous session's endgame, then one `dm` block saying what level the party returns at and how the session is structured. (Session 1 opens with "Our story begins" instead.)
- **Part One, the read chapter.** `("h1", "Part One: ...")` with NO hardbreak so it shares the recap page. Then a `bridge` one-liner, a half-page plate, and alternating `h2` scene beats, `gold` narration, sparse `dm` notes, `img` plates at 6.2in, `imgrow` pairs, and `railrow` rows. Sub-headings inside Part One are `h1` without hardbreak so they flow. A per-hero level-up handout gets `{"hardbreak": True}` on its `h1` and on each hero's `h2`, so each hero starts and ends on their own page.
- **Part Two, the played chapter.** `("h1", "Part Two: ...", {"hardbreak": True})`, a `bridge`, a threshold plate, then a `dm` block pointing at the board appendix. Then the arrival scene (explicitly no encounter), then the numbered locations as `h2` headings reading "1. The Brightshoal: ..." and so on.
- **The homecoming.** `("h1", "The Way Home")` then `h2` beats for the aftermath, a `reward_card` for what the session gave them, an `h2` for what each hero carries home, an `h2` for threads left hanging, and a closing `lore` fragment.
- **APPENDIX: The DM's Run Sheet.** `("appendix_title", "APPENDIX", "The DM's Run Sheet", "Every DC, dial, and spotlight, in play order. Keep this page at your elbow.")`, then `h1` sections built almost entirely from `body` blocks: "The Shape of the Session" (the whole night as arrow-chained prose), "Fights at a Glance" (one paragraph per fight giving AC, HP, key attacks and THE LEVER in bold), "The Resource Picture", "Spotlights & Seeds", "Foreshadow Tracker", plus any session-specific rule teaching.
- **APPENDIX: The Board.** `appendix_title`, an `h2` "How the Board Works", the board image at 6.4in with `{"hmax": 4.1}`, then five or six `dm` blocks giving the movement rule, the dot-resolution rule, the fixed-location rule, the short-rest call, and the note on the numbers. Then `("h1", "The Road Between", {"hardbreak": True})` with the road events as `h2` entries, some inside `railrow` rows. Closes with a `lore` fragment and the two printable board halves as full-page `img` blocks at 6.5in with `{"hmax": 8.7}`.
- **APPENDIX: Bestiary.** `appendix_title`, then for each encounter IN PLAY ORDER: a `fight_header`, an `enemy_cards` row, and a `tactics` paragraph. Multi-type encounters go 2-up or 3-up; the boss goes solo full-width with a plate. Random-encounter mobs get their own trailing header and card row, because the appendix must be self-sufficient. Closes with a `lore` fragment.

### 7.5 The combat section shape (DM-adjudicated 2026-08-18)

Fixed. The DM runs combat live; the page supports him.

1. Ambiance read-alouds going INTO the fight.
2. Optionally ONE `dm` block offering 2 to 4 short character lines the kids can grab.
3. ONE `h2` "Running the Fight" made of terse `dm` pointers labeled in bold: **Battlefield** / **The pressure** / **The lever** / **Companions** / **Describe cues** (one line per big sensory beat) / **Scaling dials** (too easy / too hard). Boss fights add **The rescue**, **He does not finish them**, **Jobs**.
4. A SHORT `gold` exit read-aloud at the pivot out of combat.

**Never place a "when X happens, read the following" script inside combat.** Fold that imagery into a describe cue.

### 7.6 Layout rules and the QA loop

**The geometry, straight out of `build_doc`.** US Letter 12240 x 15840 twips. Left and right margins 1440 twips (1.00in). Top margin 1080 twips (0.75in, y = 54pt). Bottom margin 1300 twips (0.90in, content limit y = 727pt). Text band 6.5in wide, x = 72pt to 540pt. Page colour is parchment `#F9F2E2`. Note a documentation drift: `templates/session_template.md` says "0.75 inch top/bottom" while the engine sets the bottom to 1300 twips. **The engine wins**, and all the instruments are calibrated to it (`img_geom.py` uses `BAND_L, BAND_R, BOT = 72.0, 540.0, 727.0`).

**The layout rules, with the file that proves each:**

- **NO CROPPING** (DM ruling 2026-08-18, `book-layout-standards.md`): "you've cropped a lot of them, and I don't want them cropped." 3:2 sources run 6.2in wide; squares run full width, or 5.9in when that lets a header, a plate and text share a page, or side by side as an uncropped `imgrow` pair. The engine still supports `{"crop": ...}`; the style forbids it on story plates.
- **No centered image narrower than about 92 percent of the text band.** Justin: "either large enough to expand to the width of the page, or inline in text." `img_geom.py` flags below 90 percent.
- **No floating images in story flow.** `railrow` exists as "the engine-safe replacement for anchored floats" (`book_style.py:583`). Prefer `img`, `imgrow`, or `railrow`; reserve `imgfloat` for compact appendix contexts and re-run `img_geom.py` when you use it. Session 8 uses seven `railrow` blocks and zero `imgfloat`.
- **Packing comes from ORDER, not from crops.** Justin: "a lot can be accomplished just by changing the order of the picture and the text and you seem to avoid doing that." Proven moves: plate directly under the section header with text flowing after; the initiative or lines block before the battle plate; a plate after the first paragraph instead of the header when the header page is nearly full.
- **Major section headers start a page; minor subsections flow.** Parts, each hero path, each subclass get `{"hardbreak": True}`; minor sub-headers were deliberately de-hardbroken in the Compendium because they stranded whitespace. "A header stranded alone with its first card pushed to the next page is a bug."
- **Special playable mechanics are set pieces** and get the teal `game` card, never a small `dm` blurb. "Remember this is supposed to be a playable game."
- **Half-page landscape plates.** Openers and establishing shots run 5.6 to 6.2in; Session 8's standing plate is 6.2in with `{"hmax": 4.2}`. Villains get big showings. Creature and NPC floats run 2.9 to 3.3in.

**The QA loop, every time you change a session document:**

```
python templates/build_session_09.py
python templates/render_check.py sessions/session_09_unda.docx art_review/qa_s9 110
python templates/img_geom.py art_review/qa_s9/session_09_unda.pdf
python templates/ws_probe.py art_review/qa_s9/session_09_unda.pdf 30
```

Then READ THE PAGE PNGs in `art_review/qa_s9/`. `img_geom.py`'s own docstring says it plainly: "Instruments are triage, not signoff: eyeball every page before shipping." Only when all of that is clean do you run `publish.py`. A one-page smoke render through Word COM took 16.4 seconds on this machine, so budget minutes for a 66-page illustrated session.

Also run this lint the moment you finish editing BLOCKS, before spending minutes on a build:

```
python -c "import sys,os,re; sys.path.insert(0,'templates'); import build_session_09 as b; paths=sorted({x for blk in b.BLOCKS for x in re.findall(r'assets/[\w/.-]+\.(?:png|jpg|jpeg|webp)', repr(blk))}); miss=[p for p in paths if not os.path.exists(p)]; print('blocks',len(b.BLOCKS),'assets',len(paths),'missing',len(miss)); [print('  MISSING',m) for m in miss]"
```

It counts blocks and proves every referenced asset exists. Importing the module also proves the file parses. **This lint is the only thing that catches a missing card portrait**, because `book_style` silently swallows image failures inside `statblock`, `enemy_cards` and `reward_card` with a bare `except: pass`.

**What the instruments measure:**

| Script | Usage | What it catches |
|---|---|---|
| `render_check.py` | `python templates/render_check.py <docx> <out_dir> [dpi]` | Not a check, the conversion engine. `docx_to_pdf()` drives Word via PowerShell COM (`Word.Application`, `Documents.Open`, `SaveAs2(path, 17)`, 300s timeout, raises RuntimeError if "converted" is absent from stdout); `pdf_to_pngs()` rasterizes with PyMuPDF at 90 dpi default |
| `img_geom.py` | `python templates/img_geom.py <pdf>` | (A) images narrower than 90 percent of the text band that are not legitimate floats, (B) any image whose bottom passes y = 727pt, (C) an edge-hugging float with fewer than 12 words beside it. Images under 40pt either dimension are skipped; genuine side-by-side pairs are exempt automatically. Session 8 reports 0 / 0 / 0 |
| `ws_probe.py` | `python templates/ws_probe.py <pdf> [minpct]` | Per page: whitespace percent, blank flag, image count, largest image size, topmost heading and bottommost line, so a gappy page traces back to the block that caused it |
| `geom_audit.py` | `python templates/geom_audit.py <docx>` | Renders straight from the docx and reports margin violations (image bbox outside x 70.5 to 541.5, or below y 728), blank pages, and pages over 33 percent whitespace, without needing a book render |
| `montage.py` | `python templates/montage.py <docx> <outdir>` | A 6-column thumbnail contact sheet at `<outdir>/_montage.png` for fast eyeball review |
| `audit_embedded_art.py` | `python templates/audit_embedded_art.py` | Maps every image embedded in a docx back to its repo asset by perceptual similarity (Word recompresses, so hashes do not match). Flags images whose best match is outside the expected folder, and assets used more than once. Its `DOCX` constant is hardcoded to `sessions/session_07_gearhaven.docx`; edit it for another session |

**Reading `ws_probe` output as a diagnosis, not a score:**

- A page whose `top:` line is the MIDDLE OF A SENTENCE and whose whitespace is high is a spill. Live example in the shipped gold standard: `10_Session_8_Underroot.pdf` p63 reports `ws=91%` with no images, holding only the 499-character tail of the Fight 3 `tactics` paragraph after the 2-up cards filled p62.
- A page reported `ws=BLANK` that also reports a large image is NOT blank; it is a full-page plate. `ws_probe` decides blankness on text length under 15 characters, so Session 8 p58 and p59 (the printable board halves) report BLANK and are correct.
- A genuinely blank or near-blank page (over 85 percent, no image) is the worst outcome in this book: "NEVER create a blank or near-blank page; those are worse than a 40% tail."
- Around 35 percent on a text-full page that precedes an atomic plate is acceptable book rhythm. 40 percent or more mid-flow is not.

**How to trim a spill, in the order to try them. Never delete content to fix pagination.**

1. **Reorder** the plate and the text within the section. Costs nothing, and it is the DM's own first suggestion.
2. **Resize the plate** a step (6.2 to 5.9, or lower `hmax`) so header plus plate plus text share the page. Stay at or above 90 percent of the band.
3. **Fill the tail with a `lore` fragment** sourced from `lore/world_history.md`, or with additional approved art. This is the sanctioned filler and it is why the `lore` block exists.
4. **Split a long `gold` at a paragraph break**, especially inside a `railrow`, where the text must not outlive the rail image.
5. **Add or remove a `hardbreak`.** Add one when the preceding page ends more than 70 percent full; remove one from a minor sub-header that is stranding whitespace.
6. **Compact the cards.** `{"pack": True}` on `enemy_cards` shrinks minor-mob thumbnails to half a column; `{"compact": True}` on `fight_header` lets a fight begin low on a page.
7. **Only then, tighten the prose.** A `tactics` paragraph that spills should lose its restatements, not its rulings.

### 7.7 Writing the builder itself

Copy the skeleton of `templates/build_session_08.py`:

1. A header comment that is a **canon manifest**: bullet points naming exactly which adjudicated facts are baked into the document, each with its ruling date, each traceable to `memory/campaign_canon.md`. Session 8's has nine. Write this block FIRST; it is the checklist the document is graded against.
2. `sys.path.insert(0, os.path.dirname(__file__))` then `from book_style import build_doc`.
3. Path shorthands: `A = "assets"`, `S9 = f"{A}/session_09"`, `M = f"{A}/monsters"`.
4. `BLOCKS = [ ... ]`, one flat list.
5. A `__main__` guard that chdirs to the repo root and calls `build_doc(BLOCKS, "sessions/session_09_unda.docx")`. Because it chdirs itself, all asset paths inside BLOCKS are repo-relative and the script runs correctly from any working directory.

**Do NOT machine-generate blocks from design notes.** A regex parser that turns notes into blocks produces the right shape with none of the decisions (which beat gets a plate, which pointer is a `dm` line versus a describe cue, where the lever goes in the tactics paragraph) and the result reads as filler. If a session has genuinely repetitive tabular content, write a small helper that takes explicit per-creature dicts, the way `build_session_08.py` writes its `enemy_cards`, so the data is still authored rather than extracted.

---

## 8. Stage 5: Make the art

This is where the expensive mistakes happened. The pipeline has since been rebuilt to make them structurally impossible. **Do not bypass it.**

### 8.1 Stage 0: read before writing one prompt

In this order: `assets/character_refs.md` (the canonical look of every recurring character AND the standing negative rules), `assets/art_production_guide.md` (the HARD-WON GENERATION LESSONS section), and **the board map image itself**. For Session 9 that is `assets/session_09/unda_board.png` (4608x3072). Open it with the Read tool and look at it.

The last agent wrote location prompts without ever opening the board, twice. The DM's verdict is recorded verbatim at `templates/s9_locations.py:14`: "I don't think they match the map and look too much like the old design." Both halves were true.

### 8.2 The reference rule that cost 41 plates

`assets/character_refs.md` line 12, in full:

> **Attach a reference for EVERY hero in the frame.** Plate I of Session 8 came back off-model for Stabby and Ursa because the ref set was Ghostbloom, Aelwyn, Vane and Puff, with no hero refs at all. Describing them in the prompt is not a substitute. The per-request practical cap is about five images, so pick the five whose likeness matters most and describe the rest.

41 of 54 plates went out with no character reference at all and every person came back a stranger.

The fix is `templates/s9_art_plan.py`, and it is the file to copy for every future session. It declares, per plate, **where it happens and who is in it**:

- `LOCATIONS` : location key to approved plate file. Six new Unda rooms plus three already-approved Gearhaven rooms reused from Sessions 7 and 8 (`guild`, `tavern`, `rift_hall`; never regenerate an approved room).
- `CHARACTER_REFS` : token to file.
- `PLAN` : `plate_name -> (location_key, [character tokens])`.
- `MONSTER_LOCATION` : `plate_name -> location_key`. Creature portraits get the setting reference and no cast.
- `BOARD = "assets/session_09/unda_board.png"`, attached as the reference for every location plate.
- `STAGE1` : the six location keys that must be approved before stage 2 runs.
- `refs_for_plate(name)` : returns location first, then people, capped at five.
- `missing_locations()` : returns stage-1 plates not yet approved into `assets/`.
- `banked_path(name)` : where an approved plate landed, used by the runner's resume check.

```python
def refs_for_plate(name):
    if name.startswith("s9_loc_"):
        return [BOARD]
    if name in MONSTER_LOCATION:
        where, who = MONSTER_LOCATION[name], []
    elif name in PLAN:
        where, who = PLAN[name]
    else:
        return []
    out = []
    if where:
        out.append(LOCATIONS[where])
    out += [CHARACTER_REFS[c] for c in who if c in CHARACTER_REFS]
    return out[:5]
```

The seven registered Session 9 characters, all verified present on disk:

| key | file |
|---|---|
| lilly | `assets/art_refs/REF_lilly_6_level7.png` |
| stabby | `assets/art_refs/REF_stabby_4_level7.png` |
| ursa | `assets/art_refs/REF_ursa_4_level7.png` |
| sandshrew | `assets/characters/sandshrew.png` |
| piplup | `assets/companions/piplup.png` |
| aelwyn | `assets/art_refs/REF_aelwyn.webp` |
| puff | `assets/art_refs/REF_homunculus.png` |

**Professor Aelwyn Ravenstone is a tall silver-haired HIGH ELF with emerald eyes.** He is not an elderly human. He has had a reference on file since the Session 2 art. `templates/batch_art_s9.py` line 47 now carries the correction inline: "He is an ELF, not the human I briefly invented for him." The wrong description is still sitting in the `s9_aelwyn_and_the_reed` scene line in that file, which calls him "the elderly scholar"; fix it when you touch that plate. `campaign_canon.md:19` also lists "elderly man with a silver beard" in the canonical-names table as an error to fix on revision.

**Hero references are ERA-SPLIT** (`assets/art_production_guide.md` step 2): EARLY (S1 to S3, no relics), LATER (S4 to S7), TIMESKIP (S8 onward, the `_level7` set). Never attach a later ref to an earlier scene. Each hero has four level-7 variants: `_level7` (portrait, the default), `_level7_fullbody` (action and scene plates), `_level7_painted` (should read hand-made), `_level7_model` (flat costume sheet, cleanest source). `CHARACTER_REFS` currently points at the portrait for all three; consider swapping in the fullbody variant for a full-body action plate. From Session 8 on, attach each hero's signature item alongside the portrait: `assets/items/boomstick.png`, `nichirin_katana.png`, `staff_of_waking_constellations.png`, plus `REF_homunculus.png` whenever Puff is in frame.

**Recurring NPCs with canonical refs** (all under `assets/art_refs/`, 48 files in that directory): Aelwyn (`REF_aelwyn.webp`), Guildmaster Vane (wild-haired old human inventor with brass goggles), Quill (elegant silver Mechagnome archivist), Elaria (starlight-and-vine goddess with a seven-point star at the brow), Nyxthid (hooded shadow herald, unnamed to the party until late), Davy Jones, the Krampusshade, Faelan, Ash Catchum, Puff, Skitch, Pikachu, Poots Glimmergear, Captain Brynn Wavewarden, Maera, Ghostbloom, Floraburst, Lickgloom, plus `REF_piplup.png`, `REF_chimchar.png` and four Togekiss refs. **Documented gaps** (recur but have no portrait yet): Henna Brasspot, Burl, Mara Sprocket, Tock, Pinion, all Gearhaven hub regulars from Session 7 on. The registry's instruction is to crop from existing Session 7 scenes if they recur.

### 8.3 The standing negatives that reference images will NOT enforce

`assets/character_refs.md`, DM ruling 2026-08-17: "Reference images alone will not enforce them: the generator copies jewelry it sees in the refs, so the older refs actively work against these rules and the prompt has to override them." State these as explicit negatives in every prompt:

- Lilly wears exactly ONE small earring on one ear; her other ear is bare. Stabby and Ursa wear NONE, both ears completely bare.
- Boomstick is brass with an ELECTRIC BLUE chamber, never orange or amber. Always attach `assets/items/boomstick.png`.
- Lilly does NOT wear a glowing sphere on her chest.
- Stabby holds the katana TWO-HANDED, dominant hand under the guard, tip up, and the glow is on the OUTER convex cutting edge. Inner-edge glow reads as holding the sword upside down.
- Ursa does not carry the Sigil-Stone in every shot; elsewhere his off hand is empty.
- Ghostbloom is a FOUR-LEGGED chubby translucent teal quadruped with a flame-like bloom of leaves from her back. Not a wisp, not a jellyfish, not a floating fairy.
- Puff's ears are upright triangles with blue inner faces, and she is never larger than Lilly's head.

And: **search `assets/` before generating any reference.** Lickgloom had canonical art at `assets/monsters/lickgloom.png` since Session 1 and a duplicate was generated anyway, in the wrong colours. Grep `monsters/`, `npcs/`, `characters/`, `items/`, `companions/` and `art_refs/` by name first.

### 8.4 Prompt discipline: seven rules learned the hard way

Every prompt is assembled as `STYLE + " " + blocks_for(tokens) + " " + scene` in `batch_art_s9.gen_one`. `STYLE` (line 28) asks for a "lush warm golden palette", and that single string caused a whole failed pass.

1. **State the setting first, not in a clause.** `s9_locations.BELL` opens with "THE MOST IMPORTANT THING ABOUT THIS PICTURE: the viewer is standing in AIR, not underwater." Unda's defining feature is domes of air on the seabed with the sea held back overhead as a wall, not a medium. Two passes painted ordinary underwater photographs because the fact sat in a subordinate clause. `s9_monster_queue.py` does the same with its `UNDA` prefix, which opens all 22 creature prompts.
2. **A later instruction must explicitly override an earlier one.** `s9_locations.PALETTE` begins "PALETTE, and this overrides any earlier instruction about a warm or golden style: this world is COOL" and then names the forbidden result: "Do NOT paint honey-gold sand, amber sunbeams, warm golden caustics or a tropical-postcard reef." Without it, all six locations came back drenched in honey gold because STYLE runs first and nothing argued back. The board's actual colours are turquoise, jade, petrol blue, bone-grey sand, olive and rust coral, acid-olive kelp, and a nearly black trench.
3. **State scale in words the model cannot draw as a prop.** Every monster prompt carries a clause of the form "It is HUGE, roughly twenty-five feet across, and the picture must make that size unmistakable by showing it against the reef, the sand and the water wall for scale", and the `UNDA` block adds "never a built object". The first monster pass was built from one-line summaries with no size and no setting and came back at wild scales against the wrong plane.
4. **Forbid people and buildings explicitly when a plate should be empty.** `s9_locations.EMPTY` is a 90-word negative: no people, figures, humanoids, silhouettes, faces or creatures; no city, town, buildings, towers, spires, domes, houses, ruins, statues, bridges, roads, walls, boats, ships, docks, lanterns, furniture or machinery. **A location plate is the room, not the scene.** Unda has never been built on by anyone.
5. **Forbid the composition you keep getting.** `BELL` ends with "Do not default to a symmetrical view straight down a bright sand avenue with an arch of water across the top of the frame; that is the wrong picture and it has been made too many times already." Then every location carries its own explicit `CAMERA:` sentence: height, direction, what fills the frame, where the horizon sits.
6. **No text or lettering, ever.** STYLE ends with it. House style carries meaning through the heroes' accent colours instead.
7. **A safety rejection is not a verdict on the subject.** `gpt-image-2`'s filter rejects innocuous prompts. The Lapras plate needed its "prompt loosened after an IP-moderation block" (`assets/image_manifest.md` line 249). A rejection surfaces only as an `ERR <message>` line in the batch output, because `gen_one` returns `f"ERR {message}"` whenever the response has no `data` key, and it is easy to scroll past in a 55-line run. Reread for ERR lines, reword (soften a violence word, drop a proper noun that reads as IP), and rerun that one plate with a substring filter. Do not silently drop it.

### 8.5 Plate dimensions: 1536x1024

Generate every book plate at 1536x1024 (3:2). `batch_art_s9.py` already defaults to it (`SIZE = os.environ.get("GENART_SIZE", "1536x1024")`); every Session 8 plate on disk is exactly that size.

The reason is the book layout, not the API. `book_style.py:858` decides plate treatment with `landscape = ppw >= pph * 1.15`. Landscape art becomes a wide half-page plate (capped 5.7in wide, 3.5in tall); square or portrait art becomes a narrower centered figure that strands whitespace and can orphan the following intro line. 1536x1024 is a ratio of 1.50, comfortably clear of the threshold, and generating at 3:2 means never needing the `crop="4:3"` legacy rescue. `genart.py` defaults to 1024x1024 and legacy `batch_art.py` hardcodes it; set `GENART_SIZE=1536x1024` when using `genart.py` for a book plate. Reference portraits in `art_refs/` are 1024x1024, which is fine: they are inputs, not plates.

### 8.6 The two-stage pipeline, and its gate

**Stage 1: locations first, board attached, approved before anything else.**

```
python templates/batch_art_s9.py --locations
```

Six location plates from `templates/s9_locations.py`, board map attached as the reference. Writes `art_review/PENDING_s9_loc_*.png`. Approve them, bank them into `assets/session_09/`, and only then does stage 2 unlock.

**Stage 2: everything else, each plate carrying its approved location plus every person in frame.**

```
python templates/batch_art_s9.py
```

`batch_art_s9.py` lines 178 to 188 call `s9_art_plan.missing_locations()` and hard-exit with a printed STOP block if any of the six is unapproved. **That gate is correct. Do not remove it.**

**State as of 2026-09-06 (commit `51b1553`): all six locations are approved and banked into `assets/session_09/`. `missing_locations()` returns `[]` and stage 2 is UNLOCKED.** The banked files are `s9_loc_blackwater_seam.png`, `s9_loc_brightshoal.png`, `s9_loc_guardians_trench.png`, `s9_loc_kelp_cathedral.png`, `s9_loc_open_water.png`, `s9_loc_rift_gate.png`, alongside `unda_board.png` and its print splits. Confirm this yourself with the command in section 12 before spending money; do not take this paragraph's word for it.

Flags and behaviors:

- A bare first argument is a substring filter on the plate name: `python templates/batch_art_s9.py loc_` or `mon_`.
- **Resume is the default**, and as of `51b1553` it checks BOTH places: a plate is skipped if `art_review/PENDING_<name>.png` exists OR `s9_art_plan.banked_path(name)` finds it already approved in `assets/`. The second check was added because approving a plate used to move it out of `art_review` and the next run helpfully regenerated the thing the DM had just signed off on. Only an aggregate "resuming: N already generated" line is printed.
- **A rejected plate must be MOVED OUT of `art_review/`**, not just re-requested; leave it in place and the rerun silently skips it.
- `--force` regenerates plates that already exist. Costs money for everything in scope; prefer a substring filter alongside it.
- Every composed prompt is written to `assets/gen_prompts/<name>.txt` BEFORE the request fires, so the prompt is on disk even if the image fails, and so `approve_art.py` can cite it in the manifest. That directory holds 299 files today.
- Concurrency is split: ref-free plates run 10 concurrent, plates carrying references run 3, because only ref-carrying requests hit the org's input-images-per-minute cap. Now that almost every plate carries at least a location reference, expect the batch to run at 3 wide and take proportionally longer. That is correct behavior, not a bug.
- Reference paths are filtered through `os.path.exists` **silently** (`refs_for()` line 134). A typo drops that reference with NO warning and the plate comes back off-model looking exactly like a plate that was never given a reference. The five-image truncation in `refs_for_plate` is silent too: list six people and the sixth is discarded. Audit before spending money (section 12).

### 8.7 Review, approve by letter, bank

1. `python templates/review_gallery.py` writes `art_review/review.html`: a self-contained board with every `PENDING_*` image inlined as a base64 JPEG data URI and lettered A, B, ... Z, AA, AB by position in the sorted list. Base64 stays on disk and never enters model context. Image size scales down as the board grows (1300px at 8 or fewer, 900px to 20, 620px beyond) because multi-image boards at 2000px exceed roughly 8 MB and can fail to load in the artifact viewer. Approved images are deliberately excluded (`done = []`): the board shows only what still needs a decision.
2. Publish `art_review/review.html` as an Artifact, or hand the DM the file. Then **WAIT**.
3. The DM approves by LETTER. `python templates/approve_art.py A B C` reads `art_review/_letter_map.json`, moves only the named plates into `assets/` by name prefix, and appends a row to `assets/image_manifest.md` recording the destination, the letter, and the prompt file. Case-insensitive, tolerates trailing commas, prints NOT FOUND for letters it cannot resolve.
4. `python templates/approve_art.py --list` prints the current letter map without moving anything.

`dest_for()` routes by prefix: `s9_*` to `assets/session_09/`, `S8mon_*` to `assets/monsters/` (with the `S8` stripped), `S8_*` to `assets/session_08/`, `mon_*` to `assets/monsters/`, and anything else falls back to `assets/session_09/`. Both the `s9_` rule and the fallback need editing for Session 10.

**Rejection has no script.** Move the file out by hand: `mv art_review/PENDING_<name>.png art_review/_superseded/`. Never delete (per `CLAUDE.md`). As of 2026-09-06 that directory holds 94 rejected plates and `art_review/_approved_archive/` holds 22; there are no `PENDING_*.png` files at the top level.

**EVERY image needs the DM's yes.** `approve_art.py`'s own header: "Nothing here decides anything: approval is the DM's, and a plate stays in art_review/ until he says a letter out loud." Do not curate the queue down on his behalf: build everything the plan calls for, publish all of it, and move only the letters he names.

### 8.8 Repair, do not re-roll

An approved plate is a DM-approved composition and a re-roll loses it. Two repair tools:

- **Whole-image edit.** Pass the finished plate to the images edits endpoint with a tight instruction that changes one thing. Proven on 2026-08-17 (the earring pass) and 2026-08-18 (all four Session 8 battle plates, where edits fixed off-model characters and then reframed the composition wider). Edit prompt templates live at `assets/gen_prompts/_earring_removal_edit_template.txt`, `_sphere_removal_edit_lilly.txt` and `_puff_scale_edit.txt`.
- **Region inpaint.** `python templates/inpaint.py <src.png> <out.png> <prompt_file> x0 y0 x1 y1 [more rects...]` where the rect coordinates are FRACTIONS of width and height so they read the same at any resolution. It builds an RGBA mask (opaque means keep, transparent means repaint), posts both to the edits endpoint, and resizes the result back to source size if the API returns different dimensions.

Cautions: never run two edits on the same file concurrently; the provider has refused edits on some hero images before, so log holdouts rather than forcing them; and run `python templates/audit_embedded_art.py` after any batch that touches embedded session art.

**Check hands whenever a plate is enlarged.** The v1 Pikachu plate gave Ursa two right hands and a raised hand with no forearm; nobody noticed until it went from 4.1 to 5.8 inches. Chirality test: with the BACK of a hand toward the viewer, a LEFT hand's thumb sits on the viewer's left. Spell the intended hand out per-hand when a figure holds something.

### 8.9 Rate limits are not errors

The org caps input images at about five per minute, so ref-heavy queues trip 429s constantly. `templates/genart.py` has the better retry: a `RateLimited` exception carries `retry_after` parsed out of the API message with `re.search(r"try again in ([\d.]+)s", ...)`, and rate limits get their own budget (`rate_limit_attempts=8`) that does NOT consume one of the three real attempts; connection errors and timeouts get 3 attempts with 5s / 10s / 15s backoff. `batch_art_s9.gen_one` sleeps `retry-after + 5` and RECURSES on itself with no attempt ceiling; it works, but a sustained rate limit will recurse indefinitely rather than fail loudly. Port the `genart.py` pattern when you touch it. Timeouts: 900 seconds per request in `batch_art_s9.py`, 600 in `genart.py` and `inpaint.py`. The API key lives at `~/.openai_key` and never in the repo.

### 8.10 Porting the pipeline to Session 10 (Fire rift, Chimchar)

Copy, do not generalize.

1. Build the board map first. `templates/build_rift_board.py` header lines 16 to 18 explain the reskin: copy the config, swap the backdrop, the location medallions and the winding waypoints. Output to `assets/session_10/<plane>_board.png`.
2. Copy `s9_locations.py` to `s10_locations.py`. Rewrite `PALETTE` from the new board by reading the actual colours off the image, rewrite the setting-defining block that replaces `BELL` for the new plane's physics, keep `EMPTY` almost verbatim, and write a per-location `CAMERA:` sentence for every one.
3. Copy `s9_art_plan.py` to `s10_art_plan.py`. Update `LOCATIONS`, `STAGE1`, `BOARD`, `CHARACTER_REFS` (swap piplup for chimchar: `assets/companions/chimchar.png`, ref `assets/art_refs/REF_chimchar.png`), and **hand-write `PLAN` and `MONSTER_LOCATION` row by row** from the finished session design.
4. Copy `batch_art_s9.py` to `batch_art_s10.py`. Update the imports, `STYLE` if the plane's palette demands it, and `BLK`. Keep the stage gate, the two-place resume check, the split concurrency pools and the 1536x1024 size.
5. Edit `approve_art.py` `dest_for()` to route `s10_*` to `assets/session_10/` and change the fallback.
6. `review_gallery.py` needs no changes.

Commit the generator and its output together, in one commit, the same session.

---

## 9. Stage 6: Publish and write back

### 9.1 publish.py

`python templates/publish.py` does three things in order:

1. `rebuild_sources()` runs every script in `BUILDERS` as a subprocess and prints `[ok]` or `[FAIL]` per script. **Session 7 is absent on purpose** and must stay absent.
2. `render_book()` walks the `BOOK` list of `(source docx, root PDF name)` pairs and renders each through Word COM. Missing sources print `MISSING` and are skipped rather than aborting.
3. `merge_char_sheets()` appends the three `characters/*_sheet_v3.pdf` files to the Compendium PDF with pypdf. **It does not rebuild them**: the comment there says sheet rebuilds are deliberate, reviewed events, not a book-render side effect.

`python templates/publish.py --pdf-only` skips step 1.

The current `BOOK` runs 01 Foreword, 02 The World of Elaria, 03 to 10 Sessions 1 through 8, 11 The Compendium. `BUILDERS` runs foreword, lore, sessions 01 to 06 and 08, then `build_compendium.py`, `build_bestiary.py`, `build_compendium_full.py`.

### 9.2 The four explicit edits that add a session to the book

1. Write `templates/build_session_09.py`, reading its enemy numbers from `reference/campaign/session_09_enemies.md` and its art from approved files in `assets/session_09/`, writing `sessions/session_09_<stem>.docx`.
2. Add `"build_session_09.py"` to `BUILDERS` in `publish.py`, after `build_session_08.py` and before the compendium builders.
3. Add `("sessions/session_09_<stem>.docx", "11_Session_9_<Title>.pdf")` to `BOOK` and RENUMBER the compendium from `11_The_Compendium.pdf` to `12_The_Compendium.pdf`. Renaming a shipped PDF means `git mv` on the old file, per the repo's destructive-operations rule. The Compendium is always last.
4. Update `README.md`. Its markdown table IS the table of contents. Add a row `| 11 | [Session 9: <Title>](11_Session_9_<Title>.pdf) | <one-line teaser> |` and bump the Compendium row to 12 with its link updated. Keep the teaser in the voice of the existing rows: one clause naming the place and the turn of the story, never a spoiler summary. Compare row 10: "The reunion after the year apart, the first rift run, and the freeing of Groudon".

**Editing only one of `BUILDERS` and `BOOK` fails silently.** A builder absent from BUILDERS never runs; a docx absent from BOOK never renders, and the only signal is a `MISSING` line scrolling past.

### 9.3 What gets written back into canon

`memory/campaign_canon.md` lockdown protocol (lines 3 to 9) governs how you edit it: every change is a dated DM ruling with no undated edits; a new ruling that touches an old one names it; nothing is deleted, overturned material moves to the "Superseded lore" section; session plans are canon-of-plan until played.

A settled session writes back:

- **The design block**, beside the other session design blocks (see `campaign_canon.md:120` and `:122` for the two Session 9 models). It carries: the locations, the board file and its space count, the terrain ruling and the rules source it was checked against, the per-fight enemy HP totals with the delta against the Session 8 anchor, the number of enemy types per fight, expected knockdowns and deaths, where the short rest falls, and **a pointer to the roster file for the attack routines canon deliberately does not carry.**
- **The timeline row** in "Session and level timeline", with the level and a summary anchor.
- **New locations** into the "Locations gazetteer".
- **New or changed NPCs** into the "NPC roster".
- **New items, relics or discharges** into "Major items and relics". A printed-text grant ships with its own **SYNC LIST** naming every file that must change in the same commit; see `session_09_enemies.md:735` for the model, including the note "This is a publish-affecting edit: the Compendium PDF changes."
- **Foreshadowing** into the "Open threads" ledger with its planned payoff session. Session 9 plants three silent ones: the case with five loops and three empty (the three spent spikes are Vega, Algol and Groudon's), the spike carved with the same half-finished sign of Elaria as Ash's Sigil-Stone, and Stabby's idol going cold and pulling toward the trench.
- **Anything genuinely undecided** into "Open DM decisions", which is explicitly the complete list.
- **Anything overturned** into "Superseded lore", with the reason and a SUPERSEDED marker left in place rather than a deletion.

**The split that must be preserved: canon carries the design decisions, the roster file carries the attack routines.** Duplicating stat lines into canon is what produced the current drift. Cite the roster file by path rather than restating its numbers; if you must restate, restate only the fight totals and add the components to check they sum.

**Also append an entry to `memory/session_log.md`**, 5 to 10 lines, newest last, after the session is actually played.

**Update canon in the SAME work session as any design change.** A stale encounter total sat in canon for a day and a separate simulator session faithfully simulated it.

### 9.4 Committing

Per `CLAUDE.md`: commit at the end of every work phase with a descriptive message, and push. Commit messages here are prose sentences, not conventional-commit prefixes, and they name the ruling: "Daylight lights a place, not a person"; "Session 9's enemies get their real numbers written down"; "Session 9's six locations are approved, and the roster stops contradicting itself". Match that style, and use the body to explain what changed and why.

Per `memory/commit-generated-code-artifacts.md`: **the generator and its output go in the same commit**, and the script's Status or header comment is updated the same session anything changes. A deliverable newer than its committed generator is a defect.

---

## 10. THE TRAPS

Every one of these is an expensive mistake that has already been made in this repo. Stated as a rule, with the reason, and the thing to do instead.

### Art

**1. Never generate a plate containing a hero, companion or named NPC without attaching their reference image, no matter how well the prompt describes them.**
Why: `assets/character_refs.md` line 12 ruled on this in August. 41 of 54 Session 9 plates went out ref-free and every person came back a stranger. Session 8's Plate I came back off-model for Stabby and Ursa for exactly this reason.
Instead: let `templates/s9_art_plan.py` decide. Every plate has a row in `PLAN` or `MONSTER_LOCATION` giving `(location, [people])`, and `refs_for_plate()` returns the location plate first then each person's ref, capped at five. If you add a plate, add its PLAN row in the same edit. If more than four people are in frame, attach the four whose likeness matters most and describe the rest.

**2. Never write a location art prompt without opening the board map image first.**
Why: the DM's verdict on the second Session 9 pass was "I don't think they match the map and look too much like the old design." Both halves were true. The board is the plane's colour language and its geography, and the players will have it on the table all night.
Instead: Read `assets/session_09/unda_board.png` and the `UNDA` config in `templates/build_unda_board.py` before writing a word. Write `PALETTE` by naming the colours you can actually see. Keep both mechanisms in `s9_locations.py`: the board attached as a reference, and the PALETTE string that explicitly overrides the warm-gold STYLE line.

**3. Never describe a registered character from memory.**
Why: Aelwyn Ravenstone was written into prompts as an elderly human. He is a tall silver-haired high elf with emerald eyes and has had a canonical reference on disk since the Session 2 art. The registry is 90 lines and takes a minute to read.
Instead: look every named character up in `assets/character_refs.md` and copy the description from the row. If they are not in the registry, that is itself information: they have no canonical look yet, and once the DM approves their first portrait it becomes their ref and gets a row.

**4. Never build an art queue by regex-parsing design notes.**
Why: `templates/s9_build_queue.py` does exactly this and its own comments record the failure. The detector attaches refs only when a hero is literally named, over-attaches when a mention is incidental, and cannot see "a goblin's bare hand", "a gnome and a goblin", "the party turning to look up", or "one small figure with her hands up". Every one of those needed a hand-written `REF_OVERRIDE` entry. Deciding who is in a picture is the judgment the job consists of, and it was automated away.
Instead: hand-write the plan, one line per plate naming its location and cast, in the `s9_art_plan.PLAN` style. It is thirty minutes of work for a whole session. Treat the generated `s9_art_queue.py` as a first draft and read all its entries; if you regenerate it, clear every line of the WARNING block it prints ("people in frame with no reference art attached") before generating a single image.

**5. Never feed an approved campaign plate back in as a reference for a fresh generation.**
Why: the output-stage safety filter rejects it as `moderation_blocked`, category "other", 4 of 4 attempts on 2026-08-13. Generations attaching only `art_refs/` portraits go through normally.
Instead: for a fix to an approved plate, use an IN-PLACE EDIT (`templates/inpaint.py`, or the edits endpoint on the whole plate). It works, it is the documented preferred repair, and it preserves the approved composition a re-roll would throw away.

**6. Never approve art on the DM's behalf, and never trim the queue to the plates you think are good.**
Why: every image needs Justin's explicit yes. `approve_art.py`'s header states it: a plate stays in `art_review/` until he says a letter out loud.
Instead: generate everything the plan calls for, publish the review board, present ALL of it, and move only the letters he names. Offering an opinion on which you would cut is fine; acting on it is not.

**7. Never publish a review board and then approve letters against a `_letter_map.json` you did not regenerate in the same breath.**
Why: letters are positional over a sorted glob, so adding or removing one plate shifts every letter after it. **Nothing in the repo actually writes that file**: a repo-wide grep finds exactly one mention, the read in `approve_art.py:17`. `review_gallery.build()` computes letters with `code_for(i)` and never persists them. The map on disk today holds a single stale entry (`{"A": "s9 loc rift gate"}`) against zero pending plates.
Instead: fix `review_gallery.build()` to write `art_review/_letter_map.json` from the same `enumerate(shown)` loop that renders the cards, so board and map can never disagree. Until then, run `approve_art.py --list` and compare its labels against the published board before banking anything.

**8. Never assume rerunning a batch will regenerate a rejected plate.**
Why: resume is the default; a plate is silently skipped if it has a `PENDING_*.png` in `art_review/` OR is already banked in `assets/`.
Instead: move rejects to `art_review/_superseded/` before rerunning, or pass `--force` with a substring filter narrow enough that you are not paying to re-roll approved-quality work.

**9. Never treat `art_review/` as durable storage.**
Why: it is gitignored (`.gitignore` line 7). Nothing in it is committed. `templates/s9_build_queue.py` reads its source list from `art_review/_s9_art_list.txt`, so 15 KB of reconciled design work exists only on one machine.
Instead: keep design source under version control in `reference/campaign/` or `templates/`, and use `art_review/` only for pending images, the generated `review.html`, and the letter map. The durable record of every approved plate and its prompt is `assets/image_manifest.md`.

### Canon and numbers

**10. Never let `memory/campaign_canon.md` carry a design number that a newer reference file has superseded, even for a day.**
Why: canon briefly recorded encounter totals of 308/444/412/458. The difficulty bump replaced them with 404/552/530/558, the stale numbers sat in canon for a day, and a separate simulator session faithfully simulated them. The 458 never even added up: Kyogre 250 plus the Quiet Hand 120 is 370.
Instead: `reference/campaign/session_09_enemies.md` is the declared source of truth for Session 9 enemies. Update canon in the SAME work session as any design change, and mark the old figure SUPERSEDED in place rather than deleting it, which is what the current canon entry does correctly.

**11. Never take `campaign_canon.md` lines 123 to 126 as the Session 9 enemy roster.**
Why: those bullets are the pre-bump rosters and are still on disk today. Canon says Kyogre 250 and the Quiet Hand 120; the enemy file says 280 and 150, and canon's own paragraph two lines above already delegates to it.
Instead: read `reference/campaign/session_09_enemies.md` for every count, HP, AC, save DC and attack routine. Use `campaign_canon.md` only for the fight's intent, its objective and the foreshadowing beats.

**12. Never read a Session 9 stat block without first reading the RECONCILER ADJUSTMENTS block at `session_09_enemies.md:18`.**
Why: the cards were written by five designers in parallel and the reconciliation pass that followed was recorded in the totals table but never carried back into them. The block overrides four things: Needlemaw is 4 not 5, the Kept collapse after two rounds not three, the second Drownbell arrives round four not three, and Kyogre's legendary uses run 1 / 2 / 2 by phase. A card read on its own is wrong on all four counts.
Instead: apply the reconciler first, then read the card. And when you write a reconciliation into a roster of your own, carry it back into the cards in the same edit rather than leaving an override block on top.

**13. Never believe a fight total without adding up the components.**
Why: the roster file exists because a total did not add up, and the arithmetic is what caught it, not the simulator's statistics.
Instead: compute every total as `sum(Count x HP)` and print the working. With the reconciler applied all four Session 9 fights now re-derive exactly (404, 552, 530, 558 on the board). If yours does not, stop and reconcile before running a sweep, because a sweep against wrong numbers looks authoritative and is worthless.

**14. Never treat the three hero kit files as current just because they are the most specific source.**
Why: they were written 2026-07-25 and are outranked by dated rulings added to `memory/house_rules.md` through 2026-09-05. `lilly_kit.md:29` still says two attunement slots free; `:98` still lists the Drowning Lull among the locked discharges.
Instead: read the kit for structure and the easy-to-forget checklist, then read `house_rules.md` end to end and let any dated bullet override. When they disagree, correct the kit in the same commit.

**15. Never honour a `[DM CHECK]` in a reference file or a simulator without checking whether a dated ruling already settled it.**
Why: `reference/expansions/druid-circle-of-stars.md` still prints Cosmic Omen self-target as open ("the safe reading is others-only"), which house rule 3 settled on 2026-09-05. `templates/playthrough_session_09.py` still carries a `[DM CHECK]` on Fight 2's total, which the reconciler block settled on the same day.
Instead: grep `memory/house_rules.md` and the roster file's own override blocks before honouring any flag, and delete the flag in the same commit as the fix.

**16. Never state a 2024 rule from memory, and never reach for WebFetch on dnd2024.wikidot.com.**
Why: recall has caused documented errors here on True Strike, Divine Order, Origin feats and firearm proficiency. WebFetch loops on the wiki's HTTP-to-HTTPS redirect and cannot reach the site at all.
Instead: grep `reference/srd/`, then `reference/expansions/`, then read the wiki page through the in-app browser. Cite the file or URL and the date. If you cannot verify it, write "unverified, check your PHB".

**17. Never label Gearhaven as Session 8 or leave a gap between 6 and 8.** Adjudicated 2026-07-06. Gearhaven is Session 7; the chronicle runs 1 through 7 continuously.

**18. Never write Kyogre's defeat as a kill, and never let the party attack the spike in its back.**
Why: the 280 is the corruption riding it, not its life; at 0 the guardian is FREE. The spike is not a target at all and cannot be attacked, moved, dispelled, sundered, grappled or targeted by any effect. Attacking a spike was last session's objective and repeating it undoes the design.
Instead: no death saves, no wound described. The enemy file instructs the DM to say this out loud before initiative if the players look worried. The three SPENT spikes the Quiet Hand plants in the sand later are ordinary objects and are fair game; the party is allowed to notice the difference without help.

**19. Never cite `lore/rift_run_design.md` for how the rift run works.** `campaign_canon.md:231` marks it a provenance-banned draft: its growth tables, catch procedure, choose-1-of-3, stone-shell and Terranox boss are all dead, and `house_rules.md` separately says its tier table and its "~14 damage per turn" companion ceiling were never DM-authored. The live rules are the socketed-Mote engine and the companion swap rule at `campaign_canon.md:66` and `:101-102`.

**20. Never give Ursa a Signature Partner or the Mightier Summons upcast.** Those belong to Door C, Beast Handler, which he did NOT take. `ursa_kit.md` documents all three doors; use only Always-on plus Door B. The same applies to Lilly (Door C only) and Stabby (Door B only).

**21. Never give a fight a social or environmental way out.** See section 5.1 rule 2. Close the off-ramp on the monster card, not in a DM note.

**22. Never lower enemy hit points to fix a round-one damage spike.**
Why: hit points are the difficulty budget and the session is aiming 20 to 30 percent above the Session 8 anchor. The real problem is concentration of damage on one body, not the amount on the board.
Instead: add a targeting rule to a card (They Share, It Lamps the Far Ones, It Is Not Aiming) or delay the big effect ("never on round one").

**23. Never let an enemy attack a hero at 0 hit points.** Implement it once centrally in the simulator, and still write the flavoured version on each card so the DM has a line to read.

### Documents and layout

**24. Never write `{"pagebreak": True}` on an h1.**
Why: the h1 branch reads only `blk[2].get("hardbreak")` (`book_style.py:299`). The key `pagebreak` is read by nothing. The block builds, the render succeeds, and the part quietly starts mid-page. Nothing errors and no instrument flags it, because a part starting mid-page is not a geometry violation.
Instead: use `{"hardbreak": True}`. An h1 whose title starts with "Appendix" page-breaks automatically.

**25. Never put a full scene's text inside a `railrow`.**
Why: `railrow` is ONE table row. The narrow text column is reserved for the whole row, so text longer than the rail image is tall keeps running down a skinny column beside dead white space. The DM flagged this by name on 2026-08-18: "the text columns should expand after the image." Its inner dispatch also handles only `h2`, `gold` and `dm`; every other kind silently renders as plain body text, so an `("img", ...)` inside one becomes a caption-shaped string.
Instead: put only rail-height's worth of text in the row and continue the rest as full-width blocks after it. Split a long `gold` at a paragraph break.

**26. Never pass `{"crop": ...}` on a story plate.** Superseded by DM ruling 2026-08-18: "you've cropped a lot of them, and I don't want them cropped." The engine option still works, so nothing stops you, and the result is a silently beheaded composition in a book he is printing as a hardcover.

**27. Never make a solo boss card's plate as big as possible.**
Why: a card filling about 95 percent of a page orphans the next creature's intro line onto a near-blank page, and `keep_with_next` cannot bridge a paragraph to a table, so the usual rescue fails. This is written into the engine comment at `book_style.py:858`.
Instead: let the engine's caps do the work (landscape 5.7 x 3.5in, square and portrait 4.1in). Part-opener plates go about 5.7in wide with `hmax` about 3.4. Verify with `ws_probe` afterward, looking for a following page whose top line is a creature name.

**28. Never assume you get the image width you requested.**
Why: every image block silently shrinks to satisfy a height cap: `img` recomputes `w = hmax/aspect` with `hmax` defaulting to 4.2in, `imgrow` caps each image at 3.6in tall, `imgfloat` at 3.4, statblock portraits at 2.6, reward_card images at 3.2. A 6.5in request on a portrait source can land under the 90 percent threshold and be flagged NARROW with no obvious cause.
Instead: supply landscape source art, or raise `hmax` explicitly the way the printable board pages use `{"hmax": 8.7}`. When `img_geom` flags NARROW, check the source aspect ratio before touching the width.

**29. Never trust a clean `img_geom` report as signoff.** Its own docstring: "Instruments are triage, not signoff: eyeball every page before shipping." It cannot see a plate on the wrong page, art showing the wrong character, a caption contradicting the picture, or a section starting mid-page. Session 8 reports 0/0/0 and still carries a 91 percent whitespace page at p63.

**30. Never treat a `ws_probe` BLANK line as automatically a defect.** It decides blankness on text length under 15 characters, so a legitimate full-page plate reports BLANK. Read the whole line: BLANK with a large image is a full-page plate; BLANK with `no-img` is a real blank page and is the worst defect in this book.

**31. Never run `render_check.py` or `publish.py` while the target docx or a generated PDF is open in Word or a PDF viewer.** The COM conversion either fails outright or blocks until the 300 second timeout, and the failure message is a raw COM error. There is no LibreOffice fallback on this machine. If a conversion fails, check for an orphaned WINWORD.EXE before blaming the document.

**32. Never print PyMuPDF page text straight to stdout in an ad-hoc one-liner.** Windows stdout is cp1252 here and the book is full of U+2726 stars; the script dies with UnicodeEncodeError mid-inspection, which reads like a corrupt PDF. Wrap output as `line.encode('ascii','replace').decode()`, which is what `ws_probe.py` does.

**33. Never add a session builder without registering it in BOTH `BUILDERS` and `BOOK`.**

**34. Never try to regenerate Session 7 from a builder.** There is no `templates/build_session_07.py`. `sessions/session_07_gearhaven.docx` is the gold-standard document, edited in place, and `publish.py` omits it from BUILDERS with a comment saying so. Writing one and running it would replace the reference document the whole house style was extracted from.

### Scripts and the environment

**35. Never write or patch a Python file through a bash heredoc, `python -c "open(...).write(...)"`, or `echo`.**
Why: literal backslash-n written inside a heredoc destroys the file's line structure. This happened repeatedly, wiped out edits, and once left a stale script in place that then ran and burned a whole batch of paid image generations. The file may still parse, which makes the corruption invisible until the output is wrong.
Instead: use the Write and Edit tools for all Python source, with absolute paths. If a heredoc is unavoidable for non-Python content (a prompt file, say), quote the delimiter: `cat <<'EOF' > file`. Unquoted `EOF` expands `$` and backticks.

**36. Never launch a paid generation run against a script you just edited without verifying it landed.**
Verify in this order, cheapest first:
```
python -c "import ast;p='templates/batch_art_s9.py';ast.parse(open(p,encoding='utf-8').read());print('syntax ok',sum(1 for _ in open(p,encoding='utf-8')),'lines')"
git status --short templates/ && git diff --stat templates/
```
Then run the generator filtered to a SINGLE plate, look at that one result, and only then run the batch.

**37. Never run `templates/build_hero_sheets.py` to rebuild the party's character sheets.**
Why: it does not touch the live sheets. It slices `templates/build_sheets.py`, whose line 25 says "level 5, relics attuned, cannon smoking", and writes `characters/<hero>_sheet.pdf` with no `_v3` suffix. `publish.py` merges only the `_v3` files, so the level-5 output looks plausible, sits beside the real files, never reaches the book, and nobody notices until a kid is handed the wrong sheet.
Instead: `cd characters/builders && python build_lilly.py` (and `build_stabby.py`, `build_ursa.py`). Those write `../<hero>_sheet_v3.pdf`, say Level 7 in their header tables, and **must be run from that folder** because every path in them is relative.

**38. Never trust `characters/builders/README.md` or `PROVENANCE.md`.** Both predate the timeskip. PROVENANCE says the party is level 5 and that Cosmic Omen is correctly absent as a level-6 feature. README names portraits `stabby_portrait.png` and `ursa_portrait.png` (the real files are `stabby_new.png` and `ursa_new.png`) and an output `Ursa_Catchum_Sheet.pdf` that no script writes. Read the three `build_<hero>.py` files instead.

**39. Never run `templates/build_unda_board.py`.** The Session 9 board is already built and DM-approved, `campaign_canon.md:120` says do not respin it, and every approved location plate was generated against that exact image. Open the PNG to look at it; read the `UNDA` dict at the bottom of the file for the geometry. Also ignore that file's header: line 1 says `# build_rift_board.py` and line 20 names the Session 8 output. Both are copy-paste leftovers.

**40. Never go looking for `templates/s9_build_monster_queue.py`.** `s9_monster_queue.py` line 2 claims to be generated by it. It does not exist anywhere in the repo. Treat the 22-entry queue as hand-maintained source and edit it directly.

**41. Never trust a docstring or comment header over the code beside it.** `playthrough_session_08.py`'s "Sources of record" block still lists the pre-retune numbers while the code runs the retuned ones. When you change a number, update its comment in the same edit.

**42. Never assume monster plates banked by `approve_art.py` will be picked up by the bestiary.** `dest_for()` sends `mon_*` to `assets/monsters/mon_<name>.png`, while `templates/build_bestiary.py` has 44 art references of the form `assets/monsters/<name>.png` and zero with a `mon_` prefix. `assets/monsters/` already holds byte-identical duplicate pairs (`chime_warden.png` with `mon_chime_warden.png`, `rootrot_crawler.png` with `mon_rootrot_crawler.png`) because someone hand-copied to reconcile the two conventions. Pick one, fix `dest_for`, and move the losers to `_triage/`.

**43. Never delete a file.** `CLAUDE.md`: move unclear or superseded files to `_triage/`, and use `git mv` for renames so history is preserved.

### Shell notes for this machine

- The Bash tool here is **Git Bash**, not cmd or PowerShell. PowerShell here-strings (`@'...'@`) are a parse error there.
- The PowerShell tool is **Windows PowerShell 5.1**: no `&&`, no `||`, no ternary. Chain with `A; if ($?) { B }`.
- Run scripts with `PYTHONUTF8=1` when they contain the box-drawing and star glyphs the house style uses. The repo's allowlist shows `export PYTHONUTF8=1` as a standing pattern.
- Environment variables in Bash: `S8_HPX=1.5 python ...`. In PowerShell: `$env:S8_HPX='1.5'` first, on its own statement.
- Ripgrep-based Glob and Grep return false negatives inside `C:/Users/jhffm/claude-archive`. Enumerate that tree with PowerShell `Get-ChildItem`; Read works normally. This does not affect the campaign repo.

---

## 11. Map of the repo: what is live, what is a decoy

### Live session builders

`build_session_01.py` through `build_session_06.py` and `build_session_08.py` are LIVE and re-run by `publish.py` on every render. `sessions/session_07_gearhaven.docx` is LIVE but HAS NO BUILDER. `templates/build_session_09.py` DOES NOT EXIST as of 2026-09-06; `reference/campaign/session_09_enemies.md:3` already names it as the file that must read from it.

### Live character sheets

`characters/builders/build_lilly.py`, `build_stabby.py`, `build_ursa.py` write `../<hero>_sheet_v3.pdf`. ReportLab, level 7 in the header table (`build_lilly.py:95`, `build_stabby.py:100`, `build_ursa.py:111`), shared `characters/builders/sheet_style.py` (parchment `#F7F1E1`, gold double frame `#8A6D1F`, Times serif, per-hero accent). All paths inside are RELATIVE; run them only from `characters/builders/`.

### Live compendium and handout builders

| Script | Reads | Writes |
|---|---|---|
| `build_bestiary.py` | its own `B` list | `compendium/bestiary.docx` (data source; no longer published alone) |
| `build_compendium.py` | its own `I` and `C` lists | `compendium/*.docx` (same caveat) |
| `build_compendium_full.py` | `build_bestiary.B`, `build_compendium.I` and `.C`, `build_sheets.S` | `compendium/the_compendium.docx`, the published volume. Part IV is only a divider page; the real sheets are merged in by publish.py |
| `build_foreword.py` | its own BLOCKS | `frontmatter/foreword.docx` |
| `build_lore.py` | its own BLOCKS, drawn from canon and `lore/` | `frontmatter/lore_primer.docx` |
| `build_path_rewards.py` | `build_compendium.C` | `characters/path_rewards/*_v3.docx` and `.pdf`, on demand. Strips `dm` blocks so a player handout carries no DM text |
| `build_companion_cards.py` | `build_bestiary.B` | `characters/<companion>_statblock.docx` for Ghostbloom, Sandshrew, Piplup, Chimchar, Togekiss, on demand |

The pattern worth copying: **every play aid is SLICED from the book's own block list rather than retyped**, so the card at the table cannot drift from the book. `build_path_rewards.py` uses `h1_index()` and `next_h1()` to cut a hero's section out of `C`; `build_companion_cards.py` matches on the card's `name` prefix inside `enemy_cards` blocks.

### Board and map builders

`build_rift_board.py` (Session 8 board, reads `assets/world/s8_underroot_board.png`), `build_unda_board.py` (Session 9 board, reads `assets/world/s9_unda_board.png`, DO NOT RUN), `split_board_for_print.py` (any board PNG on argv, producing two Letter halves plus a 2-page PDF), `build_region_map.py` and `label_region_map.py` (one-time world map; the first's docstring carries the canonical west-to-east geography, the second overlays crisp serif labels because image models garble text).

How a board works: all geometry is computed in a base 1536x1024 space with the print seam at exactly half the width, then scaled by `cfg["scale"]` (default 3, giving 4608x3072 at roughly 270 dpi across two Letter sheets). The builder self-checks for overlapping spaces, space-to-seam clearance, and locations bumping the title, and refuses to render on failure. `split_board_for_print.py` relies on the seam being at exactly `width // 2`; its docstring warns explicitly against detecting the dashed seam line visually, which lands about 48 px off true. Print at 100 percent / actual size, never "fit to page".

The Session 9 board config (`UNDA`, from line 227) is the geography of record: five slots, ordered The Rift Gate, 1 The Brightshoal, 2 The Kelp Cathedral, 3 The Blackwater Seam, 4 The Guardian's Trench, on 16 waypoints (waypoints are spline control points, not spaces; the spaces are computed along the spline by `"step": 68`, and canon records the printed result as 18 spaces).

### Decoys and dead ends

| Thing | Status |
|---|---|
| `templates/build_hero_sheets.py` | DECOY. Writes level-5 sheets under names one character away from the live ones |
| `templates/build_sheets.py` | LEVEL-5 snapshot. Still LIVE for one purpose only: it supplies the Compendium's Part IV prose pages |
| `characters/builders/README.md`, `PROVENANCE.md` | Stale, pre-timeskip. Trust the code |
| `templates/build_ghostbloom_card.py` | SUPERSEDED by `build_companion_cards.py` |
| `templates/batch_art.py` | Sessions 1 to 7 era. Its `BLK` character blocks describe the heroes at ages 7 and 8 with pre-timeskip gear, and it hardcodes 1024x1024. Read only for the pattern |
| `templates/fit_plates_s7.py` | SUPERSEDED. Regex XML surgery depending on `templates/s7_unpacked/`, which is not in the repo |
| `templates/lettered_board.py` | Session 8 era. Superseded by `review_gallery.py`, but it is the only tool that orders plates by an explicit manifest rather than filename |
| `templates/s9_build_queue.py` | The regex parser that automated away judgment. Read it as a cautionary tale |
| `templates/s9_build_monster_queue.py` | DOES NOT EXIST |
| `templates/sim_session_07.py`, `sim_session_08.py` | Archived Monte Carlo scripts, superseded by the playthrough engine |
| `templates/oneshots/` | 13 scripts plus a `gen/` subfolder of 10 art generators, recovered 2026-07-26 from a raw session log. Its own README says they are not part of the active pipeline and may need path adjustments. Reference only |
| `lore/rift_run_design.md` | Provenance-banned draft (`campaign_canon.md:231`) |
| `art_review/_letter_map.json` | STALE and unwritten by anything. One entry against zero pending plates. Regenerate the board before approving anything |

---

## 12. Command reference

Every command below is copy-pasteable from the repo root unless noted.

### Reading and checking

```
sed -n '1,10p' memory/campaign_canon.md
```
The lockdown protocol: the precedence rule and the amendment rule. Read before anything else in that file. (Git Bash uses `/c/` paths; in PowerShell use `Get-Content -TotalCount 10` with the `C:\` path.)

```
grep -n '2026-09' memory/house_rules.md memory/campaign_canon.md
```
Every ruling made in the last month, which is where the kit files most often go stale.

```
grep -rn 'Underwater Combat' reference/srd/
```
The first step of a rules check. 13,405 lines across 14 files, so grep is the access method. Absence from the SRD is itself the signal to check `reference/expansions/` and then the wiki.

```
grep -n 'RECONCILER ADJUSTMENTS' -A 10 reference/campaign/session_09_enemies.md
```
The four overrides that beat every stat block in that file. Read this before any card.

```
grep -n 'AC\*\* \|Count:\*\*' reference/campaign/session_09_enemies.md
```
Every Session 9 statblock's count and defences in one pass, so you can re-derive a difficulty total yourself.

```
ls assets/art_refs/
```
Confirm a reference image exists before naming it in a prompt. 48 files. Aelwyn is `.webp`, not `.png`.

```
git log --oneline -20 -- memory/campaign_canon.md memory/house_rules.md reference/campaign/
```
The order rulings landed in, which resolves any recency question the files leave ambiguous.

### Simulating

```
python templates/playthrough_session_09.py 20260905
```
One seeded, logged, grid-based playthrough of Session 9's four fights. Thousands of lines; pipe it.

```
python templates/playthrough_session_09.py sweep 200
```
Monte Carlo: net damage taken minus healed with a 95 percent CI, mean rounds, mean knockdowns, wipes. Target 3 to 4 knockdowns, zero deaths, zero wipes. Roughly a minute per 5 seeds.

```
S8_HPX=1.5 python templates/playthrough_session_09.py sweep 200
```
Scaling stress test. Bash tool only.

### Building the document

```
python templates/build_session_08.py
```
Rebuilds `sessions/session_08_underroot.docx` (about 14 MB). It chdirs to the repo root itself. Takes about a minute because every image is reopened, cropped, downscaled and re-encoded to JPEG at quality 82, which is also why it shows as modified in `git status` even when content is unchanged.

```
python -c "import sys,os,re; sys.path.insert(0,'templates'); import build_session_09 as b; paths=sorted({x for blk in b.BLOCKS for x in re.findall(r'assets/[\w/.-]+\.(?:png|jpg|jpeg|webp)', repr(blk))}); miss=[p for p in paths if not os.path.exists(p)]; print('blocks',len(b.BLOCKS),'assets',len(paths),'missing',len(miss)); [print('  MISSING',m) for m in miss]"
```
Lint a builder without rendering: counts blocks, proves the module parses, and proves every referenced asset exists. Session 8 reports 337 blocks, 64 assets, 0 missing.

```
python -c "import glob; bad=[(f,i+1) for f in glob.glob('templates/*.py') for i,l in enumerate(open(f,encoding='utf-8')) if chr(8212) in l]; print(len(bad),'lines with em dash'); [print(' ',f,i) for f,i in bad]"
```
Enforce the no-em-dash rule across every builder. Currently reports 0. Uses `chr(8212)` so the checker cannot contain the character it hunts. Extend the glob to `characters/builders/*.py` when touching hero sheets.

### Layout QA

```
python templates/render_check.py sessions/session_09_unda.docx art_review/qa_s9 110
python templates/img_geom.py art_review/qa_s9/session_09_unda.pdf
python templates/ws_probe.py art_review/qa_s9/session_09_unda.pdf 30
python templates/geom_audit.py sessions/session_09_unda.docx
python templates/montage.py sessions/session_09_unda.docx art_review/s9_check
python -c "import fitz; d=fitz.open('10_Session_8_Underroot.pdf'); print(d.page_count)"
```
The last one is the fastest sanity check that a change did not blow up pagination. Session 8 is 66 pages, Session 7 is 54. A jump of several pages after an edit almost always means a card or table stopped fitting; go to `ws_probe` next.

### Character sheets

```
cd characters/builders && python build_lilly.py && python build_stabby.py && python build_ursa.py
```
The LIVE level-7 sheets. MUST be run from that folder. Needs reportlab. Never use `templates/build_hero_sheets.py` for this.

### Art

```
python -c "import sys;sys.path.insert(0,'templates');import s9_art_plan as P;print('missing locations:',P.missing_locations())"
```
Is stage 2 unblocked? An empty list means yes. **Verified empty on 2026-09-06: stage 2 is unlocked.**

```
python -c "import sys;sys.path.insert(0,'templates');import s9_art_plan as P;from s9_art_queue import QUEUE as S;from s9_monster_queue import QUEUE as M;names=[q[0] for q in S if not q[0].startswith('mon_')]+[q[0] for q in M];[print('NO PLAN:',n) for n in names if n not in P.PLAN and n not in P.MONSTER_LOCATION and not n.startswith('s9_loc_')];[print(n,'->',P.refs_for_plate(n)) for n in names]"
```
**Run this before every batch.** It prints which reference images each queued plate will actually receive. Any plate with a person in it whose printed list lacks that person's file is a plate that will come back off-model. It currently prints zero NO PLAN lines across the queue.

```
python templates/batch_art_s9.py --locations
python templates/batch_art_s9.py
python templates/batch_art_s9.py loc_
python templates/batch_art_s9.py --force
python templates/review_gallery.py
python templates/approve_art.py --list
python templates/approve_art.py A B C
mv art_review/PENDING_<name>.png art_review/_superseded/
```

```
python templates/genart.py assets/scratch/test.png assets/gen_prompts/foo.txt assets/art_refs/REF_lilly_6_level7.png assets/items/boomstick.png
```
Single-image generation with explicit references. Refs go through the images/edits endpoint; no refs falls back to plain generation. Env: `GENART_MODEL` (default gpt-image-2), `GENART_SIZE` (default 1024x1024, set 1536x1024 for a book plate), `GENART_QUALITY`, `GENART_BACKGROUND`.

```
python templates/inpaint.py assets/session_09/plate.png assets/session_09/plate_fixed.png assets/gen_prompts/fix.txt 0.30 0.10 0.60 0.50
```
Repair one region of an approved plate. Rect coords are FRACTIONS of width and height, repeatable for multiple rects. Never run two edits on the same file concurrently.

```
python templates/audit_embedded_art.py
```
Perceptually maps every image embedded in a docx back to its repo asset and flags mismatches. Its `DOCX` constant is hardcoded to `sessions/session_07_gearhaven.docx`; edit it for another session.

```
python templates/split_board_for_print.py assets/session_09/unda_board.png
```

### Publishing

```
python templates/publish.py
python templates/publish.py --pdf-only
```
The full run requires Microsoft Word and pypdf, takes several minutes, and prints `[ok]` / `[FAIL]` per builder and `MISSING` for absent sources rather than aborting. It does NOT rebuild the character sheets.

---

## 13. What is unfinished: the OPEN list

Do not resolve any of these unilaterally. Ask the DM, or flag `[DM CHECK: ...]` in the document.

### Resolved since the surveys were written (recorded so nobody reopens them)

- **Fight 2's total is SETTLED at 552 with four Needlemaws**, by the RECONCILER ADJUSTMENTS block dated 2026-09-05. Earlier notes calling this open are stale. What remains is a code fix, listed under machinery defects below.
- **The six Session 9 location plates are approved and banked.** `missing_locations()` returns `[]`; stage 2 of the art pipeline is unlocked.
- **The `batch_art_s9.py` resume check now looks in `assets/` as well as `art_review/`**, so approving a plate no longer causes the next run to regenerate it.

### Session 9, blocking or near-blocking

1. **The Session 9 document filename is unsettled.** Every existing session follows `sessions/session_NN_short_title.docx`. The plane is Unda; the art queue's working title is "THE UNDERSEA". No file in the repo commits to a stem. Ask before creating it, because renaming later means `git mv` on a shipped PDF too.
2. **`templates/playthrough_session_09.py` still runs five Needlemaws** and still carries the now-stale `[DM CHECK]` in its docstring. Fix the count to four, delete the flag, verify the other three reconciler overrides against the code, and re-run the sweep before quoting any balance number.
3. **The four fight totals do not use one accounting convention.** Fights 1 and 2 include round-three arrivals; Fight 4's "558 on the board" excludes them (748 if you count everything). Pick one convention and restate all four, or the +26/+24/+29/+30 deltas are not comparable.
4. **`campaign_canon.md` lines 123 to 126 carry the stale pre-bump rosters** and the superseded Kyogre 250 / Quiet Hand 120 numbers. This needs a dated correction in canon written in the file's own supersession style. It is the exact failure the DM already paid for once.
5. **The Drowning Lull SYNC LIST is unapplied.** `templates/build_compendium.py` lines 822 to 826 still hold the superseded Incapacitated-and-Speed-0 sketch, and `lilly_kit.md:98` still lists the Lull among the locked discharges. This is publish-affecting: the Compendium PDF changes when it lands.
6. **The Session 9 companion is contested across files.** `playthrough_session_09.py` sets `S8_COMPANION=sandshrew` and states Sandshrew is out for Session 9; `campaign_canon.md:120` says Piplup manifests at the homecoming. Both can be true if Piplup arrives at the END, but any document or art plate showing the party mid-session must field Sandshrew. Confirm before writing.
7. **The board space count is recorded two ways.** `campaign_canon.md:120` says 18 spaces, corrected 2026-09-05 against the printed plate. The `UNDA` config lists 16 waypoints, but waypoints are spline control points and the spaces are computed along the spline by `"step": 68`. If an exact count matters for the session text, read it off the printed plate; do not respin the board to count them.
8. **Canon says the Session 9 board is "a NEW spiral geometry in the S8 visual system"** while the comment above the `UNDA` config says "Geometry inherited from the S8 board; the backdrop is the S8 board repainted as Unda." Unresolved, and not worth resolving by running the builder.

### Machinery defects, verified 2026-09-06 and unfixed

9. **Nothing writes `art_review/_letter_map.json`.** `approve_art.py:17` reads it and exits if absent; a repo-wide grep finds exactly one mention, that read. The copy on disk holds a single stale entry against zero pending plates. Fix `review_gallery.build()` to write it from the same `enumerate(shown)` loop. **Fix this before the next approval round.**
10. **`approve_art.py` banks monster plates to a path the bestiary does not read** (`mon_` prefix versus the bestiary's 44 unprefixed references), and byte-identical duplicate pairs already exist in `assets/monsters/`.
11. **`approve_art.py` appends 2-column rows to a 3-column manifest table.** The header is `| New path | Original filename | Notes |`; the append writes two cells, losing the Notes column where the reference set is normally recorded.
12. **`batch_art_s9.refs_for()` drops nonexistent reference paths silently** (line 134). A typo produces an off-model plate indistinguishable from a plate given no reference. Add a printed warning.
13. **`batch_art_s9.gen_one` recurses unboundedly on HTTP 429.** Port `genart.generate()`'s separate `rate_limit_attempts=8` budget.
14. **Session 8 p63 renders at 91 percent whitespace**, holding only the tail of the Fight 3 `tactics` paragraph. This violates the never-a-near-blank-page rule in an already-shipped, DM-seen document. Whether to fix it or leave an approved layout alone is the DM's call.
15. **Sessions 1 through 7 still carry 5 to 9 narrow-centered images each** under the current `img_geom` threshold. Fixing them means touching DM-approved layouts; explicitly deferred to the DM.
16. **The bottom-margin documentation drift.** `templates/session_template.md` says 0.75in top and bottom; `build_doc` sets the bottom to 1300 twips (0.90in) and all the instruments are calibrated to the engine value. Cheap fix, but it is a change to a DM-facing spec, so flagging rather than assuming.
17. **The `s9_aelwyn_and_the_reed` scene line in `batch_art_s9.py` still calls Aelwyn "the elderly scholar"**, three lines below the comment correcting exactly that error. Fix it when you touch that plate.

### Undecided policy questions

18. **Does new session art have to be entered in `assets/image_manifest.md`, and in which format?** `session_template.md` says "every image used should exist in the manifest", but 55 of the 64 assets referenced by `build_session_08.py` have no basename match there. The manifest's table appears to be the Phase 2 old-path-to-new-path mapping with post-Phase-2 generations appended unevenly as prose rows.
19. **Should `templates/build_sheets.py` be refreshed to level 7?** It supplies the Compendium's Part IV prose pages, which currently describe the heroes at level 5, and `build_compendium_full.py`'s own divider text also says level 5, which suggests intent (Part IV as a historical snapshot with the live level-7 PDFs merged in after it). Do not change it on the recency rule alone.
20. **Which builder is authoritative for a printed sheet.** `PROVENANCE.md` says `templates/build_sheets.py`; `house_rules.md:34` names `characters/builders/build_lilly.py` as the live spell list and that file is in fact current at level 7. Recency favours `characters/builders/`, but confirm before regenerating anything.
21. **Should Session 9's builder be a fresh file on the Session 8 pattern, or a refactor that lifts shared scaffolding?** The standing preference is the smallest thing that works.
22. **Should Session 7 ever be back-ported to a block list**, which would make the whole book regenerable from source?
23. **The earring backlog from 2026-08-17.** `assets/character_refs.md` records a DM request to strip extra earrings from existing approved plates by in-place edit, session by session, newest first, re-running `audit_embedded_art.py` after each batch. No log or marker shows how far it got. Confirm status before starting, and do not start it as a side effect of session work.
24. **The five open DM decisions at `campaign_canon.md:215-221`** are still open and must not be resolved unilaterally: Stabby's idol payoff mechanism (retargeted to Session 12), the one-shot Ash Catchum sheet versus Ursa's origin, the map compass truth, the Guardians of Fire and Air plus the finale boon mechanics, and the Session 6 grave name (never invent it).
25. **Lilly's five Replicate plans are unrecorded**, flagged OPEN in `house_rules.md`. Only three are inferable from her gear (+1 Half Plate, Wand of Magic Missiles, and the plan that became the Spell-Refueling Ring). Plans swap only at level-up, so this gates what she can build for the rest of the campaign.
26. **Whether Session 8 has actually been played at the table.** `memory/session_log.md` ends at Session 7 and canon marks Session 8 "(planned)". That determines whether its outcomes are now hard canon.
27. **The real provider limit on reference images per request.** The repo says two different things: `s9_art_plan.py` says "about five reference images per request", `genart.py` says "the cap is 5 input-images per minute". Both are repo folklore, not cited to provider documentation. The five-image truncation is safe under either reading, but nobody has checked whether the real constraint is looser.
28. **Whether `art_review/_s9_art_list.txt` should move into version control.** It is 15 KB of reconciled design work sitting in a gitignored directory. Recommendation: move it to `reference/campaign/`.
29. **Whether the DM wants a round-one worst-case table written down per fight.** The guarantee is currently encoded implicitly, as targeting and delay traits on individual cards. The worked trench arithmetic in section 5.3 is a reconstruction, not a figure recorded anywhere.
30. **Whether the DM wants a browse mode for already-approved art.** `review_gallery.py` deliberately sets `done = []` so the board only shows what still needs a decision.
31. **There is no Session 9 design narrative** equivalent to `session_08_draft.md` and `session_08_part_two.md`. The beats currently exist only as canon bullets, the roster's Role and Art brief lines, and `art_review/_s9_art_list.txt`. Whoever writes the document is writing that narrative for the first time.

---

*Written 2026-09-06, verified against commit `51b1553`. When this manual and a repo file disagree, the repo file wins and this manual should be corrected in the same work session.*