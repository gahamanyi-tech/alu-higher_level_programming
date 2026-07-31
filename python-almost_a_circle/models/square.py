#!/usr/bin/python3
"""Defines the Square class inheriting from Rectangle."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square shape."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square instance.

        Args:
            size (int): Size of the sides.
            x (int, optional): Horizontal position offset. Defaults to 0.
            y (int, optional): Vertical position offset. Defaults to 0.
            id (int, optional): Identity integer. Defaults to None.
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Get or set the size of the Square."""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        """Return human-readable string representation of Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """Update attributes with positional arguments or keyword arguments.

        Args:
            *args (list): 1st=id, 2nd=size, 3rd=x, 4th=y.
            **kwargs (dict): Key/value attribute mappings.
        """
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for idx, arg in enumerate(args):
                if idx < len(attrs):
                    setattr(self, attrs[idx], arg)
        elif kwargs:
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Return dictionary representation of a Square."""
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
