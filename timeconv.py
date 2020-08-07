"""
Implements functions that help with converting serialised time into human-readable time
"""
from typing import Tuple
from num2words import num2words

def minutes_to_hours_minutes(minutes: int) -> Tuple[int, int]:
    return minutes // 60, minutes % 60

def am_or_pm(minutes: int) -> str:
    return ["AM", "PM"][minutes >= 720]

def minutes_to_human_readable(minutes: int) -> str:
    hrs, mins = minutes_to_hours_minutes(minutes)
    mins_text = ""
    if mins > 0:
        if mins < 10:
            mins_text += " oh"
        mins_text += f" {num2words(mins)}"

    return str.title(f"{num2words(hrs % 12)}{mins_text} ") + am_or_pm(minutes)

def test():
    t = 623
    print(minutes_to_human_readable(t))
    print(minutes_to_hours_minutes(t))

if __name__ == "__main__": test()