#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for lst in matrix:
        len_list = len(lst)
        if len_list > 0:
            no_braces = "{:d} " * (len_list - 1) + "{:d}"
            print(no_braces.format(*lst))
        else:
            print()
