# preview_trio.py: render the Beast Handler "Signature Three" entry as it
# would appear in the book, for DM format approval. Not part of the repo.
# v2: ONE combined UA-anatomy stat block (banded headers, labeled rows,
# ability table, "(Partner Only)" entries), Growing Together dropped.
import os, sys
REPO = r"C:\Users\jhffm\dnd-campaign"
sys.path.insert(0, os.path.join(REPO, "templates"))
os.chdir(REPO)
from book_style import build_doc

SP = r"C:\Users\jhffm\AppData\Local\Temp\claude\C--Users-jhffm-dnd-campaign\d55dee86-bf0a-4655-8235-d6a529a61fc9\scratchpad"

B = [
    ("h2", "Beast Handler: The Living World (the road into the wild)"),
    ("gold", "*“You went out to learn the speech of wild things. You came back, and three "
             "of them followed you home.”*"),
    ("stat", "Beast Handler (feat)", [
        "*Story Feat*",
        "You gain the following benefits.",
        "**Mightier Summons.** Whenever you cast the Summon Beast spell, the spell takes "
        "effect as if you had cast it using a spell slot of the highest level you can cast, "
        "without expending a slot of that level.",
        "**Signature Partners.** Your Summon Beast spell no longer conjures a nameless "
        "spirit. When you cast the spell, one of your three partners answers the call: "
        "Arcanine, Lapras, or Noctowl. The partner uses the Signature Partner stat block "
        "below, with the traits and actions marked for it.",
        "**Wild Speech.** You and any beast you summon can communicate simple ideas with "
        "each other telepathically.",
    ]),
    ("body", "*Ursa walked the wild year with three companions, and they answer his call "
             "still. These are not spirits wearing borrowed shapes; they are his friends, and "
             "he named each one the day it chose him.*"),
    ("ua_stat", {
        "name": "Signature Partner",
        "type_line": "Beast (Arcanine: Medium, Land. Lapras: Large, Water. Noctowl: Small, Air), Unaligned",
        "top": [
            ("Armor Class", "11 + the level of the spell (natural armor)"),
            ("Hit Points", "30 + 10 for each spell level above 2nd (Noctowl: 20 + 10 for "
             "each spell level above 2nd)"),
            ("Speed", "40 ft., climb 40 ft. (Arcanine only); 30 ft., swim 40 ft. (Lapras "
             "only); 20 ft., fly 60 ft. (Noctowl only)"),
        ],
        "abilities": [("STR", "18 (+4)"), ("DEX", "11 (+0)"), ("CON", "16 (+3)"),
                      ("INT", "4 (−3)"), ("WIS", "14 (+2)"), ("CHA", "5 (−3)")],
        "meta": [
            ("Senses", "darkvision 60 ft., passive Perception 12"),
            ("Languages", "understands the languages you speak"),
            ("Challenge", "—"),
            ("Proficiency Bonus", "equals your bonus"),
        ],
        "sections": [
            ("Traits", [
                ("Intimidate (Arcanine Only)",
                 "When the partner appears, each enemy within 15 feet of it must succeed "
                 "on a Wisdom saving throw against your spell save DC or take a −2 penalty "
                 "to attack rolls until the end of its next turn."),
                ("Shell Armor (Lapras Only)",
                 "Attack rolls against the partner can't be Critical Hits."),
                ("Keen Eye (Noctowl Only)",
                 "The partner's attack rolls can't have Disadvantage, and its sight isn't "
                 "impeded by Dim Light or Darkness."),
                ("Flyby (Noctowl Only)",
                 "The partner doesn't provoke Opportunity Attacks when it flies out of an "
                 "enemy's reach."),
            ]),
            ("Actions", [
                ("Multiattack",
                 "The partner makes a number of Rend attacks equal to half this spell's "
                 "level (rounded down)."),
                ("Rend",
                 "*Melee Attack Roll:* your spell attack modifier, reach 5 ft. *Hit:* "
                 "1d8 + 4 + the spell's level Slashing damage."),
                ("Extreme Speed (Arcanine Only)",
                 "The partner moves up to its Speed without provoking Opportunity Attacks "
                 "and makes one Rend attack. On a hit, the target takes extra Fire damage "
                 "equal to twice the spell's level."),
                ("Ice Beam (Lapras Only)",
                 "When the partner uses Multiattack, it can replace any Rend with an Ice "
                 "Beam. *Ranged Attack Roll:* your spell attack modifier, range 60 ft. "
                 "*Hit:* 1d8 + 4 + the spell's level Cold damage, and the target's Speed "
                 "decreases by 10 feet until the start of the partner's next turn."),
                ("Hypnosis (Noctowl Only; Recharge 5–6)",
                 "One creature the partner can see within 30 feet must succeed on a Wisdom "
                 "saving throw against your spell save DC or have the Incapacitated "
                 "condition until the end of the partner's next turn or until it takes "
                 "damage."),
            ]),
        ],
    }),
    ("body", "**Arcanine.** *Legendary for its speed, it is said to run six thousand miles "
             "in a day and a night, driven by a flame that burns within. The old tales say "
             "folk stood entranced just watching it run.*"),
    ("body", "**Lapras.** *Intelligent enough to understand speech, it ferries travelers "
             "across cold water on its broad back, and it sings where sailors can hear.*"),
    ("body", "**Noctowl.** *Its eyes see by the faintest starlight, its head turns all the "
             "way around when it thinks, and its wings make no sound at all.*"),
    ("stat", "The Wildheart Token", [
        "*Wondrous Item (carved by his own hand)*",
        "Three small totems strung on one leather cord, one for each partner, whittled "
        "beside the wild year's campfires. When a partner you summoned would drop to 0 "
        "Hit Points, it drops to 1 Hit Point instead. Once this property is used, it "
        "can't be used again until the next dawn.",
    ]),
]

out_docx = os.path.join(SP, "preview_trio.docx")
print("built", build_doc(B, out_docx))
import render_check
out_pdf = os.path.join(SP, "preview_trio.pdf")
render_check.docx_to_pdf(out_docx, out_pdf)
print("rendered", out_pdf)

import base64, fitz
doc = fitz.open(out_pdf)
imgs = []
for i, page in enumerate(doc, 1):
    pix = page.get_pixmap(dpi=185)
    png = os.path.join(SP, f"preview_trio_p{i}.png")
    pix.save(png)
    imgs.append(base64.b64encode(pix.tobytes("png")).decode())
    print("page", i, "->", png)

parts = ["""<style>
  .wrap { max-width: 1180px; margin: 0 auto; padding: 1.5rem 1rem 3rem; font-family: Georgia, serif; color:#2a2118; }
  .masthead { text-align:center; border-bottom:2px solid #b8860b; padding-bottom:.8rem; margin-bottom:1.4rem; }
  .kicker { font-size:.72rem; letter-spacing:.28em; text-transform:uppercase; color:#8a6d1f; margin:0; }
  h1 { font-size:1.6rem; font-weight:600; color:#7a4a12; margin:.2rem 0 .2rem; }
  .note { font-size:.9rem; font-style:italic; color:#6b5d45; margin:0; }
  .page { margin:0 0 2rem; border:1px solid #e6dcc4; border-radius:10px; overflow:hidden; box-shadow:0 2px 10px rgba(0,0,0,.08); }
  .page img { display:block; width:100%; height:auto; }
  @media (prefers-color-scheme: dark) {
    .wrap { color:#e8dfce; } h1 { color:#e0b658; } .kicker { color:#c99f4a; } .note { color:#b3a179; }
    .page { border-color:#4a3d22; }
  }
</style>
<div class="wrap">
  <header class="masthead">
    <p class="kicker">The Guardians of Elaria &middot; format preview v2</p>
    <h1>Beast Handler: The Signature Three</h1>
    <p class="note">One combined summon-style stat block, official anatomy: banded headers, ability table, (Partner Only) entries. Growing Together dropped; the formulas carry the growth.</p>
  </header>"""]
for i, b in enumerate(imgs, 1):
    parts.append(f'  <figure class="page"><img src="data:image/png;base64,{b}" alt="page {i}"/></figure>')
parts.append("</div>")
open(os.path.join(SP, "beast_handler_preview.html"), "w", encoding="utf-8").write("\n".join(parts))
print("wrote beast_handler_preview.html")
