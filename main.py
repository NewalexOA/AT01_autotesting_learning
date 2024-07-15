import unittest


def calculate_remainder(dividend, divisor):
    if divisor == 0:
        raise ValueError("Деление на ноль невозможно.")
    return dividend % divisor


class TestCalculateRemainder(unittest.TestCase):
    def test_remainder_positive_numbers(self):
        self.assertEqual(calculate_remainder(10, 3), 1)

    def test_remainder_negative_numbers(self):
        self.assertEqual(calculate_remainder(-10, 3), 2)

    def test_remainder_zero_dividend(self):
        self.assertEqual(calculate_remainder(0, 3), 0)

    def test_remainder_divisor_greater_than_dividend(self):
        self.assertEqual(calculate_remainder(3, 10), 3)

    def test_division_by_zero(self):
        with self.assertRaises(ValueError):
            calculate_remainder(10, 0)


if __name__ == '__main__':
    unittest.main()
