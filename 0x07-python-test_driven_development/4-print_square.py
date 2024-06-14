#!/usr/bin/python3
"""This function prints a square using '#'"""


def print_square(size):
    """Prints square using '#' based on size"""
    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError("size must be an integer")
    if isinstance(size, int) and size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for h in range(0, int(size)):
        i = int(size)
        for w in range(0, i):
            print("#", end="")
        print()
