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

    def area(self) -> int:
        """ Returns the area(int) of the square"""
        ar = self.__size * self.__size
        return (ar)

    def my_print(self):
        """Prints in the stdout the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            ar = self.__size
            i = 0
            while i < ar:
                for j in range(ar):
                    print("#", end="")
                print()
                i += 1
