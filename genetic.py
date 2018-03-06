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

    def performGeneticAlgorithmWithRanking(self):
        start_time = timer()
        population = p.Population(self.input_data, self.population_size, self.crossover_probability, self.mutation_probability)
        population.create_population()
        population.evaluate(0)
        logging.getLogger("GENERATION")

        for generation in range(1, self.generations):
            population.crossover(population.selection_by_ranking(generation))
            population.mutation()
            population.evaluate(generation)
            logging.info("Generation no.", generation, population.history[generation])

        end_time = timer()
        time = start_time - end_time
        logging.info("Total time: ", time)
        print("Total time: ", time)
        logging.info("Total number of cost count: ", population.cost_count)
        return population.best_specimen

had12 = qap.QAP("had12.dat")
genetic = GeneticAlgorithm(10, had12, 20, 0.1, 0.05)
print("Best: ", genetic.performGeneticAlgorithmWithRanking())