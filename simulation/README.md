# The combat simulators

Turn-by-turn Monte Carlo simulators for the campaign's sessions. They exist to
answer one question before the table does: **is this encounter the fight we meant
to build?**

They are not a rules engine and they are not a substitute for play. They are a
way to run four fights three hundred times and find the thing that only shows up
on the eightieth run.

## What is here

| File | What it is |
|---|---|
| `templates/playthrough_session_08.py` | The engine. Every hero, companion, item, cannon and Puff routine lives here, plus the Session 8 (Underroot) fights. ~4,600 lines. |
| `templates/playthrough_session_09.py` | Session 9 (the Undersea). Imports the engine wholesale and defines only the four new fights and the two party changes. ~950 lines. |
| `reference/campaign/sim_standing_rulings.md` | Table rulings and known traps every sim setup must declare. Read it before writing a new one. |
| `simulation/ENCOUNTER_VALIDATION.md` | **The method.** How to validate an encounter, what the metrics mean, and the ways this has gone wrong before. |
| `simulation/HANDOFF.md` | State of the work, open questions, what to do next. |

## Running them

```bash
python templates/playthrough_session_08.py 7          # one day, seed 7, full transcript
python templates/playthrough_session_09.py 7          # same, Session 9
python templates/playthrough_session_09.py sweep 300  # 300 days, summary line only
```

Session 8 has no sweep entry point of its own; drive it from a short script that
imports it and calls `run_day(seed)` in a loop, redirecting stdout. Every example
in ENCOUNTER_VALIDATION.md does exactly that.

Both are configured entirely by environment variable, so an A/B is a shell loop
and never an edit:

```bash
for C in ghostbloom sandshrew piplup chimchar togekiss; do
  S8_COMPANION=$C python templates/playthrough_session_09.py sweep 300
done
```

The canonical Session 8 configuration is
`S8_COMPANION=ghostbloom S8_COHESION=1 S8_WITHER=1 S8_LILLY_AID=1`. Those three
flags default off for historical reasons but are all canon; a run without them is
not the party as played. Session 9 sets its own defaults and needs no flags.

## What they measure

Three numbers, and only three. They were fixed by the DM and everything else is
diagnostic:

- **Rounds.** Tempo. How long the day takes in initiative.
- **Knockdowns.** How close the floor gets. The honest safety metric.
- **Damage taken minus healing.** The party's net cost for the day.

**Total damage dealt is not a metric.** It is bounded by the enemies' hit points,
so it is nearly constant across configurations and tells you who rolled the dice,
not who won the fight. Damage share is the same trap wearing a percentage sign.

## The one thing to remember

Every "A beats B" result out of these simulators has, at least once, turned out
to be measuring something other than A and B. The list of specific ways is in
ENCOUNTER_VALIDATION.md and it is the most useful page in this folder.
