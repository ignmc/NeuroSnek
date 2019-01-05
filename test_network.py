import pickle

from src.Snake.MiniSnake import play
from src.Snake.neural_controller import NeuralController


def test_network(network):
    controller = NeuralController(network)
    return play(controller)

NETWORK_INDEX = 50

# No olvides reducir la variable FPS en el archivo src/Snake/MainSnake para visualizar mejor cómo juega la red

if __name__ == "__main__":
    with open('networks5.dump', 'rb') as f:
        networks = pickle.load(f)
    test_network(networks[50])
