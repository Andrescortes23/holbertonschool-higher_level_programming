#!/usr/bin/python3
"""Module to verify instance"""


def inherits_from(obj, a_class):
    """Check if object inherited from specified class"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    else:
        return False
