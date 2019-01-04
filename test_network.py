from src.Snake.MiniSnake import play
from src.Snake.neural_controller import NeuralController


def test_network(network):
    controller = NeuralController(network)
    return play(controller)
