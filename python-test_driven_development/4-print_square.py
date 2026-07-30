#!/usr/bin/python3
"""
This module provides a function `print_square` that prints a square
using the `#` character.
"""


def print_square(size):
    """
    Prints a square with the character #.

    Args:
        size: Length of the square side.

    Raises:
        TypeError: If size is not an integer or is a float < 0.
        ValueError: If size is < 0.
    """
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
