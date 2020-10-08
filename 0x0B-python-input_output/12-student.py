#!/usr/bin/python3
"""Module class Student"""


class Student:
    """Class Studen"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Function to get dict"""
        if type(attrs) is list:
            if all(isinstance(a, str) for a in attrs):
                nwe = {}
                for a in attrs:
                    if a in self.__dict__:
                        nwe[a] = self.__dict__[a]
            return nwe
        else:
            return self.__dict__
