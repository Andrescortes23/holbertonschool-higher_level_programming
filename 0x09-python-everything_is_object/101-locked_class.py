#!/usr/bin/python3
"""Module to create a class"""


class LockedClass:
    """Class that prevent new instance create new attributes"""
    __slots__ = "first_name"
