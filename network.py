from __future__ import annotations
from typing import List, Callable, TypeVar, Tuple
from functools import reduce
from layer import Layer
from util import sigmoid, derivative_sigmoid

T = TypeVar('T')  # output type of interpretation of neural network

class Network:
    def __init__(self, layer_structure: List[int], learning_rate: float,
    activation_function: Callable[[float], float] = sigmoid,
    derivative_activation_function: Callable[[float], float] = derivative_sigmoid) -> None:
        if len(layer_structure) < 3:
            raise ValueError('error: should be at least 3 layers (1 input, 1 hidden, 1 output)')
        self.layers: List[Layer] = []
        input_layer: Layer = Layer(None, layer_structure[0], learning_rate,
        activation_function, derivative_activation_function)
        self.layers.append(input_layer)
        # hidden layers and output layer
        for previous, num_neurons in enumerate(layer_structure[1::]):
            next_layer = Layer(self.layers[previous], num_neurons, learning_rate,
            activation_function, derivative_activation_function)
            self.layers.append(next_layer)

    # pushes input data to first layer, then output from first
    # as input to second, second to third, etc.
    def outputs(self, input: List[float]) -> List[float]:
        return reduce(lambda inputs, layer: layer.outputs(inputs),
        self.layers, input)

    # figure out each neurons changes based on errors of output
    # vs the expected outcome
    def backpropagate(self, expected: List[float]) -> None:
        # calculate delta for output layer neurons
        last_layer: int = len(self.layers) - 1
        self.layers[last_layer].calculate_deltas_for_output_layer(expected)
        # calculate delta for hidden layers in reverse order
        for l in range(last_layer - 1, 0, -1):
            self.layers[l].calculate_deltas_for_hidden_layer(self.layers[l + 1])

    # backprop doesn't actually change any weights
    # this function uses the deltas calculated in backpropagate()
    # to actually make changes to the weights
    def update_weights(self) -> None:
        for layer in self.layers[1:]:  # skip input layer
            for neuron in layer.neurons:
                for w in range(len(neuron.weights)):
                    neuron.weights[w] = neuron.weights[w] + (neuron.learning_rate \
                        * (layer.previous_layer.output_cache[w]) * neuron.delta)

    # train() uses the results of outputs() run over many inputs and compared
    # against expecteds to feed backpropagate() and update_weights()
    def train(self, inputs: List[List[float]], expecteds: List[List[floats]]) -> None:
        for location, xs, in enumerate(inputs):
            ys: List[float] = expecteds[location]
            outs: List[float] = self.outputs(xs)
            self.backpropagate(ys)
            self.update_weights()

    # for generalized results that require classification
    # this function will return correct number of trials
    # and percentage correct out of the total
    def validate(self, inputs: List[List[float]], expecteds: List[T],
    interpret_output: Callable[[List[float]], T]) -> Tuple[int, int, float]:
        correct: int = 0
        for input, expected in zip(inputs, expecteds):
            result: T = interpret_output(self.outputs(input))
            if result == expected:
                correct += 1
        percentage: float = correct / len(inputs)
        return correct, len(inputs), percentage