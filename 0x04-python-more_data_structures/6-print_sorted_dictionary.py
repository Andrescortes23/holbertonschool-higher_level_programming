#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    newdic = sorted(a_dictionary)
    for a in newdic:
        print("{}: {}".format(a, a_dictionary[a]))
