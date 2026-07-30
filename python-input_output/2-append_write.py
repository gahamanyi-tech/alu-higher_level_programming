#!/usr/bin/python3
"""
Module 2-append_write
Contains a function that appends a string at the end of a text file.
"""


def append_write(filename="", text=""):
    """Appends a string to a UTF8 text file and returns
    the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
