import random
import numpy as np

def count_current_permutation_cost(D, F, permData):
    cost = 0.0
    for i in range(len(permData)):
        for j in range(len(permData)):
            distance = D[i][j]
            flow = F[permData[i] - 1][permData[j] - 1]
            cost += distance * flow
    return cost


def generate_random_permutation(size):
    return random.sample(range(size), size)