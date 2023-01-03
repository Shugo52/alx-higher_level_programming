#!/usr/bin/python3
"""Test module for the 6-max_integer module"""

import unittest

max_int = __import__("6-max_integer").max_integer


class TestMaxInteger(unittest.TestCase):
    """Class to test the max_integer function."""

    def test_valid_arguments(self):
        """Valid arguments to max int function"""

        self.assertEqual(max_int([1,2, 3]), 3)
        self.assertEqual(max_int([1,2, 3][::-1]), 3)
        self.assertEqual(max_int([1,2, -33]), 2)
        self.assertEqual(max_int([-1, -62, -33]), -1)
        self.assertEqual(max_int([1]), 1)
        self.assertEqual(max_int([]), None)
        self.assertEqual(max_int(), None)
        self.assertEqual(max_int((1, 2, 3)), 3)
        # self.assertEqual(max_int("[1, 2, 3]"), 3)

    def test_invalid_arguments(self):
        """Invald arguments for max_int function"""

        self.assertRaises(TypeError, max_int, [1,2, "3"])
        self.assertRaises(TypeError, max_int, None)


if __name__ == "__main__":
    unittest.main()
