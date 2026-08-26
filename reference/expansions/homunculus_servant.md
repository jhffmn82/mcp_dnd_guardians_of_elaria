# Homunculus Servant (Puff)

**Source: Eberron - Forge of the Artificer.** Read from dnd2024.wikidot.com on
2026-08-24. Not SRD; recorded here so the campaign cites a source rather than
memory.

**Level 2 Conjuration (Artificer)**

- **Casting Time:** 1 hour or Ritual
- **Range:** 10 feet
- **Components:** V, S, M (a gem worth 100+ GP)
- **Duration:** Instantaneous

You summon a special homunculus in an unoccupied space within range. It uses the
Homunculus Servant stat block. **If you already have a homunculus from this spell,
the homunculus is replaced by the new one.**

It is an ally to you and your allies. In combat it shares your Initiative count
but takes its turn immediately after yours. It obeys your commands (no action
required by you); with no orders it Dodges and avoids danger.

***Using a Higher-Level Spell Slot.*** Use the slot's level for the spell's level
in the stat block.

## Homunculus Servant

Tiny Construct, Neutral. **AC 13.** **HP 5 + 5 per spell level** (15 at 2nd level,
matching Puff). Hit Dice: d4s equal to the spell's level. **Speed 20 ft., Fly 30 ft.**
STR 4 (-3), DEX 15 (+2), CON 12 (+1), INT 10 (+0), WIS 10 (+0), CHA 7 (-2).
Immunities: Poison; Exhaustion, Poisoned. Darkvision 60 ft. Telepathy 1 mile
(with its creator only).

## What this settles for the campaign

**THE GEM IS NOT CONSUMED (DM, 2026-08-24).** The component line is "M (a gem
worth 100+ GP)" with no "which the spell consumes" clause, and the word "consume"
does not appear anywhere in the spell. It is reused every casting, like a focus.
An earlier note here said rebuilding Puff cost a gem; that was wrong.

**So rebuilding Puff is FREE.** Casting Time is "1 hour or Ritual", and the SRD
Ritual rule is "10 minutes longer to cast than normal. It also doesn't expend a
spell slot." A Short Rest is an hour. So Lilly rebuilds her over a rest at a cost
of ten extra minutes and nothing else, or in exactly an hour if she spends one of
her spare 2nd-level slots.

**Which settles the open targeting question: Puff SHOULD be a valid target.**
There was never a rules basis for shielding her; the simulator's
`S8_WING_PICKS_PUFF` was a placeholder. Measured over 250 days, with the rebuild
modelled correctly:
                                rounds  NET  knockdowns  Puff drops  floor  Puff dmg
  not targetable                  14.6  105        0.07        0.01    67%        69
  targetable, rebuilt             14.7  112        0.05        0.50    70%        70
She keeps her FULL output because she comes back, and the heroes get SAFER, not
more exposed: she draws the Shardwings' dives onto a construct that cannot stay
dead. Hero knockdowns fall and the floor rises.

**A SIMULATOR BUG this exposed:** `revive_between` revived only Lilly, Stabby,
Ursa and the companion, and the short rest restored Puff's hit points without
clearing her downed flag. So once Puff dropped she was out for the whole day, and
the first measurement of "Puff targetable" understated her by nearly half (37
damage instead of 70). Fixed; `S8_PUFF_REBUILD` also allows the rebuild to happen
between fights if the DM rules an hour passes on the road.

**Still open for the DM:** whether her carried items (Ring of Spell Storing, Wand
of Magic Missiles, Pipes of Haunting) drop where she falls, and whether a rebuilt
Puff is narratively "the same Puff" given the heart Lilly chose from three offered
cores in Session 7. The spell says the old homunculus "is replaced by the new
one", which is a mechanics sentence, not an answer about the character.
