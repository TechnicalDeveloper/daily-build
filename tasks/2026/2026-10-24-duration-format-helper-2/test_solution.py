import unittest
from solution import format_duration

class TestFormatDuration(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(format_duration(0), '0 seconds')
    def test_singular(self):
        self.assertEqual(format_duration(1), '1 second')
        self.assertEqual(format_duration(60), '1 minute')
        self.assertEqual(format_duration(3600), '1 hour')
        self.assertEqual(format_duration(86400), '1 day')
    def test_plural(self):
        self.assertEqual(format_duration(2), '2 seconds')
        self.assertEqual(format_duration(120), '2 minutes')
        self.assertEqual(format_duration(7200), '2 hours')
        self.assertEqual(format_duration(172800), '2 days')
    def test_combination(self):
        # 1 day, 2 hours, 3 minutes, 4 seconds
        seconds = 86400 + 7200 + 180 + 4
        self.assertEqual(format_duration(seconds), '1 day, 2 hours, 3 minutes and 4 seconds')
    def test_no_seconds(self):
        # 1 hour exactly
        self.assertEqual(format_duration(3600), '1 hour')
    def test_mixed_singular_plural(self):
        # 1 day and 1 second
        self.assertEqual(format_duration(86401), '1 day and 1 second')
        # 1 hour and 1 minute
        self.assertEqual(format_duration(3660), '1 hour and 1 minute')
        # 2 days and 1 hour
        self.assertEqual(format_duration(172800 + 3600), '2 days and 1 hour')

if __name__ == '__main__':
    unittest.main()
