# build_foreword.py
# Front matter of the book: title, foreword, how-to-read, the Guardians
# (dramatis personae), and the tale-so-far timeline.
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from book_style import build_doc

A = "assets"
BLOCKS = [
    ("titlepage", "A CHRONICLE AND HOMEBREW EXPANSION", "The Guardians of Elaria",
     "The Complete Chronicle",
     "Being the true account of three young heroes, the worlds they mended, and the sleeping goddess who lit their way."),

    ("h1", "Foreword"),
    ("gold", "This book is a keepsake. Every adventure inside it truly happened, told across a "
             "kitchen table over many evenings, rolled up out of dice and imagination and more "
             "snacks than any goblin could carry. The heroes are real, because the people who play "
             "them are real, and this is their story set down so it will not be forgotten."),
    ("gold", "It is also a small homebrew expansion for the world's greatest roleplaying game. "
             "Read the story aloud, borrow the creatures, hand the relics to your own heroes, and "
             "carry the lantern a little further down the road. Everything here is meant to be used, "
             "not just kept on a shelf."),
    ("body", "The chronicle runs in reading order: this front matter, a primer on the world of "
             "Elaria, then the sessions in the order they were played, and at the end a compendium "
             "of every creature, treasure, and hero-path the Guardians gathered along the way."),

    ("h1", "How to Read This Book"),
    ("gold", "Passages in warm gold, like this one, are the story itself. Read them aloud. They are "
             "written to be heard at the table, in the voice of a narrator who has been waiting all "
             "week to find out what happens next."),
    ("dm", "Passages in lavender, marked with an arrow, are notes for the Dungeon Master: a check "
           "and its difficulty, the shape of a fight, a treasure gained. They are asides, not story."),
    ("body", "Creature and item statistics are kept brief in each session's closing appendix; the "
             "full write-ups, with lore and pictures, live in the compendium volumes at the back. "
             "The rules are the 2024 revision of fifth edition, with a handful of house rules noted "
             "in the compendium."),

    ("h1", "The Guardians"),
    ("h2", "Lilly Glimmergear"),
    ("body", "A deep gnome girl from the deep places, all silver hair and red eyes and restless "
             "cleverness. An {color:lilly}Artificer{/} of the Artillerist school, trained at "
             "Glimmerspire, she carries the Essence Sphere her mother Poots pressed into her hands, "
             "and the sleeping spark of a friend named Pikachu. She builds, she tinkers, and she "
             "does not leave anyone behind, caged or otherwise."),
    ("h2", "Stabby Sharpblade"),
    ("body", "A goblin boy of the Bloodfang Clan, green and grinning and far too fast, trained a "
             "little and tamed not at all by the monk Kaelon Windstep. A {color:stabby}Monk{/} who "
             "fights like a rumor and laughs like a landslide, he came for the adventure and stayed "
             "for the friends."),
    ("h2", "Ursa Catchum"),
    ("body", "A human boy who reads the night sky like a map, son of the lost wildfire druid Ash "
             "Catchum. A {color:ursa}Druid{/} of the Circle of the Eternal Stars, he carries three "
             "enchanted potatoes and a great many questions, and a dragonmark that stirs whenever "
             "something frightened and voiceless needs him."),
    ("h2", "Ghostbloom"),
    ("body", "Their companion: once the little plant-sprite Floraburst, now a spirit of pale teal "
             "ghost-light who chimes like frost and glows toward trouble. Some say she is the "
             "sleeping goddess's own small voice, sent to walk beside her chosen."),

    ("h1", "The Tale So Far"),
    ("body", "The Guardians began their road at 3rd level and, by the close of this chronicle, "
             "stand at 5th, on the eve of a year apart that will return them stronger. Each session "
             "is a chapter."),
    ("gold", "**One. The Gathering of Friends.** Three strangers meet in a tavern in Eldridge Vale, "
             "befriend a creature of the Feywild, and learn that the doors between worlds are coming "
             "open."),
    ("gold", "**Two. The Road to Ravenstone.** A rival clan, a stone serpent, and a vision of the "
             "goddess Elaria in a moonlit glade, who names the danger and sets the quest."),
    ("gold", "**Three. The Quest for Knowledge.** Professor Aelwyn examines the Sphere, a companion "
             "is chosen, and on the storm-cliffs a cloaked figure boasts that he is unmaking the world."),
    ("gold", "**Four. Awakening to Shadows and Songs.** In wintry Havenmoor the Krampusshade steals "
             "the children, and eight holiday bells rung in harmony set them free."),
    ("gold", "**Five. The Curse of Davy Jones.** A storm, a shipwreck, and a ghost ship whose "
             "captain harvests magic itself; the Guardians sink him and escape as their companion "
             "begins to change."),
    ("gold", "**Six. Lanterns in the Fog.** The village of Wraithpine forgets its own dead to a "
             "singing monster; the Guardians remember, set it right, and receive the three relics of "
             "Elaria from a single vine-bound chest."),
    ("gold", "**Eight. Gearhaven, the Clockwork City.** In the great city of inventors the Sphere "
             "reveals its purpose, the stars are found to be going dark one by one, and a gentle "
             "giant is freed. Then the heroes part for a year, and this chronicle pauses, to be "
             "continued."),
    ("dm", "There was no seventh session at the table; the Wraithpine arc was the sixth, and "
           "Gearhaven kept its number. The chapters read straight through regardless."),
]

if __name__ == "__main__":
    repo = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo)
    print("built", build_doc(BLOCKS, "frontmatter/foreword.docx"))
