#!/usr/bin/python3
"""
Module 9-rectangle
Defines class Rectangle with area calculation and string representation.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class representation."""

    def __init__(self, width, height):
        """Initializes width and height with validation."""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns rectangle area."""
        return self.__width * self.__height

    def __str__(self):
        """Returns human-readable representation of Rectangle."""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
