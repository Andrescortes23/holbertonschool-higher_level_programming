#!/usr/bin/python3
"""Module with function to print a square with the character #"""


def print_square(size):

    """
    Method to print # size numbers time size times
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size < 0 and type(size) is float:
        raise TypeError("size must be an integer")

    row = 1
    column = 0
    while column < size:
        row = 0
        while row < size:
            print("#", end='')
            row += 1
        print()
        column += 1
