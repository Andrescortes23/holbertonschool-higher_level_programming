#!/usr/bin/python3
"""Module to get the sum of two numbers (integers or floats
   and return the sum of those numbers casted as integers"""


def add_integer(a, b=98):
    """
    Method to add two integers or floats

    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
