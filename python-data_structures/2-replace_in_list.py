#!/usr/bin/python3
"""Module that defines replace_in_list."""


def replace_in_list(my_list, idx, element):
    """Replace an element in a list at a given index, C-style.

    If idx is negative or out of range, the list is left unchanged.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
