#!/usr/bin/python3
"""
Module 8-rectangle
Defines class Rectangle inheriting from BaseGeometry.
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
