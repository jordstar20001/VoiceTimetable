import voicehelpers as voice

import os

from datetime import datetime as dt

from timeconv import minutes_to_human_readable, hours_minutes_to_minutes, minutes_now, minutes_to_hours_minutes, duration_repr

from timetabling import Timetable

TIMETABLE = Timetable(loc = "data/timetable.json")

active = True

battery_saver = False

max_asks_before_sleep = 3

times_asked = 0

while active:
    print("Say a command:")
    command = voice.get().lower()
    print(f"Command issued: {command}")
    command_split = command.split()
    if command in ["what is the time", "what's the time", "current time", "time"]:
        minutes = minutes_now()
        voice.say(f"The current time is {minutes_to_human_readable(minutes)}")

    elif "next" in command_split and "class" in command_split:
        next_class = TIMETABLE.get_sequential_class(0)
        if next_class:
            class_start_mins, class_end_mins = next_class["start_time"], next_class["end_time"]
            time_delta = class_end_mins - class_start_mins

            time_delta_h, time_delta_m = minutes_to_hours_minutes(time_delta)
            time_delta_str = duration_repr(time_delta_h, time_delta_m)

            time_till_class_start_mins = class_start_mins - minutes_now()
            t_hrs, t_mins = minutes_to_hours_minutes(time_till_class_start_mins)

            time_left_str = duration_repr(t_hrs, t_mins)

            voice.say(f"You have a class at {minutes_to_human_readable(class_start_mins)} that goes for {time_delta_str}. It starts in {time_left_str}")
        else:
            voice.say("You have no more classes today. Congratulations! Get some fresh air, and dive into the hell that is your homework.")

    elif command in "exit quit close goodbye bye".split() + ["see you later"]:
        active = False

    

    