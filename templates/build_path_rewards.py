# build_path_rewards.py
# The Guardians of Elaria: the three level-7 path-reward handouts (v3).
# Single-sourced from build_compendium.py's C list so the handouts can never
# drift from the book again: each handout = titlepage + the shared "The Three
# Doors" intro + that hero's section, with DM-only ("dm", ...) blocks stripped.
# Outputs docx + PDF side by side in characters/path_rewards/.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc
from build_compendium import C
import render_check

NOTE = "A player handout for The Guardians of Elaria. Choose your door with open eyes."

HANDOUTS = [
    ("Warrior of Breathing (Stabby's Path)", "THE THREE DOORS: STABBY",
     "Warrior of Breathing", "characters/path_rewards/warrior_of_breathing_v3"),
    ("Paths of the Stars (Ursa's Path)", "THE THREE DOORS: URSA",
     "Paths of the Stars", "characters/path_rewards/ursa_path_rewards_v3"),
    ("Glimmerstone Artifacts (Lilly's Path)", "THE THREE DOORS: LILLY",
     "Glimmerstone Artifacts", "characters/path_rewards/glimmerstone_artifacts_v3"),
]

def h1_index(blocks, text):
    for i, b in enumerate(blocks):
        if isinstance(b, tuple) and b and b[0] == "h1" and b[1] == text:
            return i
    raise SystemExit(f"h1 not found: {text!r}")

def next_h1(blocks, start):
    for i in range(start + 1, len(blocks)):
        b = blocks[i]
        if isinstance(b, tuple) and b and b[0] == "h1":
            return i
    return len(blocks)

def section(blocks, h1_text):
    i = h1_index(blocks, h1_text)
    return blocks[i:next_h1(blocks, i)]

def strip_dm(blocks):
    return [b for b in blocks if not (isinstance(b, tuple) and b and b[0] == "dm")]

def build():
    # Each handout opens directly on its hero's path (DM directive
    # 2026-07-13): the shared "Three Doors" intro lives in the Compendium
    # only, so the players aren't handed the same two pages three times.
    for h1, kicker, sub, out in HANDOUTS:
        body = strip_dm(section(C, h1))
        blocks = [("titlepage", "THE GUARDIANS OF ELARIA", kicker, sub, NOTE)] + body
        docx = out + ".docx"
        print("built", build_doc(blocks, docx))
        render_check.docx_to_pdf(docx, out + ".pdf")
        print("rendered", out + ".pdf")

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    build()
