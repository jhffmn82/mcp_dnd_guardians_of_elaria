# Simulator handoff

State as of 2026-09-06. Read `ENCOUNTER_VALIDATION.md` first for the method; this
file is what has been measured, what is decided, and what is still open.

---

## 1. Where things stand

**Session 8 (Underroot) is validated and stable.** 400 days, canonical config
(`S8_COMPANION=ghostbloom S8_COHESION=1 S8_WITHER=1 S8_LILLY_AID=1`):

```
net damage 195.3 +/-5.2   rounds 14.43   knockdowns 0.030   wipes 0/400
```

**Session 9 (the Undersea) is rebuilt on the real roster and is not settled.**
200 days per companion:

```
             net dmg   rounds   knockdowns   wipes/200
Sandshrew     569.6    20.97      3.32          82
Ghostbloom    444.1    20.76      3.35          98
Piplup        354.7    21.68      2.09          48
```

Knockdowns of 3.2 to 3.4 hit the design's stated target of "three to four hero
knockdowns." The wipe rate does not, and section 4 says why that is probably not
a simulator bug.

---

## 2. Decisions taken, with the measurement behind each

| Decision | Measured |
|---|---|
| Puff carries **5x Entangle** in the Ring of Spell Storing | 195.4 against 206.9 for Faerie Fire and 225.5 for an empty ring, over 400 days |
| Puff **holds station at 40 to 60 ft**, not 90 | Worth 18 points, four times the loadout choice. She takes 8 more so Ghostbloom takes 24 less, and she rebuilds free |
| Ursa **loads the ring on a rest day** | Costs nothing on the adventuring day. He ends a fighting day with 3.73 of 4 first-level slots unspent |
| Stabby **holds Uncanny Metabolism past the short rest** | Firing it at fight one regains nothing and heals nothing. Worth ~7 HP a day, and the feature is nearly dead weight either way |
| Piplup's **Sea Mist lasts 1 round**, not 3 | 3 rounds blanketed a whole fight twice a day. 170.0 to 183.4, and his lead over Ghostbloom fell from 25.3 to 11.9 |
| Lilly runs **Tectonic Slam, not Aether Ward**, from Session 9 | 156 against 200 on the same shared pool. The Ward measures -1.8 against a bare party; the cannon's Protector preload does its safety job for free |
| **Chimchar stays a deliberate trap** | Most companion damage (274), second-worst outcome, only companion that wipes. Recorded so it is never "fixed" |

---

## 3. Open questions for the DM

1. **Can Puff speak?** Her stat block lists no language, only telepathy. The 2024
   rule names being gagged or in magical silence as what blocks a Verbal
   component, not muteness, so the printed text supports letting her cast.
   Entangle is V,S and Faerie Fire is V. **Everything about the ring rests on
   this.**
2. **Session 9 fight 2 is 580, not the 552 in the canon table.** 552 is the
   arithmetic for four Needlemaws; the card's Count line says five.
3. **Aid does nothing.** +0.2 net for two of Lilly's three 2nd-level slots. Those
   slots are free if you want them elsewhere.
4. **Sandshrew leaves Session 9 with no healer.** The party heals 25 hit points
   across the whole day. Canon has Piplup manifesting at the *end* of Session 9,
   so this is forced unless you move him.
5. Smaller, all defaulted off and all harmless: whether Shardwings may target
   Puff (`S8_WING_PICKS_PUFF`), whether Puff flies aloft by default
   (`S8_PUFF_ALOFT`), whether her carried items drop where she falls, and whether
   a rebuilt Puff is narratively the same Puff.

---

## 4. The next piece of work, and why

**Implement the four Session 9 levers and measure what each is worth.** The
design gives every fight one clever answer the DM must never offer, and the
simulator currently uses none of them:

- **The Blackcask's tripod** (AC 13, 20 hit points). Destroying it ends Still
  Pouring, Blackwater Surge and Sheathed in Black at once. Probably the single
  largest lever in the session.
- **The Kept's anchor spikes** (AC 12, 10 hit points, ordinary objects). Knock
  one over and its Kept is Prone and loses its next action.
- **Thorn Whip on the Drownbell.** It pulls a Small creature 10 ft, which drops
  the bell out of the water ceiling and switches it off permanently.
- **The Pipes of Haunting on the Notched Fin.** She is deliberately not immune to
  Frightened and nobody is to be told.

That measurement answers the real question, which is not "is the trench too
hard" but "**how much does the table gain by finding the answers**," and it turns
the current wipe rate from a worry into a designed gap.

Second: Session 9's fight 4 currently caps at 16 rounds and reaches it often. If
the levers do not close the gap, the next suspects in order are the Quiet Hand's
regeneration going unanswered, and whether the party should be splitting fire
rather than focusing Kyogre.

---

## 5. Files

```
templates/playthrough_session_08.py     the engine, plus Session 8's fights
templates/playthrough_session_09.py     Session 9, importing the engine
reference/campaign/session_09_enemies.md  Session 9 stat blocks, source of truth
reference/campaign/sim_standing_rulings.md  rulings every sim must declare
reference/campaign/{lilly,stabby,ursa}_kit.md  the three heroes' kits
reference/expansions/                   non-SRD rules, transcribed with provenance
memory/campaign_canon.md                design intent and session plans
simulation/ENCOUNTER_VALIDATION.md      the method and the failure modes
```

A readable per-character breakdown of Session 8, built from the 400-day run, is
published as an artifact: <https://claude.ai/code/artifact/f8cd9bde-8955-47f7-a7f8-f04136d9e6f3>

---

## 6. Rules discipline

Non-negotiable, from CLAUDE.md, and it caught real errors repeatedly this pass:

**Never state a 2024 rule from memory.** Check `reference/srd/`, then
`reference/expansions/`, then the 2024 wiki at dnd2024.wikidot.com through the
in-app browser (WebFetch loops on that site's redirect). Cite what you used. If
you cannot verify it, say so plainly rather than asserting it.

Things that check found this pass: Spell-Storing Item is level 11 and Lilly is 7;
Uncanny Metabolism regains only *expended* Focus; temporary hit points do not
stack; Moonbeam moves on a Magic action, not a Bonus action; Magic Item Tinker
only works on items you created with Replicate Magic Item; Faerie Fire is not on
the Artificer list.
