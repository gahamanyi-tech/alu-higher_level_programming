#!/usr/bin/python3
"""
Module 4-inherits_from
Checks subclass inheritance status.
"""


def inherits_from(obj, a_class):
    """Returns True if obj inherited (directly/indirectly) from a_class."""
    return issubclass(type(obj), a_class) and type(obj) is not a_class
