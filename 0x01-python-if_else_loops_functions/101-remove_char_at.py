#!/usr/bin/python3
def remove_char_at(str, n):
    newstring = ''
    for a in range(len(str)):
        if a != len(str) and a != n:
            newstring += str[a]
    return (newstring)
