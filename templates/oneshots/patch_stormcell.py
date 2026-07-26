# patch_stormcell.py: baseline Boomstick on every road (Shard retires everywhere),
# Storm Cell door with Arc/Thunder Wave/Counter-Bolt rounds (2 each per Long Rest).
import ast, io, os
os.chdir(r"C:\Users\jhffm\dnd-campaign")
p = "templates/build_compendium.py"
t = open(p, encoding="utf-8").read()
LQ, RQ = "“", "”"

old_intro = '''    ("gold", "Three masterworks of deep gnome artifice, forged for Lilly Glimmergear in the year "
             "apart. Three masterworks, one choice. Each door of Lilly's year apart leads to one "
             "of these treasures: stay and build the portal (the Sentinel), go home to "
             "Glimmerspire and Poots (Boomstick), or give the year to mote research (the Awakened "
             "Sphere). She walks one road and claims one masterwork. Every road fits inside her "
             "three attunement slots. On the Sphere's road the ledger closes at exactly three: "
             "Shard, Dynamo, Sphere. On the Sentinel's road a slot stays free, for the Dynamo "
             "itself is rebuilt into the guardian: two of three. And on Boomstick's road the "
             "Shard truly retires, unattuned at her belt, a keepsake and one day a gift: two of "
             "three, with room to spare."),'''
new_intro = '''    ("gold", "Three masterworks of deep gnome artifice, forged for Lilly Glimmergear in the year "
             "apart. Three masterworks, one choice. Each door of Lilly's year apart leads to one "
             "of these treasures: stay and build the portal (the Sentinel), go home to "
             "Glimmerspire and Poots (the Storm Cell), or give the year to mote research (the "
             "Awakened Sphere). And on every road she carries Boomstick, Poots's parting work: "
             "a Level 7 Artillerist does not walk into the rifts without her sidearm. Boomstick "
             "takes the dagger's watch on every road, so the Frostbite Shard retires to her "
             "belt, unattuned, a keepsake and one day a gift. The attunement ledger runs light: "
             "the Sphere's road holds two of three (Dynamo, Sphere); the Sentinel's road just "
             "one (the guardian itself, the Dynamo rebuilt inside it); the Storm Cell's road "
             "two (Dynamo, the Cell). Room to grow on every path."),

    ("h2", "Boomstick, Poots's Parting Work"),
    ("imgfloat", "assets/items/boomstick.png", 2.2),
    ("gold", "*''' + LQ + '''It doesn't jam. It doesn't misfire. It simply states its opinion, "
             "loudly.''' + RQ + '''*"),
    ("body", "Whichever road Lilly walks, a parcel finds her, wrapped in waxed paper and string, "
             "postmarked Glimmerspire. Boomstick becomes her spellcasting focus and her "
             "designated Arcane Firearm (an artificer designates only one). With her shield in "
             "the other hand, her hands are exactly full: pistol, shield, and nothing wasted. "
             "Its clockwork drum conjures its own rounds, so Lilly will never want for "
             "ammunition again."),
    ("stat", "Boomstick", [
        "*Weapon (Repeating Pistol), Rare*",
        "**Repeating Pistol, +2.** You gain a +2 bonus to attack rolls and damage rolls made "
        "with this magic weapon, which deals 1d10 Thunder damage on a hit. The weapon requires "
        "no ammunition and never needs reloading.",
        "**Spell Focus and Arcane Firearm.** While holding Boomstick, you can use it as a "
        "Spellcasting Focus for your Artificer spells, and it is your designated Arcane Firearm. "
        "When you cast an Artificer spell through Boomstick, you can add 1d8 to one of the "
        "spell's damage rolls; the extra damage is Thunder damage.",
        "*Forged by the masters of Glimmerstone.*",
    ]),'''
assert old_intro in t, "intro not found"
t = t.replace(old_intro, new_intro)

old_door = '''    ("h2", "Boomstick"),
    ("imgfloat", "assets/items/boomstick.png", 2.2),
    ("gold", "*''' + LQ + '''It doesn't jam. It doesn't misfire. It simply states its opinion, "
             "loudly.''' + RQ + '''*"),
    ("body", "On this road, Boomstick takes the dagger's watch. Boomstick becomes Lilly's "
             "spellcasting focus and her designated Arcane Firearm (an artificer designates only "
             "one). With her shield in the other hand, her hands are exactly full: pistol, shield, "
             "and nothing wasted. Its clockwork drum conjures its own rounds, so Lilly will never "
             "want for ammunition again. The Frostbite Shard retires to her belt as a keepsake, or "
             "one day, a gift."),
    ("stat", "Boomstick", [
        "*Weapon (Repeating Pistol), Rare (Requires Attunement by Lilly)*",
        "**Repeating Pistol, +2.** You gain a +2 bonus to attack rolls and damage rolls made "
        "with this magic weapon, which deals 1d10 Thunder damage on a hit. The weapon requires "
        "no ammunition and never needs reloading.",
        "**Wand of the War Mage.** While holding Boomstick, you gain a +2 bonus to spell attack "
        "rolls, and you ignore Half Cover when making a spell attack. Your Eldritch Cannon also "
        "gains a +2 bonus to its attack rolls.",
        "**Spell Focus and Arcane Firearm.** While holding Boomstick, you can use it as a "
        "Spellcasting Focus for your Artificer spells, and it is your designated Arcane Firearm. "
        "When you cast an Artificer spell through Boomstick, you can add 1d8 to one of the "
        "spell's damage rolls; the extra damage is Thunder damage.",
        "**Concussion Infusion.** When a creature takes damage from a spell you cast through "
        "Boomstick, that creature takes an extra 2 Thunder damage and can't take Reactions "
        "until the start of its next turn.",
        "**Made to Channel.** When you cast True Strike using Boomstick, the attack uses your "
        "Intelligence and counts as a spell attack, gaining Boomstick's +2 bonus to spell "
        "attack rolls and ignoring Half Cover. On a hit, the attack deals Boomstick's Thunder "
        "damage plus the spell's Radiant damage.",
        "*Forged by the masters of Glimmerstone.*",
    ]),'''
assert old_door in t, "door not found"
new_door = '''    ("h2", "Boomstick, Stormcharged (the Storm Cell)"),
    ("gold", "*''' + LQ + '''Gearhaven runs on lightning. So does she, now.''' + RQ + '''*"),
    ("body", "On this road Lilly goes home to Glimmerspire, and the masters open the deep "
             "workshops for Poots's brightest student. What she brings back is the Storm Cell: "
             "a humming capacitor drum fitted to Boomstick's frame, charged each night with "
             "bottled lightning, Gearhaven's own element."),
    ("stat", "The Storm Cell", [
        "*Wondrous Item (Boomstick augmentation), Rare (Requires Attunement by Lilly)*",
        "**Wand of the War Mage.** While holding Boomstick, you gain a +2 bonus to spell attack "
        "rolls, and you ignore Half Cover when making a spell attack. Your Eldritch Cannon also "
        "gains a +2 bonus to its attack rolls.",
        "**Charged Rounds.** The Storm Cell holds two charged rounds of each kind below, and "
        "you regain all expended rounds when you finish a Long Rest. If a round requires a "
        "saving throw, the DC equals your spell save DC.",
        "**Arc Round.** When you hit a creature with Boomstick, you can expend one Arc Round "
        "to make the shot leap: lightning arcs from the target to up to two other creatures of "
        "your choice within 15 feet of it. Each must make a Dexterity saving throw, taking 2d6 "
        "Lightning damage on a failed save, or half as much damage on a successful one.",
        "**Thunder Wave Round.** When you hit a creature with Boomstick, you can expend one "
        "Thunder Wave Round to overload the shot: the target takes an extra 1d10 Lightning "
        "damage and must succeed on a Constitution saving throw or have the Stunned condition "
        "until the end of your next turn.",
        "**Counter-Bolt.** When a creature you can see within 60 feet makes an attack roll "
        "against one of your allies, you can take a Reaction and expend one Counter-Bolt to "
        "fire into the attack: the triggering attack roll has Disadvantage, and you make one "
        "Boomstick attack against the creature. On a hit, it takes an extra 1d10 Lightning "
        "damage.",
        "**Made to Channel.** When you cast True Strike using Boomstick, the attack uses your "
        "Intelligence and counts as a spell attack, gaining the Storm Cell's +2 bonus to spell "
        "attack rolls and ignoring Half Cover. On a hit, the attack deals Boomstick's Thunder "
        "damage plus the spell's Radiant damage.",
        "*Fitted by the masters of Glimmerstone, in the workshop where Boomstick was born.*",
    ]),'''
t = t.replace(old_door, new_door)

ast.parse(t)
open(p, "w", encoding="utf-8", newline="\n").write(t)
print("Storm Cell restructure applied; em dashes:", t.count(chr(0x2014)))
