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

ENEMIES: every AC and hit point total below is verbatim from the locked Session 9
encounter design in memory/campaign_canon.md, and the per-fight totals reproduce
its 308 / 444 / 412 figures exactly.

[DM CHECK 1] Canon states the four fights total **308 / 444 / 412 / 458**. The
first three are exact. Fight 4 as written is Kyogre at 250 Black Water plus the
Quiet Hand at 120 = **370**, which is 88 short of 458. Nothing has been invented
to close the gap; the simulator runs the printed stat blocks and the trench is
therefore ~19% softer than the canon total implies.

[DM CHECK 2] Canon fixes AC, hit points, and each enemy's ONE clever line, but
not their attack routines. Every to-hit and damage expression marked PLACEHOLDER
below was calibrated against the Session 8 enemy occupying the same slot, so the
difficulty comparison between sessions is meaningful. They are guesses and should
be replaced with the real numbers before this drives any balance decision.

Knobs: S8_* knobs from the Session 8 engine all apply. S9-specific:
  S9_TEMP=13        temp HP everyone starts each fight with (0 disables)
  S9_SLAM=1         Lilly spends the shared pool on Tectonic Slam
  S9_WARD=0         ...or set 1 to put her back on Aether Ward for the A/B
"""
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

def hero_round(st, name, live, rnd, melee_only=False):
    """One hero's (or the companion's) whole turn. Shared by all four fights."""
    if not live:
        return
    if name == 'Stabby' and st.stabby.alive:
        st.s_speed_left = 65 if st.s_ignited else 55
        st.stabby.dodging = False
        order = sorted(live, key=lambda t: (t.hp, st.stabby.dist_ft(t)))
        if st.stabby.hp < 25:
            stabby_defensive(st, order)
            return
        stabby_attack_routine(st, order, rnd)
    elif name == 'Lilly' and st.lilly.alive:
        if WARD_ON and not SLAM_ON and st.l_ward > 0 and rnd == 1:
            cast_ward(st, 'as the water wall bulges')
        elif not tectonic_slam(st, live):
            t = min(live, key=lambda g: (g.hp, st.lilly.dist_ft(g)))
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


def run_fight(st, label, blurb, groups, enemy_turn, cap=12):
    """Generic driver: initiative, then rounds until one side is done."""
    log("  " + "=" * 62)
    log(f"  {label}")
    log(f"  {blurb}")
    prime_temp_hp(st, 'before they step in')
    foes = [a for _, actors, _ in ((g[0], g[1], g[2]) for g in groups) for a in actors]
    stabby_initiative(st, last=(label.startswith('FIGHT 4')))
    order = initiative(st, groups)
    rnd = 0
    while any(f.hp > 0 for f in foes) and any(h.alive for h in st.heroes) and rnd < cap:
        rnd += 1
        start_round(st, rnd)
        for _, name, actors in order:
            live = [f for f in foes if f.hp > 0]
            if not live or not any(h.alive for h in st.heroes):
                break
            if name in ('Stabby', 'Lilly', 'Ursa', 'Ghostbloom', 'Sandshrew',
                        'Piplup'):
                hero_round(st, name, live, rnd)
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


# ---------------------------------------------------------------- the four fights

def fight1(st):
    """THE BRIGHTSHOAL. Glimmerfin x8 (AC 14, 13 HP) + Surgehorn x3 (AC 15, 68).
    308 hit points, matching canon. A stampede of refugees fleeing the far end,
    so nothing here is hunting the party: it is running through them."""
    st.lilly.pos = [15, 20]; st.stabby.pos = [14, 19]; st.ursa.pos = [16, 20]
    st.ghost.pos = [15, 21]; st.puff.pos = [14, 21]; st.cannon.pos = [16, 21]
    fins = [Actor(f'Glimmerfin-{i+1}', 'f', 'foe', 14, ehp(13), p, 45,
                  saves=dict(str=-1, dex=4, con=1, wis=0))
            for i, p in enumerate([(11, 11), (13, 10), (15, 9), (17, 10),
                                   (19, 11), (12, 13), (18, 13), (15, 12)])]
    for f in fins:
        f.wall_slip = True          # canon: it can vanish into the water wall
    horns = [Actor(f'Surgehorn-{i+1}', 'H', 'foe', 15, ehp(68), p, 50,
                   saves=dict(str=5, dex=1, con=4, wis=-1),
                   # canon: blind panic, it cannot be calmed
                   cond_imm={'charmed', 'frightened'})
             for i, p in enumerate([(13, 7), (16, 6), (19, 8)])]

    def enemies(st_, actors, rnd):
        for f in actors:
            if f.hp <= 0:
                continue
            if f.name.startswith('Glimmerfin'):
                # PLACEHOLDER routine, calibrated to the S8 Mossmite slot.
                _bite(st_, f, 5, 1, 6, 3, 'slashing', 'slips past and rakes')
                if getattr(f, 'wall_slip', False) and f.hp < 7:
                    f.hidden = True
                    log(f"    {f.name} WALL-SLIPS into the water and is gone.")
                    f.hp = 0
            else:
                # PLACEHOLDER, calibrated to the S8 Rotbloom slot (a panicked
                # trample, not a predator).
                _bite(st_, f, 6, 2, 6, 4, 'bludgeoning', 'stampedes over')

    return run_fight(
        st, 'FIGHT 1: THE BRIGHTSHOAL',
        '(Eight Glimmerfin and three Surgehorn come through the gallery the '
        'wrong way, running from something behind them.)',
        [('Glimmerfins', fins, 4), ('Surgehorns', horns, 1)], enemies)


def fight2(st):
    """THE KELP CATHEDRAL. Pillarback x2 (AC 17, 126) + Needlemaw x6 (AC 14, 32).
    444 hit points, matching canon. Nothing shoots and nothing flies: the room is
    built so that Stabby, who owns no ranged attack, never has a dead turn."""
    st.lilly.pos = [15, 20]; st.stabby.pos = [15, 18]; st.ursa.pos = [17, 20]
    st.ghost.pos = [14, 19]; st.puff.pos = [16, 21]; st.cannon.pos = [17, 21]
    backs = [Actor(f'Pillarback-{i+1}', 'P', 'foe', 17, ehp(126), p, 25,
                   saves=dict(str=6, dex=-1, con=5, wis=1),
                   resist={'nm-bludgeoning', 'nm-piercing', 'nm-slashing'})
             for i, p in enumerate([(13, 11), (18, 11)])]
    maws = [Actor(f'Needlemaw-{i+1}', 'n', 'foe', 14, ehp(32), p, 40,
                  saves=dict(str=1, dex=3, con=2, wis=0))
            for i, p in enumerate([(12, 14), (14, 13), (16, 13), (18, 14),
                                   (13, 15), (17, 15)])]

    def enemies(st_, actors, rnd):
        for f in actors:
            if f.hp <= 0:
                continue
            if f.name.startswith('Pillarback'):
                # PLACEHOLDER, calibrated to the S8 Chimestone slot.
                _bite(st_, f, 7, 2, 10, 5, 'bludgeoning', 'brings a column down on', 10)
            else:
                # PLACEHOLDER, calibrated to the S8 Shardwing slot, grounded.
                _bite(st_, f, 5, 2, 6, 3, 'piercing', 'darts in and bites')

    return run_fight(
        st, 'FIGHT 2: THE KELP CATHEDRAL',
        '(The prettiest room in the campaign, and a straight brawl in it. The '
        'Choristers sing in the canopy overhead and take no part; one has a '
        'notched fin.)',
        [('Pillarbacks', backs, 0), ('Needlemaws', maws, 3)], enemies)


def fight3(st):
    """THE BLACKWATER SEAM. Blackcask (AC 17, 152) + Hollowsong x5 (AC 15, 52).
    412 hit points, matching canon. The Choristers from the Cathedral come back
    wrong. DIM light, not Darkness, so the one hero without darkvision keeps his
    whole kit. The Blackcask's regeneration is keyed to RADIANT damage."""
    st.lilly.pos = [15, 21]; st.stabby.pos = [15, 19]; st.ursa.pos = [17, 21]
    st.ghost.pos = [14, 20]; st.puff.pos = [16, 22]; st.cannon.pos = [17, 22]
    cask = Actor('Blackcask', 'B', 'foe', 17, ehp(152), (15, 10), 30,
                 saves=dict(str=5, dex=1, con=6, wis=2),
                 resist={'nm-bludgeoning', 'nm-piercing', 'nm-slashing'},
                 immune={'poison'})
    cask.took_radiant = False
    songs = [Actor(f'Hollowsong-{i+1}', 'h', 'foe', 15, ehp(52), p, 35,
                   saves=dict(str=2, dex=3, con=3, wis=1),
                   immune={'poison'})
             for i, p in enumerate([(12, 12), (14, 11), (16, 11), (18, 12),
                                    (15, 13)])]

    def enemies(st_, actors, rnd):
        for f in actors:
            if f.hp <= 0:
                continue
            if f.name == 'Blackcask':
                # Canon: regeneration answered by RADIANT damage, not by light.
                if not f.took_radiant and f.hp < f.hp_max:
                    f.hp = min(f.hp_max, f.hp + 10)
                    log(f"    {f.name} knits shut again (+10). Only radiance stops it.")
                f.took_radiant = False
                # PLACEHOLDER, calibrated to the S8 Glass Weeper slot.
                _bite(st_, f, 8, 2, 8, 5, 'necrotic', 'pours black water over', 10)
            else:
                # CANON: Cleansing Edge CURES here. A Hollowsong the Nichirin has
                # cut, once Bloodied, is freed and leaves the fight ALIVE. It is
                # a second way to clear a body and it is still an attack roll in
                # initiative, so it costs Stabby nothing but his usual swing.
                if getattr(f, 'cleansed', False) and f.hp <= f.hp_max // 2:
                    log(f"    {f.name}: the Nichirin's burn finishes its work. The "
                        "black water lets go and it swims for the canopy, ALIVE.")
                    f.hp = 0
                    st_.tally['prevented']['Cleansing Edge (freed alive)'] += 1
                    continue
                # PLACEHOLDER, calibrated to the S8 Cinderoll slot.
                _bite(st_, f, 6, 2, 6, 4, 'psychic', 'sings something wrong at')

    return run_fight(
        st, 'FIGHT 3: THE BLACKWATER SEAM',
        '(Dim light, and the singing is coming from the wrong direction. One of '
        'them has a notched fin. Stabby\'s Nichirin does not kill these: '
        'CLEANSING EDGE on a bloodied Hollowsong frees it, and it leaves alive.)',
        [('Blackcask', [cask], 0), ('Hollowsongs', songs, 2)], enemies)


def fight4(st):
    """THE GUARDIAN'S TRENCH. Kyogre (AC 18, 250 Black Water) + The Quiet Hand
    (AC 17, 120). Kyogre's hit points are the corruption riding it, not its life:
    at 0 the guardian is FREE. The spike is NOT a target; that was last session.

    [DM CHECK] 250 + 120 = 370, against the 458 the canon total implies."""
    st.lilly.pos = [15, 23]; st.stabby.pos = [15, 21]; st.ursa.pos = [17, 23]
    st.ghost.pos = [14, 22]; st.puff.pos = [16, 24]; st.cannon.pos = [17, 24]
    kyogre = Actor('Kyogre', 'K', 'foe', 18, ehp(250), (15, 10), 60,
                   saves=dict(str=8, dex=3, con=7, wis=4),
                   resist={'nm-bludgeoning', 'nm-piercing', 'nm-slashing'},
                   immune={'cold', 'poison'},
                   cond_imm={'charmed', 'frightened', 'prone', 'restrained'},
                   reach=20)
    kyogre.undertow = 0
    hand = Actor('The Quiet Hand', 'Q', 'foe', 17, ehp(120), (14, 8), 30,
                 saves=dict(str=4, dex=4, con=4, wis=5))
    hand.looked_up = False

    def enemies(st_, actors, rnd):
        for f in actors:
            if f.hp <= 0:
                continue
            if f.name == 'The Quiet Hand':
                if not f.looked_up:
                    # Canon: until it looks up it takes no action but driving the
                    # spike, does not defend itself, and every attack against it
                    # has Advantage. [DM CHECK] it looks up when Bloodied here.
                    f.exposed = True
                    if f.hp <= f.hp_max // 2:
                        f.looked_up = True
                        f.exposed = False
                        log("    THE QUIET HAND stops. It sets the hammer down, "
                            "and for the first time it looks up.")
                    else:
                        log("    The Quiet Hand drives the spike another inch. "
                            "It has not looked up.")
                    continue
                # PLACEHOLDER hammer.
                _bite(st_, f, 9, 2, 10, 5, 'force', 'swings the hammer at')
                continue
            # ---- Kyogre
            phase = 1 if f.hp > 175 else (2 if f.hp > 100 else 3)
            if phase == 3 and not getattr(f, 'announced', False):
                f.announced = True
                log("    THE UNDERTOW TURNS. It stops trying to leave. "
                    "Everything it has left, it spends here.")
            if f.undertow <= 0 or phase == 3:
                f.undertow = 3 if phase < 3 else 1
                pool = [h for h in st_.pcs if h.alive and f.dist_ft(h) <= 60]
                if pool:
                    log("    Kyogre: UNDERTOW, the whole gallery pulls toward the "
                        "trench (DEX DC 17).")
                    for h in pool:
                        raw = d(4, 10)
                        if st_.hero_save(h, 'dex', 17):
                            got = deal(st_, h, [(raw // 2, 'bludgeoning')], attacker=f)
                            log(f"      {h.name} sets their feet: {got}.")
                        else:
                            got = deal(st_, h, [(raw, 'bludgeoning')], attacker=f)
                            log(f"      {h.name} is dragged under for {got}.")
                    continue
            f.undertow -= 1
            # Fluke, +13 for 3d8+5 at reach 20 (canon).
            _bite(st_, f, 13, 3, 8, 5, 'bludgeoning', 'lands the FLUKE on', 20)

    return run_fight(
        st, 'FIGHT 4: THE GUARDIAN\'S TRENCH',
        '(Kyogre is mid-corruption and the spike is still being driven. The '
        'hit points are the black water riding it, not its life: at zero the '
        'guardian is free.)',
        [('Kyogre', [kyogre], 2), ('The Quiet Hand', [hand], -3)], enemies, cap=14)


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
