import random


class Perceptron:
    def __init__(self):
        self.learning_rate = 0.1
        self._create_weights()

    def _create_weights(self):
        self.weights = [random.uniform(-1, 1) for _ in range(2)]

    def guess(self, inputs):
        sum_ = 0
        for i in range(len(self.weights)):
            sum_ += inputs[i] * self.weights[i]
        guess = self._activation_function(sum_)
        return guess

    def train(self, inputs, correct_value):
        error = int(correct_value) - self.guess(inputs)
        for i in range(len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learning_rate
        return error

    @staticmethod
    def _activation_function(number):
        if number >= 0:
            return 1
        else:
            return -1

