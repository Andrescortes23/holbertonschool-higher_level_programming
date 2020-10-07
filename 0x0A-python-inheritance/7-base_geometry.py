#!/usr/bin/python3
"""Module of class"""


class BaseGeometry:
    """Class BaseGeometry"""
    def area(self):
        """area not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate if parameter is integer"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        self.name = name
        self.value = value
