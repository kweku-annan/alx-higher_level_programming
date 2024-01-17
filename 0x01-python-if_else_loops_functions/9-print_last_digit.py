#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        ls_dg = number % 10
    else:
        ls_dg = (number * -1) % 10
    print("{}".format(ls_dg), end="")
    return ls_dg
