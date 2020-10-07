#!/usr/bin/python3
"""Module to count number of lines in file"""


def number_of_lines(filename=""):
    """Function to count number of lines in file"""
    with open(filename, encoding='UTF8') as op:
        lines = len(op.readlines())
    return lines
