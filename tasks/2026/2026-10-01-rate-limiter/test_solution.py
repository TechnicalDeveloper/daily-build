import unittest
from solution import RateLimiter
from unittest.mock import patch

class TestRateLimiter(unittest.TestCase):
    def test_basic_allowed_denied(self):
        """Allow up to max_requests, then deny."""
        with patch('solution.time.time', side_effect=[0.0, 0.2, 0.4, 0.6, 1.0]) as mock_time:
            lim = RateLimiter(3, 1.0)
            self.assertTrue(lim.allow_request())   # time 0.0
            self.assertTrue(lim.allow_request())   # 0.2
            self.assertTrue(lim.allow_request())   # 0.4
            self.assertFalse(lim.allow_request())  # 0.6 – still 3 inside window
            # At time 1.0 the first timestamp (0.0) expires exactly
            self.assertTrue(lim.allow_request())   # 1.0 – now only 2 inside window

    def test_window_expiry(self):
        """Old requests expire and free up capacity."""
        with patch('solution.time.time', side_effect=[0.0, 0.6, 0.7, 1.0]) as mock_time:
            lim = RateLimiter(2, 1.0)
            self.assertTrue(lim.allow_request())   # 0.0
            self.assertTrue(lim.allow_request())   # 0.6
            self.assertFalse(lim.allow_request())  # 0.7 – two still inside window
            # At time 1.0 cutoff=0.0, the 0.0 timestamp expires
            self.assertTrue(lim.allow_request())   # 1.0 – only 0.6 remains

    def test_zero_max_requests(self):
        """Zero max_requests always deny."""
        lim = RateLimiter(0, 10.0)
        self.assertFalse(lim.allow_request())
        self.assertFalse(lim.allow_request())

    def test_negative_window(self):
        """Negative window always deny."""
        lim = RateLimiter(5, -1.0)
        self.assertFalse(lim.allow_request())
        self.assertFalse(lim.allow_request())

    def test_large_window(self):
        """Many requests allowed within a large window."""
        with patch('solution.time.time', side_effect=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5]) as mock_time:
            lim = RateLimiter(5, 100.0)
            for _ in range(5):
                self.assertTrue(lim.allow_request())
            self.assertFalse(lim.allow_request())

    def test_window_reset_clear(self):
        """After the window fully clears, a request is allowed."""
        with patch('solution.time.time', side_effect=[0.0, 1.0, 1.0]) as mock_time:
            lim = RateLimiter(1, 1.0)
            self.assertTrue(lim.allow_request())
            # At time 1.0, the 0.0 timestamp is expired (0.0 <= 0.0) so removed
            self.assertTrue(lim.allow_request())

if __name__ == '__main__':
    unittest.main()
