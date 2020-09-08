#!/usr/bin/python3
def element_at(my_list, idx):
    lenoflist = len(my_list)

    for a in range(lenoflist):
        if a == idx:
            return (my_list[a])
