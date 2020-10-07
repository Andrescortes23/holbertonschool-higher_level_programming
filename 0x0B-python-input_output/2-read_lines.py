#!/usr/bin/python3
"""Module to read nb lines of file"""


def read_lines(filename="", nb_lines=0):
    """Function to read nb lines of file"""
    count = 0
    with open(filename, encoding='UTF8') as myFile:
        lines = len(myFile.readline())
        myFile.seek(0)
        if nb_lines <= 0 or nb_lines >= lines:
            print(myFile.read(), end='')
        else:
            while count < nb_lines:
                print(myFile.readline(), end='')
                count += 1
