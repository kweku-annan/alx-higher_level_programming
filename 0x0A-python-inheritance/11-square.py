#!/usr/bin/python3
"""Inherits from the Rectangle class and calculates square"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Inherits from the Rectangle class and implements the area of
    a square
    """

    def __init__(self, size):
        """Instantiates the size of the square
        Args:
            size (int): Must always be a positive integer
        """
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return ("[Square] {}/{}".format(self.__size, self.__size))

    def area(self):
        """Calculates the area of the Square"""
        return (self.__size * self.__size)
