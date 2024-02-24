#!/usr/bin/python3
"""Contains a function that returns a list of available
attributes and methods of an object.
"""


def lookup(obj):
    """Returns a list of available attributes of obj

    Args:
        obj:
            Object to return attribute of.

    Returns:
        A list of attributes and methods available to obj
    """
    return (dir(obj))
