#!/usr/bin/python3
"""Unittest for max_integer([..])"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_max_at_beginning(self):
        """Test a list where max integer is at index 0."""
        self.assertEqual(max_integer([4, 3, 2, 1]), 4)

    def test_empty_list(self):
        """Test an empty list."""
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(max_integer([7]), 7)

    def test_floats(self):
        """Test a list of float numbers."""
        self.assertEqual(max_integer([1.5, 2.3, 0.9]), 2.3)

    def test_ints_and_floats(self):
        """Test a list with integers and floats."""
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_string(self):
        """Test a string input."""
        self.assertEqual(max_integer("Python"), 'y')

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["apple", "zebra", "banana"]), "zebra")

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)


if __name__ == '__main__':
    unittest.main()
