import utils
import numpy as np

class Specimen:

    def __init__(self, input_data, permutation):
        self.input_data = input_data
        self.permutation = permutation
        self.cost = utils.count_current_permutation_cost(input_data.D, input_data.F, permutation)

    #factor is selection provability
    def mutation(self, factor):
        random_indexes = np.random.choice(range(self.input_data.size),
                                              int(factor * self.input_data.size / 2) * 2, replace=False)
        mutated_locations = self.permutation.copy()
        mutated_locations[random_indexes] = mutated_locations[random_indexes[::-1]]

        return Specimen(self.input_data, mutated_locations)