class NeuralLayer:
    def __init__(self, neurons, previous_layer=None, next_layer=None):
        self.neurons = neurons
        self.previous_layer = previous_layer
        self.next_layer = next_layer

    def feed(self, inputs):
        output = []
        for neuron in self.neurons:
            output.append(neuron.feed(inputs))
        if self.is_output_layer():
            return output
        return self.next_layer.feed(output)

    def is_first_layer(self):
        if self.previous_layer is None:
            return True
        return False

    def is_output_layer(self):
        if self.next_layer is None:
            return True
        return False

    def backward_propagate_error(self, expected_output):
        if self.is_output_layer():  # output layer
            for i, neuron in enumerate(self.neurons):
                error = expected_output[i] - neuron.output
                neuron.adjust_delta_with(error)
        else:  # hidden layer
            for i, neuron in enumerate(self.neurons):
                error = sum([next_neuron.weights[i] * next_neuron.delta for next_neuron in self.next_layer.neurons])
                neuron.adjust_delta_with(error)
        if self.previous_layer is not None:
            self.previous_layer.backward_propagate_error(None)

    def update_weights_and_bias(self, inputs, lr):
        if self.is_first_layer():
            previous_inputs = inputs
        else:
            previous_inputs = [previous_neuron.output for previous_neuron in self.previous_layer.neurons]

        for neuron in self.neurons:
            neuron.adjust_weights_with_input(previous_inputs, lr)
            neuron.adjust_bias_using_learning_rate(lr)

        if self.next_layer is not None:
            self.next_layer.update_weights_and_bias(inputs, lr)
