#!/usr/bin/python3
"""Contains a function that adds two integers"""


def add_integer(a, b=98) -> int:

    """Making sure that a is an integer or a float"""
    if not isinstance(a, int) or isinstance(a, float):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")

    """Making sure that b is an integer or a float"""
    if not isinstance(b, int) or isinstance(b, float):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")

    return (a + b)
