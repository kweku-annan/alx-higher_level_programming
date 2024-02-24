#!/usr/bin/python3
"""Contains a class 'MyList' that inherits from 'list'"""


class MyList(list):
    """Prints a list but sorted"""
    def print_sorted(self):
        print(sorted(self))
