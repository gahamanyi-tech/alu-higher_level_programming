#!/usr/bin/python3
"""
Module 3-is_kind_of_class
Checks class instance or inheritance matching.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of or inherited from a_class."""
    return isinstance(obj, a_class)
