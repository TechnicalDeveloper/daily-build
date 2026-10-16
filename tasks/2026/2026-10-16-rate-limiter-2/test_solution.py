import unittest
from unittest.mock import patch

from solution import RateLimiter


class TestRateLimiter(unittest.TestCase):
    def test_allows_initial_calls(self):
        limiter = RateLimiter(3, 1.0)
        with patch("solution.time.monotonic", side_effect=[0.0, 0.1, 0.2]):
            self.assertTrue(limiter.allow())
            self.assertTrue(limiter.allow())
            self.assertTrue(limiter.allow())

    def test_denies_over_max_calls(self):
        limiter = RateLimiter(2, 1.0)
        with patch("solution.time.monotonic", side_effect=[0.0, 0.0, 0.0]):
            self.assertTrue(limiter.allow())
            self.assertTrue(limiter.allow())
            self.assertFalse(limiter.allow())

    def test_refills_after_period(self):
        limiter = RateLimiter(2, 1.0)
        with patch("solution.time.monotonic", side_effect=[0.0, 0.5, 1.0, 1.1]):
            self.assertTrue(limiter.allow())
            self.assertTrue(limiter.allow())
            self.assertTrue(limiter.allow())
            self.assertFalse(limiter.allow())

    def test_sliding_window_edge(self):
        limiter = RateLimiter(1, 1.0)
        with patch("solution.time.monotonic", side_effect=[0.0, 0.99, 1.0, 1.01]):
            self.assertTrue(limiter.allow())
            self.assertFalse(limiter.allow())
            self.assertTrue(limiter.allow())
            self.assertFalse(limiter.allow())

    def test_invalid_arguments_raise(self):
        with self.assertRaises(ValueError):
            RateLimiter(0, 1.0)
        with self.assertRaises(ValueError):
            RateLimiter(1, 0)


if __name__ == "__main__":
    unittest.main()
