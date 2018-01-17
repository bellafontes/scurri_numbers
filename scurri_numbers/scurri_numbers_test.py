#!/usr/bin/env python3
import unittest
from scurri_numbers import Numbers


class TestScurriNumbers(unittest.TestCase):
    """
    Test
    """
    def setUp(self):
        self.numbers = Numbers()

    def test_print_multiple_three_number(self):
        number = 6
        result = "Three"
        self.assertIs(result, self.numbers.validate(number))

    def test_print_multiple_five_number(self):
        number = 10
        result = "Five"
        self.assertEqual(result, self.numbers.validate(number))

    def test_print_multiple_three_and_five_number(self):
        number = 30
        result = "ThreeFive"
        self.assertEqual(result, self.numbers.validate(number))

    def test_print_no_multiple_number(self):
        number = 77
        result = number
        self.assertEqual(result, self.numbers.validate(number))

    def test_print_first_multiple_sequence_number(self):
        number = 1
        result = number
        self.assertEqual(result, self.numbers.validate(number))

    def test_print_last_multiple_sequence_number(self):
        number = 100
        result = "Five"
        self.assertEqual(result, self.numbers.validate(number))


if __name__ == '__main__':
    unittest.main()
