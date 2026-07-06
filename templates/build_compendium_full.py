# build_compendium_full.py
# The Guardians of Elaria: THE COMPENDIUM, one merged volume.
#   Part I:   The Bestiary (every creature, companion, and enemy)
#   Part II:  Treasures & Relics (every gift and relic of the road)
#   Part III: Custom Content (house rules, subclasses, hero-paths)
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

NOTE = "A running reference for The Guardians of Elaria. Updated as the chronicle grows."


def part(number, title, blocks):
    # Drop the source volume's own titlepage (blocks[0]) and open the part on
    # a fresh page with an h1 divider; the source's gold intro follows it.
    return [("pagebreak",), ("h1", f"Part {number}: {title}")] + list(blocks[1:])


FULL = (
    [
        ("titlepage", "THE GUARDIANS OF ELARIA", "THE COMPENDIUM",
         "Bestiary, Treasures, and Custom Content", NOTE),
        ("gold", "One volume for everything the road has taught the Guardians: every "
                 "creature they have faced, freed, or befriended; every treasure and "
                 "relic they carry; and the house rules, homebrew paths, and mysteries "
                 "of this table. Three parts, one book, growing with the chronicle."),
    ]
    + part("I", "The Bestiary", BESTIARY)
    + part("II", "Treasures & Relics", TREASURES)
    + part("III", "Custom Content", CUSTOM)
)

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    print("built", build_doc(FULL, "compendium/the_compendium.docx"))
