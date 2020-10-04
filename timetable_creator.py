"""
Create a timetable for the voicetimetable software

Note! This must sort the data otherwise the software will NOT work!
"""

from timetabling import Timetable, _days_of_week

from timeconv import minutes_to_hours_minutes as m2hm, hours_minutes_to_minutes as hm2m

TIMETABLE = Timetable(loc=input("Enter the (relative) location of the timetable JSON file : "))

def b_input(t):
    return input(f"\n{t}")
def b_print(t):
    print(f"\n{t}")

def view_day_by_id(id: int) -> list:
    classes = TIMETABLE.get_day_classes(id)
    if not classes:
        print("NO CLASSES FOUND!")
    for i, i_class in enumerate(classes):
        hs, ms = m2hm(i_class["start_time"])
        if ms < 10: ms = "0"+str(ms)
        he, me = m2hm(i_class["end_time"])
        if me < 10: me = "0"+str(me)
        print(f"{i} --> Name: {i_class['title']} | Start: {hs}:{ms} | End: {he}:{me}")
    return classes

def add_class(day):
    b_print("Note: times should be in format hours:minutes (meaning 4:05 would be 4:5)")
    data_input = lambda param: b_input(f"Enter value for 'class {param}' : ")
    title, start, end, desc, zoom_link = [data_input(prompt) for prompt in "name start-time end-time description zoom-link".split()]
    start = [int(i) for i in start.split(":")]
    end = [int(i) for i in end.split(":")]
    start_minutes = hm2m(*start)
    end_minutes = hm2m(*end)
    
    TIMETABLE.create_new_class(day=day, start_minutes_after_12am=start_minutes, end_minutes_after_12am=end_minutes, title=title, description=desc, zoom_link=zoom_link)
    
def remove_class(day, class_index):
    return TIMETABLE.remove_class(day, class_index)

while True:
    verdict = b_input("Would you like to edit the current timetable, or create a new one (Y/N) : ").lower()
    if verdict == "y":
        TIMETABLE.establish(int(b_input("How many days would you like the timetable to be for? : ")))

    elif verdict == "n":
        break

    else:
        b_print("Invalid input. Try again.")

while True:
    for i in range(len(TIMETABLE.days.keys())):
        print(f"{i} --> {list(TIMETABLE.days.keys())[i]}")
    day_selection = int(b_input("Enter day ID : "))
    if 0 <= day_selection < len(TIMETABLE.days):
        classes = view_day_by_id(day_selection)
        while True:
            verd = b_input("Would you like to [a]dd a class or [r]emove one? : ")
            if verd.lower() == "a":
                # Add
                add_class(day_selection)
                print("Day created!")
                break

            elif verd.lower() == "r":
                c = remove_class(day_selection, int(b_input("Enter the class ID to remove : ")))
                b_print(f"Class '{c['title']}' was removed from {_days_of_week[day_selection]}.")
                break
            else:
                b_print("Sorry but that's invalid. Try again.")
    else:
        b_print("Invalid selection!")
        continue
    