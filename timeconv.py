"""
Implements functions that help with converting serialised time into human-readable time
"""
from typing import Tuple
from num2words import num2words
from datetime import datetime as dt

def minutes_to_hours_minutes(minutes: int) -> Tuple[int, int]:
    return minutes // 60, minutes % 60

def minutes_now():
    current_time = dt.now().time()
    minutes = hours_minutes_to_minutes(current_time.hour, current_time.minute)
    return minutes

def hours_minutes_to_minutes(hours: int, minutes: int) -> int:
    return 60*hours + minutes

def am_or_pm(minutes: int) -> str:
    return ["AM", "PM"][minutes >= 720]

def minutes_to_human_readable(minutes: int) -> str:
    hrs, mins = minutes_to_hours_minutes(minutes)
    mins_text = ""
    if mins > 0:
        if mins < 10:
            mins_text += " oh"
        mins_text += f" {num2words(mins)}"

    return str.title(f"{num2words(hrs % 12 if hrs != 12 else 12)}{mins_text} ") + am_or_pm(minutes)

def duration_repr(t_hrs, t_mins):
    time_str = ""
    if t_hrs and t_mins:
        time_str = f"{t_hrs} hours and {t_mins} minutes"
    elif t_hrs:
        time_str = f"{t_hrs} hours"
    elif t_mins:
        time_str = f"{t_mins} minutes"
    
    return time_str

def test():
    t = 623
    print(minutes_to_human_readable(t))
    print(minutes_to_hours_minutes(t))

if __name__ == "__main__": test()