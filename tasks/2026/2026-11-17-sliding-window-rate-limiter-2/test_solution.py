import unittest
from solution import RateLimiter

class FakeClock:
    def __init__(self, start=0.0):
        self.time = start
    def __call__(self):
        return self.time
    def advance(self, delta):
        self.time += delta

class TestRateLimiter(unittest.TestCase):
    def test_allows_within_limit(self):
        clock = FakeClock()
        limiter = RateLimiter(3, 10, clock=clock)
        for _ in range(3):
            self.assertTrue(limiter.allow())
        self.assertFalse(limiter.allow())

    def test_window_slides(self):
        clock = FakeClock()
        limiter = RateLimiter(2, 5, clock=clock)
        self.assertTrue(limiter.allow())
        clock.advance(4.9)
        self.assertTrue(limiter.allow())
        self.assertFalse(limiter.allow())
        clock.advance(0.2)  # now 5.1, first event expired
        self.assertTrue(limiter.allow())

    def test_boundary_expiration(self):
        clock = FakeClock()
        limiter = RateLimiter(1, 5, clock=clock)
        self.assertTrue(limiter.allow())
        # exactly 5 seconds later, the event is expired
        clock.advance(5.0)
        self.assertTrue(limiter.allow())

    def test_max_events_zero(self):
        clock = FakeClock()
        limiter = RateLimiter(0, 10, clock=clock)
        self.assertFalse(limiter.allow())

    def test_validation(self):
        with self.assertRaises(ValueError):
            RateLimiter(-1, 10)
        with self.assertRaises(ValueError):
            RateLimiter(1, 0)
        with self.assertRaises(ValueError):
            RateLimiter(1, -5)

if __name__ == '__main__':
    unittest.main()
