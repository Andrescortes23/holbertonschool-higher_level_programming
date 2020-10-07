#!/usr/bin/python3
"""Method to check if object is instance of a class"""


def is_same_class(obj, a_class):
    """Function return True if the type of obj is the same of class"""
    if type(obj) == a_class:
        return True
    else:
        return False
