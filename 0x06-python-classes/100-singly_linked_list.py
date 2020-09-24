#!/usr/bin/python3
"""Here is a module"""


class Node:
    """Here is a class"""
    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_value

    @next_node.setter
    def next_node(self, value):
        if type(next_node) is not Node or None:
            raise TypeError ("next_node must be a Node object")

class SinglyLinkedList:
    """Here is a class"""
    def __init__(self, head):
        self.__head = head
