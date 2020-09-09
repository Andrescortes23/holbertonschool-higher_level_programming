#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in (matrix):
        spc =''
        for b in a:
            print("{:s}{:d}".format(spc, b), end="")
            spc =' '
        print()
