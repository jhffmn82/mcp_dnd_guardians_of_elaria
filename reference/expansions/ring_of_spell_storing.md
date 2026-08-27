# Ring of Spell Storing (Puff's)

**Source: 2024 Dungeon Master's Guide.** Read verbatim from
`dnd2024.wikidot.com/magic-item:ring-of-spell-storing` on 2026-08-27. Not in the
SRD 5.2.1 transcription (that document has no magic-item chapter), so it is
recorded here rather than quoted from memory.

**Ring, Rare (Requires Attunement)**

> This ring stores spells cast into it, holding them until the attuned wearer
> uses them. The ring can store up to 5 levels worth of spells at a time. When
> found, it contains 1d6 - 1 levels of stored spells chosen by the DM.
>
> Any creature can cast a spell of level 1 through 5 into the ring by touching
> the ring as the spell is cast. The spell has no effect other than to be stored
> in the ring. If the ring can't hold the spell, the spell is expended without
> effect. The level of the slot used to cast the spell determines how much space
> it uses.
>
> While wearing this ring, you can cast any spell stored in it. The spell uses
> the slot level, spell save DC, spell attack bonus, and spellcasting ability of
> the original caster but is otherwise treated as if you cast the spell. The
> spell cast from the ring is no longer stored in it, freeing up space.

## What this settles for the campaign

**It is the ITEM, not the class feature.** Spell-Storing Item is an Artificer
level 11 feature (`reference/expansions/artificer.md:58`) and Lilly is level 7.
She does not have it and will not for a long time. Puff's ring is the Rare
wondrous item above, handed over in the Session 8 Handover.

**"Otherwise treated as if you cast the spell" is the whole design.** Three
consequences, and they drive every choice about what to load:

1. **Puff holds the Concentration**, not the storer. This is the point. Ursa's
   concentration is owned by Conjure Animals every round of every fight, which
   makes every Concentration spell on his list dead weight to him. Stored in the
   ring, Puff holds it instead, and she has nothing else to concentrate on.
   She can still only hold ONE at a time, so five stored spells is a magazine of
   five fights, not five simultaneous effects.
2. **Puff supplies the components.** Her stat block lists no spoken language,
   only "Telepathy 1 mile (works only with you)". The 2024 rule
   (`reference/srd/10_spells_intro_and_a-c.md:202`) names being *gagged* or in
   *magical silence* as what blocks a Verbal component, not muteness, so the
   permissive reading is the one the printed text supports. **[DM CHECK]**
   whether Puff can vocalise. Everything below depends on it.
3. **Puff's own casting time applies.** A Bonus Action spell out of the ring
   leaves her Action free for the Wand of Magic Missiles.

**Ursa should be the one who loads it, not Lilly.** Lilly's two spare 2nd-level
slots already go to Aid twice at dawn, and her 1st-level slots are working.
Ursa's Concentration spells are otherwise unusable, so storing them costs him
nothing he was going to spend. Both cast at **DC 16**, so nothing is lost.

## Measured loadouts (400 days each, Ghostbloom, 2026-08-27)

The ring was not modelled at all before this pass; Puff was carrying an empty
ring all session.

CORRECTED 2026-08-27 (DM: "faerie fire doesn't prevent any damage though"). He
was right, and the earlier table in this file was measuring the wrong thing.

Faerie Fire's range is 60 ft and Entangle's is 90 ft, so a Puff who flies only
as far as each spell requires ends up **30 ft further forward when she casts
Faerie Fire**. Every point of Faerie Fire's apparent advantage was that
positioning, not the spell. Decomposed at the boss, the whole 16-point gap was
one line: Ghostbloom took 28.6 with Entangle and 5.6 with Faerie Fire, because
a Puff standing further forward soaks the hits that otherwise land on the
companion. Hold her position constant and Faerie Fire's edge disappears.

```
                              she flies only as far     she holds station
                              as the spell needs        at 50 ft
  ent    5 x Entangle               213.8                   195.4  <-- best
  entff  3 Entangle + 2 Faerie      200.3                   199.5
  ff     5 x Faerie Fire            206.9                   206.9
```

`ent` and `entff` are inside each other's error bars at 400 days (195.4 +/-5.2
against 199.5 +/-5.0), so this is not a large win. Five Entangles is the pick on
simplicity: one spell for the table to remember, same slot cost, and numerically
ahead. Both cost Ursa five 1st-level slots, which is four plus one bought with
Wild Resurgence.

**PUFF'S POSITION IS WORTH MORE THAN THE LOADOUT.** 18 points, against roughly 4
for the best spell choice:

```
  she holds at   taken-heal  hero knock  Puff drops  Ghostbloom took  Puff took
     90 ft (back)   213.8      0.065       0.01          68.9            7.6
     60 ft          195.4      0.033       0.09          44.6           15.3
     40 ft          195.4      0.030       0.07          44.7           15.2
     25 ft          212.7      0.045       0.22          45.8           29.3
```

She is a **free-to-rebuild decoy**: the gem is not consumed and the ritual costs
no slot (see homunculus_servant.md), so trading 8 damage onto Puff to take 24
off Ghostbloom is simply a good trade, and hero knockdowns halve with it. Inside
25 ft it reverses: she stops absorbing more than she was and starts dying, 0.22
drops a day. **The flat optimum is 40 to 60 ft.** Knob `S8_PUFF_LEAN`, default 50.

For the record, the earlier (confounded) table, kept so the correction is legible:

Re-measured 2026-08-27 after the Frightened corrections (the repeat save and
"can't approach" were both missing), 400 days each:

```
                                        casts  saves      taken-heal
  entff   3 ENTANGLE then 2 FAERIE FIRE    5    Str+Dex      200.3  <-- best
  ff      5 x Faerie Fire                  5    Dex          206.9
  webent3 1 Web + 3 Entangle               4    Dex+Str      209.6
  web2ff  2 Web + 1 Faerie Fire            3    Dex          211.3
  ent     5 x Entangle                     5    Str          213.8
  web2ent 2 Web + 1 Entangle               3    Dex+Str      214.1
  sphere  Flaming Sphere 3rd + 2nd         2    Dex          232.1
  off     empty ring (the old model)       0    -            229.4
```

**Web loses even though it is the strongest single spell here.** Its catch
clause re-triggers ("or starts its turn there") where Entangle catches once, and
it holds more per cast. It costs 2 levels, and the ring only has 5. Puff can
hold ONE concentration at a time, so a stronger spell buys nothing she can use,
while the extra level cost drops her from five casts to three across a five-fight
day. Two fights get nothing at all.

**Save diversity is the bigger lever.** All-Strength (Entangle only) is the
worst mix at 213.8; all-Dexterity (Faerie Fire only) is 206.9; the Str+Dex split
is 200.3. Entangle shreds the early crowds and slides off Groudon and Thumpaw,
who make Strength saves in their sleep. Faerie Fire covers exactly those.

**The rule for loading this ring: buy CASTS, and buy BOTH saves.** The cheapest
concentration spell that does the job beats the best one. Anything at level 3
(Conjure Animals, for instance) is worse on both axes at once, since it costs
three of the five levels for a single cast.

**Flaming Sphere is a trap.** It is the one spell that fits the "moves on a
Bonus Action" brief, it raises Puff's own damage (71.5 vs 68.9), and it makes
the party *worse* (229.3 vs 225.5). Damage was never Puff's problem.

**Order matters more than the choice.** The same five spells in the other order
lose 21 points (196.2 vs 217.4). Entangle is a **Strength** save and Faerie Fire
is a **Dexterity** save: Entangle shreds the early crowds and slides off Groudon
and Thumpaw, who tear straight out of it. Load Entangle for the fights that come
first and Faerie Fire for the heavy things at the end.

**Entangle is the better level 1 spell** (DM, 2026-08-27, and the measurement
agrees). Restrained (`reference/srd/14_rules_glossary.md:858`) is Speed 0,
Advantage on attacks against it, and **Disadvantage on its own attacks**, so it
is Faerie Fire plus a movement lock plus a defensive debuff, at 90 ft instead of
60. The difficult terrain lands whether they save or not.

Simulator knob `S8_RING`; defaults to `entff`. The simulator is deliberately
CONSERVATIVE on both spells: Entangle's escape check is taken free at the top of
the creature's turn instead of costing it an Action, and Flaming Sphere's
passive "ends its turn within 5 feet" save is not modelled at all.
