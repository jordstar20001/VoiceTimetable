import voicehelpers as voice

import os

from datetime import datetime as dt

from timeconv import minutes_to_human_readable, hours_minutes_to_minutes, minutes_now, minutes_to_hours_minutes, duration_repr

from timetabling import Timetable, _days_of_week

TIMETABLE = Timetable(loc = "data/timetable.json")

active = True

battery_saver = False

max_asks_before_sleep = 3

times_asked = 0

CLASS_CONTEXT = {}
DAY_CONTEXT = []

next_class_count = 0
def check_next(next_class_count):
    global CLASS_CONTEXT
    next_class = TIMETABLE.get_sequential_class(next_class_count)
    if next_class:
        CLASS_CONTEXT = next_class
        next_class_count += 1
        class_start_mins, class_end_mins = next_class["start_time"], next_class["end_time"]
        time_delta = class_end_mins - class_start_mins

        time_delta_h, time_delta_m = minutes_to_hours_minutes(time_delta)
        time_delta_str = duration_repr(time_delta_h, time_delta_m)

        time_till_class_start_mins = class_start_mins - minutes_now()
        t_hrs, t_mins = minutes_to_hours_minutes(time_till_class_start_mins)

        time_left_str = duration_repr(t_hrs, t_mins)

        voice.say(f"{next_class['title']} at {minutes_to_human_readable(class_start_mins)} that goes for {time_delta_str}. It starts in {time_left_str}")
    else:
        voice.say("You have no more classes today.")
        next_class_count = 0

def say_class(c):
    class_start_mins, class_end_mins = c["start_time"], c["end_time"]
    time_delta = class_end_mins - class_start_mins

    time_delta_h, time_delta_m = minutes_to_hours_minutes(time_delta)
    time_delta_str = duration_repr(time_delta_h, time_delta_m)

    voice.say(f"{c['title']} at {minutes_to_human_readable(class_start_mins)} that goes for {time_delta_str}.")

order_words = "first second third fourth fifth".split()
while active:
    print("Say a command:")
    command = voice.get().lower()
    print(f"Command issued: {command}")
    command_split = command.split()
    
    if command != "next": next_class_count = 0
    else:
        check_next(next_class_count)
        next_class_count += 1
    
    

    if command in order_words:
        if not DAY_CONTEXT:
            voice.say("I don't know what day you're talking about")
            continue
        else:
            i = order_words.index(command)
            if i >= len(DAY_CONTEXT):
                voice.say("You have less classes than that!")
                continue
            c = DAY_CONTEXT[i]
            CLASS_CONTEXT = c
            say_class(c)
            continue

    found_day = False
    for i, day in enumerate(_days_of_week):
        if day in command.title():
            found_day = True
            classes = TIMETABLE.get_day_classes(i)
            DAY_CONTEXT = classes
            if not classes:
                voice.say(f"You have nothing on {day}s")
                break
            voice.say(f"Here's what you have on {day}s")
            for c in classes:
                say_class(c)
    # if not found_day:
    #     DAY_CONTEXT = []

    if command in ["what is the time", "what's the time", "current time", "time"]:
        minutes = minutes_now()
        voice.say(f"The current time is {minutes_to_human_readable(minutes)}")

    

    elif "next" in command_split and "class" in command_split:
        check_next(next_class_count)
    elif command.startswith("open zoom"):
        if CLASS_CONTEXT == {}:
            voice.say("No class selected. Ask me for a class first.")
            continue
        zoom_link = CLASS_CONTEXT['zoom_link']
        os.system(f"start chrome.exe {zoom_link}")
        if "pwd=" in zoom_link:
            passw = ", ".join(list(zoom_link.split("=")[-1]))
            voice.say(f"The password for this zoom is: {passw}")
            voice.say(f"I repeat: {passw}")
    elif command in "exit quit close goodbye bye".split() + ["see you later"]:
        active = False

    

    