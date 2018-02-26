import random
import numpy as np

class Genetic:

    def __init__(self, file, permData):
        size, A, B = self.read_data_from_file(file)
        self.size = size
        self.A = A
        self.B = B
        self.perm = permData


    # file structure to load
    # quadratic matrix size
    # empty line
    # first matrix A
    # empty line
    # second matrix B

    def read_data_from_file(self, file):
        with open(file, mode='r', encoding='utf-8') as data:
            size = int(data.readline())
            data.readline()
            A = self.load_data_to_matrix(data, size)
            data.readline()
            B = self.load_data_to_matrix(data, size)
        return (size, A, B)

    def load_data_to_matrix(self, f, size):
        matrix = []
        i = size
        while (i > 0):
            l = f.readline()
            matrix.append([int(x) for x in l.split(' ') if x != ''])
            i -= 1
        return matrix

    def random_permutation(self):
        return random.sample(range(self.size), self.size)

    def count_current_permutation_cost(self):
        cost = 0.0
        for i in range(len(self.perm)):
            for j in range(len(self.perm)):
                cost = cost + self.A[i][j] * self.B[self.perm[i]-1][self.perm[j]-1]
        return cost

# count sample cos for 12 x 12
permHad12 = [int(x) for x in "3,10,11,2,12,5,6,7,8,1,4,9".split(",")]
had12 = Genetic("had12.dat", permHad12)
print("Optimum dla 12x12: ")
print(had12.count_current_permutation_cost())

# count sample cos for 14 x 14
permHad14 = [int(x) for x in "8,13,10,5,12,11,2,14,3,6,7,1,9,4".split(",")]
had14 = Genetic("had14.dat", permHad14)
print("Optimum dla 14x14: ")
print(had14.count_current_permutation_cost())

# count sample cos for 16 x 16
permHad16 = [int(x) for x in "9,4,16,1,7,8,6,14,15,11,12,10,5,3,2,13".split(",")]
had16 = Genetic("had16.dat", permHad16)
print("Optimum dla 16x16: ")
print(had16.count_current_permutation_cost())

# count sample cos for 18 x 18
permHad18 = [int(x) for x in "8,15,16,6,7,18,14,11,1,10,12,5,3,13,2,17,9,4".split(",")]
had18 = Genetic("had18.dat", permHad18)
print("Optimum dla 18x18: ")
print(had18.count_current_permutation_cost())

# count sample cos for 20 x 20
permHad20 = [int(x) for x in "8,15,16,14,19,6,7,17,1,12,10,11,5,20,2,3,4,9,18,13".split(",")]
had20 = Genetic("had20.dat", permHad20)
print("Optimum dla 20x20it: ")
print(had20.count_current_permutation_cost())