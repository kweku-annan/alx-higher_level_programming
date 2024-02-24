#!/usr/bin/python3
"""Checks if a specified object is an instance of a specified class"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Args:
        obj:
            Object to check class of.
        a_class:
            Class to check if obj is an instance of

    Returns:
       True: If obj is an instance of a_class
       False: if obj is not an instance of a_class
    """

    if type(obj) is a_class:
        return (True)
    else:
        return (False)
