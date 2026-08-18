# Session Template (extracted from Session 7, the gold standard)

Every revised session document follows this structure and the house style implemented in `templates/book_style.py`. Build scripts live in `templates/build_session_NN.py`; run them with python to regenerate the docx.

## Page and type

- US Letter (12240 x 15840 twips), margins: 1 inch sides, 0.75 inch top/bottom.
- Body: Georgia 10.5pt, ink #222222. Captions: 9pt gray italic (#888888), centered.
- H1 (part titles): 16pt bold goldenrod #B8860B, page break before each part after the first.
- H2 (scene beats): 13pt bold sienna #A0522D.
- Footer: centered "✦ page ✦" in gray.
- Dividers between parts: centered "✦ ✦ ✦" in goldenrod.

## Voice and boxes

- GOLD boxes (fill #FBF6EA, 2.25pt goldenrod left rule): the story itself, read aloud at the table. Second person, present tense, warm storybook voice. NPC dialogue lives here with the speaker bolded.
- HERO lines: suggested player-character lines inside gold boxes, name bolded in that kid's accent color (Lilly #1F6FB8, Stabby #A32B2B, Ursa #5B2A86, Ghostbloom #1F7A78).
- PURPLE boxes (fill #F4F0FA, purple left rule, 9.5pt, "▶" prefix): brief table notes only: a check and its DC, a fight's shape, a boon gained. No tactics essays, no branching trees, no XP bookkeeping. The chronicle records what happened.
- STAT boxes (fill #FCF6F6, crimson left rule): compact appendix statblocks, one title line + a few 9pt lines.
- BRIDGE paragraphs: italic third-person past-tense connective tissue after dividers.

## Document skeleton

1. Title block: ✦ ✦ ✦ / THE GUARDIANS OF ELARIA / SESSION N / Session Title / gray note "An illustrated adventure. Read the gold boxes aloud; the purple boxes are for the DM."
2. "Previously, on The Guardians of Elaria..." recap in gold (Session 1 opens with "Our story begins" instead).
3. Parts (3-6 per session), each: H1 with page break, H2 scene beats, gold narration, sparse purple notes, one to three images with captions per part.
4. Closing bridge: where the heroes are headed next.
5. Appendix: "Creatures of this Session" compact stat boxes (full detail lives in compendium/bestiary).

## Content rules

- Canon per memory/campaign_canon.md and CONTRADICTIONS.md rulings; house rules never regressed.
- No em dashes anywhere. No "if the party..." branches: adjudicated outcomes only.
- Added lore is welcome where it enriches (per DM 2026-07-06) but never changes table events.
- Kids-safe: adventurous, real stakes, never gruesome.
- Images come from assets/; every image used should exist in the manifest.

## Combat sections (DM-adjudicated 2026-08-18, from the Session 8 rework)

The DM runs combat live; the page supports him, it does not script him. Model
is Session 7's running block, proven again in Session 8:

1. Ambiance read-alouds going INTO the fight (vivid, natural voice).
2. Optionally one dm block offering 2-4 short character lines the kids can grab.
3. ONE "Running the Fight" sequence of terse dm pointers: **Battlefield** /
   **The pressure** / **The lever** / **Companions** / **Describe cues** (one
   line per big sensory beat, for the DM to improvise from) / **Scaling dials**
   (too easy / too hard).
4. A SHORT exit read-aloud at the pivot out of combat.

Never place a "when X happens, read the following" script inside combat; fold
that imagery into a describe cue. Prose everywhere: natural storytelling voice,
no aphorism chains, no trailer fragments; at most one turned phrase per section.
