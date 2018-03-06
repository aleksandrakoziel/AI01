import utils
import random

class Specimen:

    def __init__(self, input_data, permutation):
        self.input_data = input_data
        self.permutation = permutation
        self.cost = utils.count_current_permutation_cost(input_data.D, input_data.F, permutation)

    def __str__(self):
        return str(self.permutation) + str(self.cost)

    def mutation(self, probability_mutation):
        random_indexes = random.sample(range(1, len(self.permutation)), 2)
        mutated_locations = self.permutation.copy()
        swap = mutated_locations[random_indexes[0]]
        mutated_locations[random_indexes[0]] = mutated_locations[random_indexes[1]]
        mutated_locations[random_indexes[1]] = swap
        return Specimen(self.input_data, mutated_locations)