import voicehelpers as voice

import os

from datetime import datetime as dt

from timeconv import minutes_to_human_readable, hours_minutes_to_minutes

from timetabling import Timetable

TIMETABLE = Timetable(loc = "data/timetable.json", new=True)

active = True

battery_saver = True

# voice.say("What is your name?")
# name = voice.get("What is your name? Speak!", indefinite=True, vocal=True)
# voice.say(f"Hello, {name}!")

max_asks_before_sleep = 3

times_asked = 0

while active:
    print("Say a command:")
    command = voice.get().lower()
    print(f"Command issued: {command}")

    if command in ["what is the time", "what's the time", "current time", "time"]:
        current_time = dt.now().time()
        minutes = hours_minutes_to_minutes(current_time.hour, current_time.minute)
        voice.say(f"The current time is {minutes_to_human_readable(minutes)}")

    elif command in "exit quit close goodbye bye".split() + ["see you later"]:
        active = False

    elif command.startswith("jarvis"):
        sys_commands = {
            "commence system shutdown": "shutdown.exe /s /t 20",
            "standby": "rundll32.exe powrprof.dll,SetSuspendState 0,1,0"
        }

        

        command_spec = " ".join(command.split()[1:])

        if command_spec == "beatbox":
            voice.say("Boots and cats and Boots and cats and Boots and cats and Boots and cats and Boots and cats and Boots and cats and ")

        if command_spec in sys_commands:
            if command_spec == "commence system shutdown":
                voice.say("Confirming that you want to shut down sir?")
                verdict = voice.get(indefinite=True, vocal=True).lower()
                if not("shutdown" in verdict or "yes" in verdict or "confirm" in verdict):
                    voice.say("No worries sir.")
                    continue
            os.system(sys_commands[command_spec])

        else:
            voice.say("Sorry boss, I didn't quite catch that beat.")


    elif command.startswith("open application"):
        app = "".join(command.split()[2:])
        os.system(f"start {app}.exe")

    else:
        times_asked += 1
    
    if times_asked >= max_asks_before_sleep and battery_saver:
        input("Press enter to wake...")
        times_asked = 0