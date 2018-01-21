import random
from globals import *


class Point:
    def __init__(self, x=None, y=None, func=None):
        self.x = random.uniform(-1, 1) if x is None else x
        self.y = random.uniform(-1, 1) if y is None else y
        self.b = 1
        self.func = (lambda x_: x_) if func is None else func
        self._labeling()

    def _labeling(self):
        self.label = Label.up if self.y > self._line_y else Label.below

    @property
    def _line_y(self):
        return self.func(self.x)

    @property
    def pixel_x(self):
        return self.remapping(self.x, -1, 1, 0, WIDTH)

    @property
    def pixel_y(self):
            return self.remapping(self.y, -1, 1, HEIGHT, 0)

    @property
    def inputs(self):
        return [self.x, self.y, self.b]

    @staticmethod
    def remapping(value, start1, stop1, start2, stop2):
        try:
            return start2 + (stop2 - start2) * ((value - start1) / (stop1 - start1))
        except ZeroDivisionError:
            print("Oops! Can't remap", value, "from space", start1, "-", stop1, "into space", start2, "-", stop2)
            return None




