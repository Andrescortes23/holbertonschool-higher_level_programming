#!/usr/bin/python3
"""Module to Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method for area of rectangle"""
        return self.height * self.width

    def display(self):
        """method to display rectangle image"""
        for y in range(self.y):
            print()
        for a in range(self.height):
            for x in range(self.x):
                print(" ", end='')
            for b in range(self.width):
                print("#", end='')
            print()

    def __str__(self):
        """method to return representation of Rectangle"""
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """method to assign argument to all attributes"""
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
                if len(args) > 2:
                    self.height = args[2]
                    if len(args) > 3:
                        self.x = args[3]
                        if len(args) > 4:
                            self.y = args[4]
        elif len(args) is 0:
            for a in kwargs:
                if a is "id":
                    self.id = kwargs[a]
                if a is "width":
                    self.width = kwargs[a]
                if a is "height":
                    self.height = kwargs[a]
                if a is "x":
                    self.x = kwargs[a]
                if a is "y":
                    self.y = kwargs[a]

    def to_dictionary(self):
        """method to return dictionary of instances"""
        retDict = {"id": self.id, "width": self.width,
                   "height": self.height, "x": self.x, "y": self.y}
        return retDict
