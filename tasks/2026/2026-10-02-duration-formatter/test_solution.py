import unittest
from solution import format_duration

class TestFormatDuration(unittest.TestCase):
    def test_zero_seconds(self):
        self.assertEqual(format_duration(0), "now")

    def test_single_second(self):
        self.assertEqual(format_duration(1), "1 second")

    def test_multiple_seconds(self):
        self.assertEqual(format_duration(62), "1 minute, 2 seconds")

    def test_hours_minutes_seconds(self):
        self.assertEqual(format_duration(3661), "1 hour, 1 minute, 1 second")

    def test_days_only(self):
        self.assertEqual(format_duration(172800), "2 days")

    def test_mixed_units(self):
        self.assertEqual(format_duration(90061), "1 day, 1 hour, 1 minute, 1 second")

if __name__ == '__main__':
    unittest.main()
