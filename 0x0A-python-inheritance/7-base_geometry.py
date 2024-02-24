#!/usr/bin/python3
"""An Geometry Class with public instance methods"""


class BaseGeometry:
    """A base Geometry Class with a public instance method"""

    def area(self):
        """Raises an exception if it is being used"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the parameter 'value
        Args:
            name (str): It will always be a string
            value (int): Must always be an integer and always greater than 0
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
