#!/usr/bin/python3
"""Defines the Base class."""


class Base:
    """Base class for managing id attributes across future classes.

    Attributes:
        __nb_objects (int): Number of instantiated Base objects.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int, optional): ID to assign to the instance. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
