import random

from src.NN.neural_network import NeuralNetwork


class Individual:

    @staticmethod
    def get_random(network_shape):
        network = NeuralNetwork(layers_sizes=network_shape)
        return network

    def __init__(self, sequence):
        self.sequence = sequence

    def __str__(self):
        return "Individual with genes {}".format(str(self.sequence))

    def __repr__(self):
        return "Individual with genes {}".format(str(self.sequence))
