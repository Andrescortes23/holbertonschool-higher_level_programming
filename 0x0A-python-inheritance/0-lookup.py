#!/usr/bin/python3
"""Module to look up a list of methods and attributes of an object"""


def lookup(obj):
    """Function to return a list of __dict__"""
    return(list(obj.__dict__))
