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
        next = 0
        localizations = set(range(0, self.size))
        best_cost = float("inf")
        best_permutation = list([])

        #find start point: the shortest path with the biggest flow for all matrix

        # for i in range(self.size):
        #     for j in range(self.size):
        #         distance = self.D[i][j]
        #         flow = self.F[i][j]
        #         if (distance != 0 and flow != 0):
        #             factor = distance / flow
        #             if minimum_factor > factor:
        #                 minimum_factor = factor
        #                 current = i
        #                 next = j
        #
        # localizations.remove(current)
        # solution.append(current)
        # current = next


        for a in localizations:

            permutation = list([])
            current = a
            localizations_to_visit = set(range(0, self.size))

            while localizations_to_visit != set([]):

                factor_next = float("inf")

                for l in localizations_to_visit:
                    distance = self.D[current][l]
                    flow = self.F[current][l]
                    if (distance != 0 and flow != 0):
                        factor = utils.count_current_permutation_cost(self.D, self.F, (current, l))
                        if factor < factor_next:
                            factor_next = factor
                            next = l

                localizations_to_visit.remove(current)
                permutation.append(current)
                current = next

            cost = utils.count_current_permutation_cost(self.D, self.F, permutation)

            if (cost < best_cost):
                best_cost = cost
                best_permutation = permutation


        return best_cost, best_permutation


# count sample cos for 12 x 12
print("\n12 x 12")
permHad12 = [int(x) for x in "3,10,11,2,12,5,6,7,8,1,4,9".split(",")]
had12 = QAP("had12.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had12.D, had12.F, permHad12), ",", permHad12)
print("Random Search: ")
print(had12.random_search(1000))
print("Greedy Algorithm: ")
print(had12.greedy_algorithm())


# count sample for 14 x 14
print("\n14 x 14")
permHad14 = [int(x) for x in "8,13,10,5,12,11,2,14,3,6,7,1,9,4".split(",")]
had14 = QAP("had14.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had14.D, had14.F, permHad14), ",", permHad14)
print("Random Search: ")
print(had14.random_search(2000))
print("Greedy Algorithm: ")
print(had14.greedy_algorithm())

# count sample for 16 x 16
print("\n16 x 16")
permHad16 = [int(x) for x in "9,4,16,1,7,8,6,14,15,11,12,10,5,3,2,13".split(",")]
had16 = QAP("had16.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had16.D, had16.F, permHad16), ",", permHad16)
print("Random Search: ")
print(had16.random_search(3000))
print("Greedy Algorithm: ")
print(had16.greedy_algorithm())

# count sample for 18 x 18
print("\n18 x 18")
permHad18 = [int(x) for x in "8,15,16,6,7,18,14,11,1,10,12,5,3,13,2,17,9,4".split(",")]
had18 = QAP("had18.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had18.D, had18.F, permHad18), ",", permHad18)
print("Random Search: ")
print(had18.random_search(4000))
print("Greedy Algorithm: ")
print(had18.greedy_algorithm())

# count sample for 20 x 20
print("\n20 x 20")
permHad20 = [int(x) for x in "8,15,16,14,19,6,7,17,1,12,10,11,5,20,2,3,4,9,18,13".split(",")]
had20 = QAP("had20.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had20.D, had20.F, permHad20), ",", permHad20)
print("Random Search: ")
print(had20.random_search(5000))
print("Greedy Algorithm: ")
print(had20.greedy_algorithm())