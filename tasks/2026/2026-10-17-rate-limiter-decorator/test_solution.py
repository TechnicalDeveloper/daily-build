import unittest
from unittest.mock import patch
from solution import rate_limiter

class TestRateLimiter(unittest.TestCase):

    def test_allows_calls_within_limit(self):
        @rate_limiter(max_calls=3, time_window=10)
        def foo():
            return "ok"
        for _ in range(3):
            self.assertEqual(foo(), "ok")

    def test_raises_when_exceeded(self):
        @rate_limiter(max_calls=2, time_window=10)
        def bar():
            return "ok"
        bar()
        bar()
        with self.assertRaises(RuntimeError):
            bar()

    def test_resets_after_window(self):
        mock_time = [100.0]
        def fake_monotonic():
            return mock_time[0]
        with patch('solution.time.monotonic', side_effect=fake_monotonic):
            @rate_limiter(max_calls=1, time_window=5)
            def baz():
                return "ok"
            self.assertEqual(baz(), "ok")
            # Advance time but stay within window
            mock_time[0] = 104.0
            with self.assertRaises(RuntimeError):
                baz()
            # Advance beyond window
            mock_time[0] = 106.0
            self.assertEqual(baz(), "ok")

    def test_multiple_functions_independent(self):
        @rate_limiter(max_calls=2, time_window=10)
        def f1():
            return "f1"
        @rate_limiter(max_calls=1, time_window=10)
        def f2():
            return "f2"
        self.assertEqual(f1(), "f1")
        self.assertEqual(f1(), "f1")
        self.assertEqual(f2(), "f2")  # f2 first call succeeds
        with self.assertRaises(RuntimeError):
            f1()  # f1 exceeded (2 calls already)
        with self.assertRaises(RuntimeError):
            f2()  # f2 exceeded (1 call already)

if __name__ == '__main__':
    unittest.main()
