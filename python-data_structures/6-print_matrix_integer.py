#!/usr/bin/python3
"""Module that defines print_matrix_integer."""


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers, space-separated, one row per line."""
    for row in matrix:
        print(" ".join("{}".format(n) for n in row))
