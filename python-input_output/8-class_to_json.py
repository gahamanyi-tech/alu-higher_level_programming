#!/usr/bin/python3
"""
Module 8-class_to_json
Contains a function that returns the dictionary description for JSON serialization.
"""


def class_to_json(obj):
    """Returns dictionary representation of simple data structure for JSON serialization."""
    return obj.__dict__
