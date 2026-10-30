import unittest

from solution import RateLimiter


class TestRateLimiter(unittest.TestCase):
    def test_allows_up_to_limit(self):
        limiter = RateLimiter(2, 10)
        self.assertTrue(limiter.allow(0))
        self.assertTrue(limiter.allow(1))
        self.assertFalse(limiter.allow(2))

    def test_window_slides(self):
        limiter = RateLimiter(2, 10)
        self.assertTrue(limiter.allow(0))
        self.assertTrue(limiter.allow(5))
        self.assertFalse(limiter.allow(9))
        self.assertTrue(limiter.allow(10))
        self.assertFalse(limiter.allow(10.5))
        self.assertTrue(limiter.allow(15))

    def test_boundary_exact_window(self):
        limiter = RateLimiter(1, 5)
        self.assertTrue(limiter.allow(0))
        self.assertFalse(limiter.allow(4.999))
        self.assertTrue(limiter.allow(5))

    def test_zero_limit(self):
        limiter = RateLimiter(0, 10)
        self.assertFalse(limiter.allow(0))
        self.assertFalse(limiter.allow(100))

    def test_same_timestamp_counts_separately(self):
        limiter = RateLimiter(2, 10)
        self.assertTrue(limiter.allow(5))
        self.assertTrue(limiter.allow(5))
        self.assertFalse(limiter.allow(5))

    def test_invalid_arguments(self):
        with self.assertRaises(ValueError):
            RateLimiter(-1, 10)
        with self.assertRaises(ValueError):
            RateLimiter(1, 0)


if __name__ == "__main__":
    unittest.main()
