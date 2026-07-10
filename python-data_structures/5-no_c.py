#!/usr/bin/python3
"""Module that defines no_c."""


def no_c(my_string):
    """Return a copy of my_string with all 'c' and 'C' removed."""
    return "".join([c for c in my_string if c != 'c' and c != 'C'])
