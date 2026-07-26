# build_hero_sheets.py
# The living, printable table copies, one standalone PDF per hero, sliced
# from the SAME block list that builds the book's Part IV (build_sheets.S).
# This makes the code the single source of truth: the book's compendium and
# each kid's table sheet come from one place and cannot drift. Aurora Builder
# (characters/source_dnd5e/*.dnd5e) remains the rules/leveling engine; the
# hand-made characters/*_sheet_v3.pdf originals retire to historical/.
#   python templates/build_hero_sheets.py            # -> characters/<hero>_sheet.pdf
#   python templates/build_hero_sheets.py --preview  # -> art_review/<hero>_sheet.pdf
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from book_style import build_doc  # noqa: E402
from build_sheets import S  # noqa: E402
import render_check  # noqa: E402

NOTE = "A living table copy for The Guardians of Elaria. Regenerated from the campaign source."

# (h1 heading in S, output stem, subtitle)
HEROES = [
    ("Lilly Glimmergear", "lilly_glimmergear_sheet", "Deep Gnome Artificer (Artillerist), Level 5"),
    ("Stabby Sharpblade", "stabby_sharpblade_sheet", "Goblin Monk (Way of the Kensei), Level 5"),
    ("Ursa Catchum", "ursa_catchum_sheet", "Human Druid (Circle of the Stars), Level 5"),
]


def _h1_indices():
    return [i for i, b in enumerate(S) if b[0] == "h1"]


def slice_for(heading):
    """The blocks from this hero's h1 up to (not including) the next h1."""
    starts = _h1_indices()
    at = next(i for i in starts if S[i][1] == heading)
    nxt = next((i for i in starts if i > at), len(S))
    return S[at:nxt]


if __name__ == "__main__":
    preview = "--preview" in sys.argv
    out_dir = "art_review" if preview else "characters"
    for heading, stem, sub in HEROES:
        # The slice already opens with the hero's h1, portrait, and class line,
        # so it needs no separate cover: that would just duplicate the name and
        # cost a page. A one-line running note sits under the h1 instead.
        body = slice_for(heading)
        blocks = list(body)
        blocks.insert(1, ("body", f"*{NOTE}*"))
        docx = f"{out_dir}/{stem}.docx"
        build_doc(blocks, docx)
        render_check.docx_to_pdf(docx, f"{out_dir}/{stem}.pdf")
        print("built", f"{out_dir}/{stem}.pdf")
