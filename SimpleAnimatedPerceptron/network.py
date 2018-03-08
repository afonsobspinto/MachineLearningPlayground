import point
import perceptron


def f(x):
    return 0.3 * x + 0.2


class Network:
    def __init__(self, gui):
        self.function = f
        self.gui = gui
        self.points = self.create_points()
        self.perceptron = perceptron.Perceptron(3)
        self._draw_data()

    def train_perceptron(self):
        for point_ in self.points:
            color = "green" if self.perceptron.train(point_.inputs, point_.label) == 0 else "red"
            self.gui.draw_circle(point_.pixel_x, point_.pixel_y, color)
        self._suggest_line()

    def _draw_data(self):
        self.gui.draw_line(point.Point(-1, f(-1), f), point.Point(1, f(1), f), "yellow")
        self.gui.draw_points(self.points)

    def _suggest_line(self):
        self.gui.delete_items()
        point1 = point.Point(-1, self.perceptron.guess_y(-1), f)
        point2 = point.Point(1, self.perceptron.guess_y(1), f)
        self.gui.to_delete.append(self.gui.draw_line(point1, point2, "blue"))

    @staticmethod
    def create_points():
        return [point.Point(None, None, f) for _ in range(100)]

