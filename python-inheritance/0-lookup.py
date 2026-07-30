#!/usr/bin/python3
"""
Module 0-lookup
Returns the list of available attributes and methods of an object.
"""


def lookup(obj):
    """Returns a list object of available attributes and methods."""
    return dir(obj)
