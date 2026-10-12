from solution import format_duration
import unittest

class TestFormatDuration(unittest.TestCase):

    def test_zero_duration(self):
        self.assertEqual(
            format_duration("2024-01-01T00:00:00", "2024-01-01T00:00:00"),
            "0 minutes"
        )

    def test_one_day(self):
        self.assertEqual(
            format_duration("2024-01-01T00:00:00", "2024-01-02T00:00:00"),
            "1 day"
        )

    def test_mixed_components(self):
        self.assertEqual(
            format_duration("2024-01-01T12:00:00", "2024-01-02T13:30:00"),
            "1 day, 1 hour, 30 minutes"
        )

    def test_singular_plural(self):
        self.assertEqual(
            format_duration("2024-01-01T00:00:00", "2024-01-03T02:02:00"),
            "2 days, 2 hours, 2 minutes"
        )

    def test_negative_end_raises(self):
        with self.assertRaises(ValueError):
            format_duration("2024-01-02T00:00:00", "2024-01-01T00:00:00")

if __name__ == '__main__':
    unittest.main()
