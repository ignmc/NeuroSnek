from src.GA.genetic_algorithm import GA
from src.NN.neural_network import NeuralNetwork
from src.Snake.MiniSnake import play
from src.Snake.neural_controller import NeuralController, fit


class Dummy:
    def feed(self, **kw):
        print(kw)

NETWORK_SHAPE = (6, 7, 5, 3)
ga = GA(100, NETWORK_SHAPE, fit, 0.01)
ga.get_initial_population()
avg_fitness = []
for generation in range(65):
    print("generation: {}".format(generation))
    ga.build_mating_pool(20)
    avg_fitness.append(sum(ga.fill_population_fitness()) / ga.p_size)
    ga.reproduction()
