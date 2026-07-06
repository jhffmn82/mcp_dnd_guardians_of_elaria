# publish.py
# Assembles the finished book: rebuilds every source docx, then renders an
# ordered set of PDFs into the repo root so the GitHub file listing reads as
# the table of contents. Numeric prefixes force reading order.
import os, sys, subprocess
sys.path.insert(0, os.path.dirname(__file__))
import render_check

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

# (source docx, root pdf name in reading order)
BOOK = [
    ("frontmatter/foreword.docx",                      "01_Foreword_and_the_Guardians.pdf"),
    ("frontmatter/lore_primer.docx",                   "02_The_World_of_Elaria.pdf"),
    ("sessions/session_01_gathering_of_friends.docx",  "03_Session_1_The_Gathering_of_Friends.pdf"),
    ("sessions/session_02_oakshade_village.docx",      "04_Session_2_The_Road_to_Ravenstone.pdf"),
    ("sessions/session_03_quest_for_knowledge.docx",   "05_Session_3_The_Quest_for_Knowledge.pdf"),
    ("sessions/session_04_shadows_and_songs.docx",     "06_Session_4_Awakening_to_Shadows_and_Songs.pdf"),
    ("sessions/session_05_curse_of_davy_jones.docx",   "07_Session_5_The_Curse_of_Davy_Jones.pdf"),
    ("sessions/session_06_wraithpine.docx",            "08_Session_6_Lanterns_in_the_Fog.pdf"),
    ("sessions/session_08_gearhaven.docx",             "09_Session_8_Gearhaven_the_Clockwork_City.pdf"),
    ("compendium/bestiary.docx",                       "10_Compendium_I_Bestiary.pdf"),
    ("compendium/treasures_and_relics.docx",           "11_Compendium_II_Treasures_and_Relics.pdf"),
    ("compendium/custom_compendium.docx",              "12_Compendium_III_Custom_Content.pdf"),
]

# Source builders to run first (session 8 has no builder; it is edited in place).
BUILDERS = [
    "build_foreword.py", "build_lore.py",
    "build_session_01.py", "build_session_02.py", "build_session_03.py",
    "build_session_04.py", "build_session_05.py", "build_session_06.py",
    "build_compendium.py",
]

def rebuild_sources():
    for b in BUILDERS:
        r = subprocess.run([sys.executable, os.path.join("templates", b)],
                           capture_output=True, text=True)
        tag = "ok" if r.returncode == 0 else "FAIL"
        print(f"  [{tag}] {b}", r.stderr.strip()[:200] if r.returncode else "")

def render_book():
    for src, pdf in BOOK:
        if not os.path.exists(src):
            print(f"  MISSING {src}"); continue
        render_check.docx_to_pdf(src, os.path.join(ROOT, pdf))
        print(f"  {pdf}")

if __name__ == "__main__":
    if "--pdf-only" not in sys.argv:
        print("rebuilding sources...")
        rebuild_sources()
    print("rendering book PDFs to repo root...")
    render_book()
    print("done")
