
import Escape_Room_demo
import time
import sys
from introductionDEMO import intro
import json
import actualmenu_demo
import pickle


def print_char(s):
    for c in s:
        sys.stdout.write( '%s' % c )
        sys.stdout.flush()
        time.sleep(.1)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)

# #def onstart():
#     delay_print("WELCOME TO THE ESCAPE ROOM!")
#     print("")
#     delay_print("~*~*~*~*~*~*~* A Text Based Escape Room Simulator")

#     print("")
#     print("To begin, please enter your name --")

#     name = input()
#     delay_print("Hello, " + name + ". What would you like to do?")
    
#     actualmenu_demo.menu()



def write_json(new_data, filename='savefiles.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        file_data["file_save"].append(new_data)
        file.seek(0)
        json.dump(file_data, file, indent = 2)

#onstart()


