#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    newmatrix = [[b ** 2 for b in a] for a in matrix]
    return newmatrix
