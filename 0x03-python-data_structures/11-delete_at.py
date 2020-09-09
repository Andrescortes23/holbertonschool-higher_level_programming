#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list):
        return (my_list)

    for a in range(len(my_list)):
        if a == idx:
            del(my_list[a])
            return (my_list)
