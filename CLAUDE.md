# The Guardians of Elaria — Campaign Repo

Family D&D campaign (2024 rules) run by Justin (the DM) for his kids. This repo is the single source of truth for all campaign material. The long-term goal is a complete, consistent, well-organized campaign archive that can someday be compiled into a keepsake book for the kids.

## Current state of this repo

Phases 1 and 2 are complete. The repo uses the target layout: `sessions/`, `lore/`, `characters/` (with `path_rewards/` and `historical/`), `assets/` (with `image_manifest.md` preserving all original filenames and DALL-E prompts), `handoffs/`, `memory/`, `templates/`, `_triage/` (superseded drafts, duplicates, zips, third-party reference images). INVENTORY.md describes the pre-reorganization state; `assets/image_manifest.md` maps every old path to its new one.

The `memory/` folder is live and must be maintained:
- `memory/campaign_canon.md` — world state, timeline, NPCs, locations, relics, factions, plot threads
- `memory/session_log.md` — one short entry per session (5-10 lines), newest last
- `memory/house_rules.md` — house rules plus standing DM document rulings

## The party (all level 5 as of Session 8)

- **Lilly Glimmergear** — deep gnome Artificer (Artillerist), accent color frost-blue, relic: Pocket Dynamo
- **Stabby Sharpblade** — goblin Monk (Kensei), accent color candy-red, relic: Sash of the Swift Current
- **Ursa Catchum** — human Druid (Circle of Stars), accent color starlight-purple, relic: Staff of Waking Constellations

All three relics came from a single Wraithpine chest as Elaria's gift (one chest, three relics; Session 6 text is explicit). A year-apart timeskip to level 7 is planned after Session 8, with individual path reward documents (Ursa's includes a custom "Warden" constellation for Starlit Channeler).

**Session numbering (DM-adjudicated 2026-07-05):** the Wraithpine / False Hydra arc was Session 6 only; there was never a Session 7 at the table. Gearhaven keeps its "Session 8" branding. The played sequence is 1, 2, 3, 4, 5, 6, 8. Do not renumber Session 8 and do not flag the 6-to-8 gap as a contradiction.

**Level timeline (DM-confirmed points; refine during Phase 3):** the party started at level 3 in Session 1. They are level 5 as of Session 8, and the planned timeskip takes them to 7. The "pre 4 / post 4" sheets in Old blocks are pre- and post-SESSION-4 snapshots (DM confirmed), bracketing the Session 4 item rewards and any level-up that came with it. Pin the exact 3-to-4 and 4-to-5 level-up moments from session text during canon extraction, and flag with [DM CHECK] if the docs do not settle them.

## House rules and standing rulings (seed for memory/house_rules.md)

1. Ursa's Starseed +1d4 applies only to actual druid spells, NOT the Starry Form Archer luminous arrow.
2. Patient Defense (Monk) grants a free Disengage, not Dodge.
3. Shillelagh replaces Primal Savagery on Ursa's sheet (2024 rules).
4. Goodberry: eating a berry is a Bonus Action (2024).
5. Air spirit HP is 20.
6. Deep gnome uses the current 2024-era printing.

## Rules of engagement

- 2024 (revised 5e) rules only. Where 2014 and 2024 text conflict, 2024 wins.
- House rules override RAW. Never regress the RAW fixes above when revising documents.
- **Never invent campaign events.** When revising sessions 1-7: fix consistency, names, lore, and formatting only. Never change what happened at the table. When in doubt, flag it in the document with [DM CHECK: ...] instead of changing it.
- **Recency wins.** The project evolved over time and fixes were never back-populated, so the newest documents (Session_8_Gearhaven_v2, Campaign_Handoff_v2) are the most accurate. When older and newer docs conflict, the newer one is canon.
- **Fix clear inconsistencies without asking** (spelling drift, name drift, stale titles, rules drift): apply the recency rule and correct silently. Reserve CONTRADICTIONS.md and [DM CHECK] flags for genuinely ambiguous questions about what actually happened at the table.
- Session 8 (`sessions/session_08_gearhaven.docx`, formerly Session_8_Gearhaven_v2) is the gold-standard format. All session revisions target that structure.
- Content is for kids: adventurous tone, real stakes, never gruesome.
- No em dashes in any generated document; use commas, colons, semicolons, or parentheses.
- Destructive operations: never delete files. Move unclear or superseded files to `_triage/`. Use `git mv` for renames so history is preserved.
- Commit at the end of every work phase with a descriptive message, and push.

## Phase workflow

Work proceeds in phases, ideally one phase per session. Check git log / INVENTORY.md to see where things stand.

**Phase 1 — Inventory (read-only).** Read everything, change nothing. Produce INVENTORY.md: every file, its type (session doc, lore, handoff, art, character sheet, duplicate, junk), and which session/character it relates to. Flag duplicates, unclassifiable files, and anything referenced but missing. Specifically: locate Session 6 if it exists anywhere, and list all image files with long DALL-E prompt filenames.

**Phase 2 — Reorganize.** Plan first, then execute with approval. Target layout: `sessions/`, `lore/`, `characters/`, `assets/`, `handoffs/`, `memory/`, `templates/`, `_triage/`. Rename to consistent patterns (`session_03_title.docx`). Rename long DALL-E-prompt image filenames to short descriptive names, and record every original filename → new filename mapping in `assets/image_manifest.md` (the original filenames are the art generation prompts and must be preserved there).

**Phase 3 — Canon extraction.** Read all session and lore docs. Build out `memory/campaign_canon.md`. Produce CONTRADICTIONS.md listing every cross-session inconsistency (name spellings, timeline conflicts, NPC drift, rules drift) for DM adjudication. Do not resolve contradictions unilaterally.

**Phase 4 — Format lockdown and session revision.** Extract the Session 8 structure into `templates/session_template.md`. Then revise ONE session per work session to match the template and adjudicated canon, showing diffs, committing each separately.

**Phase 5 — The keepsake compilation.** Only after 1-8 are revised and consistent: compile "The Guardians of Elaria: The Complete Chronicle" as a single polished document.

## Keepsake deliverable requirements (running list)

- A campaign timeline outline: the party's level at each point and the major events of each session (build during Phase 3 into memory/campaign_canon.md).
- Historical character sheets: old sheets are kept as per-level snapshots, normalized to a consistent format. The DM will supply missing old sheets. Do not bury old sheets in _triage as junk; they are chronicle material.
- Art: track illustration gaps per session; new graphics will be generated as work proceeds. Fleshing out prose is welcome but must never invent table events.

## After each real-world game session

Append an entry to `memory/session_log.md` and update `memory/campaign_canon.md` if world state changed.
