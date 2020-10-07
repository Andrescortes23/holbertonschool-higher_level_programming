#!/usr/bin/python3
"""Module if Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class from class Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
