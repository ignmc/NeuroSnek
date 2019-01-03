import random

from src.GA.individual import Individual
from src.NN.neural_network import NeuralNetwork


class GA:
    def __init__(self, p_size, network_shape, fit, mutation_prob, **kwargs):
        self.p_size = p_size
        self.network_shape = network_shape
        self.population = []
        self.mating_pool = []
        self.fit = fit
        self.mutation_prob = mutation_prob
        self.fit_kwargs = kwargs
        self.population_fitness = []
        self.generation = 0

    def get_initial_population(self):
        for _ in range(self.p_size):
            ind = Individual.get_random(self.network_shape)
            self.population.append(ind)
        self.population_fitness = [None] * self.p_size
        self.generation = 1

    def tournament_selection(self, tournament_size):
        best = None
        best_fitness = None
        pop_size = len(self.population)
        for _ in range(tournament_size):
            random_index = random.randrange(pop_size)
            candidate = self.population[random_index]
            candidate_fitness = self.population_fitness[random_index] or self.fit(candidate, **self.fit_kwargs)
            self.population_fitness[random_index] = candidate_fitness
            print(candidate_fitness)
            if not best or candidate_fitness > best_fitness:
                best = candidate
                best_fitness = candidate_fitness
        return best

    def build_mating_pool(self, tournament_size):
        self.mating_pool.clear()
        self.fill_population_fitness()
        for _ in range(self.p_size * 2):
            parent = self.tournament_selection(tournament_size)
            self.mating_pool.append(parent)

    def reproduction(self):
        self.generation += 1
        self.population.clear()
        random.shuffle(self.mating_pool)
        for _ in range(self.p_size):
            parent1, parent2 = self.mating_pool.pop(), self.mating_pool.pop()
            sequence_size = len(parent1.sequence())
            middle_gen = random.randint(0, sequence_size)
            resulting_sequence = parent1.sequence()[:middle_gen] + parent2.sequence()[middle_gen:]

            # mutate genes
            for i in range(len(resulting_sequence)):
                if random.random() < self.mutation_prob:
                    replacing = resulting_sequence[i]
                    n_input = len(replacing) - 1
                    random_weights = [random.uniform(-2, 2) for _ in range(n_input)]
                    random_bias = [random.uniform(-2, 2)]

                    resulting_sequence[i] = random_bias + random_weights
            child = NeuralNetwork.from_sequence(resulting_sequence, self.network_shape)
            self.population.append(child)
        self.population_fitness = [None] * self.p_size

    def has_solution(self, optimal_fit=0):
        for individual in self.population:
            if self.fit(individual, **self.fit_kwargs) >= optimal_fit:
                return individual
            return None

    def avg_fitness(self):
        s = 0
        for individual in self.population:
            s += self.fit(individual, **self.fit_kwargs)
        return s / len(self.population)

    def fill_population_fitness(self):
        for i, fitness in enumerate(self.population_fitness):
            if not fitness:
                self.population_fitness[i] = self.fit(self.population[i], **self.fit_kwargs)
        return self.population_fitness
