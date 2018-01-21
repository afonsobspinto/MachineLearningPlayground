import point
import perceptron


class Network:
    def __init__(self, gui):
        self.gui = gui
        self.points = self.create_points()
        self.perceptron = perceptron.Perceptron()

    def train_perceptron(self):
        for point_ in self.points:
            color = "green" if self.perceptron.train(point_.inputs, point_.label) == 0 else "red"
            self.gui.draw_circle(point_.x, point_.y, color)

    @staticmethod
    def create_points():
        return [point.Point() for _ in range(100)]

