#!/usr/bin/python3
"""Contains a class Rectangle, that inherits from the class BaseGeometry"""
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Inherits some method from BaseGeometry and uses the validator to
    validate the arguments of the __init__ method
    """

    def __init__(self, width, height):
        """Instantiates the width and height of the rectangle
        Args:
            width: Must always be an integer and greater than 0
            height: Must always be an integer and greater than 0
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
