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

```
                                    rounds  knock  taken-heal
  off  (empty ring, the old model)   14.51  0.140     225.5
  sphere  Flaming Sphere 3rd + 2nd   14.49  0.095     229.3
  ffent   3 Faerie Fire then 2 Ent   14.15  0.058     217.4
  ff      5 x Faerie Fire            14.27  0.055     209.4
  ent     5 x Entangle               14.37  0.040     205.6
  entff   3 ENTANGLE then 2 FAERIE FIRE  14.50  0.033  196.2   <-- best
```

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
