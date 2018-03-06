import utils as utils
import data as data
import random

class QAP:


    def __init__(self, file):
        size, D, F = data.read_data_from_file(file)
        self.size = size
        self.D = D # distances
        self.F = F # flows


    def random_search(self, randomSearchIterationValue):

        best_cost = float("inf")
        best_permutation = utils.generate_random_permutation(self.size)

        for i in range(randomSearchIterationValue):
            current_permutation = utils.generate_random_permutation(self.size)
            current_cost = utils.count_current_permutation_cost(self.D, self.F, current_permutation)
            if (current_cost < best_cost):
                best_cost = current_cost
                best_permutation = current_permutation

        return best_cost, best_permutation


    def greedy_algorithm(self):

        localizations = set(range(0, self.size)) # all factories
        best_cost = float("inf")
        best_permutation = list([])

        for a in localizations:

            permutation = list([])
            current = a # where am I now
            next = 0 # where should I go
            localizations_to_visit = set(range(0, self.size))

            while localizations_to_visit != set([]):

                cost_next = float("inf")
                localizations_to_visit.remove(current)

                for l in localizations_to_visit:
                    cost = utils.count_current_permutation_cost(self.D, self.F, (current, l))
                    if cost < cost_next:
                        cost_next = cost
                        next = l


                permutation.append(current)
                current = next

            cost = utils.count_current_permutation_cost(self.D, self.F, permutation)

            if (cost < best_cost):
                best_cost = cost
                best_permutation = permutation


        return best_cost, best_permutation
