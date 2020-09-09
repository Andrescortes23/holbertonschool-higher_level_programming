#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    elif len(tuple_b) == 0:
        tuple_b = (0, 0)
    elif len(tuple_b) > 2:
        tuple_b = (tuple_b[0], tuple_b[1])

    add1 = tuple_a[0] + tuple_b[0]
    add2 = tuple_a[1] + tuple_b[1]
    new_tuple = (add1, add2)

    return (new_tuple)
