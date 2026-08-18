"""Session 8 (Underroot) full-run combat simulation.

Party of three level-SEVEN heroes plus DM-run Ghostbloom and Puff, per:
  characters/builders/build_lilly.py / build_stabby.py / build_ursa.py (v3, L7)
  reference/campaign/{lilly,stabby,ursa}_kit.md
  reference/campaign/session_08_part_two.md (all four fights)
  memory/house_rules.md

Run structure: LONG REST -> Fight 1 (Mosslight) -> Fight 2 (Chime Reef) ->
SHORT REST -> Fight 3 (Glassed Gallery) -> BOSS (Groudon). Resources carry.

Table-relative tactics: model what the kids actually do, not RAW-optimal play.
The sim assumes they find each fight's intended lever, but only after a round
of flailing, which is how the Session 7 sim was tuned.

Simplifications, for the report:
- Positioning abstracted to melee/ranged bands; cones and lines hit the cluster.
- Fight 2: the party works out thunder-stun from round 2 (Thunderwave, Shatter,
  and the reef-spire trick), which is the designed solution.
- Fight 3: the roots lever is used from round 2 by whoever is free.
- Boss: they go for the SPIKE from round 1, because Aelwyn told them to look for
  what is hurting it. The encounter ends when the spike breaks; Groudon's own HP
  is tracked only to confirm they never have to chew through it.
- Stabby's Cleansing Edge is applied whenever he connects, which is what shuts
  off Rotbloom re-bloom and Weeper regeneration.
"""
import random
from statistics import mean

N_RUNS = 3000
rng = random.Random(20260817)

# LEVERS: set False to simulate a table that never works out the intended
# solution to a fight. The gap between the two runs is the real design margin.
LEVERS = True


def d(n, s):
    return sum(rng.randint(1, s) for _ in range(n))


def d20(adv=False, dis=False):
    r = rng.randint(1, 20)
    if adv and not dis:
        r = max(r, rng.randint(1, 20))
    if dis and not adv:
        r = min(r, rng.randint(1, 20))
    return r


def attack(bonus, ac, adv=False, dis=False):
    r = d20(adv=adv, dis=dis)
    if r == 20:
        return 'crit'
    if r == 1:
        return False
    return r + bonus >= ac


class Hero:
    def __init__(self, name, ac, hp, saves):
        self.name = name
        self.ac = ac
        self.hp_max = hp
        self.hp = hp
        self.saves = saves
        self.temp = 0
        self.down = False
        self.drops = 0
        self.deflect = False      # Stabby only: reaction available this round

    def save(self, stat, dc, adv=False, run=None):
        roll = d20(adv=adv) + self.saves.get(stat, 0)
        if roll < dc and run is not None and run.l_genius_left > 0                 and not run.lilly.down and roll + 5 >= dc:
            run.l_genius_left -= 1
            return True
        return roll >= dc

    def take(self, dmg):
        if self.down:
            return
        if self.deflect:          # Deflect Attacks, once per round
            self.deflect = False
            dmg = max(0, dmg - (d(1, 10) + 12))
        if self.temp:
            absorbed = min(self.temp, dmg)
            self.temp -= absorbed
            dmg -= absorbed
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0
            self.down = True
            self.drops += 1

    def heal(self, amt):
        self.hp = min(self.hp_max, self.hp + amt)
        if self.hp > 0:
            self.down = False


class Enemy:
    def __init__(self, name, ac, hp, con=0, dex=0, vuln=None,
                 resist_nonmagic=False, regen=0):
        self.name = name
        self.ac = ac
        self.hp = hp
        self.hp_max = hp
        self.con = con
        self.dex = dex
        self.vuln = vuln or set()
        self.resist_nonmagic = resist_nonmagic
        self.regen = regen
        self.stunned = False
        self.cleansed = False
        self.vulnerable_now = False

    @property
    def alive(self):
        return self.hp > 0

    def take(self, dmg, dtype='untyped', magical=True):
        if getattr(self, 'thunder_only', False) and dtype != 'thunder':
            dmg //= 2
        if (not magical) and self.resist_nonmagic and dtype in (
                'bludgeoning', 'piercing', 'slashing'):
            dmg //= 2
        if dtype in self.vuln:
            dmg *= 2
        if self.vulnerable_now:
            dmg *= 2
        self.hp -= dmg
        # Re-Bloom / Glassbound are shut off by radiant OR force OR Cleansing
        # Edge, exactly as the statblocks say. Ursa's radiant and Lilly's force
        # both count; it is not Stabby's job alone.
        if dtype in ('radiant', 'force'):
            self.cleansed = True


class Run:
    def __init__(self):
        self.lilly = Hero('Lilly', 20, 52,
                          {'dex': 2, 'con': 5, 'int': 8, 'wis': 1, 'str': -1})
        self.stabby = Hero('Stabby', 18, 59,
                           {'dex': 8, 'con': 3, 'str': 2, 'wis': 2})
        self.ursa = Hero('Ursa', 18, 52,
                         {'dex': 2, 'con': 2, 'wis': 8, 'int': 4})
        self.ghost = Hero('Ghostbloom', 14, 52, {'dex': 3, 'con': 2, 'wis': 3})
        self.puff = Hero('Puff', 13, 15, {'dex': 4, 'con': 3, 'wis': 2})
        self.s_focus = 7
        self.s_metab = True
        self.s_fury = 3
        self.l_slot1 = 4
        self.l_slot2 = 3
        self.l_ward = 2
        self.l_genius = 5
        self.l_mm = 7
        self.u_slot3 = 3
        self.u_slot4 = 1
        self.u_bolts = 10
        self.u_fey_hp = 0
        self.u_hword = 4          # 1st-level slots he will spend on Healing Word
        self.u_aura = True        # Ash's Sigil-Stone, Aura of Vitality, 1/day
        self.u_aura_on = 0        # rounds remaining
        self.l_genius_left = 5
        self.g_light = 3

    @property
    def heroes(self):
        return [self.lilly, self.stabby, self.ursa]

    def alive_heroes(self):
        return [h for h in self.heroes if not h.down]

    def short_rest(self):
        for h in self.heroes:
            h.heal(int(h.hp_max * 0.45))
        self.stabby.deflect = True
        self.ghost.heal(self.ghost.hp_max)
        self.puff.heal(self.puff.hp_max)
        self.s_focus = 7
        self.g_light = 3
        self.l_ward = 2

    def ignite(self):
        if self.s_metab:
            self.s_metab = False
            self.s_focus = 7
            self.stabby.heal(7 + d(1, 8))
        if self.s_focus > 0:
            self.s_focus -= 1
            return True
        return False

    def ward(self):
        """Aether Ward: 2d8+5 temp HP to the party, 2 per short rest."""
        if self.l_ward > 0 and not self.lilly.down:
            self.l_ward -= 1
            t = d(2, 8) + 5
            for h in self.heroes:
                if not h.down:
                    h.temp = max(h.temp, t)
            return True
        return False


def pick_target(run):
    live = run.alive_heroes()
    return rng.choice(live) if live else None


def stabby_turn(run, foes, ignited, spike=None, climber=False):
    s = run.stabby
    if s.down:
        return

    def live():
        out = [f for f in foes if f.alive]
        if spike is not None and spike.alive and climber:
            out = [spike] + out
        return out

    for _ in range(2):
        ls = live()
        if not ls:
            return
        t = ls[0]
        res = attack(10, t.ac)
        if res:
            dmg = d(2 if res == 'crit' else 1, 10) + 7
            if ignited:
                dmg += 2
            if run.s_fury > 0:
                dmg += 3
                run.s_fury -= 1
            t.take(dmg, 'force' if ignited else 'slashing')
            t.cleansed = True
    ls = live()
    if not ls:
        return
    t = ls[0]
    if run.s_focus > 0:
        run.s_focus -= 1
        if attack(10, t.ac):
            before = t.alive
            t.take(d(3, 8) + 9, 'force')
            t.cleansed = True
            if before and not t.alive:
                run.s_focus += 1
    else:
        if attack(10, t.ac):
            t.take(d(1, 8) + 7, 'force')
            t.cleansed = True


def lilly_turn(run, foes, clumped=0, big=None, spike=None):
    l = run.lilly
    if l.down:
        return
    ls = [f for f in foes if f.alive]
    tgt = big if (big and big.alive) else (ls[0] if ls else None)
    if tgt is None and not (spike and spike.alive):
        return
    # bonus action: cannon, Force Ballista
    if tgt is not None and attack(8, tgt.ac):
        tgt.take(d(2, 8) + 2, 'force')
    # action
    if clumped >= 3 and run.l_slot2 > 0 and ls:
        run.l_slot2 -= 1
        for e in ls[:clumped]:
            dmg = d(3, 8) + d(1, 8)
            e.take(dmg if d20() + e.con < 16 else dmg // 2, 'thunder')
    elif spike is not None and spike.alive:
        # ranged fire at a spike embedded in a moving mountain: disadvantage
        if run.l_slot2 > 0:
            run.l_slot2 -= 1
            for _ in range(3):
                if attack(8, spike.ac, dis=True):
                    spike.take(d(2, 6), 'force')
        elif attack(10, spike.ac, dis=True):
            spike.take(d(1, 10) + 7 + d(1, 6) + d(1, 8), 'force')
    elif tgt is not None and attack(10, tgt.ac):
        tgt.take(d(1, 10) + 7 + d(1, 6) + d(1, 8), 'thunder')
    # Puff with the wand of magic missiles
    if not run.puff.down and run.l_mm > 0:
        run.l_mm -= 1
        pool = [f for f in foes if f.alive]
        if spike is not None and spike.alive:
            pool = [spike] + pool
        for _ in range(3):
            if pool:
                pool[0].take(d(1, 4) + 1, 'force')
                pool = [f for f in pool if f.alive]


def ursa_turn(run, foes, big=None, spike=None):
    u = run.ursa
    if u.down:
        return

    def live():
        return [f for f in foes if f.alive]

    ls = live()
    if not ls:
        ls = [spike] if (spike is not None and spike.alive) else []
    if not ls:
        return
    # bonus: star-arrow
    if attack(10, ls[0].ac):
        ls[0].take(d(1, 8) + 5, 'radiant')
    # the fey spirit acts on his turn
    if run.u_fey_hp > 0:
        ls = live()
        if ls and attack(10, ls[0].ac):
            ls[0].take(d(2, 6) + 6, 'force')
    # action
    ls = live()
    if not ls:
        return
    ground = [f for f in foes if f.alive]
    if spike is not None and spike.alive and len(ground) < 3:
        if attack(10, spike.ac, dis=True):
            spike.take(d(2, 8) + 5 + d(1, 8), 'radiant')
    elif len(ground) >= 4 and run.u_slot4 > 0:
        run.u_slot4 -= 1
        for e in ground[:5]:
            dmg = d(2, 10) + d(4, 6)
            e.take(dmg if d20() + e.dex < 16 else dmg // 2, 'cold')
    elif big is not None and big.alive and run.u_bolts > 0:
        run.u_bolts -= 1
        if attack(10, big.ac):
            big.take(d(4, 6) + d(1, 8), 'radiant')
    elif attack(10, ls[0].ac):
        ls[0].take(d(2, 8) + 5 + d(1, 8), 'radiant')


def ghost_turn(run):
    if run.ghost.down or run.g_light <= 0:
        return
    hurt = [h for h in run.heroes if h.down or h.hp < h.hp_max * 0.35]
    if hurt:
        run.g_light -= 1
        hurt[0].heal(d(1, 8) + 3)


def round_start(run):
    run.stabby.deflect = True
    if run.u_aura_on > 0:
        run.u_aura_on -= 1
        hurt = sorted(run.alive_heroes() + [h for h in run.heroes if h.down],
                      key=lambda h: h.hp)
        if hurt:
            hurt[0].heal(d(2, 6))


def party_turn(run, foes, ignited, clumped=0, big=None, spike=None, climber=False):
    # Ursa triages before anything else: a downed friend is the priority
    downed = [h for h in run.heroes if h.down]
    if downed and not run.ursa.down:
        if run.u_hword > 0:
            run.u_hword -= 1
            downed[0].heal(d(2, 4) + 5)
        elif run.u_aura:
            run.u_aura = False
            run.u_aura_on = 10
            downed[0].heal(d(2, 6))
    stabby_turn(run, foes, ignited, spike=spike, climber=climber)
    lilly_turn(run, foes, clumped=clumped, big=big, spike=spike)
    ursa_turn(run, foes, big=big, spike=spike)
    ghost_turn(run)


def fight1(run):
    ignited = run.ignite()
    foes = ([Enemy('Rotbloom', 13, 28, con=3, dex=1, regen=8) for _ in range(5)] +
            [Enemy('Mossmite', 13, 10, con=1, dex=3) for _ in range(5)])
    if run.u_slot3 > 0:
        run.u_slot3 -= 1
        run.u_fey_hp = 30
    rnds = 0
    while any(f.alive for f in foes) and run.alive_heroes() and rnds < 12:
        rnds += 1
        round_start(run)
        for f in foes:
            cleansed = f.cleansed
            # Re-Bloom: dropped without radiant or Cleansing Edge, it comes back
            if f.regen and not f.alive and not cleansed:
                f.hp = f.hp_max
            f.cleansed = False
        party_turn(run, foes, ignited, clumped=4)
        for f in [x for x in foes if x.alive]:
            t = pick_target(run)
            if not t:
                break
            if f.name == 'Rotbloom':
                if rng.random() < 0.5:      # Spore Puff on the cluster
                    for h in run.alive_heroes():
                        dmg = d(2, 6)
                        h.take(dmg // 2 if h.save('con', 12) else dmg)
                elif attack(5, t.ac):
                    t.take(d(2, 4) + 3)
            elif attack(5, t.ac):
                t.take(d(1, 4) + 3)
    return rnds


def fight2(run):
    ignited = run.ignite()
    stones = [Enemy('Chimestone', 17, 68, con=4, dex=-1, vuln={'thunder'}) for _ in range(3)]
    for st in stones:
        st.resist_nonmagic = True
    foes = (stones +
            [Enemy('Shardwing', 15, 28, con=1, dex=4, vuln={'thunder'}) for _ in range(3)])
    rnds = 0
    while any(f.alive for f in foes) and run.alive_heroes() and rnds < 14:
        rnds += 1
        round_start(run)
        if LEVERS and rnds >= 2:
            for f in [x for x in foes if x.alive][:3]:
                if d20() + f.con < 14:
                    f.stunned = True
                    f.vulnerable_now = True
        party_turn(run, foes, ignited, clumped=3)
        for f in [x for x in foes if x.alive]:
            f.vulnerable_now = False
            if f.stunned:
                f.stunned = False
                continue
            t = pick_target(run)
            if not t:
                break
            if f.name == 'Chimestone':
                for _ in range(2):
                    if attack(7, t.ac):
                        t.take(d(2, 8) + 4)
            elif attack(7, t.ac):
                t.take(d(2, 6) + 4 + d(1, 6))
    return rnds


def fight3(run):
    ignited = run.ignite()
    run.ward()
    weeper = Enemy('Glass Weeper', 17, 140, con=5, dex=-1,
                   resist_nonmagic=True, regen=12)
    rolls = [Enemy('Cinderoll', 15, 22, con=1, dex=2) for _ in range(5)]
    foes = [weeper] + rolls
    burst_done = 0
    rnds = 0
    while weeper.alive and run.alive_heroes() and rnds < 16:
        rnds += 1
        round_start(run)
        # Glassbound: it knits ALL the way back unless somebody stripped it
        stripped = weeper.cleansed or weeper.vulnerable_now
        if weeper.regen and not stripped and weeper.alive:
            weeper.hp = weeper.hp_max
        weeper.cleansed = False
        weeper.vulnerable_now = (LEVERS and rnds >= 2 and d20() + 5 >= 14)
        was_stripped = weeper.vulnerable_now
        party_turn(run, foes, ignited, clumped=3, big=weeper)
        weeper.vulnerable_now = False
        if weeper.alive:
            for _ in range(3):
                t = pick_target(run)
                if t and attack(8, t.ac):
                    t.take(d(2, 8) + 5)
            if rnds % 2 == 0:
                for h in run.alive_heroes():
                    dmg = d(6, 6)
                    h.take(dmg if not h.save('con', 15, run=run) else dmg // 2)
        for c in [x for x in rolls if x.alive]:
            t = pick_target(run)
            if t and attack(5, t.ac):
                t.take(d(2, 4) + 2 + d(2, 6))
        # Burst: every Cinderoll killed this round detonates on whoever is close
        dead_now = len([x for x in rolls if not x.alive]) - burst_done
        for _ in range(max(0, dead_now)):
            burst_done += 1
            for h in run.alive_heroes():
                if rng.random() < 0.45:
                    dmg = d(2, 6)
                    h.take(0 if h.save('dex', 12) else dmg)
    return rnds


def boss(run):
    ignited = run.ignite()
    run.ward()
    groudon = Enemy('Groudon', 18, 230, con=7, dex=-2, resist_nonmagic=True)
    spike = Enemy('Spike', 18, 110)
    glasslings = []
    climbing = False
    rnds = 0
    while spike.alive and run.alive_heroes() and rnds < 20:
        rnds += 1
        round_start(run)
        glasslings.append(Enemy('Glassling', 14, 10, con=1, dex=3))
        glasslings = [g for g in glasslings if g.alive]
        # Agony: every other round, and only whoever is close in
        if rnds % 2 == 0:
            for h in run.alive_heroes():
                if rng.random() < 0.45:
                    dmg = d(3, 6)
                    h.take(0 if h.save('dex', 16) else dmg)
        party_turn(run, glasslings, ignited, big=groudon, spike=spike,
                   climber=climbing)
        if not spike.alive:
            break
        # Thrash: the spike was struck, so Groudon tries to shake the climber off
        if climbing and not run.stabby.down:
            if d20() + 8 < 15:
                climbing = False
                run.stabby.take(d(3, 6))
        elif not run.stabby.down:
            climbing = True   # spends his movement re-climbing
        if rnds % 3 == 0:
            # Magma Vent is a telegraphed LINE: they scatter, so it catches some
            for h in run.alive_heroes():
                if rng.random() < 0.55:
                    dmg = d(10, 6)
                    h.take(dmg // 2 if h.save('dex', 17, run=run) else dmg)
        else:
            # he swings at whatever is on him, which is the climber
            t = run.stabby if (climbing and not run.stabby.down) else pick_target(run)
            if t and attack(12, t.ac):
                t.take(d(3, 10) + 8)
        for g in [x for x in glasslings if x.alive]:
            t = pick_target(run)
            if t and attack(5, t.ac):
                t.take(d(1, 6) + 3)
    return rnds, spike.alive, groudon.hp


def simulate():
    s = {'wipe': 0, 'spike_failed': 0, 'rounds': [], 'drops': [],
         'f1': [], 'f2': [], 'f3': [], 'boss': [], 'hp_pre_rest': [],
         'gh': [], 'dl': 0, 'ds': 0, 'du': 0, 'wipe_where': {}}
    for _ in range(N_RUNS):
        run = Run()
        r1 = fight1(run)
        if not run.alive_heroes():
            s['wipe'] += 1
            s['wipe_where']['f1'] = s['wipe_where'].get('f1', 0) + 1
            continue
        for h in run.heroes:
            if h.down:
                h.heal(d(2, 4) + 5)
        r2 = fight2(run)
        if not run.alive_heroes():
            s['wipe'] += 1
            s['wipe_where']['f2'] = s['wipe_where'].get('f2', 0) + 1
            continue
        s['hp_pre_rest'].append(sum(h.hp for h in run.heroes))
        run.short_rest()
        r3 = fight3(run)
        if not run.alive_heroes():
            s['wipe'] += 1
            s['wipe_where']['f3'] = s['wipe_where'].get('f3', 0) + 1
            continue
        for h in run.heroes:
            if h.down:
                h.heal(d(2, 4) + 5)
        r4, spike_alive, gh = boss(run)
        if not run.alive_heroes():
            s['wipe'] += 1
            s['wipe_where']['boss'] = s['wipe_where'].get('boss', 0) + 1
            continue
        if spike_alive:
            s['spike_failed'] += 1
        s['f1'].append(r1)
        s['f2'].append(r2)
        s['f3'].append(r3)
        s['boss'].append(r4)
        s['rounds'].append(r1 + r2 + r3 + r4)
        s['gh'].append(gh)
        s['drops'].append(sum(h.drops for h in run.heroes))
        s['dl'] += run.lilly.drops
        s['ds'] += run.stabby.drops
        s['du'] += run.ursa.drops
    return s


if __name__ == '__main__':
    s = simulate()
    ok = max(1, len(s['rounds']))
    line = '=' * 64
    print(line)
    print('SESSION 8: UNDERROOT   %d runs, three heroes at level 7' % N_RUNS)
    print(line)
    print('Party wipes .................. %d  (%.2f%%)'
          % (s['wipe'], 100.0 * s['wipe'] / N_RUNS))
    if s['wipe_where']:
        print('   where: %s' % ', '.join('%s %d' % kv for kv in sorted(s['wipe_where'].items())))
    print('Spike never broken ........... %d  (%.2f%%)'
          % (s['spike_failed'], 100.0 * s['spike_failed'] / N_RUNS))
    print()
    print('Mean rounds per fight')
    print('   1  Mosslight, Rotblooms ... %.1f' % mean(s['f1']))
    print('   2  Chime Reef ............. %.1f' % mean(s['f2']))
    print('   3  Glassed Gallery ........ %.1f' % mean(s['f3']))
    print('   4  Groudon, to the spike .. %.1f' % mean(s['boss']))
    print('      whole run .............. %.1f' % mean(s['rounds']))
    print()
    print('Party HP pool entering the short rest .. %.0f of 163'
          % mean(s['hp_pre_rest']))
    print('Hero drops to 0 per run ................ %.2f' % mean(s['drops']))
    print('   Lilly %.2f   Stabby %.2f   Ursa %.2f'
          % (s['dl'] / ok, s['ds'] / ok, s['du'] / ok))
    print('Groudon HP left when the spike broke ... %.0f of 230' % mean(s['gh']))
    print(line)
