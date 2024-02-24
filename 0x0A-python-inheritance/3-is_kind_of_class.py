#!/usr/bin/python3
"""Checks if an object is an instance of, or if the object is an instance
of a class that inherited from the specified class"""


def is_kind_of_class(obj, a_class):
    """Returns True of obj is an instance or inherits from a_class otherwise
    False.

    Args:
        obj:
            Object to check its class
        a_class:
            Class to check if obj is an instance of

    Returns:
        True: if obj is an instance of, or if obj is an instance of a class
            that inherited from the specified class.
        False: If otherwise.
    """
    return (isinstance(obj, a_class))
