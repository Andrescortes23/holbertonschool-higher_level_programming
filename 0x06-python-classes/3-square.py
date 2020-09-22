#!/usr/bin/python3
"""Here is a module"""


class Square:
    """Here is a class"""
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        return self.__size * self.__size
