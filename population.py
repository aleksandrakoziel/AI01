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
    def evaluate(self, generation=None):
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
        if generation is not None:
            self.history[generation] = current_population_parameters

        return current_population_parameters

    def selection_by_tournament(self, tour_size):
        pass

    def selection_by_roulette(self, previous_generation):

        current_population = self.population
        max_cost = max(current_population, key=lambda specimen: specimen.cost)
        total_cost = sum(specimen.cost for specimen in current_population)

        probability_distribution = []
        for specimen in self.population:
            probability_distribution.append((max_cost.cost - specimen.cost)/(total_cost))


        summarize_probability = sum(probability_distribution)
        probability_distribution[-1] = probability_distribution[-1] + 1 - summarize_probability

        to_crossover = np.random.choice(current_population,
                                        int(self.population_size * self.crossover_probability),
                                        replace=False,
                                        p=probability_distribution)
        for x in to_crossover:
            print(x.permutation)

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

        specimen_to_crossover = [specimen for specimen in ranking[:count_specimens]]
        return specimen_to_crossover


    def crossover(self, selected_to_cross):
        for specimen in selected_to_cross:
            self.population.remove(specimen)

        for specimen in range(0, len(selected_to_cross), 2):
            offspring_1, offspring_2 = self.crossover_specimens(selected_to_cross[specimen], selected_to_cross[specimen + 1])
            self.population.append(offspring_1)
            self.population.append(offspring_1)
            self.cost_count += 2


    def crossover_specimens(self, mother, father):
        if len(mother.permutation) != len(father.permutation):
            raise ValueError("Permutation sizes mismatch!")

        offspring_1, offspring_2 = mother.permutation.copy(), father.permutation.copy()
        pivot = npr.randint(1, self.input_data.size - 1)
        offspring_1[:pivot] = father.permutation[:pivot]
        offspring_2[:pivot] = mother.permutation[:pivot]
        self.fix_locations(offspring_1)
        self.fix_locations(offspring_2)
        return [s.Specimen(self.input_data, offspring_1),
                s.Specimen(self.input_data, offspring_2)]

    def crossover_PMX(self, mother, father):
        if len(mother.permutation) != len(father.permutation):
            raise ValueError("Cannot crossover two subjects with different perm size")
        cut_points = sorted(random.sample(range(1, len(mother.permutation)), 2))

        offspring_1, offspring_2 = s.Specimen(self.input_data, mother.permutation), s.Specimen(self.input_data, father.permutation)

        for localisation in range(cut_points[0], cut_points[1]):
            offspring_2.permutation[localisation] = mother.permutation[localisation]
            offspring_1.permutation[localisation] = father.permutation[localisation]

        mapping = dict()
        for i in [x for x in range(len(mother.permutation)) if x not in range(cut_points[0], cut_points[1])]:
            mapping[i] = [mother.permutation[i], father.permutation[i]]

        for i in mapping:
            if mother.permutation[i] not in offspring_1.permutation:
                offspring_1.permutation[i] = mapping[i][0]
            else:
                offspring_1.permutation[i] = mapping[i][1]
            if mother.permutation[i] not in offspring_2.permutation:
                offspring_2.permutation[i] = mapping[i][0]
            else:
                offspring_2.permutation[i] = mapping[i][1]

        return offspring_1, offspring_2

    def fix_locations(self, locations):
        number_of_occurrences = np.bincount(locations, minlength=self.input_data.size)
        for replace_from, replace_to in zip(np.where(number_of_occurrences == 2)[0],
                                            np.where(number_of_occurrences == 0)[0]):

            locations[np.where(locations == replace_from)[0][0]] = replace_to


    def mutation(self):
        mutations = int(npr.binomial(self.population_size, self.mutation_probability))
        npr.choice(range(self.population_size), mutations, replace=False)
        for i in npr.choice(range(self.population_size), mutations, replace=False):
            self.population[i] = self.population[i].mutation(self.mutation_probability)
            self.cost_count += 1

