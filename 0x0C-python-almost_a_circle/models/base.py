#!/usr/bin/python3
"""This module contains the base class 'Base' for our package"""


class Base:
    """This class, 'Base', has the following class attributes:

    Attributes:
        __nb_objects (int): A private class attribute initialized with 0

    """

    __nb_objects = 0


    def __init__(self, id=None):
        """The class constructor with args id.

        Args:
            id (int): Either __nb_objects or a different number

        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
