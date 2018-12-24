from argparse import ArgumentError
import random

from NN.neural_layer import NeuralLayer
from NN.sigmoid_neuron import SigmoidNeuron


class NeuralNetwork:

    def __init__(self, first_layer=None, layers=None, layers_sizes=None):

        def connect_layers(layers_list):
            for i in range(len(layers_list) - 1):
                layers_list[i].next_layer = layers_list[i + 1]
                layers_list[i + 1].previous_layer = layers_list[i]
            return layers_list[0], layers_list[-1]

        if layers is None:
            if first_layer is None:
                if layers_sizes is None:
                    raise ArgumentError("No layers specified")
                else:
                    layers = []
                    for i in range(len(layers_sizes) - 1):
                        input_size = layers_sizes[i]
                        layer_size = layers_sizes[i+1]
                        neurons = []
                        for j in range(layer_size):
                            weights = [random.uniform(-2, 2) for _ in range(input_size)]
                            bias = random.uniform(-2, 2)
                            neurons.append(SigmoidNeuron(weights, bias))
                        layers.append(NeuralLayer(neurons))

                    self.first_layer, self.output_layer = connect_layers(layers)
            else:
                # Case: only the first layer of an already built network was supplied
                self.first_layer = first_layer
                temp_layer = first_layer
                while temp_layer.next_layer is not None:  # Find the output layer
                    temp_layer = temp_layer.next_layer
                self.last_layer = temp_layer
        else:
            # All the layers were supplied. Let's connect them in the same order they are listed
            self.first_layer, self.output_layer = connect_layers(layers)

    def feed(self, inputs):
        return self.first_layer.feed(inputs)

    def backward_propagate_error(self, expected_outputs):
        self.output_layer.backward_propagate_error(expected_outputs)

    def update_weights(self, inputs, learning_rate):
        self.first_layer.update_weights_and_bias(inputs, learning_rate)

    def train(self, inputs, expected_outputs, learning_rate):
        outputs = self.feed(inputs)
        self.backward_propagate_error(expected_outputs)
        self.update_weights(inputs, learning_rate)
