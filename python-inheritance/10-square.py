#!/usr/bin/python3
"""
Module 10-square
Defines class Square inheriting from Rectangle.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class representation."""

    def __init__(self, size):
        """Initializes size with validation."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns square area."""
        return self.__size ** 2
