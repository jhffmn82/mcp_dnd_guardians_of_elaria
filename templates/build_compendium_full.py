# build_compendium_full.py
# The Guardians of Elaria: THE COMPENDIUM, one merged volume.
#   Part I:   The Bestiary (every creature, companion, and enemy)
#   Part II:  Treasures & Relics (every gift and relic of the road)
#   Part III: Custom Content (house rules, subclasses, hero-paths)
#   Part IV:  The Guardians' Character Sheets (the heroes at level 5)
# Per DM directive the custom content is rolled into the compendium itself.
# Sources: the block lists in build_bestiary.py (B) and build_compendium.py
# (I and C). Those builders still produce their individual docx files but are
# no longer published; this merged volume is the published one.
# Build:  python templates/build_compendium_full.py  ->  compendium/the_compendium.docx
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc
from build_bestiary import B as BESTIARY
from build_compendium import I as TREASURES, C as CUSTOM
from build_sheets import S as SHEETS

NOTE = "A running reference for The Guardians of Elaria. Updated as the chronicle grows."


def part(number, title, blocks, opener=None):
    # Drop the source volume's own titlepage (blocks[0]) and open the part on
    # a fresh page with an h1 divider; the source's gold intro follows it.
    # The h1 carries the page break itself (hardbreak) rather than a separate
    # pagebreak paragraph: a loose break paragraph can spill off a full page
    # and strand an entirely blank page before the part opener.
    # opener: a landscape section-plate placed right under the part heading.
    head = [("h1", f"Part {number}: {title}", {"hardbreak": True})]
    if opener:
        head.append(("img", opener, None, 6.2, {"crop": "3:2", "hmax": 4.2}))
    return head + list(blocks[1:])


FULL = (
    [
        ("titlepage", "THE GUARDIANS OF ELARIA", "THE COMPENDIUM",
         "Bestiary, Treasures, Custom Content & Character Sheets", NOTE),
        # Frontispiece sits ON the title page as a centered vignette (not a
        # separate plate), with the descriptive box beneath it, so page one
        # reads as one composed title spread rather than two half-empty pages.
        ("img", "assets/world/compendium_frontispiece.png",
         "Every wonder of the road, gathered in one book.", 4.0, {"crop": "5:6", "hmax": 3.7}),
        ("gold", "One volume for everything the road has taught the Guardians: every "
                 "creature they have faced, freed, or befriended; every treasure and "
                 "relic they carry; the house rules, homebrew paths, and mysteries "
                 "of this table; and the heroes' own character sheets, ready for the "
                 "table. Four parts, one book, growing with the chronicle."),
    ]
    + part("I", "The Bestiary", BESTIARY)
    + part("II", "Treasures & Relics", TREASURES, opener="assets/world/treasures_opener.png")
    + part("III", "Custom Content", CUSTOM, opener="assets/world/paths_opener.png")
    + part("IV", "The Guardians' Character Sheets", SHEETS)
)

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    print("built", build_doc(FULL, "compendium/the_compendium.docx"))
