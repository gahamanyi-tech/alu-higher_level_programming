#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # Pad both tuples with (0, 0) and slice the first two elements
    a = (tuple_a + (0, 0))[:2]
    b = (tuple_b + (0, 0))[:2]

    # Return the sum of the respective elements as a new tuple
    return (a[0] + b[0], a[1] + b[1])
