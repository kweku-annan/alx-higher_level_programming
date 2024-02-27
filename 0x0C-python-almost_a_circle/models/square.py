#!/usr/bin/python3
"""This module contains a Square class that inherits from the Rectangle
class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """This class is Square class that inherits from the Rectangle
    class and implements a square shape of rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """This is the constructor of the Square class with the
        following:

        Args:
            width (int): Width of the square set to a private instance
                attributes.
            height (int): Height of the square set to a private
                instance attribute.
            x (int): x coordinate of the square
            y (int): y coordinate of the square
            id (int): id of the rectangle
        """

        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        """Prints the string of Square"""
        string = "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id,
            self.x, self.y, self.height
            )
        return (string)

    @property
    def size(self):
        """Getter for size"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.__size = value
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Updates the attributes"""
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
