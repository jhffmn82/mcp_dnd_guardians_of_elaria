"""Session 9: THE UNDERSEA. Turn-by-turn combat simulator.

This imports the Session 8 engine wholesale (Actor, deal, attack_roll, and every
hero, companion, cannon, Puff and item routine) and defines only what Session 9
actually changes. Nothing about the party's kit is re-implemented here, so any
fix made to the Session 8 sim is inherited automatically.

WHAT IS DIFFERENT ABOUT THE PARTY (DM, 2026-09-05)
--------------------------------------------------
1. **Sandshrew is the companion.** He manifests at the Session 8 homecoming
   (campaign_canon.md), so Session 9 is the first session he is out.

2. **Lilly has TECTONIC SLAM and no longer casts Aether Ward.** The Earth Mote
   is installed at the Session 8 homecoming, which unlocks the Earth discharge
   (reference/campaign/lilly_kit.md:97). Both draw on the SAME pool of 2 uses
   per short rest, so this is a straight swap of what she spends it on.

   The DM's reasoning, checked and confirmed: the Eldritch Cannon's **Protector**
   mode grants "the cannon and chosen creatures within 10 ft ... 1d8 + Int (min 1)
   temp HP" (reference/expansions/artificer.md:87), the mode is re-picked on
   every activation, and activating is a Bonus Action with no daily limit. Out of
   combat she can simply keep activating until everyone has rolled the maximum,
   so the party walks into every fight already carrying **13 temporary hit
   points** each. Temporary hit points do not stack: "If you have Temporary Hit
   Points and receive more of them, you decide whether to keep the ones you have
   or to gain the new ones" (reference/srd/01_playing_the_game.md:823). Aether
   Ward grants 2d8+5, which beats a standing 13 only when it rolls 14 or better
   (about 58% of the time) and then only by the excess. It was always nearly
   redundant, and both pool uses are better spent on the earthquake.

ENEMIES: every stat block is read from `reference/campaign/session_09_enemies.md`,
which the 2026-09-05 difficulty pass made the source of truth. That file
SUPERSEDED the earlier 308 / 444 / 412 / 458 totals this simulator was first
built against: the real figures are **404 / 552 / 530 / 558**, +26% to +30% over
Session 8 slot for slot, with every fight fielding four or five enemy types
instead of two. The 458 never added up, which this simulator is what caught.

[DM CHECK] Fight 2 reconciles to **580**, not the 552 in the canon table. 552 is
the arithmetic for FOUR Needlemaws; the Needlemaw card's own Count line says
five, and five is what runs here. One Needlemaw is 28 points.

Implemented from the cards, not invented: Schooling, Wall-Slip, Blind Panic and
It Breaks Past, the Inkmantle pair never both stinging in a round, the
Blackfroth arriving at the top of round three, Kelp Mantle and Column Fall,
Quillfrond's Range Finder (it shoots the FARTHEST thing and rakes anything
inside 10 ft), the two false air-bells dropping on round three with Toll capped
at twice a fight, Still Pouring answered only by radiant or Cleansing Edge,
Sheathed in Black, the Blackcask silent on round one, IT WAS SINGING YESTERDAY
(a Bloodied Chorister cut with Cleansing Edge is FREED alive, and freeing the
Notched Fin frees the whole remaining choir and ends the fight), Kyogre's three
phases with legendary actions scaling 1/2/3, The Water Closes, Undertow
uncharged at initiative, The Deep Voice from phase two, the Quiet Hand At Work
for two rounds (no actions, Advantage against it) then Near the Work healing,
the Kept rising on round three and collapsing after three rounds each, the
Brine-Thing respawn capped at four, and the Drownbell lamping whoever is
farthest from Kyogre.

EVERY enemy in this session has some form of "It Does Not Finish": none of them
attack or target a creature at 0 hit points. That is handled once, in _marks().

Knobs: S8_* knobs from the Session 8 engine all apply. S9-specific:
  S9_TEMP=13        temp HP everyone starts each fight with (0 disables)
  S9_SLAM=1         Lilly spends the shared pool on Tectonic Slam
  S9_WARD=0         ...or set 1 to put her back on Aether Ward for the A/B
"""
import math
import os

# Sandshrew is the Session 9 companion. Set before importing the engine, which
# reads its configuration at import time.
os.environ.setdefault('S8_COMPANION', 'sandshrew')

import importlib.util as _ilu
import sys as _sys

_here = os.path.dirname(os.path.abspath(__file__))
_spec = _ilu.spec_from_file_location(
    'playthrough_session_08', os.path.join(_here, 'playthrough_session_08.py'))
S8 = _ilu.module_from_spec(_spec)
_sys.modules['playthrough_session_08'] = S8
# The Session 8 engine parses sys.argv at module level, outside any main guard,
# so hide our own arguments from it while it loads.
_argv, _sys.argv = _sys.argv, _sys.argv[:1]
try:
    _spec.loader.exec_module(S8)
finally:
    _sys.argv = _argv

from playthrough_session_08 import (          # noqa: E402
    Actor, State, ehp, d, d20, log, LOG, deal, attack_roll, foe_save,
    initiative, start_round, render_map, close_up,
    stabby_attack_routine, stabby_initiative, stabby_defensive,
    true_strike, cannon_fire, companion_turn, cast_ward,
    puff_turn, puff_pipes, ursa_starry, ursa_triage, star_arrow, starry_wisp,
    guiding_bolt, conjure_animals, pack_tick, wither_and_bloom, tether,
    short_rest, revive_between, print_tally,
)

TEMP_HP = int(os.environ.get('S9_TEMP', '13'))       # Protector, pre-loaded
SLAM_ON = os.environ.get('S9_SLAM', '1') == '1'
WARD_ON = os.environ.get('S9_WARD', '0') == '1'


# ---------------------------------------------------------------- party changes

def prime_temp_hp(st, why=''):
    """Protector, spammed out of combat until everyone has the maximum.

    1d8 + Int 5 caps at 13. It is a Bonus Action with no expendable resource and
    the mode is chosen fresh on each activation, so between fights she simply
    keeps doing it. Temp HP do not stack, so this sets a floor rather than adding.
    """
    if TEMP_HP <= 0:
        return
    who = [h for h in st.pcs if h.alive] + [st.cannon]
    for h in who:
        h.temp = max(getattr(h, 'temp', 0), TEMP_HP)
    log(f"  Lilly walks the line with the cannon on PROTECTOR{' ' + why if why else ''}: "
        f"everyone tops out at {TEMP_HP} temporary hit points before a blow is struck.")


def tectonic_slam(st, targets):
    """Lilly's Earth discharge (reference/campaign/lilly_kit.md:97).

    Magic action, 20-ft-radius Sphere within 120 ft, DEX save DC 16 for 6d8
    force and Prone, half and no prone on a success; the raised stone is
    difficult terrain. Shares the 2-per-short-rest pool with Aether Ward.
    """
    if not SLAM_ON or st.l_ward <= 0 or st.lilly.down:
        return False
    live = [t for t in targets if t.hp > 0 and st.lilly.dist_ft(t) <= 120]
    if len(live) < 2:
        return False
    # Centre on whichever living enemy catches the most others in a 20-ft radius.
    best, centre = 0, None
    for t in live:
        n = sum(1 for g in live if t.dist_ft(g) <= 20)
        if n > best:
            best, centre = n, t
    if best < 2:
        return False
    caught = [g for g in live if centre.dist_ft(g) <= 20]
    st.l_ward -= 1
    log(f"    Lilly: TECTONIC SLAM. The sand galleries buck and split under "
        f"{len(caught)} of them. [{st.l_ward} discharges left]")
    for g in caught:
        raw = d(6, 8)
        if foe_save(g, g.saves.get('dex', 0), 16):
            dmg = deal(st, g, [(raw // 2, 'force')], credit='Lilly')
            log(f"      {g.name} rides the buckling floor: {dmg} force.")
        else:
            dmg = deal(st, g, [(raw, 'force')], credit='Lilly')
            g.slowed = 1
            g.prone = True
            log(f"      {g.name} is thrown down for {dmg} force and lands PRONE.")
        if g.hp <= 0:
            log(f"      {g.name} does not get up.")
    return True


# ---------------------------------------------------------------- hero turns

def hero_round(st, name, live, rnd, priority=None):
    """One hero's (or the companion's) whole turn. Shared by all four fights.

    `priority` orders the kill list. The default, weakest-and-nearest first, is
    right when every enemy is finite: clear the chaff, then break the anchor. It
    is exactly WRONG in the trench, where the Brine-Things respawn one per
    Kyogre turn forever, so a party chasing the weakest target farms chaff all
    night and never touches the objective."""
    if not live:
        return
    if priority is not None:
        live = priority(live)
    if name == 'Stabby' and st.stabby.alive:
        st.s_speed_left = 65 if st.s_ignited else 55
        st.stabby.dodging = False
        order = (live if priority is not None
                 else sorted(live, key=lambda t: (t.hp, st.stabby.dist_ft(t))))
        if st.stabby.hp < 25:
            stabby_defensive(st, order)
            return
        stabby_attack_routine(st, order, rnd)
    elif name == 'Lilly' and st.lilly.alive:
        if WARD_ON and not SLAM_ON and st.l_ward > 0 and rnd == 1:
            cast_ward(st, 'as the water wall bulges')
        elif not tectonic_slam(st, live):
            t = (live[0] if priority is not None
                 else min(live, key=lambda g: (g.hp, st.lilly.dist_ft(g))))
            true_strike(st, t)
        pool = [g for g in live if g.hp > 0]
        if pool:
            cannon_fire(st, 'ballista', pool)
        pool = [g for g in live if g.hp > 0]
        if pool and not puff_pipes(st, pool):
            puff_turn(st, min(pool, key=lambda g: g.hp), use_mm=True)
    elif name == 'Ursa' and st.ursa.alive:
        pack_tick(st, live)
        bonus = ursa_triage(st)
        if not bonus and not st.u_starry:
            bonus = ursa_starry(st, targets=live)
        if st.pack is None and st.u_slots[3] > 0:
            conjure_animals(st, tuple(st.ursa.pos), targets=live)
        t = next((g for g in live if g.hp > 0), None)
        if t is not None:
            if st.u_gbolt > 0:
                guiding_bolt(st, t)
            else:
                starry_wisp(st, t)
        if not bonus and st.u_starry:
            star_arrow(st, next((g for g in live if g.hp > 0), None))
    elif name in ('Ghostbloom', 'Sandshrew', 'Piplup') and st.ghost.alive:
        companion_turn(st, live)


def run_fight(st, label, blurb, groups, enemy_turn, cap=12, wave=None,
              priority=None, win=None):
    """Generic driver: initiative, then rounds until one side is done."""
    log("  " + "=" * 62)
    log(f"  {label}")
    log(f"  {blurb}")
    prime_temp_hp(st, 'before they step in')
    foes = [a for _, actors, _ in ((g[0], g[1], g[2]) for g in groups) for a in actors]
    stabby_initiative(st, last=(label.startswith('FIGHT 4')))
    order = initiative(st, groups)
    rnd = 0
    while rnd < cap and any(h.alive for h in st.heroes):
        rnd += 1
        if wave is not None:
            wave(st, rnd)
        if win is not None and win():
            break
        if not any(f.hp > 0 for f in foes):
            break
        start_round(st, rnd)
        for _, name, actors in order:
            live = [f for f in foes if f.hp > 0]
            if not live or not any(h.alive for h in st.heroes):
                break
            if win is not None and win():
                break
            if name in ('Stabby', 'Lilly', 'Ursa', 'Ghostbloom', 'Sandshrew',
                        'Piplup'):
                hero_round(st, name, live, rnd, priority=priority)
            else:
                enemy_turn(st, [a for a in actors if a.hp > 0], rnd)
    log(f"  {label} ENDS after round {rnd}.")
    return rnd


def _bite(st, foe, bonus, dice, die, flat, dtype, verb, reach=5):
    """One ordinary enemy attack against the nearest reachable hero."""
    pool = [h for h in st.pcs if h.alive and not getattr(h, 'aloft', False)]
    if not pool:
        return
    tgt = min(pool, key=lambda h: foe.dist_ft(h))
    if foe.dist_ft(tgt) > reach:
        foe.approach(tgt, reach, foe.speed)
    if foe.dist_ft(tgt) > reach:
        return
    hit, crit, _ = attack_roll(st, bonus, tgt, attacker=foe)
    if hit:
        dmg = deal(st, tgt, [(d(dice * (2 if crit else 1), die) + flat, dtype)],
                   attacker=foe)
        log(f"    {foe.name}: {verb} {tgt.name} for {dmg}.")
    else:
        log(f"    {foe.name}: {verb} at {tgt.name} and misses.")


# ---------------------------------------------------------------- enemy helpers

def _marks(st):
    """Everything an enemy is willing to hit. EVERY Session 9 enemy has some
    form of "It Does Not Finish": none of them attack or target a creature at
    0 hit points. That is a rule of the whole session, not a per-card quirk,
    so it lives here once."""
    return [h for h in st.pcs if h.alive and not h.down
            and not getattr(h, 'aloft', False)]


def _atk(st, foe, bonus, dice, die, flat, dtype, verb, reach=5,
         adv=False, tgt=None, extra=None, exclude=(), move=True):
    """One enemy attack. `extra` is (n, die, type) added on a hit.
    `exclude` holds creatures this attacker has already struck this round, for
    the cards that say "never the same creature twice in a round"."""
    pool = [h for h in _marks(st) if h not in exclude]
    if not pool:
        return None
    if tgt is None or tgt.down or not tgt.alive or tgt in exclude:
        tgt = min(pool, key=lambda h: foe.dist_ft(h))
    if foe.dist_ft(tgt) > reach and foe.speed and move:
        foe.approach(tgt, reach, foe.speed)
    if foe.dist_ft(tgt) > reach:
        return None
    hit, crit, _ = attack_roll(st, bonus, tgt, adv=adv, attacker=foe)
    if not hit:
        log(f"    {foe.name}: {verb} at {tgt.name} and misses.")
        return None
    parts = [(d(dice * (2 if crit else 1), die) + flat, dtype)]
    if extra:
        parts.append((d(extra[0] * (2 if crit else 1), extra[1]), extra[2]))
    dmg = deal(st, tgt, parts, attacker=foe)
    log(f"    {foe.name}: {verb} {tgt.name} for {dmg}.")
    return tgt


def _cone(foe, pool, length):
    """A cone is as wide as it is long, its point at the caster. Aimed down the
    axis toward the centre of mass of everyone in range, and anything within 45
    degrees of that axis is in it."""
    near = [h for h in pool if foe.dist_ft(h) <= length]
    if not near:
        return []
    ax = sum(h.pos[0] for h in near) / len(near) - foe.pos[0]
    ay = sum(h.pos[1] for h in near) / len(near) - foe.pos[1]
    n = math.hypot(ax, ay) or 1.0
    ax, ay = ax / n, ay / n
    out = []
    for h in near:
        dx, dy = h.pos[0] - foe.pos[0], h.pos[1] - foe.pos[1]
        dn = math.hypot(dx, dy)
        if dn == 0 or (dx * ax + dy * ay) / dn >= 0.707:
            out.append(h)
    return out


def _line(foe, pool, length, width=5):
    """A line `width` feet wide, aimed at the nearest target in range."""
    near = [h for h in pool if foe.dist_ft(h) <= length]
    if not near:
        return []
    lead = min(near, key=lambda h: foe.dist_ft(h))
    ax, ay = lead.pos[0] - foe.pos[0], lead.pos[1] - foe.pos[1]
    n = math.hypot(ax, ay) or 1.0
    ax, ay = ax / n, ay / n
    out = []
    for h in near:
        dx, dy = h.pos[0] - foe.pos[0], h.pos[1] - foe.pos[1]
        along = dx * ax + dy * ay
        if along < 0:
            continue
        perp = abs(dx * -ay + dy * ax) * 5.0
        if perp <= width / 2.0 + 2.5:
            out.append(h)
    return out or [lead]


def _sphere(foe, pool, radius, cast_rng):
    """A sphere dropped on whichever point catches the most of them."""
    cands = [h for h in pool if foe.dist_ft(h) <= cast_rng]
    if not cands:
        return []
    best = []
    for c in cands:
        grp = [h for h in cands if c.dist_ft(h) <= radius]
        if len(grp) > len(best):
            best = grp
    return best


def _aoe(st, foe, dc, stat, dice, die, dtype, name, rng=30, on_fail=None,
         shape='emanation', radius=10, width=5):
    """A save-for-half area effect, resolved in its REAL shape. Evasion is
    handled inside deal/hero_save."""
    marks = _marks(st)
    if shape == 'cone':
        pool = _cone(foe, marks, rng)
    elif shape == 'line':
        pool = _line(foe, marks, rng, width)
    elif shape == 'sphere':
        pool = _sphere(foe, marks, radius, rng)
    else:
        pool = [h for h in marks if foe.dist_ft(h) <= rng]
    if not pool:
        return False
    log(f"    {foe.name}: {name}")
    for h in pool:
        raw = d(dice, die)
        if st.hero_save(h, stat, dc):
            got = deal(st, h, [(raw // 2, dtype)], attacker=foe)
            log(f"      {h.name} rides it out: {got}.")
        else:
            got = deal(st, h, [(raw, dtype)], attacker=foe)
            log(f"      {h.name} is caught for {got}.")
            if on_fail:
                on_fail(h)
    return True


def _recharge(foe, attr, lo=5):
    """Recharge N-6 at the top of its turn."""
    if getattr(foe, attr, 0) <= 0 and d20() >= lo:
        setattr(foe, attr, 1)


# ---------------------------------------------------------------- the four fights

def fight1(st):
    """1 THE BRIGHTSHOAL, 404 hit points. Glimmerfin x8, Surgehorn x3,
    Inkmantle x2, and the Blackfroth arriving at the top of round three.
    Nothing here is hunting the party: it is a stampede going through them."""
    st.lilly.pos = [15, 20]; st.stabby.pos = [14, 19]; st.ursa.pos = [16, 20]
    st.ghost.pos = [15, 21]; st.puff.pos = [14, 21]; st.cannon.pos = [16, 21]
    fins = [Actor(f'Glimmerfin-{i+1}', 'f', 'foe', 14, ehp(13), p, 40,
                  saves=dict(str=-1, dex=4, con=1, wis=1))
            for i, p in enumerate([(11, 11), (13, 10), (15, 9), (17, 10),
                                   (19, 11), (12, 13), (18, 13), (15, 12)])]
    horns = [Actor(f'Surgehorn-{i+1}', 'H', 'foe', 16, ehp(68), p, 50,
                   saves=dict(str=4, dex=1, con=3, wis=0),
                   cond_imm={'charmed', 'frightened'}, reach=10)
             for i, p in enumerate([(13, 6), (16, 5), (19, 7)])]
    for h in horns:
        h.charge = 0
    inks = [Actor(f'Inkmantle-{i+1}', 'I', 'foe', 14, ehp(28), p, 30,
                  saves=dict(str=1, dex=3, con=3, wis=2), reach=15)
            for i, p in enumerate([(10, 8), (20, 8)])]
    for k in inks:
        k.sting = 0
        k.stung = False
    froth = Actor('Blackfroth', 'B', 'foe', 15, ehp(40), (15, 3), 30,
                  saves=dict(str=2, dex=2, con=1, wis=0),
                  resist={'necrotic', 'poison'}, vuln={'radiant'},
                  cond_imm={'blinded', 'charmed', 'deafened', 'frightened',
                            'prone'})
    froth.hp = 0                 # off the board until round three
    froth.sour = 0
    froth.arrived = False

    def enemies(st_, actors, rnd):
        for k in inks:
            k.stung = False
        for f in actors:
            if f.hp <= 0:
                continue
            n = f.name
            if n.startswith('Glimmerfin'):
                pool = _marks(st_)
                if not pool:
                    continue
                t = min(pool, key=lambda h: f.dist_ft(h))
                # Schooling: Advantage when another Glimmerfin is on the target.
                adv = any(g is not f and g.hp > 0 and g.dist_ft(t) <= 5
                          for g in fins)
                _atk(st_, f, 6, 1, 6, 2, 'piercing', 'nips at', 5, adv=adv, tgt=t)
            elif n.startswith('Surgehorn'):
                _recharge(f, 'charge')
                if f.charge and rnd > 1:
                    f.charge = 0
                    _aoe(st_, f, 15, 'dex', 4, 8, 'bludgeoning',
                         'BLIND CHARGE, fifty feet in a straight line, and it '
                         'cannot see anyone.', rng=50, shape='line', width=10)
                else:
                    _atk(st_, f, 8, 2, 8, 4, 'bludgeoning', 'gores', 10)
            elif n.startswith('Inkmantle'):
                _recharge(f, 'sting')
                # The pair never both sting in the same round.
                if f.sting and rnd > 1 and not any(k.stung for k in inks):
                    f.sting = 0
                    f.stung = True
                    _aoe(st_, f, 14, 'con', 2, 6, 'poison',
                         'INK STING, a bloom of stinging dark twenty feet across.',
                         rng=60, shape='sphere', radius=20,
                         on_fail=lambda h: setattr(h, 'blinded', 1))
                else:
                    _atk(st_, f, 7, 2, 6, 4, 'slashing', 'lashes a tendril at', 15)
            elif n == 'Blackfroth':
                _recharge(f, 'sour')
                if f.sour and any(f.dist_ft(h) <= 10 for h in _marks(st_)):
                    f.sour = 0
                    _aoe(st_, f, 15, 'con', 3, 6, 'necrotic',
                         'SOUR CURRENT, the black going out of it in a ring.',
                         rng=10)
                else:
                    _atk(st_, f, 7, 2, 8, 3, 'necrotic', 'spits froth at', 60)

    def wave(st_, rnd):
        if rnd == 3 and not froth.arrived:
            froth.arrived = True
            froth.hp = froth.hp_max
            log("  THE BLACKFROTH ARRIVES, sixty feet out, from the direction "
                "the herd came. It is a hole cut in a beautiful picture, and it "
                "is what they were all running from.")

    return run_fight(
        st, 'FIGHT 1: THE BRIGHTSHOAL',
        '(A stampede coming through the gallery the wrong way. Nothing here is '
        'hunting anyone: it is running, and the party is standing in the road.)',
        [('Glimmerfins', fins, 4), ('Surgehorns', horns, 1),
         ('Inkmantles', inks, 3), ('Blackfroth', [froth], 2)],
        enemies, wave=wave)


def fight2(st):
    """2 THE KELP CATHEDRAL, 580 hit points on the printed counts. Pillarback x2,
    Needlemaw x5, Quillfrond x3, and two Gullet Bells dropping at the top of
    round three. Nothing shoots but the rooted Quillfronds, and nothing flies.

    [DM CHECK] the canon table says 552, which is the arithmetic for FOUR
    Needlemaws; the card's own Count line says five. Five is used here."""
    st.lilly.pos = [15, 21]; st.stabby.pos = [15, 19]; st.ursa.pos = [17, 21]
    st.ghost.pos = [14, 20]; st.puff.pos = [16, 22]; st.cannon.pos = [17, 22]
    backs = [Actor(f'Pillarback-{i+1}', 'P', 'foe', 17, ehp(126), p, 20,
                   saves=dict(str=5, dex=-1, con=4, wis=1),
                   resist={'bludgeoning', 'piercing'},
                   cond_imm={'prone'}, reach=10)
             for i, p in enumerate([(13, 12), (18, 12)])]
    for b in backs:
        b.column = 0
    maws = [Actor(f'Needlemaw-{i+1}', 'n', 'foe', 14, ehp(28), p, 40,
                  saves=dict(str=2, dex=3, con=1, wis=1))
            for i, p in enumerate([(12, 15), (14, 14), (16, 14), (18, 15),
                                   (13, 16)])]
    fronds = [Actor(f'Quillfrond-{i+1}', 'q', 'foe', 15, ehp(32), p, 0,
                    saves=dict(str=1, dex=-2, con=1, wis=0),
                    cond_imm={'charmed', 'frightened', 'grappled', 'prone'},
                    reach=10)
              for i, p in enumerate([(12, 11), (19, 11), (15, 10)])]
    bells = [Actor(f'Gullet Bell-{i+1}', 'U', 'foe', 15, ehp(46), p, 25,
                   saves=dict(str=3, dex=0, con=1, wis=1),
                   resist={'thunder'}, cond_imm={'deafened', 'prone'}, reach=10)
             for i, p in enumerate([(14, 18), (17, 18)])]
    for b in bells:
        b.hp = 0
        b.toll = 0
        b.arrived = False
    st.bell_tolls = 0            # the card: at most twice in the whole fight

    def enemies(st_, actors, rnd):
        for f in actors:
            if f.hp <= 0:
                continue
            n = f.name
            if n.startswith('Pillarback'):
                _recharge(f, 'column', 6)
                if f.column:
                    f.column = 0
                    _aoe(st_, f, 16, 'dex', 5, 10, 'bludgeoning',
                         'COLUMN FALL, thirty feet of living kelp coming over.',
                         rng=30, shape='line', width=10)
                else:
                    for _ in range(2):
                        _atk(st_, f, 9, 2, 8, 5, 'bludgeoning',
                             'closes a pincer on', 10)
            elif n.startswith('Needlemaw'):
                _atk(st_, f, 7, 2, 4, 4, 'piercing', 'bites', 5)
            elif n.startswith('Quillfrond'):
                pool = _marks(st_)
                if not pool:
                    continue
                # Range Finder: it shoots the FARTHEST thing it can see, and
                # rakes instead of shooting anything already inside 10 ft.
                far = [h for h in pool if 10 < f.dist_ft(h) <= 80]
                if far:
                    t = max(far, key=lambda h: f.dist_ft(h))
                    for _ in range(1 if rnd == 1 else 2):
                        _atk(st_, f, 7, 1, 8, 3, 'piercing',
                             'fires a quill into', 80, tgt=t)
                else:
                    _atk(st_, f, 6, 2, 6, 2, 'slashing',
                         'rakes a frond across', 10)
            elif n.startswith('Gullet Bell'):
                _recharge(f, 'toll')
                if f.toll and st_.bell_tolls < 2:
                    f.toll = 0
                    st_.bell_tolls += 1
                    _aoe(st_, f, 15, 'con', 3, 6, 'thunder',
                         'TOLL. One enormous flat brass note out of a thing '
                         'with no bell inside it.', rng=20,
                         on_fail=lambda h: setattr(h, 'reaction', False))
                else:
                    _atk(st_, f, 7, 2, 8, 4, 'bludgeoning', 'slams', 10)

    def wave(st_, rnd):
        if rnd == 3 and not bells[0].arrived:
            log("  TWO OF THE AIR-BELLS ARE NOT BELLS. They come down onto the "
                "sand, and the one piece of terrain this session told the party "
                "to trust opens underneath them.")
            pool = _marks(st_)
            for i, b in enumerate(bells):
                b.arrived = True
                b.hp = b.hp_max
                if i < len(pool):
                    t = pool[i]
                    raw = d(3, 8)
                    if st_.hero_save(t, 'dex', 15):
                        got = deal(st_, t, [(raw // 2, 'bludgeoning')], attacker=b)
                        log(f"      {t.name} steps clear: {got}.")
                    else:
                        got = deal(st_, t, [(raw, 'bludgeoning')], attacker=b)
                        log(f"      {t.name} is under it for {got}, and the "
                            "bell closes over them.")

    return run_fight(
        st, 'FIGHT 2: THE KELP CATHEDRAL',
        '(The prettiest room in the campaign and a straight brawl in it. The '
        'Choristers sing in the canopy and take no part; one has a notched fin.)',
        [('Pillarbacks', backs, -1), ('Needlemaws', maws, 3),
         ('Quillfronds', fronds, -2), ('Gullet Bells', bells, 0)],
        enemies, wave=wave)


def fight3(st):
    """3 THE BLACKWATER SEAM, 530 hit points. The Blackcask on its tripod,
    Hollowsong x4, Lancefin x3, Tanglehand x2, and the Notched Fin.

    CLEANSING EDGE CURES here: a Bloodied Hollowsong or the Notched Fin that
    Stabby cuts is FREED and leaves alive, and freeing HER frees the whole
    remaining choir and ends the fight."""
    st.lilly.pos = [15, 22]; st.stabby.pos = [15, 20]; st.ursa.pos = [17, 22]
    st.ghost.pos = [14, 21]; st.puff.pos = [16, 23]; st.cannon.pos = [17, 23]
    cask = Actor('The Blackcask', 'B', 'foe', 17, ehp(152), (15, 11), 0,
                 saves=dict(str=4, dex=-2, con=4, wis=-1),
                 resist={'cold', 'necrotic', 'nm-bludgeoning', 'nm-piercing',
                         'nm-slashing'}, immune={'poison'},
                 cond_imm={'charmed', 'exhaustion', 'frightened', 'paralyzed',
                           'poisoned', 'prone'}, reach=15)
    cask.surge = 0
    cask.cleanse_types = {'radiant'}      # radiant OR Cleansing Edge stops it
    songs = [Actor(f'Hollowsong-{i+1}', 'h', 'foe', 15, ehp(38), p, 30,
                   saves=dict(str=2, dex=3, con=1, wis=1),
                   resist={'cold', 'necrotic'}, immune={'poison'},
                   cond_imm={'charmed', 'frightened', 'poisoned'})
             for i, p in enumerate([(13, 13), (17, 13), (12, 15), (18, 15)])]
    for sg in songs[2:]:
        sg.hp = 0                         # the second pair arrives end of round 1
    lances = [Actor(f'Lancefin-{i+1}', 'l', 'foe', 16, ehp(22), p, 10,
                    saves=dict(str=-1, dex=4, con=2, wis=1),
                    resist={'cold'}, immune={'poison'},
                    cond_imm={'poisoned', 'prone'})
              for i, p in enumerate([(11, 14), (19, 14), (15, 9)])]
    hands = [Actor(f'Tanglehand-{i+1}', 'T', 'foe', 16, ehp(40), p, 0,
                   saves=dict(str=3, dex=2, con=2, wis=0),
                   resist={'cold', 'necrotic', 'nm-bludgeoning', 'nm-piercing',
                           'nm-slashing'}, immune={'poison'},
                   cond_imm={'blinded', 'charmed', 'deafened', 'exhaustion',
                             'frightened', 'poisoned', 'prone'}, reach=20)
             for i, p in enumerate([(14, 12), (16, 12)])]
    for t in hands:
        t.hp = 0
    fin = Actor('The Notched Fin', 'N', 'foe', 16, ehp(80), (15, 12), 40,
                saves=dict(str=3, dex=4, con=3, wis=1),
                resist={'cold', 'necrotic'}, immune={'poison'},
                cond_imm={'charmed', 'poisoned'}, reach=10)
    fin.hp = 0
    fin.song = 0
    fin.arrived = False
    st.freed = 0

    def cure_check(st_):
        """Cleansing Edge on a Bloodied Chorister frees it, alive. Freeing the
        Notched Fin frees every Hollowsong still standing and ends the fight."""
        for f in songs + [fin]:
            if f.hp <= 0 or not getattr(f, 'cleansed', False):
                continue
            if f.hp <= f.hp_max // 2:
                f.hp = 0
                st_.freed += 1
                st_.tally['prevented']['Cleansing Edge (freed alive)'] += 1
                if f is fin:
                    log("    THE NOTCHED FIN IS FREED. The black water lets go "
                        "of her and the song comes back right. Every Hollowsong "
                        "still standing is freed in the same breath.")
                    for sg in songs:
                        if sg.hp > 0:
                            sg.hp = 0
                            st_.freed += 1
                            st_.tally['prevented']['Cleansing Edge (freed alive)'] += 1
                else:
                    log(f"    {f.name}: the Nichirin's burn finishes its work. "
                        "The black water lets go and it swims for the canopy, "
                        "ALIVE.")

    def enemies(st_, actors, rnd):
        cure_check(st_)
        for f in actors:
            if f.hp <= 0:
                continue
            n = f.name
            if n == 'The Blackcask':
                if rnd == 1:
                    log("    The Blackcask is still pouring. It has not noticed "
                        "that anybody is here.")
                    continue
                # Still Pouring: 15 back unless radiant or Cleansing Edge landed.
                if not getattr(f, 'cleansed', False) and f.hp < f.hp_max:
                    f.hp = min(f.hp_max, f.hp + 15)
                    log("    The Blackcask pours itself full again (+15). Only "
                        "radiance or the Nichirin stops it.")
                f.cleansed = False
                _recharge(f, 'surge')
                if f.surge and rnd >= 3:
                    f.surge = 0
                    _aoe(st_, f, 16, 'con', 5, 6, 'cold',
                         'BLACKWATER SURGE. The seam exhales in a thirty-foot '
                         'cone.', rng=30, shape='cone')
                else:
                    for _ in range(2):
                        _atk(st_, f, 8, 2, 6, 4, 'bludgeoning',
                             'lashes an iron band at', 15, extra=(1, 6, 'cold'))
            elif n == 'The Notched Fin':
                _recharge(f, 'song')
                if f.song:
                    f.song = 0
                    _aoe(st_, f, 15, 'wis', 3, 8, 'psychic',
                         'THE WRONG SONG. Every note in it is off, and it is '
                         'inside your chest.', rng=30)
                else:
                    for _ in range(2):
                        _atk(st_, f, 8, 2, 6, 4, 'slashing', 'rakes', 10)
            elif n.startswith('Hollowsong'):
                for _ in range(2):
                    _atk(st_, f, 7, 1, 6, 3, 'slashing', 'rakes a fin across', 5,
                         extra=(1, 4, 'cold'))
            elif n.startswith('Lancefin'):
                _atk(st_, f, 7, 1, 8, 4, 'piercing',
                     'puts a bone lance through', 60)
            elif n.startswith('Tanglehand'):
                _atk(st_, f, 7, 2, 6, 3, 'bludgeoning',
                     'closes a hand of black water around', 20)

    def wave(st_, rnd):
        if rnd == 2:
            fresh = False
            for sg in songs[2:]:
                if sg.hp <= 0 and not getattr(sg, 'came', False):
                    sg.came = True
                    sg.hp = sg.hp_max
                    fresh = True
            for t in hands:
                if t.hp <= 0 and not getattr(t, 'came', False):
                    t.came = True
                    t.hp = t.hp_max
                    fresh = True
            if fresh:
                log("  Two more Choristers come up out of the crack, and the "
                    "black water itself puts out a pair of hands.")
        if rnd == 3 and not fin.arrived:
            fin.arrived = True
            fin.hp = fin.hp_max
            log("  SOMETHING BIGGER COMES UP OUT OF THE SEAM. Her dorsal fin "
                "has an old white notch torn clean through it.")

    return run_fight(
        st, 'FIGHT 3: THE BLACKWATER SEAM',
        '(Dim light, and the singing is coming from the wrong direction.)',
        [('The Blackcask', [cask], -2), ('Hollowsongs', songs, 3),
         ('Lancefins', lances, 4), ('Tanglehands', hands, 2),
         ('The Notched Fin', [fin], 4)],
        enemies, wave=wave, cap=14)


def _guardian_free(st, ky, brines):
    """Kyogre's total is the corruption riding it, and the card is explicit:
    it is "the only thing on the board whose total ending at 0 wins the fight".
    When it goes, "They Go With It" turns every Brine-Thing back into ordinary
    seawater in the same instant, mid-lunge, wherever it is."""
    if ky.hp > 0:
        return False
    if not getattr(st, '_freed_said', False):
        st._freed_said = True
        log("  THE BLACK WATER LETS GO. Kyogre is FREE, and every Brine-Thing "
            "on the board is ordinary seawater in the same instant, mid-lunge, "
            "wherever it is.")
        for b in brines:
            b.hp = 0
    return True


def _trench_priority(live):
    """Kyogre first: it is the objective, its total reaching 0 ENDS the fight,
    and Stabby's Cleansing Edge on it is the only thing that stops The Water
    Closes healing it 15 a turn. The Brine-Things respawn forever and are never
    worth a turn that could have gone into the whale."""
    def rank(t):
        n = t.name
        if n == 'Kyogre':
            return 0
        if n == 'The Quiet Hand':
            return 1
        if n.startswith('The Kept'):
            return 2
        if n.startswith('Drownbell'):
            return 3
        return 4                      # Brine-Things last, always
    return sorted(live, key=lambda t: (rank(t), t.hp))


def fight4(st):
    """4 THE GUARDIAN'S TRENCH, 558 on the board at initiative and 708 once the
    Kept stand up. Kyogre (280 Black Water, three phases), the Quiet Hand (150,
    defenceless for two rounds), Brine-Thing x4 respawning, a Drownbell in the
    ceiling, and three Kept rising at the top of round three.

    THE SPIKE IS NOT A TARGET. That was last session."""
    st.lilly.pos = [15, 24]; st.stabby.pos = [15, 22]; st.ursa.pos = [17, 24]
    st.ghost.pos = [14, 23]; st.puff.pos = [16, 25]; st.cannon.pos = [17, 25]
    ky = Actor('Kyogre', 'K', 'foe', 18, ehp(280), (15, 11), 20,
               saves=dict(str=8, dex=0, con=7, wis=4),
               resist={'nm-bludgeoning', 'nm-piercing', 'nm-slashing'},
               immune={'cold', 'poison'},
               cond_imm={'charmed', 'frightened', 'grappled', 'paralyzed',
                         'petrified', 'prone', 'restrained', 'stunned'},
               reach=20)
    ky.undertow = 0
    ky.voice = 0
    ky.phase = 1
    hand = Actor('The Quiet Hand', 'Q', 'foe', 17, ehp(150), (14, 9), 30,
                 saves=dict(str=3, dex=2, con=3, wis=2),
                 resist={'cold'}, cond_imm={'frightened'})
    hand.at_work = True
    hand.nail = 0
    brines = [Actor(f'Brine-Thing-{i+1}', 'b', 'foe', 15, ehp(22), p, 40,
                    saves=dict(str=1, dex=3, con=2, wis=-1),
                    immune={'cold', 'poison'},
                    cond_imm={'blinded', 'charmed', 'deafened', 'exhaustion',
                              'frightened', 'prone'})
              for i, p in enumerate([(12, 14), (18, 14), (13, 17), (17, 17),
                                     (15, 15), (15, 18), (11, 16), (19, 16)])]
    for b in brines[4:]:
        b.hp = 0                          # the respawn pool, four out at a time
    dbells = [Actor(f'Drownbell-{i+1}', 'D', 'foe', 15, ehp(40), p, 20,
                    saves=dict(str=-2, dex=3, con=1, wis=2),
                    immune={'cold'}, cond_imm={'grappled', 'restrained'},
                    fly=True)
              for i, p in enumerate([(15, 13), (16, 20)])]
    dbells[1].hp = 0
    for b in dbells:
        b.hush = 0
    kept = []
    for i, (nm, hp, spd) in enumerate((('the Horned One', 45, 60),
                                       ('the Winged One', 45, 40),
                                       ('the Heavy One', 60, 20))):
        k = Actor(f'The Kept ({nm})', 'X', 'foe', 16, ehp(hp),
                  (13 + i * 2, 10), spd,
                  saves=dict(str=3, dex=2, con=3, wis=-2),
                  immune={'poison', 'psychic'},
                  cond_imm={'charmed', 'deafened', 'exhaustion', 'frightened',
                            'poisoned'},
                  reach=10 if 'Winged' in nm else 5)
        if 'Heavy' in nm:
            k.resist = {'bludgeoning', 'piercing', 'slashing'}
        k.hp = 0
        k.rose = None
        kept.append(k)

    def enemies(st_, actors, rnd):
        for f in actors:
            if f.hp <= 0:
                continue
            n = f.name
            if n == 'Kyogre':
                # Three phases. No numbers are ever read aloud at the table.
                ph = 1 if f.hp > 180 else (2 if f.hp > 100 else 3)
                if ph != f.phase:
                    f.phase = ph
                    log("    " + ("IT NOTICES. The black comes off in ribbons "
                                  "and there is blue underneath."
                                  if ph == 2 else
                                  "THE UNDERTOW TURNS. It stops trying to leave, "
                                  "and everything it has left it spends here."))
                # The Water Closes: 15 back unless Cleansing Edge touched it.
                if not getattr(f, 'cleansed', False) and f.hp < f.hp_max:
                    f.hp = min(f.hp_max, f.hp + 15)
                    log("    The water closes over Kyogre again (+15 Black Water).")
                f.cleansed = False
                # One new Brine-Thing per Kyogre turn, four out at most.
                if sum(1 for b in brines if b.hp > 0) < 4:
                    nxt = next((b for b in brines if b.hp <= 0), None)
                    if nxt is not None:
                        nxt.hp = nxt.hp_max
                if rnd >= 2:
                    _recharge(f, 'undertow')
                if f.undertow:
                    f.undertow = 0
                    _aoe(st_, f, 17, 'dex', 4, 10, 'cold',
                         'UNDERTOW. Sixty feet of sea pulling back toward the '
                         'trench.', rng=60, shape='cone')
                    continue
                if ph >= 2:
                    _recharge(f, 'voice', 6)
                    if f.voice:
                        f.voice = 0
                        _aoe(st_, f, 17, 'wis', 4, 8, 'psychic',
                             'THE DEEP VOICE. A word in a language nobody here '
                             'speaks, and far too loud.', rng=30)
                        continue
                # It Is Not Aiming (phase one): the Flukes strike the nearest
                # creatures it can reach and NEVER the same one twice in a
                # round, and it does not move at all in phase one.
                struck = []
                for _ in range(3 if ph == 3 else 2):
                    t = _atk(st_, f, 13, 3, 8, 5, 'bludgeoning',
                             'lands the FLUKE on', 20,
                             exclude=struck, move=(ph > 1))
                    if t is not None:
                        struck.append(t)
                # Legendary actions: 1 use in phase one, 2 in phase two, 3 in
                # phase three. Take the Deep COSTS 2, so phase one cannot buy a
                # fluke at all and spends its single use on Cold Squall.
                if ph == 1:
                    _aoe(st_, f, 16, 'con', 2, 8, 'cold',
                         'COLD SQUALL, a bloom of freezing water.', rng=60,
                         shape='sphere', radius=10)
                else:
                    t = _atk(st_, f, 13, 3, 8, 5, 'bludgeoning',
                             'TAKE THE DEEP, a legendary fluke into', 20,
                             exclude=struck, move=(ph > 1))
                    if ph == 3:
                        _aoe(st_, f, 16, 'con', 2, 8, 'cold',
                             'COLD SQUALL on top of it.', rng=60,
                         shape='sphere', radius=10)
            elif n == 'The Quiet Hand':
                if f.at_work:
                    if rnd >= 3:
                        f.at_work = False
                        f.exposed = False
                        log("    THE QUIET HAND STOPS. It sets the hammer down, "
                            "opens the case, and plants three spent spikes in "
                            "the sand. THE KEPT RISE.")
                        for k in kept:
                            k.hp = k.hp_max
                            k.rose = rnd
                    else:
                        # At Work: no actions, no reactions, every attack against
                        # it has Advantage and it auto-fails every save.
                        f.exposed = True
                        log("    The Quiet Hand drives the spike another inch. "
                            "It has not looked up.")
                        continue
                # Near the Work: 10 back within 30 ft of Kyogre unless cleansed.
                if (not getattr(f, 'cleansed', False) and f.hp < f.hp_max
                        and f.dist_ft(ky) <= 30):
                    f.hp = min(f.hp_max, f.hp + 10)
                f.cleansed = False
                _recharge(f, 'nail')
                if f.nail:
                    f.nail = 0
                    _aoe(st_, f, 16, 'dex', 4, 10, 'force',
                         'NAIL. The hammer goes into the sand, and something '
                         'under the sand answers.', rng=30, shape='line')
                else:
                    for _ in range(2):
                        _atk(st_, f, 8, 3, 6, 4, 'bludgeoning',
                             'swings the hammer at', 5, extra=(1, 10, 'cold'))
            elif n.startswith('Brine-Thing'):
                _atk(st_, f, 7, 1, 8, 3, 'cold', 'closes a cold grip on', 5)
            elif n.startswith('Drownbell'):
                if rnd >= 2:
                    _recharge(f, 'hush')
                pool = _marks(st_)
                if not pool:
                    continue
                # It Lamps the Far Ones: it takes the hero farthest from Kyogre
                # and never piles onto whoever is already in melee.
                t = max(pool, key=lambda h: h.dist_ft(ky))
                if f.hush:
                    f.hush = 0
                    log("    Drownbell: HUSH. It does not make a sound. It "
                        "stops the sound of everything else.")
                    if not st_.hero_save(t, 'con', 16):
                        t.reaction = False
                        log(f"      {t.name} cannot take Reactions.")
                else:
                    _atk(st_, f, 7, 2, 8, 4, 'cold', 'puts the cold lamp on',
                         60, tgt=t)
            elif n.startswith('The Kept'):
                # Three Rounds: it collapses into sand whatever its hit points.
                if f.rose is not None and rnd - f.rose >= 3:
                    log(f"    {f.name} comes apart into ordinary sand.")
                    f.hp = 0
                    continue
                _atk(st_, f, 8, 2, 8, 4, 'force',
                     'brings a remembered blow down on', f.reach)

    def wave(st_, rnd):
        if rnd == 3 and dbells[1].hp <= 0 and not getattr(dbells[1], 'came', False):
            dbells[1].came = True
            dbells[1].hp = dbells[1].hp_max
            log("  A second Drownbell comes down out of the ceiling.")

    return run_fight(
        st, "FIGHT 4: THE GUARDIAN'S TRENCH",
        '(Kyogre is mid-corruption and the spike is still being driven. The '
        'total is the black water riding it, not its life: at zero the guardian '
        'is free. It was never a monster.)',
        [('Kyogre', [ky], 0), ('The Quiet Hand', [hand], 2),
         ('Brine-Things', brines, 3), ('Drownbells', dbells, 3),
         ('The Kept', kept, 2)],
        enemies, wave=wave, cap=16, priority=_trench_priority,
        win=lambda: _guardian_free(st, ky, brines))


# ---------------------------------------------------------------- the day

def run_day(seed):
    S8.rng = __import__('random').Random(seed)
    LOG.clear()
    st = State()
    if not WARD_ON:
        st.l_ward = 2      # the same shared pool, spent on the earthquake instead
    log("SESSION 9: THE UNDERSEA. Sandshrew is out; Lilly has the Earth Mote.")
    if S8.LILLY_AID:
        _b = 5 * S8.LILLY_AID
        for _h in (st.puff, st.ursa, st.lilly, st.stabby, st.ghost):
            _h.hp_max += _b
            _h.hp += _b
        log(f"Lilly casts AID twice before they go down: +{_b} max and current HP.")
    log(f"Ursa's Omen Dreams for the day: {st.u_omens}")
    stats = {}

    def dcount():
        return sum(h.drops for h in [st.lilly, st.stabby, st.ursa, st.ghost])

    def hp_pct():
        return 100.0 * sum(h.hp for h in st.heroes) / sum(h.hp_max for h in st.heroes)

    for i, (key, fn) in enumerate((('f1', fight1), ('f2', fight2),
                                   ('f3', fight3), ('f4', fight4))):
        stats[key] = fn(st)
        stats['drops_' + key] = dcount() - sum(
            stats.get('drops_' + k, 0) for k in ('f1', 'f2', 'f3'))
        stats['hp_' + key] = hp_pct()
        if not any(h.alive for h in st.heroes):
            stats['wipe'] = key
            stats['tally'] = st.tally
            return st, stats
        revive_between(st)
        if key == 'f2':
            short_rest(st)
            if not WARD_ON:
                st.l_ward = 2
    stats['drops'] = dcount()
    stats['tally'] = st.tally
    stats['slam_left'] = st.l_ward
    return st, stats


def sweep(n=200):
    import io, contextlib, statistics as S
    net, rds, drp = [], [], []
    N = 0
    wipes = 0
    for s in range(1, n + 1):
        with contextlib.redirect_stdout(io.StringIO()):
            st, stats = run_day(s)
        if stats.get('wipe'):
            wipes += 1
            continue
        N += 1
        net.append(sum(stats['tally']['taken'].values())
                   - sum(stats['tally']['healed'].values()))
        rds.append(sum(stats[k] for k in ('f1', 'f2', 'f3', 'f4')))
        drp.append(stats['drops'])
    ci = 1.96 * S.stdev(net) / (N ** 0.5) if N > 2 else 0
    print(f"SESSION 9  n={N}  taken-heal {S.mean(net):6.1f} +/-{ci:.1f}  "
          f"rounds {S.mean(rds):5.2f}  knockdowns {S.mean(drp):5.3f}  wipes {wipes}")
    return net, rds, drp


if __name__ == '__main__':
    if len(_sys.argv) > 1 and _sys.argv[1] == 'sweep':
        sweep(int(_sys.argv[2]) if len(_sys.argv) > 2 else 200)
    else:
        st, stats = run_day(int(_sys.argv[1]) if len(_sys.argv) > 1 else 1)
        print('\n'.join(LOG))
        print()
        print_tally(stats['tally'], header='SESSION 9 CONTRIBUTIONS')
