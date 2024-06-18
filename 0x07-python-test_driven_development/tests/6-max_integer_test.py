#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(max_integer([5, 6, 3, 1]), 6)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([1,2,3,4]), 4)
        self.assertEqual(max_integer([1,3,4,2]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([4, 3, 2, 1, 0]), 4)
        self.assertEqual(max_integer([1, 2, 4, 3, 0]), 4)
        self.assertEqual(max_integer([1, -2, 3, -4]), 3)

        with self.assertRaises(TypeError):
            max_integer(10)

        with self.assertRaises(TypeError):
            max_integer([0, True, "String"])
