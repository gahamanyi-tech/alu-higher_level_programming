#!/usr/bin/python3
"""Defines the Base class for the project."""
import json
import os


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON string representation of list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.

        Returns:
            str: JSON string representation of list_dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON string representation of list_objs to a file.

        Args:
            list_objs (list): A list of instances inheriting from Base.
        """
        filename = f"{cls.__name__}.json"
        list_dicts = []

        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]

        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """Return the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: List represented by json_string or [] if empty/None.
        """
        if json_string is None or json_string.strip() == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return an instance with all attributes already set.

        Args:
            **dictionary (dict): Key/value pairs of attributes to initialize.

        Returns:
            Base: An instance of Rectangle or Square with values updated.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Return a list of instances created from a JSON file.

        Returns:
            list: List of instances of type cls.
        """
        filename = f"{cls.__name__}.json"
        if not os.path.exists(filename):
            return []

        with open(filename, "r", encoding="utf-8") as f:
            json_str = f.read()

        dict_list = cls.from_json_string(json_str)
        return [cls.create(**d) for d in dict_list]
