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
        if type(size) is not int and type(size) is not float:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Returns size. Getter method."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        return (self.area() == other.area())

    def __lt__(self, other):
        return (self.area() < other.area())

    def __ne__(self, other):
        return (self.area() != other.area())

    def __le__(self, other):
        return (self.area() <= other.area())

    def __gt__(self, other):
        return (self.area() > other.area())

    def __ge__(self, other):
        return (self.area() >= other.area())

    def area(self) -> int:
        """ Returns the area(int) of the square"""
        ar = self.__size * self.__size
        return (ar)
