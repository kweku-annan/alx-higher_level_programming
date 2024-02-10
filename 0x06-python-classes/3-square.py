#!/usr/bin/python3
"""
This module has a class, Square, that defines a square by:
   Private instance attribute size
"""


class Square(object):
    """Square defines a square by: """

    def __init__(self, size=0):
        """
        Attributes:
            self.__size: A private instance attribute. Determines the size of
                the square.
        Args:
            size (int): default size of the square. It must be an integer and
                must be greater than or equal to 0
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def area(self) -> int:
        """ Returns the area(int) of the square"""
        ar = self.__size * self.__size
        return (ar)
