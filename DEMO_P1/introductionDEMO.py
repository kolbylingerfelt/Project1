#### Because the nature of a text based game, there will be many print statements. Take note of defined scenes.



import time
import sys


def delay_print(s):
    ##Allows for printing individual characters at a given speed
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)

def intro():
    ##Using the whole of the intro to nest the while loop required to progress.
    delay_print("*~*~*~*~*~*~*~*~*~*~*~*~*~*~ You awaken feeling as though you are falling through the air. *~*~*~*~*~*~*~" + 
    "* * *T H U D * * *")
    print("")
    delay_print(". . . You hit the ground . . .")
    print("")
    print("'Oh, man...' you groan out, 'Where am I?' ")
    print("")
    print("Silence is returned. You look around in attempt to understand your new surroundings." +
    " As your eyes adjust to the darkness, definition in the surface of the floor catches your"+
    " eye. It appears to be a stone locking mechanism.")
    
    print("")
    print("1 - to check the walls for a light switch")
    print("")   
    print("2 - yell out for help")
    print("")

    while True:

        lightOrYell = input()
        ##This while loops allows for the player to choose an integer and progress the game.

        try:
                if int(lightOrYell) == 1:
                    print("You feel along the walls with the tips of your fingers. The walls are" +
                    " concrete and there is no light switch. You yell out for help only to be silenced" +
                    " by the sound of your own echo. You appear entirely alone. You begin to cry.")
                    break
                elif int(lightOrYell) == 2:
                    print("You yell out for help only to be silenced by the sound of your own echo." +
                    " You appear entirely alone. As your heart begins to race and your eyes fill up with tears, you" +
                    " frantically pick yourself off the ground. You scoure the surface of the concrete walls" + 
                    " in the dark as yours cries begin to deafen and surround you.")
                    break
                else:
                    print("Please enter either 1 or 2:")

        except:
            delay_print("Value must be whole number 1 or 2:")
    print("")
    print("In a flash, the room illuminates a bright white and the voice of a cheery man that sets you" +
    " slightly uneasy bellows:'YOU! YES IT IS YOU! YOU WHO MUST PLAY WITH ME.'" +
    " You spin around trying to find the source of the voice. You dont understand how you've" +
    " gotten here. Well, what if I don't want to play?!' you shout. The voice laughed before all sound" +
    " ceased and it was so quiet you could hear only the sound of your own breathing. 'If you ever want to leave," +
    " you will have to find your way out. The square in the floor opens when you have successfully entered the 3 digit code." +
    " Begin as soon as you're ready to escape!' the voice cackled, before fading away.")
    
    print("")
    print("Your cheeks flush and the tears start again. You don't see how there could possibly be anywhere to look..." +
    " Yet, you take a deep breath and look around for clues. . . :")
    return lightOrYell
    





    