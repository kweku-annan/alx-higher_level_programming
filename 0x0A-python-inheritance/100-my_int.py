#!/usr/bin/python3
"""Contains a class that inherits from int"""


class MyInt(int):
    """Inverts the == and != operators of the int class"""
    def __init__(self, number):
        super().__init__()
        self.number = number
        if not isinstance(number, int):
            raise TypeError("number must be an integer")

    def __eq__(self, other):
        if self.number == other:
            return (False)
        else:
            return (True)

    def __ne__(self, other):
        if self.number != other:
            return (False)
        else:
            return (True)
