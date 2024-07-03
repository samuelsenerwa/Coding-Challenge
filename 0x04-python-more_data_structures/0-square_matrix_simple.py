#!/usr/bin/python3

"""
Prototype: def square_matrix_simple(matrix=[])
matrix is a 2 dimensional array

Returns a new matrix:
◦ Same size as matrix
◦ Each value should be the square of the value of the input
"""


def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for i in range(len(matrix)):
        new_matrix[i] = list(map(lambda x: x**2, matrix[i]))

    return new_matrix
