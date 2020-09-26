#!/usr/bin/python3
"""Module with function that divides all elements of a matrix
   and return new matrix with the result of divisions"""

def matrix_divided(matrix, div):
    """
    Method to divide numbers by a given number

    """
    tmp = []
    newlist = []

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div is 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) and len(matrix) is 0:
        raise TypeError("matrix must be a matrix (list of lists) of\
integers/floats")

    for a in matrix:
        if not isinstance(a, list) or len(a) is 0:
            raise TypeError("matrix must be a matrix (list of lists) of\
integers/floats")
        tmp = []
        for b in a:
            if type(b) is not int and type(b) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of\
integers/floats")
            tmp.append(round(b / div, 2))
        if len(a) is not len(tmp):
            raise TypeError("Each row of the matrix must have the same size")
        newlist.append(tmp)
    return newlist
