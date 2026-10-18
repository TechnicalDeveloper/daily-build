import unittest
from solution import days_in_month

class TestDaysInMonth(unittest.TestCase):

    def test_leap_year_february(self):
        self.assertEqual(days_in_month(2024, 2), 29)
        self.assertEqual(days_in_month(2000, 2), 29)

    def test_non_leap_year_february(self):
        self.assertEqual(days_in_month(2023, 2), 28)
        self.assertEqual(days_in_month(1900, 2), 28)

    def test_constant_month_days(self):
        # Months with 31 days: Jan, Mar, May, Jul, Aug, Oct, Dec
        for m in [1, 3, 5, 7, 8, 10, 12]:
            self.assertEqual(days_in_month(2024, m), 31)
        # Months with 30 days: Apr, Jun, Sep, Nov
        for m in [4, 6, 9, 11]:
            self.assertEqual(days_in_month(2024, m), 30)

    def test_invalid_month_low(self):
        with self.assertRaises(ValueError):
            days_in_month(2024, 0)

    def test_invalid_month_high(self):
        with self.assertRaises(ValueError):
            days_in_month(2024, 13)

    def test_invalid_year_negative(self):
        with self.assertRaises(ValueError):
            days_in_month(-1, 1)

    def test_invalid_year_zero(self):
        with self.assertRaises(ValueError):
            days_in_month(0, 1)

if __name__ == '__main__':
    unittest.main()
