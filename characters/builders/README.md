# D&D Character Sheet Bundle — Lilly, Stabby & Ursa

This bundle regenerates the three kids' character sheets. Keep it somewhere safe and
re-upload it to a new Claude chat whenever the party levels up.

## What's inside
- `build_lilly.py`  — Lilly Glimmergear (Artificer/Artillerist), frost-blue, 3 pages
- `build_stabby.py` — Stabby Sharpblade (Monk/Kensei), candy-red, 2 pages
- `build_ursa.py`   — Ursa Catchum (Druid/Circle of Stars), starlight-purple, 3 pages
- Portraits: `lilly_new.png`, `stabby_portrait.png`, `ursa_portrait.png`
  (each script reads its portrait from the same folder)

## How to use in a new chat
1. Start a new chat and upload this whole bundle (the .zip is fine).
2. Tell Claude what changed, e.g.:
   "Bump Ursa to level 6 using 2024 rules — add Cosmic Omen (Weal & Woe),
    update proficiency bonus, HP, and Starry Form, keep the same template.
    Re-run build_ursa.py."
3. Claude edits the relevant script and re-runs it to produce the updated PDF.

## How a sheet is built (for Claude)
Each script is standalone Python using reportlab. To produce a PDF:
    pip install reportlab --break-system-packages
    python3 build_ursa.py        # writes Ursa_Catchum_Sheet.pdf
Portraits must sit in the working directory next to the script.

## Design rules baked in (keep these consistent)
- 2024 D&D rules. Verify every combat number on level-up.
- Kid-friendly language; shared template (Letter size, Helvetica).
- Themes: Lilly frost-blue, Stabby candy-red, Ursa starlight-purple.
- Each kid's Wraithpine relic is "Elaria's gift"
  (Lilly: Pocket Dynamo, Stabby: Sash of the Swift Current, Ursa: Staff of Waking Constellations).
- Casters get a detailed 2-column spellbook page: every spell shows
  action / range / duration / save+DC (or attack) / on-hit vs on-save effect.
- House rule: Ursa's Staff "Starseed" +1d4 applies only to actual druid spells,
  NOT the Starry Form Archer star-arrow.

## Level-up checklist (per character)
- Proficiency bonus (rises at levels 5, 9, 13, 17)
- Max HP (add a hit die + Con per level)
- New class/subclass features at the new level
  (e.g., Ursa: Cosmic Omen / Weal & Woe at level 6; Twinkling Constellations upgrades Starry Form to 2d8 at level 7)
- New spell slots / spells known or prepared
- Cantrip damage scaling (levels 5, 11, 17)
- Re-verify attacks, saves, and skill bonuses against the new numbers
