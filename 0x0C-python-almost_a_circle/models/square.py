#!/usr/bin/python3
"""Module to Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """method to return representation of Square"""
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.size)

    def update(self, *args, **kwargs):
        """method to assign argument to all attributes"""
        if len(args) > 0:
            self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
                if len(args) > 2:
                    self.x = args[2]
                    if len(args) > 3:
                        self.y = args[3]
        elif len(args) is 0:
            for a in kwargs:
                if a is "id":
                    self.id = kwargs[a]
                if a is "size":
                    self.size = kwargs[a]
                if a is "x":
                    self.x = kwargs[a]
                if a is "y":
                    self.y = kwargs[a]

    def to_dictionary(self):
        """method to return dictionary of instances"""
        retDict = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return retDict
