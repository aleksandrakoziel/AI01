import random
import numpy as np
import utils as utils
import data as data

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
        cost = 0.0
        minimum_cost = float("inf")
        start = 0
        second = 0
        cost = 0.0
        for i in range(self.size):
            for j in range(self.size):
                distance = self.D[i][j]
                flow = self.F[permData[i] - 1][permData[j] - 1]
                cost += distance * flow
        for i in range(self.size):
            for j in range(self.size):
                distance = self.D[i][j]
                if minimum_distance > distance:
                    minimum_distance = distance
                    a = i
                    b = j
        for i in range(self.size):
           for j in range(self.size):
                flow = self.F[a - 1][b - 1]
                if flow > maximum_flow:
                    maximum_flow = flow

        #cost += distance * flow
        return cost,


# count sample cos for 12 x 12
print("\n12 x 12")
permHad12 = [int(x) for x in "3,10,11,2,12,5,6,7,8,1,4,9".split(",")]
had12 = QAP("had12.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had12.D, had12.F, permHad12), ",", permHad12)
print("Random Search: ")
print(had12.random_search(1000))
print("Greedy Algorithm: ")


# count sample for 14 x 14
print("\n14 x 14")
permHad14 = [int(x) for x in "8,13,10,5,12,11,2,14,3,6,7,1,9,4".split(",")]
had14 = QAP("had14.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had14.D, had14.F, permHad14), ",", permHad14)
print("Random Search: ")
print(had14.random_search(2000))
print("Greedy Algorithm: ")

# count sample for 16 x 16
print("\n16 x 16")
permHad16 = [int(x) for x in "9,4,16,1,7,8,6,14,15,11,12,10,5,3,2,13".split(",")]
had16 = QAP("had16.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had16.D, had16.F, permHad16), ",", permHad16)
print("Random Search: ")
print(had16.random_search(3000))
print("Greedy Algorithm: ")

# count sample for 18 x 18
print("\n18 x 18")
permHad18 = [int(x) for x in "8,15,16,6,7,18,14,11,1,10,12,5,3,13,2,17,9,4".split(",")]
had18 = QAP("had18.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had18.D, had18.F, permHad18), ",", permHad18)
print("Random Search: ")
print(had18.random_search(4000))
print("Greedy Algorithm: ")

# count sample for 20 x 20
print("\n20 x 20")
permHad20 = [int(x) for x in "8,15,16,14,19,6,7,17,1,12,10,11,5,20,2,3,4,9,18,13".split(",")]
had20 = QAP("had20.dat")
print("Optimum: ")
print(utils.count_current_permutation_cost(had20.D, had20.F, permHad20), ",", permHad20)
print("Random Search: ")
print(had20.random_search(5000))
print("Greedy Algorithm: ")