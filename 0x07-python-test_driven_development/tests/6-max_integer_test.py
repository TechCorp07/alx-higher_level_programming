#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer"""

    def test_typeError(self):
        """Test TypeError exception"""
        with self.assertRaises(TypeError):
            max_integer([1, 2, "Holberton", 4])
            max_integer({1, 2, 3, 4})

    def test_returnval(self):
        """Test argument types"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)

if __name__ == "__main__":
    unittest.main()
