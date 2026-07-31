#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test suites for Base class methods."""

    def setUp(self):
        Base._Base__nb_objects = 0

    def test_id_auto(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_auto_increment(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_id_custom(self):
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        res = Base.to_json_string([{'id': 12}])
        self.assertEqual(res, '[{"id": 12}]')

    def test_to_json_string_type(self):
        res = Base.to_json_string([{'id': 12}])
        self.assertIsInstance(res, str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        res = Base.from_json_string('[{"id": 89}]')
        self.assertEqual(res, [{'id': 89}])

    def test_from_json_string_type(self):
        res = Base.from_json_string('[{"id": 89}]')
        self.assertIsInstance(res, list)


if __name__ == '__main__':
    unittest.main()
