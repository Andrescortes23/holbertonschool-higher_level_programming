#!/usr/bin/python3
"""Module of MyList class who is class of list class"""


class MyList(list):
    """Class MyList"""
    def print_sorted(self):
        """Method to print sorted list"""
        print(sorted(self))
