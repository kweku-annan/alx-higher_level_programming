#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if tuple_a == ():
        tuple_a = (0, 0)
    elif len(tuple_a) < 2 and tuple_a != ():
        tuple_a = (tuple_a[0], 0)

    if tuple_b == ():
        tuple_b = (0, 0)
    elif len(tuple_b) < 2 and tuple_b != ():
        tuple_b = (tuple_b[0], 0)

    new_list = []
    for i in range(0, 2):
        new_list.append(tuple_a[i] + tuple_b[i])

    return tuple(new_list)
