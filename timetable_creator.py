"""
Create a timetable for the voicetimetable software

Note! This must sort the data otherwise the software will NOT work!
"""

from timetabling import Timetable, _days_of_week

TIMETABLE = Timetable(loc=input("Enter the (relative) location of the timetable JSON file : "))

def b_input(t):
    input(f"\n{t}")
def b_print(t):
    print(f"\n{t}")

while True:
    verdict = b_input("Would you like to edit the current timetable, or create a new one (Y/N) : ").lower()
    if verdict == "y":
        TIMETABLE.establish(int(b_input("How many days would you like the timetable to be for? : ")))

    elif verdict == "n":
        break

    else:
        b_print("Invalid input. Try again.")

while True:
    b_input("Which day would you like to view / edit?")
    for i in range(len(TIMETABLE.days.keys())):
        print(f"{i} --> {TIMETABLE.days.keys()[i]}")
    