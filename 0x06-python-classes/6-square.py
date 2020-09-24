#!/usr/bin/python3
"""Here is a module"""


class Square:
    """Here is a class"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if len(value) is not 2 or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.size * self.size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            if self.__position:
                for a in range(self.__position[1]):
                    print()
                for a in range(int(self.__size)):
                    for a in range(self.__position[0]):
                        print(" ", end='')
                    for a in range(int(self.__size)):
                        print("#", end='')
                    print()
