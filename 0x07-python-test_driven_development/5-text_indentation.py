#!/usr/bin/python3
"""Module with functions that print a text divide in parts"""


def text_indentation(text):

    """
    Method to find certain characters in the passed text, when is founded
    print two new lines and continue printing the text
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    cnt = 0
    for char in text:
        if text[cnt - 1] in (".", "?", ":") and char is " ":
            cnt += 1
            continue
        print(char, end='')
        if char in (".", "?", ":"):
            print('\n')
        cnt += 1
