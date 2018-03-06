import population as p
import logging
from timeit import default_timer as timer
import qap

class GeneticAlgorithm:
    def __init__(self, generations, input_data, population_size, crossover_probability, mutation_probability):
        #number of generations to count
        self.generations = generations
        self.input_data = input_data
        self.population_size = population_size
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability

    def performGeneticAlgorithm(self, method):
        start_time = timer()
        population = p.Population(self.input_data, self.population_size, self.crossover_probability, self.mutation_probability)
        population.create_population()
        population.evaluate(0)
        logging.getLogger("GENERATION")

        for generation in range(1, self.generations):
            population.crossover(self.selection_method(method, population, generation))
            population.mutation()
            population.evaluate(generation)
            logging.info("Generation no.", generation, population.history[generation])

        end_time = timer()
        time = end_time - start_time
        logging.info("Total time: ", time)
        print("Total time: ", time)
        logging.info("Total number of cost count: ", population.cost_count)
        return population.best_specimen

    def selection_method(self, method, population, generation):
        if method == "roulette":
            return population.selection_by_roulette(generation)
        elif method == "ranking":
            return population.selection_by_ranking(generation)



had12 = qap.QAP("had12.dat")
genetic = GeneticAlgorithm(10, had12, 20, 0.1, 0.05)
best = genetic.performGeneticAlgorithm("ranking")
print("Best: ", best.permutation, best.cost)

genetic2 = GeneticAlgorithm(100, had12, 200, 0.1, 0.05)
best = genetic2.performGeneticAlgorithm("ranking")
print("Best: ", best.permutation, best.cost)

genetic3 = GeneticAlgorithm(2000, had12, 800, 0.7, 0.01)
best = genetic3.performGeneticAlgorithm("ranking")
print("Best: ", best.permutation, best.cost)

# genetic3 = GeneticAlgorithm(2000, had12, 500, 0.1, 0.05)
# best = genetic3.performGeneticAlgorithm("ranking")
# print("Best: ", best.permutation, best.cost)