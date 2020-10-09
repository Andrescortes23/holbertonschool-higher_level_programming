#!/usr/bin/python3
"""Module function that add text to file"""


def append_after(filename="", search_string="", new_string=""):
    """Function to insert text to a file in specific position"""
    with open(filename, 'r', encoding='UTF8') as myFile:
        Newstr = ''
        for line in myFile:
            Newstr += line
            if search_string in line:
                Newstr += new_string
    with open("append_after_100.txt", 'w', encoding='UTF8') as myFile:
        myFile.write(Newstr)
