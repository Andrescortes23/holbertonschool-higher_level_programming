#!/usr/bin/python3
"""Module to check is object is an instance of class"""


def is_kind_of_class(obj, a_class):
    """Function that return True if object is instance of class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
