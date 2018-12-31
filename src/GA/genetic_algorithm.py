import random

from src.GA.individual import Individual


class GA:
    def __init__(self, p_size, network_shape, fit, mutation_prob, **kwargs):
        self.p_size = p_size
        self.network_shape = network_shape
        self.population = []
        self.mating_pool = []
        self.fit = fit
        self.mutation_prob = mutation_prob
        self.fit_kwargs = kwargs

    def get_initial_population(self):
        for _ in range(self.p_size):
            ind = Individual.get_random(self.network_shape)
            self.population.append(ind)

    def tournament_selection(self, tournament_size):
        best = None
        best_fitness = None
        pop_size = len(self.population)
        for _ in range(tournament_size):
            candidate = self.population[random.randrange(pop_size)]
            candidate_fitness = self.fit(candidate, **self.fit_kwargs)
            if not best or candidate_fitness > best_fitness:
                best = candidate
                best_fitness = candidate_fitness
        return best

    def build_mating_pool(self, tournament_size):
        self.mating_pool.clear()
        for _ in range(self.p_size * 2):
            parent = self.tournament_selection(tournament_size)
            self.mating_pool.append(parent)

    def reproduction(self):
        self.population.clear()
        random.shuffle(self.mating_pool)
        for _ in range(self.p_size):
            parent1, parent2 = self.mating_pool.pop(), self.mating_pool.pop()
            middle_gen = random.randint(0, self.p_size)
            resulting_sequence = parent1.sequence[:middle_gen] + parent2.sequence[middle_gen:]

            # mutate genes
            for i in range(len(resulting_sequence)):
                if random.random() < self.mutation_prob:
                    resulting_sequence[i] = random.choice(self.vocabulary)
            child = Individual(self.n_size, self.vocabulary)
            child.sequence = resulting_sequence
            self.population.append(child)

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
