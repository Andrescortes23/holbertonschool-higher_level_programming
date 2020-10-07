#!/usr/bin/python3
"""Module to add text to our file"""


def append_write(filename="", text=""):
    """Function to write at the end of file"""
    with open(filename, 'a', encoding='UTF8') as myFile:
        numchar = myFile.write(text)
    return numchar
