# build_ghostbloom_card.py
# Standalone Ghostbloom play aid, sliced straight out of the bestiary's own
# block list so the card at the table can never drift from the book. Emits
# both of her cards: the Sessions 1-7 form and the level-7 rift-arc form.
#   python templates/build_ghostbloom_card.py
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from book_style import build_doc  # noqa: E402
from build_bestiary import B  # noqa: E402


def _is_ghostbloom(blk):
    return (
        blk[0] == "enemy_cards"
        and any(str(c.get("name", "")).startswith("Ghostbloom") for c in blk[1])
    )


def collect():
    """Her cards, each with the italic body line that introduces it."""
    out = []
    for i, blk in enumerate(B):
        if not _is_ghostbloom(blk):
            continue
        # walk back past comments to the nearest preceding body line
        for j in range(i - 1, max(-1, i - 4), -1):
            if B[j][0] == "body":
                out.append(B[j])
                break
        out.append(blk)
    return out


if __name__ == "__main__":
    cards = collect()
    assert len(cards) >= 4, f"expected both Ghostbloom cards, found {len(cards)} blocks"
    blocks = [
        ("h1", "Ghostbloom, Spectral Blossom"),
        ("gold", "*The party's companion, kept current with the bestiary. Her earlier form "
                 "serves the Sessions 1 to 7 chronicle; the level-7 card is the one in play "
                 "from the Earth Rift onward.*"),
    ] + cards
    print("built", build_doc(blocks, "characters/ghostbloom_statblock.docx"))
