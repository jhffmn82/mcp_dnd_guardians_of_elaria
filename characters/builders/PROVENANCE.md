# Character-sheet builders (recovered)

These are the ReportLab scripts that generate the LIVING character-sheet PDFs
(`characters/*_sheet_v3.pdf`), in the real-D&D-sheet layout the DM prefers
(stat boxes, ability columns), not the book's prose style.

## Where they came from
Recovered from `_triage/zips/DnD_Sheets_Bundle.zip`. They were built in an
earlier browser session and were never committed to the repo, so when a
correction was needed the source had to be dug out of a zip. Committing them
here closes that gap: the living-sheet source is now version-controlled.

## IMPORTANT: currency
This is NOT the latest version of every builder. Verified on recovery:
- `build_ursa.py` is a STALE snapshot: it still has Primal Savagery and
  Produce Flame, and lacks Shillelagh, Cosmic Omen, and Starry Wisp. The
  current `characters/ursa_catchum_sheet_v3.pdf` was made by a LATER builder
  (with those features, plus the "+8 (9)" aura and "3 from the Star Map"
  numbers) that lived in a later session and is NOT in this zip.
- `build_lilly.py` and `build_stabby.py` look level-5-current on recovery,
  but verify before trusting.

So regenerating a CORRECT current Ursa sheet requires updating this builder's
content to match the live sheet and applying the corrections (Star Map 5 per
2024 RAW; the +1 light aura is allies-only, so his own to-hit is +8/+9 with
no self bonus). The authoritative current content lives in
`templates/build_sheets.py` and `reference/campaign/ursa_kit.md`.

## How to run
    pip install reportlab
    cd characters/builders && python build_ursa.py   # portraits must sit beside the script
