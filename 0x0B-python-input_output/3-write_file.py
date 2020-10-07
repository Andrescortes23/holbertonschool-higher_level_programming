#!/usr/bin/python3
"""Module to write in a file"""


def write_file(filename="", text=""):
    """Function to write"""
    with open(filename, 'w+', encoding='UTF8') as myFile:
        numchar = myFile.write(text)
    return numchar
