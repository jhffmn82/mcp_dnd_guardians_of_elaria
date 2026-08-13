"""Session 7 (Gearhaven) full-day combat simulation.

Party of three level-5 heroes + DM-run Ghostbloom, per:
  characters/builders/build_lilly.py / build_stabby.py / build_ursa.py (v3 sheets)
  characters/ghostbloom_statblock.docx (Sessions 1-7 card)
  sessions/session_07_gearhaven.docx appendix bestiary (all four fights)
  memory/house_rules.md (cannon mode per activation, Starseed rules, Air spirit 20 HP)

Day structure per the run sheet: LONG REST -> Fight 1 -> Fight 2 -> SHORT REST
-> Fight 3 -> Boss. Resources carry across the day.

Table-relative tactics: model what the kids actually do (katana flurries,
Stunning Strike on big targets, free Guiding Bolts, cannon every round,
telegraphed vulnerabilities exploited), not RAW-optimal play.

Simplifications (documented for the report):
- Positioning abstracted to melee/ranged bands; cones hit the melee cluster.
- Fight 2 Skitch clock: one crawler goes for Skitch when the guard hero is
  down or webbed; a reach means immediate death saves (3 fails = dead, but
  Ursa Healing Word resets; we track "Skitch reached" events).
- Fight 3 runs a fixed engagement window (Lilly reaches the engine on round 4,
  round 5 if the Drudges body-block, per the scaling dial); sim measures the
  damage the party eats in that window.
- Boss phase 1 targets legs; phase 2 the body to 0 (the HP-220 'pacing dial'
  worst case). Free prep window + party-first initiative applied.
"""
import random
from statistics import mean

N_RUNS = 3000
rng = random.Random(20260813)

def d(n, s):
    return sum(rng.randint(1, s) for _ in range(n))

def d20(adv=False, dis=False):
    r = rng.randint(1, 20)
    if adv and not dis:
        r = max(r, rng.randint(1, 20))
    if dis and not adv:
        r = min(r, rng.randint(1, 20))
    return r

class Hero:
    def __init__(self, name, ac, hp, saves):
        self.name = name; self.ac = ac; self.hp_max = hp; self.hp = hp
        self.saves = saves  # dict of mods
        self.down = False; self.dead = False
        self.drops = 0
        self.reaction = True

    def save(self, stat, dc, adv=False):
        return d20(adv=adv) + self.saves.get(stat, 0) >= dc

    def take(self, dmg, party=None):
        if self.down:
            return
        self.hp -= dmg
        if self.hp <= 0:
            self.hp = 0; self.down = True; self.drops += 1

    def heal(self, amt):
        if self.dead:
            return
        was_down = self.down
        self.hp = min(self.hp_max, self.hp + amt)
        if self.hp > 0:
            self.down = False

class Day:
    """Tracks the whole party's resources across the four fights."""
    def __init__(self):
        self.lilly = Hero('Lilly', 20, 38, {'dex': 2, 'con': 2, 'wis': 0, 'str': 0, 'int': 5})
        self.stabby = Hero('Stabby', 18, 43, {'dex': 8, 'con': 3, 'wis': 2, 'str': 2, 'int': -1})
        self.ursa = Hero('Ursa', 18, 38, {'dex': 2, 'con': 2, 'wis': 8, 'str': -1, 'int': 4})
        self.ghost = Hero('Ghostbloom', 15, 52, {'dex': 7, 'con': 7, 'wis': 5, 'str': -1, 'int': 1})
        self.heroes = [self.lilly, self.stabby, self.ursa, self.ghost]
        # resources
        self.l_slot1 = 4; self.l_slot2 = 2
        self.s_focus = 5; self.s_fury = 3; self.s_metab = True; self.s_fly = True
        self.u_slot1 = 4; self.u_slot2 = 3; self.u_slot3 = 2
        self.u_ws = 2; self.u_starmap = 5; self.u_staff = 5
        self.g_light = 3
        self.skitch_reached = 0
        self.log = {}

    def short_rest(self):
        # hit dice: kids spend freely; assume each hero heals to near-full
        # (Stabby d8+3 x4 available, etc.) - model as heal to full minus a little
        for h in [self.lilly, self.stabby, self.ursa]:
            h.heal(h.hp_max)  # generous but realistic with 4-5 hit dice each
        self.ghost.heal(self.ghost.hp_max)
        self.s_focus = 5
        self.u_ws = min(2, self.u_ws + 1)
        self.g_light = 3

    def guardian_light(self, ally):
        if self.g_light > 0 and (ally.down or ally.hp < ally.hp_max * 0.3):
            self.g_light -= 1
            ally.heal(d(1, 8) + 3)
            return True
        return False

class Enemy:
    def __init__(self, name, ac, hp, init_mod=0, resist_nonmagic=False,
                 vuln=None, con=0, dex=0, wis=0, immune_fright=False):
        self.name = name; self.ac = ac; self.hp = hp; self.hp_max = hp
        self.init = init_mod
        self.resist_nonmagic = resist_nonmagic
        self.vuln = vuln or set()
        self.con = con; self.dex = dex; self.wis = wis
        self.immune_fright = immune_fright
        self.stunned = False; self.frightened = False
        self.unreal = False; self.webbed_target = None

    @property
    def alive(self):
        return self.hp > 0

    def take(self, dmg, dtype='untyped', magical=True):
        if self.unreal and dtype not in ('force', 'radiant'):
            dmg //= 2
        if (not magical) and self.resist_nonmagic and dtype in ('bludgeoning', 'piercing', 'slashing'):
            dmg //= 2
        if dtype in self.vuln:
            dmg *= 2
        self.hp -= dmg

def attack(bonus, target_ac, adv=False, dis=False):
    r = d20(adv=adv, dis=dis)
    if r == 20:
        return 'crit'
    if r == 1:
        return False
    return r + bonus >= target_ac

# ---------------- hero turn helpers ----------------

def stabby_turn(day, targets, big=None):
    """Two katana swings + flurry/punch. Stunning Strike on `big` if focus."""
    s = day.stabby
    if s.down or not targets:
        return
    tgt = big if (big and big.alive) else targets[0]
    dmg_out = 0
    stun_tried = False
    for _ in range(2):
        if not tgt.alive:
            live = [t for t in targets if t.alive]
            if not live:
                return
            tgt = live[0]
        res = attack(9, tgt.ac, dis=tgt.frightened is False and False)
        if res:
            dmg = d(2 if res == 'crit' else 1, 10) + 6 + 2  # katana + cold
            if day.s_fury > 0:
                dmg += 3; day.s_fury -= 1  # Fury of the Small, 1/turn
            tgt.take(dmg, 'slashing')
            if (not stun_tried and big and tgt is big and day.s_focus >= 2
                    and not tgt.stunned):
                day.s_focus -= 1; stun_tried = True
                if d20() + tgt.con < 13:
                    tgt.stunned = True
    # bonus action: flurry if focus, else one punch
    swings = 2 if day.s_focus > 0 else 1
    if swings == 2:
        day.s_focus -= 1
    for _ in range(swings):
        live = [t for t in targets if t.alive]
        if not live:
            return
        if not tgt.alive:
            tgt = live[0]
        res = attack(8, tgt.ac)
        if res:
            tgt.take(d(2 if res == 'crit' else 1, 8) + 5, 'bludgeoning', magical=False)

def lilly_turn(day, targets, clumped=False, fire_vuln=False, big=None, protector_ok=False):
    """Bonus: cannon. Action: Fire Bolt (or Scorching Ray on the boss)."""
    l = day.lilly
    if l.down or not targets:
        return
    live = [t for t in targets if t.alive]
    if not live:
        return
    tgt = big if (big and big.alive) else live[0]
    if protector_ok and sum(1 for h in day.heroes if not h.down and h.hp < h.hp_max * 0.55) >= 2:
        # Protector mode: 1d8+5 shield-points to Lilly and friends (modeled as healing)
        for h in day.heroes:
            if not h.down:
                h.heal(d(1, 8) + 5)
        res = attack(8, tgt.ac)
        if res:
            n = 2 if res != 'crit' else 4
            tgt.take(d(n, 10) + d(1, 8) + 2, 'fire')
        return
    # cannon (bonus action): flamethrower on clumps / vs fire-vulnerable, else ballista
    if (clumped or fire_vuln) and len(live) >= 2 or (fire_vuln and len(live) >= 1):
        for t in live[:2]:
            dmg = d(2, 8) + 2
            if d20() + t.dex >= 16:
                dmg //= 2
            t.take(dmg, 'fire')
    else:
        res = attack(8, tgt.ac)
        if res:
            tgt.take(d(4 if res == 'crit' else 2, 8) + 2, 'force')
    # action
    live = [t for t in targets if t.alive]
    if not live:
        return
    if not tgt.alive:
        tgt = live[0]
    res = attack(8, tgt.ac)
    if res:
        n = 2 if res != 'crit' else 4
        tgt.take(d(n, 10) + d(1, 8) + 2, 'fire')  # Fire Bolt + dagger rider

def ursa_turn(day, targets, mode, spirit=None, big=None):
    """mode: 'call_lightning' | 'guiding_bolt' | 'flaming_sphere'."""
    u = day.ursa
    if u.down or not targets:
        return
    live = [t for t in targets if t.alive]
    if not live:
        return
    tgt = big if (big and big.alive) else live[0]
    if mode == 'call_lightning':
        dmg = d(3, 10)
        if d20() + tgt.dex >= 16:
            tgt.take(dmg, 'lightning')
        else:
            tgt.take(dmg // 2, 'lightning')
    elif mode == 'flaming_sphere':
        dmg = d(2, 6)
        if d20() + tgt.dex >= 16:
            dmg //= 2
        tgt.take(dmg, 'fire')
    else:
        # free Guiding Bolt while charges remain, else Starry Wisp
        if day.u_starmap > 0 or day.u_staff > 0:
            if day.u_starmap > 0:
                day.u_starmap -= 1
            else:
                day.u_staff -= 1
            res = attack(8, tgt.ac)
            if res:
                tgt.take(d(8 if res == 'crit' else 4, 6) + d(1, 4), 'radiant')
        else:
            res = attack(8, tgt.ac)
            if res:
                tgt.take(d(4 if res == 'crit' else 2, 8) + d(1, 4), 'radiant')
    # bonus: star-arrow (Starry Form assumed up: Wild Shape spent per fight as needed)
    live = [t for t in targets if t.alive]
    if live:
        t2 = big if (big and big.alive) else live[0]
        res = attack(8, t2.ac)
        if res:
            t2.take(d(2 if res == 'crit' else 1, 8) + 5, 'radiant')
    # spirit attack (shares turn)
    if spirit and spirit['hp'] > 0:
        live = [t for t in targets if t.alive]
        if live:
            t3 = big if (big and big.alive) else live[0]
            res = attack(8, t3.ac)
            if res:
                t3.take(d(1, 8) + 6, 'piercing')

def ghost_turn(day, targets, big=None):
    g = day.ghost
    if g.down or not targets:
        return
    live = [t for t in targets if t.alive]
    if not live:
        return
    tgt = big if (big and big.alive) else live[0]
    for _ in range(2):
        if not tgt.alive:
            live = [t for t in targets if t.alive]
            if not live:
                return
            tgt = live[0]
        res = attack(7, tgt.ac)
        if res:
            tgt.take(d(1, 8) + 5, 'slashing')
            tgt.take(d(1, 6), 'necrotic')
            if not tgt.immune_fright and d20() + tgt.wis < 15:
                tgt.frightened = True

def enemy_attack(day, hero, bonus, ndice, dsize, flat, dtype='bludgeoning'):
    """One enemy attack vs a hero, with Shield / Deflect reactions."""
    if hero.down:
        return 0
    r = d20()
    if r == 1:
        return 0
    crit = (r == 20)
    total = r + bonus
    hits = crit or total >= hero.ac
    # Lilly Shield reaction
    if (hits and not crit and hero is day.lilly and hero.reaction
            and day.l_slot1 > 0 and total < hero.ac + 5):
        day.l_slot1 -= 1; hero.reaction = False
        return 0
    if not hits:
        return 0
    dmg = d(ndice * (2 if crit else 1), dsize) + flat
    # Stabby Deflect vs physical
    if (hero is day.stabby and hero.reaction
            and dtype in ('bludgeoning', 'piercing', 'slashing')):
        hero.reaction = False
        dmg = max(0, dmg - (d(1, 10) + 10))
    hero.take(dmg)
    if hero.down:
        if getattr(day, 'boss_body', None) is not None:
            day.boss_drop_hp.append(day.boss_body.hp)
        day.guardian_light(hero)   # Ghostbloom catches the drop
        if hero.down and not day.ursa.down and day.u_slot1 > 0:
            day.u_slot1 -= 1       # Healing Word next turn (modeled instantly)
            hero.heal(d(2, 4) + 5)
    return dmg

# ---------------- Fight 1: the market ----------------

def fight1(day):
    servitors = [Enemy('Servitor', 15, 39, 3, con=3, dex=3, wis=-1, immune_fright=True,
                       resist_nonmagic=True) for _ in range(2)]
    hauler = Enemy('Hauler', 16, 76, -1, con=4, dex=-1, wis=-1, immune_fright=True,
                   resist_nonmagic=True, vuln={'lightning'})
    enemies = servitors + [hauler]
    rounds = 0
    grabbed = None
    while any(e.alive for e in enemies) and rounds < 12:
        rounds += 1
        for h in day.heroes:
            h.reaction = True
        live = [e for e in enemies if e.alive]
        # heroes act (rough initiative: Stabby, Ghost, Lilly, Ursa interleaved with enemies)
        stabby_turn(day, live, big=hauler)
        lilly_turn(day, [e for e in enemies if e.alive], big=hauler)
        # Ursa: Call Lightning on the telegraphed lightning-vulnerable Hauler
        ursa_turn(day, [e for e in enemies if e.alive],
                  'call_lightning' if hauler.alive else 'guiding_bolt', big=hauler)
        ghost_turn(day, [e for e in enemies if e.alive],
                   big=servitors[0] if servitors[0].alive else None)
        # death-sparks for servitors killed this round
        for s in servitors:
            if not s.alive and s.hp > -100:
                s.hp = -1000
                for h in (day.stabby, day.ghost):
                    if not h.down and not h.save('dex', 13):
                        h.take(d(2, 6))
        # enemies act
        for s in servitors:
            if not s.alive or s.stunned:
                s.stunned = False
                continue
            tgt = day.stabby if not day.stabby.down else day.ghost
            for _ in range(2):
                enemy_attack(day, tgt, 5, 1, 10, 3)
        if hauler.alive and not hauler.stunned:
            squishy = day.lilly if not day.lilly.down else day.ursa
            if grabbed is None and rng.random() < 0.5:
                if not squishy.save('dex', 14):
                    grabbed = squishy
            if grabbed and not grabbed.down:
                grabbed.take(d(3, 6))
                if rng.random() < 0.4:
                    grabbed = None  # escapes
            else:
                for _ in range(2):
                    enemy_attack(day, day.stabby if not day.stabby.down else day.ursa,
                                 6, 2, 8, 4)
        hauler.stunned = False
    day.u_slot3 -= 1  # Call Lightning slot
    day.u_ws -= 1     # Starry Form
    return rounds

# ---------------- Fight 2: the Underworks ----------------

def fight2(day):
    crawlers = [Enemy('Voltcrawler', 15, 22, 3, con=1, dex=3, wis=0) for _ in range(6)]
    brood = Enemy('Broodmother', 16, 95, 4, con=8, dex=7, wis=1, resist_nonmagic=True)
    enemies = crawlers + [brood]
    rounds = 0
    webbed = None
    while any(e.alive for e in enemies) and rounds < 14:
        rounds += 1
        for h in day.heroes:
            h.reaction = True
        # rift pulse (init 20): disadvantage modeled as a flat skip chance for enemies
        # phase-blink at start of crawler turns
        for c in crawlers:
            if c.alive:
                c.unreal = rng.randint(1, 6) <= 2
        # brood webs Stabby or Ursa turn 1+
        if brood.alive and webbed is None:
            victim = day.stabby if rng.random() < 0.5 else day.ursa
            if not victim.save('dex', 15):
                webbed = victim
        # heroes
        if webbed is day.stabby:
            # katana (cold) cuts the web: lose the turn's bonus economy, then free
            webbed = None
        else:
            stabby_turn(day, [e for e in enemies if e.alive], big=brood)
        lilly_turn(day, [e for e in enemies if e.alive], big=brood)  # Force Ballista counters Unreal
        if webbed is day.ursa:
            webbed = None if rng.random() < 0.6 else webbed
        else:
            ursa_turn(day, [e for e in enemies if e.alive], 'guiding_bolt', big=brood)
        ghost_turn(day, [e for e in enemies if e.alive])
        # Skitch clock: a crawler slips to Skitch if guard (Stabby) is down/webbed
        live_crawlers = [c for c in crawlers if c.alive]
        if live_crawlers and (day.stabby.down or webbed is day.stabby) and rng.random() < 0.5:
            day.skitch_reached += 1
        # enemies
        for c in live_crawlers:
            if c.frightened:
                c.frightened = False
                continue
            tgt = rng.choice([h for h in (day.stabby, day.ghost, day.ursa) if not h.down] or [day.lilly])
            enemy_attack(day, tgt, 5, 1, 6, 3, 'piercing')
            if rng.random() < 0.33:  # Arc recharge
                for h in (day.stabby, day.ghost):
                    if not h.down and not h.save('dex', 13):
                        h.take(d(2, 8))
        if brood.alive and not brood.stunned:
            if brood.frightened:
                brood.frightened = False
            else:
                tgt = day.stabby if not day.stabby.down else day.ursa
                for _ in range(2):
                    enemy_attack(day, tgt, 7, 1, 10, 4, 'slashing')
                if rng.random() < 0.167:  # Overcharge
                    for h in day.heroes:
                        if not h.down and h is not day.lilly:
                            if not h.save('con', 15):
                                h.take(d(4, 8))
                            else:
                                h.take(d(4, 8) // 2)
        brood.stunned = False
    day.u_ws -= 1 if day.u_ws > 0 else 0
    return rounds

# ---------------- Fight 3: the Verdant Plaza ----------------

def fight3(day):
    drudges = [Enemy('Drudge', 17, 68, -1, con=3, dex=-1, wis=-1, immune_fright=True,
                     resist_nonmagic=True, vuln={'fire'}) for _ in range(3)]
    FIX_ROUND = 4 + (1 if rng.random() < 0.5 else 0)
    rounds = 0
    sprout_count = 7
    while rounds < FIX_ROUND:
        rounds += 1
        for h in day.heroes:
            h.reaction = True
        live = [e for e in drudges if e.alive]
        # heroes: punch a hole in the ring; Lilly torches sproutlings + drudges
        stabby_turn(day, live or drudges, big=live[0] if live else None)
        # Lilly: flamethrower vs fire-vulnerable everything
        for t in (live[:2] if live else []):
            dmg = d(2, 8) + 2
            if d20() + t.dex >= 16:
                dmg //= 2
            t.take(dmg, 'fire')
        # sproutlings burn: 2-3 die per flamethrower/AoE round
        sprout_count = max(3, sprout_count - rng.randint(2, 3))
        # Ursa: Flaming Sphere (fire vuln) + star-arrow
        if day.u_slot2 > 0 and rounds == 1:
            day.u_slot2 -= 1
        ursa_turn(day, live or drudges, 'flaming_sphere', big=live[0] if live else None)
        ghost_turn(day, live or drudges)
        # enemies
        for dr in (e for e in drudges if e.alive):
            if dr.stunned:
                dr.stunned = False
                continue
            tgt = day.stabby if not day.stabby.down else (day.ghost if not day.ghost.down else day.ursa)
            for _ in range(2):
                enemy_attack(day, tgt, 6, 2, 8, 4)
            if rng.random() < 0.33:  # Sweep
                for h in (day.stabby, day.ghost):
                    if not h.down and not h.save('dex', 14):
                        h.take(d(2, 6) + 4)
        # sproutlings: shared turn, nip at whoever's up
        for _ in range(min(sprout_count, 4)):
            tgt = rng.choice([h for h in day.heroes if not h.down] or [day.lilly])
            r = d20()
            if r + 4 >= tgt.ac:
                tgt.take(d(1, 6) + 2, None)
    return rounds

# ---------------- Boss: the Grand Custodian ----------------

def boss(day, drop_log=None):
    legs = [Enemy('Leg', 15, 90, 0, con=6, dex=-2, wis=0, immune_fright=True) for _ in range(2)]
    body = Enemy('Body', 17, 220, 0, con=6, dex=-2, wis=0, immune_fright=True,
                 resist_nonmagic=True, vuln={'lightning'})
    for lg in legs:
        lg.resist_nonmagic = True
        lg.vuln = {'lightning'}
    # Uncanny Metabolism: Stabby refreshes at initiative
    if day.s_metab:
        day.s_metab = False
        day.s_focus = 5
        day.stabby.heal(5 + d(1, 8))
    # prep window: Air spirit out (20 HP house rule), Starry Form up, cannon set
    spirit = {'hp': 20}
    day.boss_body = body
    day.boss_drop_hp = getattr(day, 'boss_drop_hp', [])
    if day.u_slot2 > 0:
        day.u_slot2 -= 1
    day.u_ws = max(0, day.u_ws - 1)
    rounds = 0
    phase = 1
    core_flared = False
    while body.hp > 0 and rounds < 16:
        rounds += 1
        for h in day.heroes:
            h.reaction = True
        # ---- party acts first (huddle reward) ----
        if phase == 1:
            live_legs = [lg for lg in legs if lg.alive]
            tgt = live_legs[0] if live_legs else body
            stabby_turn(day, [tgt], big=tgt)
            lilly_turn(day, [tgt], big=tgt, protector_ok=True)
            # Ursa: free Guiding Bolts at the leg; Call Lightning if a 3rd slot remains
            mode = 'call_lightning' if day.u_slot3 > 0 else 'guiding_bolt'
            if mode == 'call_lightning' and rounds == 1:
                day.u_slot3 -= 1
            ursa_turn(day, [tgt], mode, spirit=spirit, big=tgt)
            ghost_turn(day, [tgt], big=tgt)
            if not any(lg.alive for lg in legs):
                phase = 2  # THE CRASH
        else:
            stabby_turn(day, [body], big=body)
            lilly_turn(day, [body], big=body, protector_ok=True)
            mode = 'call_lightning' if day.u_slot3 > 0 else 'guiding_bolt'
            ursa_turn(day, [body], mode, spirit=spirit, big=body)
            ghost_turn(day, [body], big=body)
        if body.hp <= 0:
            break
        hp_before = {h.name: h.down for h in day.heroes}
        # ---- giant acts ----
        melee = [h for h in (day.stabby, day.ghost) if not h.down]
        ranged = [h for h in (day.lilly, day.ursa) if not h.down]
        if phase == 1:
            # Stomp at melee or the spirit tank
            if spirit['hp'] > 0 and rng.random() < 0.5:
                spirit['hp'] -= d(2, 10) + 5
            elif melee:
                enemy_attack(day, rng.choice(melee), 8, 2, 10, 5)
            if rng.random() < 0.33 and melee:  # Backhand cone
                for h in melee:
                    if not h.save('dex', 15):
                        h.take(d(3, 8))
                    else:
                        h.take(d(3, 8) // 2)
            if ranged:  # Corrupt Bolt
                enemy_attack(day, rng.choice(ranged), 8, 3, 8, 0, 'lightning')
        else:
            # Clockwork Barrage (rech 4-6 ~ 50%)
            if rng.random() < 0.5:
                pool = [h for h in day.heroes if not h.down]
                for _ in range(3):
                    if pool:
                        enemy_attack(day, rng.choice(pool), 8, 2, 8, 3)
            # Chain Lightning Burst (rech 5-6 ~ 33%)
            if rng.random() < 0.33:
                pool = [h for h in day.heroes if not h.down]
                if pool:
                    first = rng.choice(pool)
                    enemy_attack(day, first, 8, 4, 8, 0, 'lightning')
                    for h in pool:
                        if h is not first and rng.random() < 0.6:
                            if h.save('dex', 15):
                                h.take(d(2, 8) // 2)
                            else:
                                h.take(d(2, 8))
            # Core Flare once below half
            if body.hp < 110 and not core_flared:
                core_flared = True
                for h in (day.stabby, day.ghost):
                    if not h.down and not h.save('con', 15):
                        h.take(d(2, 6))
            # kneeling stomp
            if melee and spirit['hp'] > 0 and rng.random() < 0.5:
                spirit['hp'] -= d(2, 10) + 5
            elif melee:
                enemy_attack(day, rng.choice(melee), 8, 2, 10, 5)
    if drop_log is not None:
        drop_log.append((body.hp, legs[0].hp, legs[1].hp))
    return rounds

# ---------------- run the day ----------------

stats = {k: [] for k in ['f1_rounds', 'f2_rounds', 'f3_rounds', 'boss_rounds']}
drops = {h: [0, 0, 0, 0] for h in ['Lilly', 'Stabby', 'Ursa', 'Ghostbloom']}
any_drop = [0, 0, 0, 0]
boss_drop_runs = 0
boss_droppers = {}
all_boss_drop_hp = []
skitch_events = 0
end_hp = []
slots_left = []

for _ in range(N_RUNS):
    day = Day()
    for h in day.heroes:
        h.drops = 0
    r1 = fight1(day); f1_drops = {h.name: h.drops for h in day.heroes}
    if any(f1_drops.values()):
        any_drop[0] += 1
    for h in day.heroes:
        h.drops = 0
    r2 = fight2(day)
    if any(h.drops for h in day.heroes):
        any_drop[1] += 1
    skitch_events += (1 if day.skitch_reached else 0)
    day.short_rest()
    for h in day.heroes:
        h.drops = 0
    r3 = fight3(day)
    if any(h.drops for h in day.heroes):
        any_drop[2] += 1
    for h in day.heroes:
        h.drops = 0
    day.boss_drop_hp = []
    rb = boss(day)
    all_boss_drop_hp.extend(day.boss_drop_hp)
    day.boss_body = None
    if any(h.drops for h in day.heroes):
        any_drop[3] += 1
        boss_drop_runs += 1
        for h in day.heroes:
            if h.drops:
                boss_droppers[h.name] = boss_droppers.get(h.name, 0) + 1
    stats['f1_rounds'].append(r1); stats['f2_rounds'].append(r2)
    stats['f3_rounds'].append(r3); stats['boss_rounds'].append(rb)
    end_hp.append(sum(h.hp for h in day.heroes) / sum(h.hp_max for h in day.heroes))
    slots_left.append((day.l_slot1, day.u_starmap + day.u_staff, day.s_focus, day.g_light))

print(f'runs: {N_RUNS}')
for k in stats:
    print(f'{k}: mean {mean(stats[k]):.1f}')
labels = ['Fight 1 (market)', 'Fight 2 (Underworks)', 'Fight 3 (plaza)', 'Boss (Custodian)']
for i, lab in enumerate(labels):
    print(f'{lab}: P(at least one hero drops) = {any_drop[i]/N_RUNS:.1%}')
print(f'Skitch reached by a crawler in {skitch_events/N_RUNS:.1%} of runs')
print('boss drops by hero (share of runs):',
      {k: f'{v/N_RUNS:.1%}' for k, v in sorted(boss_droppers.items())})
if all_boss_drop_hp:
    late = sum(1 for x in all_boss_drop_hp if x <= 60)
    print(f'boss drops happening at body HP <= 60 (saved by the pacing dial): {late/len(all_boss_drop_hp):.0%}')
print(f'party HP at end of day: mean {mean(end_hp):.0%} of max')
print(f'mean leftovers: Lilly 1st slots {mean(s[0] for s in slots_left):.1f}, '
      f'Ursa free bolts {mean(s[1] for s in slots_left):.1f}, '
      f'Stabby focus {mean(s[2] for s in slots_left):.1f}, '
      f"Ghostbloom Guardian's Light {mean(s[3] for s in slots_left):.1f}")
