#!/usr/bin/python3
def replace_in_list(my_list, idx, element):

    if idx < 0:
        return (my_list)
    elif idx >= len(my_list):
        return (my_list)
    elif idx >= 0:
        for a in range(len(my_list)):
            if a == idx:
                my_list[a] = element
                return (my_list)
