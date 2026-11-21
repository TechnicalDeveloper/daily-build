import unittest
from solution import format_duration

class TestDurationFormatter(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(format_duration(0), "now")

    def test_single_second(self):
        self.assertEqual(format_duration(1), "1 second")

    def test_single_minute(self):
        self.assertEqual(format_duration(60), "1 minute")

    def test_multiple_units(self):
        self.assertEqual(format_duration(62), "1 minute and 2 seconds")

    def test_pluralization(self):
        self.assertEqual(format_duration(120), "2 minutes")
        self.assertEqual(format_duration(3600), "1 hour")

    def test_negative(self):
        self.assertEqual(format_duration(-3662), "1 hour, 1 minute and 2 seconds")

    def test_large(self):
        self.assertEqual(format_duration(31536000 + 86400 + 3600 + 60 + 1), "1 year, 1 day, 1 hour, 1 minute and 1 second")

if __name__ == '__main__':
    unittest.main()
