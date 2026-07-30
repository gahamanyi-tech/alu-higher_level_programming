#!/usr/bin/python3
"""Module that provides a function for adding two integers."""


def add_integer(a, b=98):
    """Adds 2 integers.

    a and b must be integers or floats.
    Floats are casted to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
