#!/usr/bin/python3
"""Checks if an object is an instance of a class that inherited (directly or
indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class that inherited
    directly or indirectly from a specified a_class.

    Args:
        obj:
            Object to work with
        a_class:
            Class to check object of

    Return:
        True: If obj is an instance of a class that inherited
            from a specified class.
        False: If otherwise.
    """

    if type(obj) is a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
