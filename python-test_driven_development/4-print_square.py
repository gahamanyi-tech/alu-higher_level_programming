#!/usr/bin/python3
"""Module that provides a function to print a square with # characters."""


def print_square(size):
    """Prints a square with the character # of size `size`."""
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
