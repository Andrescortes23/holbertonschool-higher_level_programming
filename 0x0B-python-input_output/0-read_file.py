#!/usr/bin/python3
"""Module to read file"""


def read_file(filename=""):
    """Function to read file"""
    with open(filename, encoding='UTF8') as op:
        print(op.read(), end='')
