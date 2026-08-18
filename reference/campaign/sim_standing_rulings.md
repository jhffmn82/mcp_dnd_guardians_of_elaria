<!--
Standing table rulings and known traps for combat sims, accumulated across
the 2026-07/08 sim series (Shalewrath v1, v2, Slaghorn pack) and their
adversarial audits. A sim harness MUST declare these in its setup and a
sim auditor should check them. Repo is the home for this knowledge per the
commit-generated-artifacts rule (session scripts age out). No em dashes.
-->

# Combat-Sim Standing Rulings (declare in every sim setup)

1. **Guardian Protocol is the Sentinel's own reaction** (its stat block);
   Lilly keeps her personal reaction (Shield / Flash of Genius) the same
   round. One reaction per creature per round, and the Sentinel counts as
   its own creature for this purpose.
2. **Evasion applies only to "half damage on a success" effects.** A flat
   fail-means-damage Dex save gets no Evasion interaction.
3. **Save-based damage ignores nonmagical-attack resistance** (Deflect
   redirects, Earthquake, Shudder-style vents). Attack-roll damage respects
   it (Sandshrew's claws are natural and nonmagical; enemy nonmagical gores
   are halved by Sandshrew's resistance).
4. **The Sentinel is a device, not an ally**: Ursa's Guiding Light +1 aura
   never applies to it. It does apply to creature allies (Arcanine,
   Sandshrew, the heroes) while they are inside the 20-ft light, and NEVER
   to Ursa himself (his spell attack stays +8).
5. **Log stands-from-Prone explicitly** (half Speed), and exactly ONE d20
   per attack roll (advantage shows both dice, keep the high one).
6. **Stabby has Monk save proficiency in Str AND Dex**: Str +2, Dex +8
   (plus advantage on Dex while Beast-ignited).
7. **Summoned Signature Partners** (Arcanine/Lapras/Noctowl): attacks count
   as magical (spell-conjured); Arcanine saves Str +4, Dex +0; Intimidate
   only fires if an enemy is within 15 ft when it APPEARS, so pre-casting at
   range forfeits it (summon timing is a real choice). [DM CHECK: magical
   ruling declared for sims, not verifiable in the SRD.]
8. **Opportunity attacks require sight.** A Blinded creature (tremorsense or
   not) cannot take an OA against a creature leaving its reach.
9. **Rider windows expire.** Stunning Strike's on-success rider ("the next
   attack against it has Advantage") lasts only until the start of Stabby's
   next turn; do not bank it across rounds.
10. **Position tracking is mandatory for auras and reactions.** The +1 light
    (20 ft), Guardian Protocol (15 ft), Flash of Genius and Cosmic Omen
    (30 ft): log mover positions every turn or the auditor cannot verify a
    single one of them.

## Arithmetic traps the audits keep catching
- **Crits**: double the dice, then add the modifier ONCE (2d10 crit =
  4d10 + mod). The +mod was dropped three separate times across the series.
- **Ledger intermediates** must match the stated action order.
- **Log Cleansing Edge** on Stabby's first hit each turn vs corrupted
  enemies even when nothing tries to heal; the auditor needs to see it.
- **State enemy sizes in the setup line**: Fury of the Small (larger than
  Stabby) is unverifiable otherwise.
- **Blind/condition durations**: write the end condition when applied
  ("until the start of X's next turn") and clear it on time.

## Balance findings that carried across every sim (table-relative)
- The four-unit party throws ~10 attack rolls a round and sustains roughly
  105-200 damage per round. Single legendaries melt: 230 and 340 HP solos
  both died in under 3 rounds. **Four ~130 HP bodies hit the 4-to-6 round
  arc** (the Slaghorn pack ran exactly 5).
- A blanket Thunder/Lightning vulnerability doubles Lilly's whole package
  every turn (~15+/turn); use seam-style windows as the thunder payoff
  instead of a standing vulnerability.
- **Lilly has ended four straight sims spending zero resources.** Nothing
  prices her door until an enemy actually reaches the backline; burrowers
  and teleporters that surface next to her are the lever.
- Sandshrew's Challenge + Curl Up + nonmagical resist is near-immunity vs
  nonmagical melee packs; blind effects are the honest counter, and magical
  or cold attackers flip the matchup.
- **The Nichirin does not stun Chimestones** (DM ruling 2026-08-18): Resonant
  Body keys on thunder damage, and the katana is slashing and force. Lilly's
  Boomstick is the martial thunder source, one stun per turn.
- **S8 roster retune adopted from the 20-run sweep**: 8x Rotbloom 33 / 8x
  Mossmite, 4x Chimestone 78 / 4x Shardwing 33, Weeper 170; spike stays 60 HP
  but re-knits 20 at the start of Groudon's turn unless Cleansing Edge touched
  it since his last turn (raising spike HP just lets the ranged battery steal
  Stabby's finish).
