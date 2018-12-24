import math


class SigmoidNeuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias
        self.lr = 0.1
        self.output = None
        self.delta = None

    def feed(self, input):
        sum = 0
        for i, w in zip(self.weights, input):
            sum += i * w
        z = sum + self.bias
        self.output = 1 / (1 + math.exp(-z))
        return self.output

    def train(self, input, desired_output):
        real_output = self.feed(input)
        diff = desired_output - real_output
        for i in range(len(self.weights)):
            self.weights[i] += (self.lr * input[i] * diff)
        self.bias += (self.lr * diff)

    def adjust_delta_with(self, error):
         self.delta = error * (self.output * (1 - self.output))

    def adjust_weights_with_input(self, inputs, lr):
        for i in range(len(self.weights)):
            self.weights[i] += lr * self.delta * inputs[i]

    def adjust_bias_using_learning_rate(self, lr):
        self.bias += lr * self.delta


