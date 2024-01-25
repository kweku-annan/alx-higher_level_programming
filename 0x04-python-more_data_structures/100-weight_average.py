#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    sum = 0
    weight = 0
    for item in my_list:
        sum += item[0] * item[1]
        weight += item[1]
    w_average = sum / weight
    return w_average
