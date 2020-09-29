#!/usr/bin/python3
"""Module represent square with symbols"""


class Rectangle:
    """Class to define a rectangle with height and width"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """Method to print a rectangle"""
        newstr = ''
        if self.height is 0 or self.width is 0:
            return ''
        for a in range(self.height):
            b = 0
            for b in range(self.width):
                newstr += str(self.print_symbol)
            if a + 1 in range(self.height):
                newstr += '\n'
        return newstr

    def __repr__(self):
        """Method to create a representation of rectangle"""
        return "{}({}, {})".\
            format(self.__class__.__name__, self.width, self.height)

    def __del__(self):
        """Method to delete instance"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    print_symbol = '#'

    def bigger_or_equal(rect_1, rect_2):
        """Static method to know the biggest rectangle area based in area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() is rect_2.area():
                return rect_1
            elif rect_1.area() > rect_2.area():
                return rect_1
            elif rect_1.area() < rect_2.area():
                return rect_2

    def square(cls, size=0):
        """Class method to get a new rectangle"""
        return cls(size, size)
