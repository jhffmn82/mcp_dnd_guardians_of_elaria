# Validating an encounter before the table sees it

Written 2026-09-06 out of the Session 8 and Session 9 simulator work. This is the
method, the targets, and the specific ways it has gone wrong. If you are
generating encounters, the last section is the one that will save you.

No em dashes anywhere in generated documents, per CLAUDE.md.

---

## 1. The loop

1. **Write the stat blocks first, in the repo, as the source of truth.**
   `reference/campaign/session_09_enemies.md` is the model: AC, hit points,
   saves, traits, actions, reactions, and every attack routine, one file, with a
   header saying it is authoritative. The simulator and the session document both
   read from it so they cannot drift. `memory/campaign_canon.md` carries the
   design intent and the totals; it deliberately does not carry attack routines.

2. **Add the fight to the simulator from that file and nothing else.** If a
   number is not in the stat block, do not invent it: flag it `[DM CHECK]` in the
   module docstring and use a placeholder calibrated to the same slot in the
   previous session, so the comparison stays meaningful even while the number is
   wrong.

3. **Run one day with the full transcript and read it.** Not the summary. The
   transcript. Every bug in section 4 was found by reading a log and noticing
   something that made no sense, and none of them were visible in the summary.

4. **Sweep 200 to 400 days.** Under about 200 the confidence interval on net
   damage is wide enough to hide a 15-point effect.

5. **Compare against the targets in section 2.** If a number is off, assume the
   simulator before you assume the encounter, and work section 4 in order.

6. **A/B every change by environment variable, never by editing.** The knob costs
   three lines and makes the result reproducible a month later.

---

## 2. What "right" looks like

### Difficulty anchors, measured

| | Session 8 (Underroot) | Session 9 (the Undersea) |
|---|---|---|
| Enemy hit points per fight | 320 / 444 / 412 / 430 | 404 / 552 / 530 / 558 |
| Rounds per fight | ~3.6 | 4.1 / 5.9 / 4.2 / ~10 |
| Rounds for the day | 14.4 | ~21 |
| Hero knockdowns per day | 0.03 | 3.2 |
| Damage taken minus healing | 195 (Ghostbloom) | 445 to 570 by companion |

Session 9 is a deliberate +26% to +30% bump, and every fight fields four or five
enemy types instead of two.

### The DM's stated target for a session of this weight

> Three to four hero knockdowns, zero deaths, and two moments where the table
> should believe it might lose.

Session 8 at 0.03 knockdowns a day was **too safe**: one hero falls every
thirty-three days. That is the number a wide difficulty bump was answering.

### Party output to design against (Session 8, 400 days, per day)

- Total party damage **~1,450**, of which Stabby 462, Ursa 433, Lilly 231, the
  cannon 107, Puff 46, and the companion 125 to 274.
- **297 of that is overkill.** Roughly a fifth of everything they roll lands on
  something already dead.
- Enemies swing **61 times and land 9**, a 15% hit rate. The party's defensive
  layer is very thick and an encounter that assumes a normal hit rate will do
  nothing.
- Prevention: Lilly's Aether Ward absorbs **116**, Stabby's Deflect Attacks
  erases **73**, and the companion heals 0 to 48 depending on who is out.

### The load-bearing consequence

A fight that is merely *bigger* does not get harder in proportion, because the
party's floor is held up by things that do not scale with enemy hit points:
Deflect Attacks, the Ward, Evasion, and 15% incoming accuracy. Difficulty comes
from **action denial, forced movement, and reaction lockout**, which is exactly
what the Session 9 roster reaches for (Toll, Hush, grapples, the Kept).

---

## 3. Design rules that showed up in the numbers

- **Objectives beat roleplaying hooks in initiative.** In-combat objectives land
  at this table; RP hooks fall flat. Keep RP out of initiative.
- **Give a fight a win condition that is not "kill everything."** Kyogre's total
  reaching 0 wins the trench. The Notched Fin being freed ends the seam. Both
  measured as the difference between a clean win and a ten-round grind.
- **Respawning chaff must never be the softest target on the board**, or a party
  playing "kill the weakest" will farm it forever and never touch the objective.
  If you field respawners, give the real target a reason to be hit first.
- **Every companion must keep the party up without outshining the players.**
  Measured against Lilly's damage: Togekiss 54%, Piplup 71%, Ghostbloom 75%,
  Sandshrew 108%, Chimchar 125%. The last two fail that rule.
- **Damage is the least valuable thing a companion can bring.** Chimchar deals
  the most of any companion (274) and leaves the party worst off; Togekiss deals
  the least (125) and produces the party's best hero output.
- **A trap option is legitimate and should be recorded as deliberate**, or the
  next pass will "fix" it. Chimchar is a deliberate trap; the note lives in
  `memory/campaign_canon.md` and in `templates/build_bestiary.py`.

---

## 4. How this has gone wrong before

Nine failure modes, all of them real, all of them found in this repo. Work them
in this order when a result surprises you.

### 4.1 The ranking measures implementation quality, not balance

**The single most important line in this document.** In any simulation comparing
a simple option against a complex one, the ranking measures how well each was
implemented until proven otherwise.

Four of five companion cards had real defects. Only Chimchar, the simplest, was
clean, which is exactly why it looked dominant. Serene Grace never functioned
because `start_round` wiped it every round. Guardian's Light had an invented 40%
gate. Sandshrew charged instead of interposing. Piplup's Heal Bubble had an
invented 65% gate and counted overheal.

**Before believing any comparison, audit the loser for under-implementation.**

### 4.2 The damage column credits whoever rolls the die

It does not credit whoever made the hit land. This bit three separate times:
party totals, companion share, and hero attribution. Advantage, +1 auras, saved
saving throws and prevented natural 1s are all invisible in a damage column and
all decisive in the outcome.

### 4.3 The metric itself is an artifact

Removing Lilly's Aether Ward **lowers** recorded damage taken, from 195 to 173,
because heroes drop sooner and dropped heroes stop being attacked. The Ward is
the largest prevention effect in the party. Read the knockdown column for
anything that grants temporary hit points, and check whether `taken` is being
tallied before or after absorption.

### 4.4 A positional confound wearing a spell's name

Faerie Fire appeared to beat Entangle by 16 points at the boss. Faerie Fire's
range is 60 ft and Entangle's is 90, so a Puff who flies only as far as the spell
requires ends up 30 feet further forward on a Faerie Fire turn, where she soaks
hits that otherwise land on the companion. The entire gap was one line:
Ghostbloom took 28.6 with Entangle and 5.6 with Faerie Fire. Holding position
constant reversed the result.

**When two options differ in range, area, or reach, they also differ in where the
caster stands. Control for it.**

### 4.5 Area effects resolved as emanations

Every Session 9 area effect was being resolved as "everyone within X feet of the
attacker." A 10-ft-radius Cold Squall was hitting the whole party at 60 feet and
a 5-ft-wide Nail was hitting everyone. Cones, lines and spheres need real
geometry, and a sphere needs a chosen centre point.

### 4.6 Resource economy errors

Two shapes, both worth checking on every card:

- **Spending a resource where it does nothing.** Uncanny Metabolism was fired at
  the first fight of the day, where the party is at full Focus and full hit
  points, so it regained nothing and healed nothing and the once-per-day was
  gone. Both the kit document and the character sheet carried the same bad
  advice.
- **Ignoring what an option costs.** Kyogre was given a full extra Fluke per
  phase level every round; Take the Deep costs **2** legendary uses, so phase one
  cannot buy one at all.

### 4.7 Target priority

"Attack the weakest reachable thing" is correct when enemies are finite and
catastrophic when they are not. In the trench it made the party farm respawning
Brine-Things for ten rounds while Kyogre took 92 damage. Give each fight an
explicit priority function when the naive one is wrong, and say why in a comment.

### 4.8 The fight does not end when it is won

The trench kept running after Kyogre was freed, because the loop waited for every
enemy to die and the Quiet Hand was still at full health. Wire the printed win
condition into the loop, and check it after every actor rather than once a round.

### 4.9 Dead code that is still live

`PIPLUP_V2` was defined as `v2/v3/v4`, so a v2-era emergency branch was still
reachable under the v4 default and hard-coded a 10-round Sea Mist, bypassing the
duration knob. It fired 0.07 times a day and changed nothing, but it was wrong.
Grep every version flag for what it actually includes.

---

## 5. Checklist

Before calling an encounter validated:

- [ ] Every stat block is in a repo file that says it is the source of truth.
- [ ] The per-fight hit point totals in the simulator reconcile to that file's
      table. Session 9's fight 2 does not, and the discrepancy is flagged.
- [ ] Every invented number is marked `[DM CHECK]` in the module docstring.
- [ ] Each printed trait is either implemented or listed as deliberately not.
- [ ] Universal session rules are handled once, not per card. Every Session 9
      enemy has some form of "It Does Not Finish"; that lives in one function.
- [ ] Area effects have shapes.
- [ ] The fight has a win condition and the loop checks it.
- [ ] Target priority is correct for this board, especially with respawners.
- [ ] One full transcript has been read end to end by a person.
- [ ] 200+ days swept, with the confidence interval reported.
- [ ] Rounds, knockdowns and net damage compared against section 2.
- [ ] The losing option in any comparison has been audited for
      under-implementation (4.1).

---

## 6. What the simulator still does not do

State this whenever quoting its numbers.

- **It plays the party naively.** Each Session 9 fight carries a lever the design
  says the DM must never offer: the Blackcask's tripod, the Kept's anchor spikes,
  Thorn Whip pulling the Drownbell out of the water ceiling, the Pipes on the
  Notched Fin, who is deliberately not immune to Frightened. The simulator uses
  **none** of them, so its difficulty numbers are an upper bound on how hard the
  session plays once the table finds the answers.
- **It does not model the DM.** No mercy, no fudging, no reading the room.
- **It does not model player creativity**, terrain use, or anything not written
  as a mechanic.
- **Wipe means every hero at 0**, not deaths. Every Session 9 enemy refuses to
  attack a downed creature, so a simulated wipe is a scripted loss, not a TPK.
