#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = []
    for a in my_list:
        if a == search:
            a = replace
        new.append(a)
    return new
