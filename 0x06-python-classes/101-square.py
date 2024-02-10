#!/usr/bin/python3
"""
This module has a class, Square, that defines a square by:
   Private instance attribute size
"""


class Square(object):
    """Square defines a square by: """

    def __init__(self, size=0, position=(0, 0)):
        """
        Attributes:
            __size: A private instance attribute. Determines the size of
                the square.
            __position: A private instance attribute of type tuple, and of
                len: 2
        Args:
            size (int): default size of the square. It must be an integer and
                must be greater than or equal to 0
            position (tuple)

        """
        self.__size = size
        self.__position = position
        self.printed = self.my_print()
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(cord, int) and cord >= 0 for cord in position):
            raise TypeError("position must be a tuple of 2 positive integers")

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

    @property
    def position(self):
        """Returns position. Getter method."""
        return (self.__position)

    @position.setter
    def position(self, value=(0, 0)):
        if not isinstance(value, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(cord, int) and cord >= 0 for cord in value):
            raise TypeError("position must be a tuple of 2 positive integers")

    def __str__(self):
        """
        Enable print a square instance to have the same behavior as my_print
        """
        return (f"{self.printed}")

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
            x_cord = self.__position[0]
            [print("") for i in range(self.__position[1])]
            while i < ar:
                for cord in range(x_cord):
                    print(" ", end="")
                for j in range(ar):
                    print("#", end="")
                print()
                i += 1
