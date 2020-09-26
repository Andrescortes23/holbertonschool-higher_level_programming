#!/usr/bin/python3
"""Module with a function that prints 2 strings"""

def say_my_name(first_name, last_name=""):
    """
    Method that print check if the two arguments passed
    are strings and add to a string to print

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
