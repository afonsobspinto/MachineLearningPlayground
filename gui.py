import tkinter
import network
from globals import *


class GUI:
    def __init__(self, width, height):
        self.network = network.Network(self)
        root = tkinter.Tk()
        root.title("SimpleNeuralNetwork")
        self.canvas = tkinter.Canvas(root, width=width, height=height)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.callback)
        self._draw_points(self.network.points)
        self.draw_line()
        root.mainloop()

    def _draw_points(self, points):
        for point in points:
            self._display_point(point)

    def _display_point(self, point):
        self.draw_circle(point.x, point.y, "blue")

    def draw_circle(self, x, y, color):
        self.canvas.create_oval(x-RADIUS, y-RADIUS, x+RADIUS, y+RADIUS, outline="black", fill=color, width=2)

    def draw_line(self):
        self.canvas.create_line(0, 0, WIDTH, HEIGHT)

    def callback(self, _):
        print("Training")
        self.network.train_perceptron()
