#!/usr/bin/python3
"""Unittest for Square class."""
import unittest
import os
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test suites for Square class methods."""

    def setUp(self):
        Square._Base__nb_objects = 0

    def test_instantiation(self):
        s1 = Square(1)
        self.assertEqual(s1.size, 1)

        s2 = Square(1, 2)
        self.assertEqual(s2.x, 2)

        s3 = Square(1, 2, 3)
        self.assertEqual(s3.y, 3)

        s4 = Square(1, 2, 3, 4)
        self.assertEqual(s4.id, 4)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            Square("1")
        with self.assertRaises(TypeError):
            Square(1, "2")
        with self.assertRaises(TypeError):
            Square(1, 2, "3")

    def test_invalid_values(self):
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(1, -2)
        with self.assertRaises(ValueError):
            Square(1, 2, -3)
        with self.assertRaises(ValueError):
            Square(0)

    def test_str(self):
        s = Square(5, 2, 1, 12)
        self.assertEqual(str(s), "[Square] (12) 2/1 - 5")

    def test_to_dictionary(self):
        s = Square(10, 2, 1, 1)
        d = s.to_dictionary()
        expected = {'id': 1, 'size': 10, 'x': 2, 'y': 1}
        self.assertEqual(d, expected)

    def test_update_args(self):
        s = Square(10, 10, 10, 10)
        s.update()
        self.assertEqual(s.id, 10)
        s.update(89)
        self.assertEqual(s.id, 89)
        s.update(89, 1)
        self.assertEqual(s.size, 1)
        s.update(89, 1, 2)
        self.assertEqual(s.x, 2)
        s.update(89, 1, 2, 3)
        self.assertEqual(s.y, 3)

    def test_update_kwargs(self):
        s = Square(10, 10, 10, 10)
        s.update(**{'id': 89})
        self.assertEqual(s.id, 89)
        s.update(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s.update(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s.update(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_create(self):
        s = Square.create(**{'id': 89})
        self.assertEqual(s.id, 89)
        s = Square.create(**{'id': 89, 'size': 1})
        self.assertEqual(s.size, 1)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2})
        self.assertEqual(s.x, 2)
        s = Square.create(**{'id': 89, 'size': 1, 'x': 2, 'y': 3})
        self.assertEqual(s.y, 3)

    def test_save_to_file(self):
        Square.save_to_file(None)
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([])
        with open("Square.json", "r") as f:
            self.assertEqual(f.read(), "[]")

        Square.save_to_file([Square(1, 0, 0, 1)])
        with open("Square.json", "r") as f:
            self.assertTrue(len(f.read()) > 0)
        if os.path.exists("Square.json"):
            os.remove("Square.json")

    def test_load_from_file(self):
        if os.path.exists("Square.json"):
            os.remove("Square.json")
        self.assertEqual(Square.load_from_file(), [])

        s = Square(1, 0, 0, 1)
        Square.save_to_file([s])
        objs = Square.load_from_file()
        self.assertEqual(len(objs), 1)
        self.assertEqual(objs[0].id, 1)
        if os.path.exists("Square.json"):
            os.remove("Square.json")


if __name__ == '__main__':
    unittest.main()
