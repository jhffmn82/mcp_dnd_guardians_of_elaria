# The Guardians of Elaria — Campaign Repo

Family D&D campaign (2024 rules) run by Justin (the DM) for his kids. This repo is the single source of truth for all campaign material. The long-term goal is a complete, consistent, well-organized campaign archive that can someday be compiled into a keepsake book for the kids.

## Current state of this repo

This folder is mid-reorganization. It contains original files in their raw layout (session docs at root, `Pictures/`, `Character Sheets/`, `old stuff/`, `session 8/`, etc.). Do not assume a clean structure; consult INVENTORY.md if it exists, or generate it (see Phase 1).

If the `memory/` folder or any of its files do not exist yet, create them:
- `memory/campaign_canon.md` — world state, timeline, NPCs, locations, relics, factions, plot threads
- `memory/session_log.md` — one short entry per session (5-10 lines), newest last
- `memory/house_rules.md` — seed it with the rulings in the House Rules section below, then maintain it there

## The party (all level 5 as of Session 8)

- **Lilly Glimmergear** — deep gnome Artificer (Artillerist), accent color frost-blue, relic: Pocket Dynamo
- **Stabby Sharpblade** — goblin Monk (Kensei), accent color candy-red, relic: Sash of the Swift Current
- **Ursa Catchum** — human Druid (Circle of Stars), accent color starlight-purple, relic: Staff of Waking Constellations

All three relics came from Wraithpine chests as Elaria's gift. A year-apart timeskip to level 7 is planned after Session 8, with individual path reward documents (Ursa's includes a custom "Warden" constellation for Starlit Channeler).

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
- The DM adjudicates all lore contradictions. Collect them in CONTRADICTIONS.md; do not silently pick a winner.
- Session 8 (Session_8_Gearhaven_v2) is the gold-standard format. All session revisions target that structure.
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

## After each real-world game session

Append an entry to `memory/session_log.md` and update `memory/campaign_canon.md` if world state changed.
