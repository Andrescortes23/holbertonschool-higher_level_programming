#!/usr/bin/python3
def new_in_list(my_list, idx, element):

    new_list = []
    for a in range(len(my_list)):
        new_list.append(my_list[a])
    if idx < 0:
        return (new_list)
    elif idx >= len(my_list):
        return (my_list)
    elif idx >= 0:
        for a in range(len(my_list)):
            if a == idx:
                new_list[a] = element
                return (new_list)
