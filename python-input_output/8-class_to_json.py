#!/usr/bin/python3
"""
Module 8-class_to_json
Contains a function that returns the dictionary description for JSON.
"""


def class_to_json(obj):
    """Returns dictionary representation of simple data structure
    for JSON serialization of an object.
    """
    return obj.__dict__
