#!/usr/bin/python3
"""
Contains an empty Rectangle class that defines a rectangle by 0-rectangle.py
"""


class Rectangle:
    """An empty class that defines a rectangle"""

    def __init__(self, width=0, height=0):
        """Args of the __init__ method are:
        Args:
            width (int): Default width of the rectangle. Must be an
                int and must be >= 0.
            height (int): Default height of the rectangle. Must be an int
                and must be >= 0.
        """
        self.__width = width
        self.__height = height

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.__width = value
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.__height = value
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
