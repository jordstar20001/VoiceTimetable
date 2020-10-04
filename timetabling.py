"""
Implements functions relating to reading and saving timetable data into JSON file
"""

from typing import List

from json import dumps, loads

from datetime import datetime as dt

from timeconv import minutes_to_hours_minutes as m2hm, hours_minutes_to_minutes as hm2m

_days_of_week = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday".split()

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
        assert 1 <= days <= len(_days_of_week), f"Can't create timetable with {days} days."
        for i in range(days):
            # day is int representing day position
            day = _days_of_week[i]
            self.days[day] = []
        self.__overwrite__()
    
    def create_new_class(self, day: int, start_minutes_after_12am, end_minutes_after_12am, title, description, zoom_link):
        assert day < len(self.days), f"Can't create a class for day {day} as it doesn't exist."
        self.days[_days_of_week[day]].append({
            "start_time": start_minutes_after_12am,
            "end_time": end_minutes_after_12am,
            "title": title,
            "desc": description,
            "zoom_link": zoom_link
        })
        self.__overwrite__()

    def get_day_classes(self, day: int):
        assert day < len(self.days) - 1, f"Can't read classes for day {day} as it doesn't exist."
        return self.days[_days_of_week[day]]

    def get_sequential_class(self, class_number: int):
        time_now = dt.now().time()
        current_mins_after_12 = hm2m(time_now.hour, time_now.minute)
        day_today = _days_of_week[dt.now().weekday()]
        # Search through ALL for today until you find the class starting directly after now
        this_days_classes = self.days[day_today]
        for i in range(len(this_days_classes)):
            slot = this_days_classes[i]
            if slot["start_time"] > current_mins_after_12:
                # Found the slot
                try:
                    return this_days_classes[i+class_number]
                except:
                    return None
        
        return None

    def remove_class(self, day, index):
        re = self.days[_days_of_week[day]].pop(index)
        self.__overwrite__()
        return re

    def __overwrite__(self):
        # Sort by minutes
        for day_key in self.days:
            self.days[day_key].sort(key=lambda c: c["start_time"])
        with open(self.__data_location__, "w") as f:
            f.write(dumps(self.days, indent=4))

# return list 
def unit_test():
    tt = Timetable("data/timetable_test.json")
    tt.establish(7)
    yield tt.days
    tt.create_new_class(4, hm2m(16, 30), hm2m(17, 0), "Test Class", "In your house!")
    tt.create_new_class(4, hm2m(17, 30), hm2m(18, 0), "Second Class", "In your garage!")
    yield tt.get_sequential_class(1)

if __name__ == "__main__":
    for i, result in enumerate(unit_test()):
        print(f"Result {i}: {result}")