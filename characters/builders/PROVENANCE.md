# Character-sheet builders (recovered)

These are the ReportLab scripts that generate the LIVING character-sheet PDFs
(`characters/*_sheet_v3.pdf`), in the real-D&D-sheet layout the DM prefers
(stat boxes, ability columns), not the book's prose style.

## Where they came from
Recovered from `_triage/zips/DnD_Sheets_Bundle.zip`. They were built in an
earlier browser session and were never committed to the repo, so when a
correction was needed the source had to be dug out of a zip. Committing them
here closes that gap: the living-sheet source is now version-controlled.

## Currency
- `build_ursa.py` was recovered STALE (Primal Savagery / Produce Flame; no
  Shillelagh or Starry Wisp) and has since been **synced to the current
  level-5 content and corrected** (2026-07): cantrips are now Shillelagh and
  Starry Wisp; the combat table shows the unlit staff (+3) and the ignited
  Shillelagh (+9); Star Map gives 5 free Guiding Bolts/day (2024 RAW, Wis
  mod); the +1 light aura is stated as allies-only (his own to-hit is +8);
  Wild Resurgence and Spike Growth added; Healing Word is 2d4+5. The file was
  also normalized from `\uXXXX` escapes to real characters. It now
  regenerates the correct `characters/ursa_catchum_sheet_v3.pdf`.
- `build_lilly.py` and `build_stabby.py` looked level-5-current on recovery
  but have NOT been re-synced or re-run; verify before trusting.
- Cosmic Omen is correctly absent (it is a level-6 feature; the party is
  level 5). The authoritative current content lives in
  `templates/build_sheets.py` and `reference/campaign/ursa_kit.md`.
- Note: these sheets predate the book's no-em-dash house rule and still use
  em dashes; a punctuation cleanup is optional and was not done here.

## How to run
    pip install reportlab
    cd characters/builders && python build_ursa.py   # portraits must sit beside the script
