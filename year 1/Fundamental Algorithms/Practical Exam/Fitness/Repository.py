from Routine import *


class Repository:
    def __init__(self, items=[]):
        self.__items = items[:]

    def get_all(self):
        return self.__items[:]

    def add_item(self, Id, name, typ, dif, dur):
        if dur < 1 or dif <= 0 or (typ != "Strength" and typ != "Cardio" and typ != "Flexibility") or Id <= 0:
            raise ValueError("Invalid workout routine!")
        if name == "":
            raise ValueError("Invalid name!")
        for item in self.__items:
            if item.get_id() == Id:
                raise ValueError("Invalid id!")
        self.__items.append(Routine(Id, name, typ, dif, dur))

    def sort_workouts(self):
        self.__items = sorted(self.__items, key=lambda x: x.get_dif(), reverse=True)

    def remove_workouts(self):
        self.__items = [x for x in self.__items if x.get_type() != "Strength" or x.get_dif() <= 3]
