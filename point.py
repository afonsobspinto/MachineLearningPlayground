import random
from globals import *


class Point:
    def __init__(self):
        self.x = random.randint(RADIUS, WIDTH-RADIUS)
        self.y = random.randint(RADIUS, HEIGHT-RADIUS)
        self.label = Label.up if self.x > self.y else Label.below

    @property
    def inputs(self):
        return [self.x, self.y]


