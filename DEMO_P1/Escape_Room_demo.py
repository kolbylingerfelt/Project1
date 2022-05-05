import random
import time
import sys
from selection_demo import selection
from searchItem_demo import Floor_Puzzle, Vase, Skylight, Cabinet, Stairs, Journal, Wall_Corner, Frames, Strings, Handprint




def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(.1)

codeSegment1 = random.randint(0,9)
codeSegment2 = random.randint(0,9)
codeSegment3 = random.randint(0,9)
code = int(str(codeSegment1) + str(codeSegment2) + str(codeSegment3))
items = ["Floor_Puzzle", "Vase", "Skylight", "Cabinet", "Stairs", "Journal", "Wall_Corner", "Frames", "Strings"]
code1Location = random.randint(1,3)
code2Location = random.randint(4,6)
code3Location = random.randint (7,9)




def inspection():
	while True:
		choice = selection(items, "What do you want to inspect? ")
		if choice == 1:
			Vase(choice, code1Location, codeSegment1)
		elif choice == 2:
			Skylight(choice, code1Location, codeSegment1)
		elif choice == 3:
			Cabinet(choice, code1Location, codeSegment1)
		elif choice == 4:
			Stairs(choice, code2Location, codeSegment2)
		elif choice == 5:
			Journal(choice, code2Location, codeSegment2)
		elif choice == 6:
			Wall_Corner(choice, code2Location, codeSegment2)
		elif choice == 7:
			Frames(choice, code3Location, codeSegment3)
		elif choice == 8:
			Strings(choice, code3Location, codeSegment3)
		elif choice == 9:
			Handprint(choice, code3Location, codeSegment3)
		else:
			result = Floor_Puzzle(code)
			if result == 1:
				delay_print("Congratulations! You have escaped. If you would like to save this win, now is your chance!"
				+ "If not, feel free to play again.")
			return result
			
				


			
