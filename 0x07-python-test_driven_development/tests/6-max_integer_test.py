#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_regular_list(self):
        """Test max_integer with a regular list"""
        result = max_integer([1, 2, 3, 4])
        self.assertEqual(result, 4)

    def test_reverse_order(self):
        """Test max_integer with a list in reverse order"""
        result = max_integer([1, 3, 4, 2])
        self.assertEqual(result, 4)

    def test_empty_list(self):
        """Test max_integer with an empty list"""
        result = max_integer([])
        self.assertIsNone(result)

    def test_negative_numbers(self):
        """Test max_integer with a list of negative numbers"""
        result = max_integer([-1, -5, -2, -8])
        self.assertEqual(result, -1)

    def test_mixed_numbers(self):
        """Test max_integer with a list of mixed positive and negative numbers"""
        result = max_integer([1, -3, 7, -2])
        self.assertEqual(result, 7)

    def test_single_element_list(self):
        """Test max_integer with a list containing a single element"""
        result = max_integer([42])
        self.assertEqual(result, 42)

    def test_float_numbers(self):
        """Test max_integer with a list containing float numbers"""
        result = max_integer([1.5, 2.3, 0.7, 3.1])
        self.assertEqual(result, 3.1)

    def test_mixed_data_types(self):
        """Test max_integer with a list containing mixed data types"""
        result = max_integer(['a', 1, 'b', 3])
        self.assertEqual(result, 'b')

if __name__ == '__main__':
    unittest.main()

