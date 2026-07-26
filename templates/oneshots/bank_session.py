# bank_session.py: write the 2026-07-18 decisions into the repo's memory so
# the next session inherits them instead of re-deriving them from a stale doc.
import os
os.chdir(r"C:\Users\jhffm\dnd-campaign")

# ---- 1. campaign_canon.md: reverse the choose-1-of-3 directive (2 places) ----
p = "memory/campaign_canon.md"
t = open(p, encoding="utf-8").read()

old = ("- **PLANNED (DM directive 2026-07-06)**: after Session 8 is played, offer the party a NEW "
       "Pokemon-style companion, ideally another choose-1-of-3 (echoing Aelwyn's offer), to "
       "support the rift arcs. Fold into Session 8/9 prep.")
new = ("- **COMPANION ROSTER (DM, 2026-07-18; SUPERSEDES the 07-06 choose-1-of-3 directive)**: there "
       "is no three-way offer and nothing is caught. Each rift grants ONE designed companion, and "
       "the gathered essence takes form back home: Ghostbloom steps into the Essence Sphere as the "
       "tether (the Sphere holds only one physical form at a time) and the new creature manifests. "
       "Aelwyn briefs the party on the plane's wildlife beforehand and explains the mechanics "
       "afterward. Final roster of 6 = Ghostbloom + Earth tank (Sandshrew) + Water healer + Fire "
       "striker + Air controller + Pikachu (Session 12, revealed as Ash's). Companions are real "
       "Pokemon given 5e statblocks; art is a realistic-fantasy reinterpretation via the genart.py "
       "reference workflow, never pasted official art.")
assert old in t, "canon:51 directive not found"
t = t.replace(old, new, 1)

old2 = ("11. SESSION 8 MUST-DOS: mention Stabby's idol (found in his bag after Wraithpine, C13); "
        "plan the new companion choose-1-of-3 for after S8 (C4 directive).")
new2 = ("11. SESSION 8 MUST-DOS: mention Stabby's idol (found in his bag after Wraithpine, C13); "
        "the Earth companion (Sandshrew) manifests from the gathered essence in the homecoming "
        "scene, with Ghostbloom entering the Sphere as tether. The old choose-1-of-3 plan is "
        "retired (DM, 2026-07-18).")
assert old2 in t, "canon:125 must-do not found"
t = t.replace(old2, new2, 1)
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("campaign_canon.md: 2 reversals written")

# ---- 2. house_rules.md: today's document rulings ----
p = "memory/house_rules.md"
t = open(p, encoding="utf-8").read()
add = """
- Companion pass (DM, 2026-07-18): Ghostbloom gains a LEVEL 7 card kept alongside her original (AC 16, HP 62, +8, DC 16, one more die on Guardian's Light and the Ghostly Wail); her original card still serves the Sessions 1-7 chronicle. DREAD SHROUD is cut from every version of her: it duplicated the Frightened condition her Spectral Lash rider already imposes twice a round, at will, on a Bonus Action. Companion cards are generated from the bestiary by templates/build_companion_cards.py so a table card can never drift from the book.
- Companion power anchor (DM, 2026-07-18): a companion should outclass a 4th-level summon spell, be GM-run, and augment the team without taking the spotlight from the players. The "Sprout/Bloom/Radiant" tier table and the "~14 damage per turn" ceiling in lore/rift_run_design.md were never DM-authored; do not cite them.
- Sandshrew, the Earth companion (DM, 2026-07-18): the roster's tank. Sand Veil, Curl Up (Reaction, reduce a hit by 10, applied BEFORE resistance), Multiattack, Challenge (Bonus Action, ONE enemy within 30 ft, Disadvantage on attacks against anyone but him), Earthquake (Action, 20-ft Cube, DC 15 Dex, 3d6, Difficult Terrain for one round). No expendable uses: the Action and the Reaction are the whole limiter.
- Printed-text rulings confirmed in play (2026-07-18): the Water ignite rider reads "whenever you hit a target with IT", so Stabby's Bonus Action Unarmed Strike does NOT carry the +2 Cold; Counter-Bolt triggers only on attacks against an ALLY, never Lilly herself; Boomstick is a repeating pistol at 30/90, so Fire Bolt is the long-range option; the Sentinel's Guardian Protocol reaches only 15 ft from the Sentinel, so it must walk with the melee; Ursa carries the Warden glow to the fight rather than standing behind it.
"""
assert add.strip().splitlines()[0] not in t, "already banked"
open(p, "w", encoding="utf-8", newline="\n").write(t.rstrip() + "\n" + add)
print("house_rules.md: rulings appended")

# ---- 3. provenance banner on the stale design doc ----
p = "lore/rift_run_design.md"
t = open(p, encoding="utf-8").read()
banner = """> **PROVENANCE WARNING (2026-07-18).** Most of this document was AI-drafted in a single prior session and committed as canon without DM review. An audit found exactly ONE dated DM marker in it. Treat only dated DM rulings here as authoritative. The design of record is the `rift-run-pokemon-design` memory (2026-07-10) plus the rulings in `memory/house_rules.md` and `memory/campaign_canon.md`; where this document disagrees with those, they win. KNOWN DEAD SECTIONS: the catch procedure and Gathering check (nothing is caught; the essence manifests at home), the choose-1-of-3 offer (retired), the Sprout/Bloom/Radiant growth table and the ~14 damage ceiling (never DM-authored), the invented "stone-shell" companion (replaced by Sandshrew), and the invented Terranox-style boss (the Earth boss is Groudon). A full rebuild is pending.

"""
marker = "*The Guardians of Elaria, a family D&D campaign on 2024 revised 5e."
i = t.find(marker)
assert i > 0, "doc intro not found"
j = t.find("\n\n", i) + 2
t = t[:j] + banner + t[j:]
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("rift_run_design.md: provenance banner added")
