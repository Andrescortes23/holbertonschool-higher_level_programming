#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)

    my_list.sort()
    Biggerint = my_list[-1]

    return (Biggerint)
