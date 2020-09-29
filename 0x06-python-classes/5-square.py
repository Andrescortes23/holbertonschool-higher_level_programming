#!/usr/bin/python3
"""Here is a module"""


class Square:
    """Here is a class"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, newsize):
        if type(newsize) is not int:
            raise TypeError("size must be an integer")
        elif newsize < 0:
            raise ValueError("size must be >= 0")
        self.__size = newsize

    def area(self):
        return self.size * self.size

    def my_print(self):
        if self.size == 0:
            print()
        a = 0
        while a < self.size:
            b = 0
            while b < self.size:
                print("#", end='')
                b += 1
            print()
            a += 1
