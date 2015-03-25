#!/usr/bin/env python
# encoding: utf-8

import web
import random

render = web.template.render('templates/')

urls = (
  '/', 'index'
)

names = ["The Answer Key", "Exceeds Expectations", "Troll", "In Poor Taste", "I Wasn't Prepared For This", "Definitely Not A Deus Ex Machina",  "Amor Vincit Omnia", "And Now For Something Completely Different"]
items = [u"the Super Hufflepuff", u"his pouc", u"Quirrell's back tooth", u"a troll leg", u"Mad-Eye Moody, disguised as a Death Eater", u"a wedge of cheese", u"shotguns for legs", u"Voldemort's inability to feel love", u"his father's rock", u"Comed-Tea", u"partial transfiguration", u"Voldemort himself", u"PURE RATIONALITY", u"his irregular sleep cycle", u"the implicit destruction of the world", u"the explicit destruction of the world", u"his scientific knowledge", u"an obscure fact he read in an astrophysics textbook several years ago", u"his birth mother's love", u"antimatter", u"an unnamed science fiction novel", u"the Large Hadron Collider", u"groundbreaking research", u"carbon nanotubes", u"a totally unexpected diversion", u"a totally expected diversion", u"MAGIC", u"the Death Eaters' robes", u"the Death Eaters", u"the Unbreakable Vow", u"his mysterious dark side", u"his Time Turner", u"SPAAAAAAAACE", u"the stars", u"the gun on the wall", u"a deus ex machina", u"a formerly unnoticed plot hole"]
live_action = ["blew apart the graveyard", "created antimatter", "found the unimaged trick Dumbledore had set in play", "taught Voldemort to love", "created his own Horcrux network", "Apparated onto the Pioneer", "brought Hermione back from the dead again", "destroyed all the Horcruxes", "cast the most powerful Patronus charm ever seen", "banished Lord Voldemort for all eternity", "managed to disappear from sight", "outsmarted the Death Eaters", "revived his parents", "became one with the universe", "killed literally everyone", "attained his full potential as a rationalist", u"proved that Schrödinger's cat is neither alive nor dead", u"proved that Schrödinger's cat demonstrates a fundamental misconception of the operations of quantum mechanics", "optimized literally everything", "uncovered the secrets of the universe", "split the atom", "transfigured everything into a carbon nanotube", "rescued Dumbledore"]
dead_action = ["went out in a blaze of glory", "accidentally tore apart the stars", "fulfilled the prophecy, killing himself in the process", "destroyed death itself", "died but was reunited with his parents so it's all okay and nobody has to cry", "was stunned, then his limbs severed and the wounds cauterized, examined for any trace of unusual magics, shot many times with Voldemort's Muggle weapon, struck by as many Death Eaters as possible with the Killing Curse, had his skull and brains crushed with the mundane substance of a tombstone by Mr Grim, was verified dead by Lord Voldemort who then burned his corpse with Fiendfyre, exorcised the surrounding area in case of a ghost, and guarded this place until six hours have passed while four Death Eaters searched the surroundings for signs of anything noteworthy"]
event = ["after sneezing twice", "by snapping his fingers", "through pure rationality", "by blinking furiously", "after twitching his right eyelid", "by remembering the power of true love", "while dancing the macarena", "while singing at the top of his lungs", "after eliminating all other possibilities", "after realizing he was in a story"]
aesop = ["How? Magic.", "He will be missed.", "Rest in pieces.", "Was that really so hard?", "This is clearly the most rational solution.", "The End.", "And now for Chapter 115...", "That was the happy ending.", "That was the sad ending.", "He really should have just learned to lose.", "But they're still^in^^the^^^mirror"]

def random_phrase(phrase_list):
    rphrase = random.choice(phrase_list)
    return rphrase

def num_items():
    chance = random.randint(1,100)
    if (chance % 2) == 0:
        return " and " + random_phrase(items)
    elif (chance % 3) == 0:
        return ", " + random_phrase(items) + ", and " + random_phrase(items)
    return None

def is_dead():
    chance = random.randint(1,50)
    if chance == 1 or chance == 50:
        return (True, random_phrase(dead_action)) # HE DED
    return (False, random_phrase(live_action) + " and escaped certain death with " + random_phrase(items) + " " + random_phrase(event))

def is_aesop():
    chance = random.randint(1,10)
    if chance == 1 or chance == 10:
        return random_phrase(aesop)

def get_chapter_name(ded):
    stuff = list(names)
    if ded:
        stuff.append("Morior Invictus")
    else:
        stuff.append("Invictus Maneo")
    return random_phrase(stuff)

class index:
    def GET(self):
        deadness = is_dead()
        alive_or_dead = deadness[1]
        chapter_name = get_chapter_name(deadness[0])
        if random.randint(0, 100) == 0:
            starting_item = "the Magic of Friendship"
            other_items = None
        else:
            starting_item = random_phrase(items)
            other_items = num_items()
        aesop = is_aesop()
        return render.index(chapter_name, starting_item, other_items, alive_or_dead, aesop)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()

