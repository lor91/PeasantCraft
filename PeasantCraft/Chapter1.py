from sys import exit
from random import randint
from textwrap import dedent
from random import randrange
from damage import Damage
import stats
import random

#Global values used throughout the script, need to be edited as globals as they are referenced at various points.
health = int(10)
robbed = False
gold = int(50)
OgreHealth = int(10)




class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        #Printing out the last scenes
        current_scene.enter()




class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)




class House(Scene):
    def __init__(self):
        pass
    def room():
        global robbed
        if robbed == True:
                print("There's nothing left for you here. Go back.")
                Square.enter()
        else:
            print(dedent(f"""You enter the house. You see a useful looking breastplate mounted on the wall, but little else of value. You could steal the breastplate, any hero worth their salt always needs a little protection. An irate woman stands nearby, her eyes are fixed upon you with a baleful glare, a rolling pin held at the ready."""))
            print(dedent("""Do you "A" steal the breastplate, risking the woman's wrath, or "B" head back outside."""))
            answer = input("> ")
            while answer == "A":
                roll = randint(1,2)
                if roll == 2:
                    print("You grab the breastplate and make a run for it. Success! This should let you take a few more hits.")
                    Action.breastplate()
                    print(f"You have {health} health.")
                    Action.rob()
                    Square.enter()
                else:
                    print("You attempt to grab the breastplate, but the irate woman takes a swing at you!")
                    Action.smack()
                if answer == "B":
                    Square.enter()
                else:
                    print("Try again.")
                    House.room()




class Finished():
    def outro():
        print("Congratulations! You have completed chapter 1!")
        print("Finished")
        exit()




class Intro(object):
    print(dedent("""
    CHAPTER ONE - THE OGRE

    All your life you have been a simple peasant leading a simple life. Growing increasingly bored with your lot you decide to throw down your spade and take up the adventurer's trade.

With little but a rusty knife and a possibly over-inflated sense of self-confidence you set off in pursuit of fame and riches."""))
    print(f"You have {health} health and {gold} gold.") # This tells the player their starting hitpoints and gold




class Village(Scene):
    pass




class Death(): # prints a random quip at the player and exits the program upon death
    def enter():
        deathfile = open('deathlines.txt').read().splitlines()
#        deathread = deathfile.readline([randint(0, len(deathfile)-1)])
        deathread = random.choice(deathfile)
        print(deathread)
        exit()




class Shop(Scene):
    def witch():
        print("A wizened crone stands before you. She says nothing, on the counter you see a bright red vial, a sign next to it shows you it is a healing potion, and costs 50 gold pieces.")
        print("""Do you:
        A: Buy the potion.
        B: Leave.
        C: Attempt to steal the potion.
        A B or C?""")
        answer = input("> ")
        if answer == "A":
            Action.BuyPotion()
            Square.enter()
        elif answer == "B":
            print("You leave.")
            Square.enter()
        elif answer == "C":
            print(f"You grab the vial, holding it close as though inspecting it before darting out the door. Before the door can shut behind you a crack sounds as the witch fries your bumhairs off with lightening")
            Death.enter()




class Cave():
    def Ogre():
        print(dedent("""You see an Ogre in the cave before you. Do you:

        A. Attack the Ogre head-on
        B. Leave.
        C. Attempt to sneak around and stab the Ogre in the back.
        A, B or C?"""))
        answer = input("> ")
        if answer == "A":
            print("You charge in, swinging your blade at the Ogre")
            while OgreHealth > 0:
                if health <= 0:
                    Death.enter()
                else:
                    Action.Ogre()
            print("You win! Feeling proud of yourself you head home.")
            Finished.outro()

        if answer == "B":
            print("You head back quietly, the Ogre doesn't notice you.")
            Square.enter()
        if answer == "C":
            print("You try sneaking around the Ogre but trip, falling over just before reaching your goal. The Ogre turns around at the noise, inadvertently stomping on your head.")
            Death.enter()




class Action():
    import stat
    def rob():
        global robbed
        robbed = True
    def breastplate():
        global health
        health = health + 6
    def BuyPotion():
        if gold >= 50 and robbed == True and health < 16: #As the breastplate adds 6 health the max possible health for the player is 16
            Action.HealBreastplate()
            print(f"Handing over the coins, you drink the witch's healing potion. You have {health} health and {gold} gold")
            Square.enter()
        elif gold >= 50 and robbed == False and health < 10: # This needs to be here as otherwise the player could get 16 health without the breastplate
            Action.Heal()
            print(f"Handing over the coins, you drink the witch's healing potion. You have {health} health and {gold} gold")
            Square.enter()
        elif gold <50:
            print("You cannot afford this, come back later.")
            Square.enter()
        else:
            print("You do not need healing, come back later if you need to.")
    def HealBreastplate():
        global health
        health = 16
        global gold
        gold = gold - 50
    def Heal():
        global health
        health = 10
        global gold
        gold = gold - 50
    def smack():
        roll = randint(1,2)
        if roll == 2:
            print(f"You take damage")
            global health #this allows the function to modify the global health variable.
            health = health - 2
            print(f"Your health is now {health}") #
        else:
            print(f"You dodge, taking no damage.")
    def Ogre():
        roll = randint(1,2)
        if roll == (2):
            global OgreHealth
            print("You strike the ogre successfully, doing damage")
            OgreHealth = OgreHealth - 2
            print(f"The Ogre now has {OgreHealth} health")
        else:
            print("The Ogre dodges, taking a swing at you ")
            Action.smack()




class Office(Scene):
    def mayor():
        print(dedent("""You enter the Mayor's Office. There are few decorations of note.
    A portly man with thinning hair sits behind an oak desk. He looks you up and down.


    'Hm, Adventurer are you? Well there's an Ogre outside of town that needs dealing with.
    100 gold pieces if you slay it. Do you want the job? You will depart immediately.'

        Do you:
        A. Go to confront the Ogre
        B. Go back to town
        """))
        answer = input('> ')
        if answer == 'A' or 'a':
            Cave.Ogre()

        if answer == 'B' or 'b':
            Square.enter()




class Square(Scene):
    def enter():
        print(dedent("""You reach the village square and look around. Surely someone has a quest worthy of your "talents").

Looking around you can see a shop, a house, and the mayor's office. Where will you look? (A, B or C)"""))

        answer = input("A,B or C >> ")
        if answer == "A":
            Shop.witch()
        elif answer == "B":
            House.room()
        elif answer == "C":
            Office.mayor()
        else:
            print("DOES NOT COMPUTE! Select A, B, or C.")
            return 'village'



Square.enter()



class Pub(Scene):
    print("This scene is incomplete. Want to go back? YES/NO")
    answer = input('> ')
    if answer == 'YES':
        Square.enter()
    else:
        exit(1)




class DarkForest(Scene):
    print("This scene is incomplete. Want to go back? YES/NO")
    answer = input('> ')
    if answer == 'YES':
        Square.enter()
    else:
        exit(1)




class Map(object): #this is using a dict to map each scene/function to a returnable value

    scene = {
        'intro': House(),
        'pub': Pub(),
        'house': House(),
        'death': Death(),
        'dark_forest': DarkForest(),
        'cave': Cave(),
        'stream': Stream(),
        'village': Village(),
        'square': Square(),

            }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('house')
a_game = Engine(a_map)
a_game.play()
