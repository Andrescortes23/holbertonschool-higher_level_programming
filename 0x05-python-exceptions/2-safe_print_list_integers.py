#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    limit = 0
    count = 0
    while limit < x:
        try:
            print("{:d}".format(my_list[limit]), end='')
            limit += 1
            count += 1
        except(ValueError, TypeError):
            limit += 1
            pass
    print()
    return count
