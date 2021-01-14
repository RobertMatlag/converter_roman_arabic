import unittest
from parser import parse_roman_numeral


class RomanNumeralsTest(unittest.TestCase):
    def test_small_numbers(self):
        self.assertEqual(parse_roman_numeral("I"), 1)
        self.assertEqual(parse_roman_numeral("II"), 2)
        self.assertEqual(parse_roman_numeral("III"), 3)

    def test_middle_numbers(self):
        self.assertEqual(parse_roman_numeral("IV"), 4)
        self.assertEqual(parse_roman_numeral("V"), 5)
        self.assertEqual(parse_roman_numeral("VI"), 6)
        self.assertEqual(parse_roman_numeral("VIII"), 8)
        self.assertEqual(parse_roman_numeral("IX"), 9)
        self.assertEqual(parse_roman_numeral("X"), 10)
        self.assertEqual(parse_roman_numeral("XLVII"), 47)
        self.assertEqual(parse_roman_numeral("LXXXIX"), 89)


if __name__ == '__main__':
    unittest.main()
