import pprint
import mongoconnect_demo
import introductionDEMO
import Escape_Room_demo
import time
import sys
import json


def delay_print(s):
    #Allows to print characters at a given speed
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)

def menu():
    #Initial print of game!
    delay_print("WELCOME TO THE ESCAPE ROOM!")
    print("")
    delay_print("~*~*~*~*~*~*~* A Text Based Escape Room Simulator")
    print("")
    print("To begin, please enter your name --")
    name = input()
    delay_print("Hello, " + name + ". What would you like to do?")
    ans=True
    while ans:
            # This menu is the main menu where you can choose which function for the program to run.
            print("""
            1.Start A New Escape Room (1)
            2.Save Current Escape Room (2)
            3.View Scoreboard (3)
            4.Exit/Quit (4)
            5. UPDATE ALIAS (5)
            6. Edit Scoreboard (6)
            7. JSON Upload Center (7)
            """)
            ans=input() 
            if ans=="1": 
                #Identifies variables for saving to mongoDB while also initiating the actual game play of the game.
                introductionDEMO.intro()
                Win_or_Lose = Escape_Room_demo.inspection()
            elif ans=="2":
                #Identifies varaibles for saving to mongoDB and allows for physical saving to the database.
                print(name, Win_or_Lose) 
                myobject = {"Name": name, "Alias": name, "Win_or_Lose": Win_or_Lose}
                mongoconnect_demo.collection.insert_one(myobject)     
            elif ans=="3":
                #Allows program to find data in the database on mongoDB
                SB = mongoconnect_demo.collection.find()
                #PRINTING ALL SAVED SCOREBOARDS for user viewing stored in mongoDB
                for game in SB:
                    pprint.pprint(game)
            elif ans=="4":
                #Ends the game and closes the program
                print("\n Goodbye")
                break 
            elif ans=="5":
                #This elif allows for the user to update an existing record in our database
                if name == "":
                    print("Sorry! Please enter an existing name.")
                else: 
                    print("Please enter your new ALIAS for the Scoreboard:")
                    ans1 = input()
                    mongoconnect_demo.collection.update_one({'Alias':name},{"$set":{'Alias':ans1}})
            elif ans =="6":
                #This elif allows for deleting whole records according to the name input by user
                print("Please enter the name of the record you would like to delete.")
                ans2=input()
                game = mongoconnect_demo.collection.delete_one({'Name': ans2})
                for game in SB:
                    print("Sorry! Please choose a record to delete.")
            elif ans =="7":
                #Allows for the program to read and upload a json file to its database... Perfect for storyboard building and fleshing this application out later.
                print("Please enter the file you would like to upload. Please include (.json):")
                ans3 = input()
                f = open(ans3)
                data = json.load(f)
                for i in data['scoreboard']:
                    mongoconnect_demo.collection.insert_one(i)
                f.close()
            elif ans !="":
                print("\n Not Valid Choice Try again") 

####The starting function!!!
menu()




