#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegef(unittest.TestCase):
    """Unitests class"""
    def test_cases(self):
        """test cases for max integer"""
        self.assertIsNone(max_integer([]))
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]),     -1)
        self.assertEqual(max_integer([-1, 2, -3, 4, -5]), 4)
        self.assertEqual(max_integer([42]), 42)
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)
        self.assertRaises(TypeError, max_integer, [1, 2, 'a', 4, 5])
        self.assertRaises(TypeError, max_integer, [3, [3, 5]])
