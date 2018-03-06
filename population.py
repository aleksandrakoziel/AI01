import utils
import qap
import random
import specimen as s
import numpy.random as npr
import numpy as np

class Population:

    def __init__(self, input_data, population_size, crossover_probability, mutation_probability):

        #input data as QAP
        self.input_data = input_data

        #population parameters
        self.population_size = population_size
        self.crossover_probability = crossover_probability
        self.mutation_probability = mutation_probability

        #population
        self.population = []
        self.best_specimen = None
        self.history = dict()

        self.cost_count = 0


    #create new population
    def create_population(self):
        while(len(self.population) < self.population_size):
            self.population.append(s.Specimen(self.input_data, utils.generate_random_permutation(self.input_data.size)))
            self.population = list(set(self.population))



    #count population stats as
    # total cost,
    # minimum cost,
    # maximum cost
    # and average cost
    def evaluate(self, iteration=None):
        population_of_generation = self.population
        sum_costs = sum(specimen.cost for specimen in population_of_generation)
        average_cost = sum_costs / len(population_of_generation)

        current_population_parameters = {"Total_population": population_of_generation,
                                         "Total_costs": sum_costs,
                                         "Minimum_cost": min(population_of_generation, key=lambda specimen: specimen.cost),
                                         "Maximum_cost": max(population_of_generation, key=lambda specimen: specimen.cost),
                                         "Average_cost": average_cost}

        if self.best_specimen is None or self.best_specimen.cost > current_population_parameters["Minimum_cost"].cost:
            self.best_specimen = current_population_parameters["Minimum_cost"]
        if iteration is not None:
            self.history[iteration] = current_population_parameters

        return current_population_parameters

    def selection_by_tournament(self):
        pass

    def selection_by_roulette(self, previous_generation):

        current_population = self.history["previous_generation"]
        probability_distribution = []
        for specimen in self.population:
            probability_distribution.append((current_population["Maximum_cost"].cost - (specimen.cost + 1))
                                            /(current_population["Total_cost"] + 1))

        to_crossover = random.choices(current_population,
                                      probability_distribution,
                                      k=int(self.population_size * self.crossover_probability))

        if len(to_crossover) % 2 != 0:
            if len(to_crossover) > 2:
                to_crossover = to_crossover[:, -1]
            else:
                raise ValueError("Cannot cross one specimen!")


        return to_crossover


    def selection_by_ranking(self, generation=None):
        current = self.population

        ranking = sorted(current, key=lambda specimen: specimen.cost)
        count_specimens = int(self.population_size * self.crossover_probability)
        if count_specimens % 2 != 0:
            if count_specimens > 2:
                count_specimens = count_specimens - 1
            else:
                raise ValueError("Cannot cross one specimen!")

        specimen_to_crossover = [specimen[1] for specimen in ranking[:count_specimens]]
        return specimen_to_crossover


    def crossover(self, selected_to_cross):
            for i in zip(*[iter(selected_to_cross)] * 2):
                self.population[i[0]], self.population[i[1]] = self.crossover_specimens(self.population[i[0]],
                                                                                        self.population[i[1]])


    def crossover_specimens(self, mother, father):
        if len(mother.permutation) != len(father.permutation):
            raise ValueError("Permutation sizes mismatch!")

        offspring_1, offspring_2 =  mother.permutation.copy(), father.permutation.copy()
        pivot = npr.randint(1, self.input_data.size - 1)
        offspring_1[:pivot] = father.permutation[:pivot]
        offspring_2[pivot:] = mother.permutation[pivot:]
        self.fix_locations(offspring_1)
        self.fix_locations(offspring_2)
        return [s.Specimen(self.input_data, offspring_1),
                s.Specimen(self.input_data, offspring_2)]

    def fix_locations(self, locations):
        number_of_occurrences = np.bincount(locations, minlength=self.input_data.size)
        for replace_from, replace_to in zip(np.where(number_of_occurrences == 2)[0],
                                            np.where(number_of_occurrences == 0)[0]):

            locations[np.where(locations == replace_from)[0][0]] = replace_to


    def mutation(self):
        mutations = int(npr.binomial(self.population_size, self.mutation_probability))
        npr.choice(range(self.population_size), mutations, replace=False)
        for i in npr.choice(range(self.population_size), mutations, replace=False):
            self.population[i] = self.population[i].mutation()


had12 = qap.QAP("had12.dat")
population = Population(had12, 20, 0.1, 0.05)
print(population.create_population())
print(population.evaluate())

permHad12_1 = [int(x) for x in "5,10,11,2,12,3,6,7,8,1,4,9".split(",")]
permHad12_2 = [int(x) for x in "4,10,11,2,0,3,6,7,8,1,5,12".split(",")]
child_1, child_2 = population.crossover_specimens(s.Specimen(population.input_data, permHad12_1),
                                     s.Specimen(population.input_data, permHad12_2))
print(child_1.permutation, child_1.cost)
print(child_2.permutation, child_2.cost)