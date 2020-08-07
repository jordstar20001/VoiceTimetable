"""
Implements functions relating to reading and saving timetable data into JSON file
"""

from typing import List

from json import dumps, loads

__days_of_week___ = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()

class Timetable():
    __data_location__ = ""
    days = {}
    def __init__(self, loc, new = False):
        self.__data_location__ = loc
        if new:
            self.establish(7)
        else:
            try:
                self.__read__()
            except:
                pass

    def __read__(self):
        with open(self.__data_location__, "r") as f:
            self.days = loads(f.read())

    def establish(self, days: int):
        assert 1 <= days <= len(__days_of_week___), f"Can't create timetable with {days} days."
        for i in range(days):
            # day is int representing day position
            day = __days_of_week___[i]
            self.days[day] = []
        self.__overwrite__()
    
    def create_new_class(self, day: int, start_minutes_after_12am, end_minutes_after_12am, title, description):
        assert day < len(self.days), f"Can't create a class for day {day} as it doesn't exist."
        self.days[__days_of_week___[day]].append({
            "start_time": start_minutes_after_12am,
            "end_time": end_minutes_after_12am,
            "title": title,
            "desc": description
        })
        self.__overwrite__()

    def get_day_classes(self, day: int):
        assert day < len(self.days) - 1, f"Can't read classes for day {day} as it doesn't exist."
        return self.days[__days_of_week___[day]]

    def __overwrite__(self):
        with open(self.__data_location__, "w") as f:
            f.write(dumps(self.days, indent=4))