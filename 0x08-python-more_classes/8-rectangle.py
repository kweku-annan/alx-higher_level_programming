#!/usr/bin/python3
"""
Contains Rectangle class that defines a rectangle by 3-rectangle.py
"""


class Rectangle:
    """An empty class that defines a rectangle

    Attributes:
        number_of_instances (int): Counts the number of instances created
        print_symbol (any type): Used as symbol for string representation.
            Can be any type
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

    def __str__(self):
        return (f"{self.my_print()}")

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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

    def area(self):
        """Calculates and returns the area of the rectangle
        area = self.__width * self.__height
        """
        area = self.__width * self.__height
        return (area)

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle
        perimeter = 2 * (self.__width + self.__height)
        Returns 0 if any of the sides of the rectangle is 0
        """
        if self.__height == 0 or self.__width == 0:
            perimeter = 0
        else:
            perimeter = 2 * (self.__width + self.__height)
        return (perimeter)

    def my_print(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        result = ""
        for i in range(self.__height):
            result += str(self.print_symbol) * self.__width
            if i < self.__height - 1:
                result += '\n'
        return (result)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares two rectangles and returns the biggest
        based on its area.
        Args:
            rect_1: First Instance of the Rectangle class
            rect_2: Second Instancd of the Rectangle class.
        Returns:
            The biggest rectange based on area.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return (rect_1)
        elif rect_1.area() > rect_2.area():
            return (rect_1)
        else:
            return (rect_2)
