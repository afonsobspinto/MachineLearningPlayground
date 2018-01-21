from enum import Enum


WIDTH = 600
HEIGHT = 600
RADIUS = 10


class Label(Enum):
    up = 1
    below = -1

    def __new__(cls, value):
        member = object.__new__(cls)
        member._value_ = value
        return member

    def __int__(self):
        return self.value

