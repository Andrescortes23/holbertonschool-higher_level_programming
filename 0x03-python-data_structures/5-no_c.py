#!/usr/bin/python3
def no_c(my_string):
    newstring = ''
    for a in my_string:
        if a == 'c' or a == 'C':
            continue
        newstring = newstring + a
    return(newstring)
