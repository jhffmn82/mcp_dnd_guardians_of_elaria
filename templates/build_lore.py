# build_lore.py
# The lore primer: the world of Elaria, its cosmology, its goddess and its
# shadow, the relics, and a gazetteer. Drawn from memory/campaign_canon.md.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
BLOCKS = [
    ("titlepage", "A PRIMER FOR PLAYERS AND DUNGEON MASTERS", "The World of Elaria",
     "Cosmology, Powers, and Places",
     "The lore behind the chronicle: how the world is built, who threatens it, and what the Guardians are truly fighting for."),

    ("h1", "The Shape of the World"),
    ("gold", "There is not one world but many, turning side by side like the gears of a single "
             "great clock: the planes of Fire, Water, Air, Earth, and Shadow, and the Material world "
             "at their heart. For a thousand years the clock kept perfect time."),
    ("gold", "The planes do not spin on their own. They are held in place by anchor-stars, fixed "
             "points of light in the dark, each one cradling a plane in its orbit. While the stars "
             "burn, the worlds stay in their courses. When a star goes dark, its plane slips, and a "
             "crack opens between worlds."),
    ("body", "Through those cracks leak Motes: bright drifting fragments of the planes themselves. "
             "Motes drive machines mad and wake strange creatures, the wondrous beasts the Guardians "
             "have met and befriended along their road. Gather the loose Motes, mend the cracks, and "
             "the world steadies again. That, in the simplest telling, is the work."),
    ("img", f"{A}/world/elaria_region_map.png",
     "The lands of Elaria, from Eldridge Vale in the west to the clockwork city of Gearhaven.", 6.2),

    ("h1", "Elaria, the Sleeping Warden"),
    ("gold", "Elaria is not a goddess of war or harvest, but of balance: the Warden who once tended "
             "the lights of heaven and kept the planes in their courses. Long ago, in the War of "
             "Fractures, she led the gods against a devouring darkness and spent nearly all her "
             "power to seal it away. What remained she bound into small safeguards and scattered, "
             "and then, diminished, she fell into a deep sleep."),
    ("body", "She sleeps still, and because she sleeps the stars can be put out one by one. Who or "
             "what closed her eyes is a mystery not yet answered. She is not wholly gone, though: she "
             "guides those attuned to balance through visions and through gifts marked with her "
             "sign, a seven-pointed star wrapped in a leafed vine. When you see that star, she saw "
             "you coming."),

    ("h1", "The Shadow: Nyxthid and Maldrith"),
    ("body", "Two threats stand behind the failing world, one seen and one still hidden."),
    ("gold", "**Nyxthid, the Harbinger of Decay**, is the one the Guardians have glimpsed: a fallen "
             "celestial who once guarded the planes and now, twisted by despair, works to snuff the "
             "anchor-stars out. He deals in shadow, illusion, and fear, and he believes the kindest "
             "thing left is to let the whole clock wind down into dark."),
    ("gold", "**Maldrith, the Weaver of Fractures**, is the darkness Elaria sealed: an ancient, "
             "patient hunger from beyond the planes, pressing on the walls of every world, waiting "
             "for the last star to go dark. Nyxthid is only her herald. The heroes do not yet know "
             "her name, and should not, until the road grows much darker."),

    ("h1", "The Covenant and the Relics"),
    ("body", "When Elaria spent her power, she bound what was left into safeguards and gifts, and "
             "some of these have found their way to the Guardians."),
    ("gold", "**The Enchanted Potatoes**, three of them, carried by Ursa and left by his father "
             "Ash: humble to the eye, but remnants of the shattered covenant, holding fragments of "
             "the goddess's own essence for the day they are needed."),
    ("gold", "**The Essence Sphere**, forged by the deep-gnome masters of Glimmerspire before the "
             "crisis ever began (how they knew is its own mystery): a gatherer of loose Motes, and "
             "the beating heart the world's great Rift Portal has always lacked."),
    ("gold", "**The three relics of Wraithpine**, each bearing the seven-pointed star: the Staff of "
             "Waking Constellations that relights a star with every victory, the Sash of the Swift "
             "Current, and the Pocket Dynamo. One chest, three gifts, one goddess guiding three "
             "chosen hands. Their full powers are set down in the compendium of treasures."),

    ("h1", "A Gazetteer"),
    ("body", "The chronicle's road, west to east:"),
    ("body", "**Eldridge Vale** and the Forest of Whispers, where three strangers met. "
             "**Oakshade** and the cliffside **Ravenstone Laboratory** of Professor Aelwyn. Wintry "
             "**Havenmoor** on the coast, and the cursed sea beyond it. Fog-bound **Wraithpine** and "
             "its old theater. And **Gearhaven**, the great clockwork city of inventors, home to the "
             "Artificer's Guild, the Orrery of Planes, and the Rift Portal that will carry the "
             "Guardians to the failing worlds beyond."),
    ("body", "Farther still, unmapped and waiting: the old shrine to the east that Ash Catchum "
             "followed the dark stars toward, and the five rift-worlds the Guardians will one day "
             "walk to free their guardians and relight the sky."),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    print("built", build_doc(BLOCKS, "frontmatter/lore_primer.docx"))
