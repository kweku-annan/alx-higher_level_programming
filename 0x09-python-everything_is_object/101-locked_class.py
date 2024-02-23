#!/usr/bin/python3
"""Contains a class that does not allow user to dynamically
set attributes except when attribute name is 'first_name'
"""


class LockedClass:
    """User can only set attribute dynamically if attribute
    name is 'first_name'
    """
    def __setattr__(self, name, value):
        if name != "first_name":
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
                )
