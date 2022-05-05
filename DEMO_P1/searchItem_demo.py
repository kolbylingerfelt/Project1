import time
import sys

def print_char(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(.2)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)




def Floor_Puzzle(code):
    print(" You walk to the center of the room to the square etched in the floor. Three smaller squares linked in a line are able to rotate, like a padlock. You attempt a code...")
    while True:
        try:
            option1 = int(input(" Digit one: "))
            break
        except:
            print(" Digit one must be a whole number between 0-9:")
    while True:
        try:
            option2 = int(input("Digit two: "))
            break
        except:
            print(" Digit two must be a whole number between 0-9:")
    while True:
        try:
            option3 = int(input(" Digit three: "))
            break
        except:
            print(" Digit three must be a whole number between 0-9:")
    chosenCode = int(str(option1) + str(option2) + str(option3))
    print("")
    if chosenCode == code:
        print(" You hear a click and the three squares begin to sink out of sight into the floor. You scoot back and watch as the floor sinks downwards almost like an upside down pyramid. You follow down the stair like structure and come to a door that reads, 'OPEN ME.'")
        return (1)
    else:
        print(" You stare at the blocks a moment before realizing it was wrong. Better luck next time!")
        return(0)

##### NEED TO DECIDE IF I FINISH GAME HERE OR HAVE A SECOND LEVEL? CANT FORGET DB ASPECTS LIKE SAVING STORY CHOICES AND PRINTING ALL THE PRINTED LINES TO A SAVE FILE

def Wall_Corner(choice, codeLocation, codeValue):
    print("")
    print(" You walk over to the back wall. 'If I get a closer look, I may find one of the digits!'")
    if choice == codeLocation:
        print(" Carved just inside the bottom right corner, you see the number " + str(codeValue) + " etched into the surface.")
        print("")
    else:
        print(" You search the entire surface of the back wall to find no code.")
        print("")

def Strings(choice, codeLocation, codeValue):
    print("")
    print(" You walk over to the left wall. There are strings hanging from the ceiling and seem to almost be in patterns.")
    if choice == codeLocation:
        print(" The strings are tied and knotted just perfectly to display the number" + str(codeValue) + " .")
        print("")
    else:
        print(" These strings dont appear to be giving up any information at this time...*grumble.*")
        print("")

def Frames(choice, codeLocation, codeValue):
    print("")
    print(" You walk over to the right wall. Picture frames with no images litter the space.")
    if choice == codeLocation:
        print(" You remove every frame from the wall until you find the one with the number " + str(codeValue) + " painted ont he back.")
        print("")
    else:
        print(" You tear down every empty frame with no prevail... there is no code here.")
        print("")

def Handprint(choice, codeLocation, codeValue):
    print("")
    print(" You walk over to the front wall. You inspect the wall for anything fishy. You see a handprint and decide to place yours on top.")
    if choice == codeLocation:
        print(" As your hand makes contact with the handprint, the pressure triggers a plate to depress and reveal the number " + str(codeValue) + " .")
        print("")
    else:
        print(" Your hand makes contact with the handprint and nothing happens. Shoot.")
        print("")

def Vase(choice, codeLocation, codeValue):
    print("")
    print(" In the corner of the room you see a vase filled with flowers. ")
    if choice == codeLocation:
        print(" You dump the flowers on the floor and carved on the bottom of the vase is the number " + str(codeValue) + " .")
        print("")
    else:
        print(" You dump out the flowers and flip over the vase only to be codeless.")
        print("")

def Stairs(choice, codeLocation, codeValue):
    print("")
    print(" You walk over to an unsearched corner of the room and find a secret stairwell. You descend the stairs...")
    if choice == codeLocation:
        print(" At the bottom of the stairwell, you find a box with exactly " + str(codeValue) + " feathers inside.")
        print("")
    else:
        print(" You search the secret basement before huffing yourself back up. No code there.")
        print("")

def Skylight(choice, codeLocation, codeValue):
    print("")
    print(" You stand in the center of the room and stare up at the ceiling. You notice a tiny, circular skylight.")
    if choice == codeLocation:
        print(" After focusing closely on the skylight, you can see the number " + str(codeValue) + " marked in black on the pane.")
        print("")
    else:
        print(" You squint and strain those little eyes but they come up with nothing.")
        print("")

def Cabinet(choice, codeLocation, codeValue):
    print("")
    print(" You walk over to the largest item in the room, the china cabinet. You begin opening and searching every nook and cranny.")
    if choice == codeLocation:
        print(" After removing all the china, you start dismantling the cabinet. You remove the top shelf and see the number " + str(codeValue) + " etched into the wood.")
        print("")
    else:
        print(" You basically destroy the cabinet and find no digit for the code.")
        print("")

def Journal(choice, codeLocation, codeValue):
    print("")
    print(" You see a small journal on the floor by the china cabinet.")
    if choice == codeLocation:
        print(" You flip through the pages until you find one numbered " + str(codeValue) + " with the word CODE sprawled in red across the page.")
        print("")
    else:
        print(" You flip through every page of that journal and find not a single clue to the code.")
        print("")