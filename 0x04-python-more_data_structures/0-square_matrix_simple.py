#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    outer_list = []
    for i in matrix:
        inner_list = []
        for element in i:
            inner_list.append(element ** 2)
        outer_list.append(inner_list)
    return outer_list
