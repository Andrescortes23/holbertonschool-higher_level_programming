#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for a in range(len(my_list)):
        a = a - a - a - 1
        if a == 0:
            a = -1
        print("{}".format(my_list[a]))
