# build_companion_cards.py
# Standalone play aids for the companion roster, sliced straight out of the
# bestiary's own block list so the card at the table can never drift from the
# book. One document per companion; the handler holds the card, the DM keeps
# the bestiary. Add a roster entry when a new rift companion is designed.
#   python templates/build_companion_cards.py
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from book_style import build_doc  # noqa: E402
from build_bestiary import B  # noqa: E402

# (card-name prefix, output stem, subtitle)
ROSTER = [
    ("Ghostbloom", "ghostbloom_statblock",
     "*The party's companion, kept current with the bestiary. Her earlier form "
     "serves the Sessions 1 to 7 chronicle; the level-7 card is the one in play "
     "from the Earth Rift onward.*"),
    ("Sandshrew", "sandshrew_statblock",
     "*The Earth rift's companion and the roster's tank. It holds ground, takes "
     "the hit meant for a friend, and makes the dirt around it hard to cross.*"),
    ("Piplup", "piplup_statblock",
     "*The Water rift's companion: the one who stops it landing, then undoes what did.*"),
    ("Chimchar", "chimchar_statblock",
     "*The Fire rift's companion and the roster's striker.*"),
    ("Togekiss", "togekiss_statblock",
     "*The Air rift's companion and the roster's controller.*"),
]


def cards_for(prefix):
    """Each matching card, with the italic body line that introduces it."""
    out = []
    for i, blk in enumerate(B):
        if blk[0] != "enemy_cards":
            continue
        if not any(str(c.get("name", "")).startswith(prefix) for c in blk[1]):
            continue
        for j in range(i - 1, max(-1, i - 4), -1):
            if B[j][0] == "body":
                out.append(B[j])
                break
        out.append(blk)
    return out


if __name__ == "__main__":
    for prefix, stem, sub in ROSTER:
        found = cards_for(prefix)
        assert found, f"no bestiary card found for {prefix}"
        # the bestiary's italic lead-in duplicates the roster subtitle on a
        # standalone card and can push a tall card onto a second page
        found = [b for b in found if b[0] != "body"]
        blocks = [("h1", prefix), ("gold", sub)] + found
        print("built", build_doc(blocks, f"characters/{stem}.docx"))
