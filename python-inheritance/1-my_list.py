#!/usr/bin/python3
"""
Module 1-my_list
Defines a class MyList that inherits from list.
"""


class MyList(list):
    """Custom list class that includes sorted printing capabilities."""

    def print_sorted(self):
        """Prints the list in ascending sorted order without modifying it."""
        print(sorted(self))
