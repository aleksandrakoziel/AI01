import numpy as np


def read_data_from_file(file):
    # file structure to load
    #  quadratic matrix size
    # empty line
    # first matrix A
    # empty line
    # second matrix B

    with open(file, mode='r', encoding='utf-8') as data:
        size = int(data.readline())
        data.readline()
        A = load_data_to_matrix(data, size)
        data.readline()
        B = load_data_to_matrix(data, size)
    return (size, A, B)


def load_data_to_matrix(f, size):
    matrix = []
    i = size
    while (i > 0):
        l = f.readline()
        matrix.append([int(x) for x in l.split(' ') if x != ''])
        i -= 1
    return matrix