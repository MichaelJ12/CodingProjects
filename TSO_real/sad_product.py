from enum import Enum

class MyType(Enum):
    ENTRANCE = 1
    EXIT = 2
    BOTH = 3

class SmartAccessDevice(object):
    def __init__(self, id: str, default_open_time: int, type: MyType) -> None:
        self.id = id
        self.default_open_time = default_open_time
        self.set_type(type)

    def set_type(self, type: MyType):
        self.type = type
        if self.type == MyType.BOTH:
            self.type = MyType.EXIT

    def get_type(self):
        return self.type

    def get_actual_open_time(self, detected_age: int):
        if detected_age < 25:
            return self.default_open_time 
        elif detected_age >= 25 and detected_age <= 50:
            return self.default_open_time * 2
        else:
            return self.default_open_time * 3


    def show_sad_info(self):
        if self.default_open_time == 0:
            print(f"info: {self.id} {self.get_actual_open_time(17)} {self.get_actual_open_time(42)} {self.get_actual_open_time(57)} ")
            print(f"LET OP! Standaard wachttijd staat nopg op 0!")
        else:
            print(f"info: {self.id} {self.get_actual_open_time(17)} {self.get_actual_open_time(42)} {self.get_actual_open_time(57)} ")
        

        