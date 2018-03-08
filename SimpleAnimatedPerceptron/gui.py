import tkinter
import network
from globals import *


class GUI:
    def __init__(self, width, height):
        root = tkinter.Tk()
        root.title("SimpleNeuralNetwork")
        self.canvas = tkinter.Canvas(root, width=width, height=height)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.callback)
        self.network = network.Network(self)
        self.draw_text("Click to train.")
        self.to_delete = []
        root.mainloop()

    def draw_points(self, points):
        for point_ in points:
            self._display_point(point_)

    def _display_point(self, point_):
        color = "black" if point_.label == Label.up else "white"
        self.draw_circle(point_.pixel_x, point_.pixel_y, color)

    def draw_text(self, text):
        self.canvas.create_text(100, HEIGHT-50,
                                fill="dark slate gray", font="Times 20 italic bold", text=text)

    def draw_circle(self, x, y, color):
        return self.canvas.create_oval(x-RADIUS, y-RADIUS,
                                       x+RADIUS, y+RADIUS,
                                       outline="black", fill=color, width=2)

    def draw_line(self, start_point, stop_point, color="black"):
        return self.canvas.create_line(start_point.pixel_x, start_point.pixel_y,
                                       stop_point.pixel_x, stop_point.pixel_y,
                                       width=4, fill=color)

    def callback(self, _):
        self.network.train_perceptron()

    def delete_items(self):
        for item in self.to_delete:
            self.canvas.delete(item)



