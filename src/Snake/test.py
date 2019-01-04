import datetime
import pickle

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
start = datetime.datetime.now()
delta = datetime.timedelta(hours=5)
end = start + delta
while datetime.datetime.now() < end:
    ga.build_mating_pool(20)
    avg_fitness.append(sum(ga.fill_population_fitness()) / ga.p_size)
    ga.reproduction()

with open('snake5.dump', 'wb') as f:
    pickle.dump(avg_fitness, f)

with open('networks5.dump', 'wb') as f:
    pickle.dump(ga.population, f)

print(ga.generation)


