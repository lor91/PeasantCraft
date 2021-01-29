#This is the basic damage mechanic in place. At the moment it's a simple RNG formula but will hopefully be expanded in future to include items picked up by the player
#import game2
from stats import *

class Damage():
    def smack():
        roll = randint(1,2)
        if roll == 2:
            print(f"You take damage")
        #    global health #this allows the function to modify the global health variable.
            health = health - 2
            print(f"Your health is now {health}") #
        else:
            print(f"You dodge, taking no damage.")
