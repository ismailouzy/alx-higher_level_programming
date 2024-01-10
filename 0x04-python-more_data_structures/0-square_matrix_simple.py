#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i in matrix:
        ni = []
        for j in i:
            ni.append(j ** 2)
        new_matrix.append(ni)

    return new_matrix
