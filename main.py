import pickle

from src.GA.genetic_algorithm import GA
from src.Snake.neural_controller import fit

from matplotlib import pyplot as plt


NETWORK_SHAPE = (6, 7, 5, 3)
GENERATIONS = 3
POPULATION_SIZE = 100
MUTATION_PROB = 0.01
TOURNAMENT_SIZE = 20

if __name__ == "__main__":
    ga = GA(POPULATION_SIZE, NETWORK_SHAPE, fit, MUTATION_PROB)

    ga.get_initial_population()
    avg_fitness = []
    for _ in range(1, GENERATIONS):
        ga.build_mating_pool(TOURNAMENT_SIZE)
        avg_fitness.append(sum(ga.fill_population_fitness()) / ga.p_size)
        ga.reproduction()

    plt.plot(range(1, GENERATIONS), avg_fitness)
    plt.show()
