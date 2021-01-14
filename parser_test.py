import unittest
from parser import parse_roman_numeral


class RomanNumeralsTest(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(parse_roman_numeral("I"), 1)
        self.assertEqual(parse_roman_numeral("II"), 2)
        self.assertEqual(parse_roman_numeral("III"), 3)


if __name__ == '__main__':
    unittest.main()
