#!/usr/bin/python3
"""Module of rectangle to know the area and perimeter"""


class Rectangle:
    """Class to define a rectangle with height and width"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Method to get width"""
        return self.__width

    @width.setter
    def width(self, newwidth):
        """Method to set value to width"""
        if type(newwidth) is not int:
            raise TypeError("width must be an integer")
        if newwidth < 0:
            raise ValueError("width must be >= 0")
        self.__width = newwidth

    @property
    def height(self):
        """Method to get height"""
        return self.__height

    @height.setter
    def height(self, newheight):
        """Method to set value to height"""
        if type(newheight) is not int:
            raise TypeError("height must be an integer")
        if newheight < 0:
            raise ValueError("height must be >= 0")
        self.__height = newheight

    def area(self):
        """Method to know the rectangle area"""
        return self.width * self.height

    def perimeter(self):
        """Method to know the rectangle perimeter"""
        if self.width is 0 or self.height is 0:
            return 0
        return 2 * (self.width + self.height)
