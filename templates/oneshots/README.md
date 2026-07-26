# One-shot build scripts (recovered)

These are single-purpose scripts that were written during campaign build sessions to generate or patch specific pieces of content, then set aside. They are **not** part of the active `publish.py` pipeline; they are preserved here so the work is reproducible and nothing is lost.

## Provenance

Recovered on 2026-07-26 from the raw Claude Code session log of the 2026-07-06 "Phase 4" build session (conversation `d55dee86`). They had been written to that session's scratchpad and never committed, so they existed only inside the raw session log until this recovery. Reconstructed by replaying the session's `Write`/`Edit` tool stream (see `claude-archive/scripts/extract_code_artifacts.py`).

## Caveat

They were written to run from a scratchpad next to a copy of the repo, using `sys.path` and `os.chdir` tricks to import from `templates/` and write into `characters/`, `lore/`, etc. Run from this new location they may need path adjustments. They are kept for reference and reuse, not as drop-in tools.

## What each does (from its own header/content)

- `patch_sandshrew.py`, `patch_shrew2.py`, `patch_shrew3.py` — iterative patches to the Sandshrew statblock.
- `patch_stormcell.py`, `patch_stormarc.py`, `patch_stormarc2.py` — Storm-arc content patches.
- `patch_l7_cards.py` — level-7 hero card patches.
- `patch_ursa_sheet.py` — patch to Ursa's character sheet.
- `patch_gb_art.py`, `patch_drop_shroud.py` — Ghostbloom art / content patches.
- `preview_trio.py` — render a three-up preview of cards/sheets.
- `reorg.py` — a repository reorganization helper.
- `bank_session.py` — session-banking helper.
- `gen/` — one-shot art/asset generators: `batch_final.py`, `batch_gaps.py`, `compendium_art_gen.py`, `crystalbrook_gen.py`, `map_gen.py`, `map_relics_gen.py`, `s4_extras_gen.py`, `s6_departure_gen.py`, `undead_gen.py`, `vigil_dawn_gen.py`.
