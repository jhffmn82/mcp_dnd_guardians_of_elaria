# Narrative & Lore Consistency Review: Sessions 1 to 7

A full consistency and narrative-flow pass over the chronicle, run 2026-07-26. Ground truth: `memory/campaign_canon.md`, the front matter (`frontmatter/foreword.docx`, `lore_primer.docx`), `lore/character_backstories.docx`, and `lore/world_history.md`. Each session was read in full against that frame, in sequence, hunting the same class of error as the earlier Ghostbloom-before-the-roll slip: out-of-sequence reveals, name/timeline drift, and beats that do not flow.

Fix targets: Sessions 1 to 6 are edited in their builders (`templates/build_session_0N.py`); Session 7 is edited in place (`sessions/session_07_gearhaven.docx`, no builder). Shared item/lore text also lives in `templates/build_compendium.py` and the character-sheet builders.

## Headline

The thing we most worried about is clean. No companion, relic, or gift appears before its session. Ghostbloom appears only in Session 6, as the payoff of the sealed Session 5 roll; Session 5 (the known offender) is now airtight (the essence stays "unknown," the roll stays "sealed," and no Ghostbloom trait leaks). And in all seven sessions, no character ever speaks or learns the villain names in-world. The sequencing discipline is holding.

## The one cross-cutting decision: should the omniscient narrator name the villains?

Four reviewers flagged the name **"Maldrith"** printed in the "Lore of Elaria" boxes of Sessions 2, 3, and 4 (`build_session_02.py:287`, `build_session_03.py:446`, `build_session_04.py:795`). On its face that looks like the withheld villain name leaking years early.

But the front-matter primer (`build_lore.py:72-81`) already names BOTH villains openly to the reader, under a heading "The Shadow: Nyxthid and Maldrith," and closes with: "The heroes do not yet know her name, and should not, until the road grows much darker." So the book has a deliberate omniscient frame: the chronicler (and the adult reader) knows the names; the heroes in-world do not. Measured against that frame, the S2/S3/S4 lore boxes are CONSISTENT, not buggy. Stripping them would leave the primer loud and the sessions silent, which is less consistent, not more.

So this is a design choice, not a clear fix:
- **Option A (keep, recommended):** the omniscient frame stays. Villains are named in the primer and the meta lore boxes; never in-world. Nothing changes. It is already internally consistent, and the primer's "should not know yet" line handles the tension elegantly.
- **Option B (full reader-mystery):** hold the names back from the reader too. This means editing the primer heading and paragraph AND the three session lore boxes to use epithets ("the Weaver of Fractures," "the hunger beyond the walls"), revealing the names only at the Shadow Rift.

This decision gates whether the three lore-box lines are touched. Everything else below is independent of it.

## Clear fixes (unambiguous drift, pre-authorized to correct)

| # | Session | Where | Issue | Fix |
|---|---|---|---|---|
| C1 | 7 | `session_07_gearhaven.docx` ("on the candy-cane katana") | "candy-cane katana" used as the item NAME (name drift) in the gold-standard doc | "the Candyfang Katana" |
| C2 | 4, compendium | `build_session_04.py:808,823`; `build_compendium.py:127` | material descriptor "candy-cane steel" is a flagged variant, and disagrees with S6's "candy-striped steel" | standardize the descriptor to "candy-striped steel" (recency: S6 + the art prompts all use candy-striped); keep the NAME "Candyfang Katana" |
| C3 | 4 | `build_session_04.py:235` "Old Doran Bramblebeard" | disagrees with `:827` "Master Doran Bramblebeard" and with canon | "Master Doran Bramblebeard" |
| C4 | 4 | `build_session_04.py:568` and `:1202` | the "Bells of the Coast" lore box is duplicated (Part Three and Appendix) with divergent closing lines | keep one (the longer Appendix version); remove or differentiate the other |
| C5 | 1 | `build_session_01.py:406` "three motes of runaway magic" | undercount: the session shows four (green Duckleaf, blue Cognifin, two fey from the Mist Stalkers; see `:489`) | "motes of three kinds" (keeps the tally honest) or "four motes" |
| C6 | 1 | `build_session_01.py:476-477` DM foreshadow note | "(Door: the clan catches up with him in Session 2)" reads as Stabby's own Bloodfang, but the S2 ambushers are the RIVAL Grimfang | "(Door: a rival clan, the Grimfang, catches up with him in Session 2)". The gold "Next" teaser at `:410` already says "a rival clan" correctly. |
| C7 | 7 | `session_07_gearhaven.docx` (pervasive, ~15 spots) | Ghostbloom is "it/its" throughout S7; canon pronoun is SHE, set at her S6 emergence | she/her (unless you deliberately want an ethereal "it," in which case make S6 match) |
| C8 | backstories | `lore/character_backstories.docx` | "Whispering Breeze Clan" | "Whispering Breeze Monastery" (canon; the doc is the flagged source) |
| C9 | 4 | `build_session_04.py:395` "four desperate figures ... and a grizzled leader" | count disagrees with the stat blocks (3 bandits + 1 leader) | "three desperate figures" |

Note: the char-sheet flavor line "his prized candy-cane katana" (`build_stabby.py:192`, `build_sheets.py:241`) is the same C2 descriptor drift, low-stakes; fold it in for full consistency ("candy-striped katana") or leave as cute flavor. The item NAME on the sheets is already correct ("Candyfang Katana +1").

## DM-checks (genuine ambiguity, need your call)

- **D1. Companion staging (S3).** Canon note says Aelwyn offers the three creatures "in three warm crates," but the S3 text has them roaming the lab freely, and the S2 teaser calls them "three baskets." The event (Floraburst chosen) is unaffected. Pick one staging so S2 teaser, S3 scene, and the canon note agree.
- **D2. Essence Sphere maker (S3).** S3 credits "Poots Glimmergear" with the Sphere; canon and the primer say "Glimmerspire-forged." Poots is both Lilly's mother and a Glimmerspire master crafter, so "Poots forged it at Glimmerspire" reconciles both, but confirm the phrasing you want.
- **D3. The mystery idol (S6 to S7).** S6 currently defers the idol entirely (it never appears); S7 has it turn up cold in Stabby's bag on the road. That works. Question: do you want a single unobtrusive S6-departure line seeding it (an unaccountable cold weight he does not remember packing), or keep the clean deferral? Related: the S7 DM note says the idol "must come up again in Session 9"; after the Gearhaven renumbering the idol beat is likely Session 8 (the reunion). Confirm and update the reference.
- **D4. Graveyard rite (S6).** The doc already carries a `[DM CHECK]`: whose grave the heroes restored, and what name, was never recorded. Supply a name for the keepsake, or leave the blank intentional.
- **D5. Ordinary sash vs relic (S5).** Stabby's "candy-red sash" in S5 is his accent color, but he receives the Sash of the Swift Current in S6. Confirm the S5 sash reads as his ordinary sash (recommended: it does), or reword to avoid the echo.
- **D6. "The Circle" shorthand.** Several lore boxes use bare "the Circle." The in-world order is "the Circle of the Eternal Stars" ("Circle of Stars" is only the 2024 subclass / door label). Low priority; spell the order out once per box if you want it airtight. Same for the S7 door label "The Circle of Stars."

## Rules-verification punch list (VERIFIED against source 2026-07-26)

Checked against `reference/srd` (SRD 5.2.1), `reference/expansions`, and the SRD PDF bestiary. Citations below.

- **R1 (S7): CONFIRMED ERROR, needs DM sign-off.** SRD Monk Level 3 *Deflect Attacks*: "When an attack roll hits you and its damage includes Bludgeoning, Piercing, or Slashing damage..." It extends to "any damage type" only at Level 13 (*Deflect Energy*). At level 5, Stabby cannot legally Deflect the Custodian's Chain Lightning Burst. The S7 note already offers fallbacks. FIX (his marquee beat, so DM chooses the wording): either have him deflect a Bludgeoning/Piercing/Slashing attack instead, or answer the lightning with Patient Defense, a Dexterity save, Absorb Elements, or Uncanny Metabolism.
- **R2 (S7): NOT an error.** SRD Druid *Wild Shape*: "You regain one expended use when you finish a Short Rest, and all... on a Long Rest." The S7 line "Ursa regains one Wild Shape use" is correct as written. No change.
- **R3 (S7): naming fix (clear drift).** *Starry Wisp* is a real 2024 Druid cantrip (SRD: Action, 60 ft), but it costs an Action. Ursa's FREE 60-ft radiant Bonus Action is the Circle of Stars Archer "luminous arrow" ("star-arrows"), per `reference/expansions/druid-circle-of-stars.md`. Change the S7 note "his Starry Wisp reaches 60 ft too, and it's free" to "his star-arrows reach 60 ft too, and they're free" (matches the doc's own "star-arrows (60 ft)" line).
- **R4 (S5): intentional, no fix.** The short rest that recovers one low-level spell slot is a one-time scene boon, flagged as such in the text; non-RAW by design.
- **R5 (S4): intentional homebrew, no fix.** RAW *Arcane Firearm* applies only to a Rod/Staff/Wand/Martial-Ranged weapon (`reference/expansions/artificer.md`); the Frostbite Shard Dagger granting a "+1d8 to one spell" rider is a designed magic-item ability, internally fine.
- **R6 (S6): wording correct, minor stat deltas.** SRD Zombie *Undead Fortitude* matches S6 exactly ("Constitution saving throw (DC 5 plus the damage taken) unless the damage is Radiant or from a Critical Hit"). Small deviations: SRD Skeleton is AC 14 (S6 uses 13; vulnerable Bludgeoning is correct), SRD Swarm of Rats is HP 14 (S6 uses 24). Likely intentional tuning for a three-hero level-5 party; DM decides whether to align exactly. Low priority.

## Narrative-flow suggestions (need approval; no table events change)

Highest value first.

- **F1 (S4), the single biggest readability win.** The full "Frozen Roads" travel bestiary (a 20-entry d20 table, a gift-box table, and a page of creature write-ups) sits in the read-aloud spine between the bell hunt and Faelan's cottage. It reads as DM prep dropped into the story, and it forward-references barriers the reader has not met yet. Move the deck and creature notes to the Appendix (where the stat blocks already live) and leave a one-line in-story bridge plus a DM pointer. This also fixes the forward-reference.
- **F2 (S7).** The gold-standard session is very long: four hard fights plus a heavy exposition act. Present the two-evening split (the marked breaks after Parts 3 and 5) as the DEFAULT, not a fallback. Break up Vane's "you are the key" monologue into an exchange so Part 3 is not several minutes of the DM talking. And clarify at the Gentle Death that the city's heartbeat "calmed and settled" rather than stopped (a young reader may think the city's heart died, since the Great Governor "beats slow and steady" again next morning).
- **F3 (S2).** Two fights land back-to-back (Mudskips then the Grimfang ambush) before the glade rest. Add a short connective breather between them so the second ambush lands fresh. Also, four NPC info-dumps in a row in the rumor phase; let each kid choose whom to approach.
- **F4 (S3).** The three road fights share one scaffold (scout-check block, creature speaks a menacing line, fight, mote drops, three-hero quip in the same order). Vary the closers so the midsection stays dynamic.
- **F5 (S4).** The three barriers each resolve as "sing the song, then fight." Distinct tones already mitigate this; optionally let the players pick the barrier order for agency.
- **F6 (S6).** Five fights in one day with no long rest; openly offer the short rest after the belltower and treat the cellar as trimmable if table energy flags. Optional: trim one sentence of Lilly's on-the-nose "It is Elaria, guiding us" thesis and let the seven-point stars carry it.
- **F7 (S1).** Fight density before the first rest is real but well-managed (two of four fights are non-lethal by design). The one place the narration removes a choice the mechanics preserve ("no talking their way past a guardian with a grudge and a leek"): if the kids did try to parley, a half-line acknowledging it restores their agency on the page.

## Cross-session patterns worth a deliberate call

- **The "menace line, then fight" and "sing, then fight" templates** recur (S3 road fights, S4 barriers). Individually fine; across the arc they can read as formula. Varying the resolution shape of one encounter per session keeps the chronicle dynamic.
- **Player agency is a genuine strength** in the later sessions (S6 "three threads, any order"; S7 builds the boss plan from the kids' own mouths and refuses to gate the climax on a die). The earlier sessions (S2, S3) are more of a guided corridor, which is normal for low-level travel but worth knowing as the through-line.
- **Prose quality sits at the intended young-adult bar throughout**, with real emotional landings (S1's closing trio image, S4's Milo "bells are like stars," S6's Wicke whistle, S7's Gentle Death). None of it is too gruesome. No em dashes found in the prose.
