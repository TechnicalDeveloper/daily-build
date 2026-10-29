import unittest
from unittest.mock import patch
from solution import retry

class TestRetry(unittest.TestCase):
    def test_success_on_first(self):
        count = 0
        @retry(max_attempts=3)
        def func():
            nonlocal count
            count += 1
            return "success"
        result = func()
        self.assertEqual(result, "success")
        self.assertEqual(count, 1)

    def test_success_on_third(self):
        count = 0
        @retry(max_attempts=3, base_delay=0.01)
        def func():
            nonlocal count
            count += 1
            if count < 3:
                raise ValueError("fail")
            return "success"
        with patch('time.sleep') as mock_sleep:
            result = func()
        self.assertEqual(result, "success")
        self.assertEqual(count, 3)
        self.assertEqual(mock_sleep.call_count, 2)

    def test_always_fails(self):
        count = 0
        @retry(max_attempts=3, base_delay=0.01)
        def func():
            nonlocal count
            count += 1
            raise ValueError("fail")
        with patch('time.sleep') as mock_sleep:
            with self.assertRaises(ValueError):
                func()
        self.assertEqual(count, 3)
        self.assertEqual(mock_sleep.call_count, 2)

    def test_different_exception_not_retried(self):
        count = 0
        @retry(max_attempts=3, base_delay=0.01, exceptions=(ValueError,))
        def func():
            nonlocal count
            count += 1
            raise TypeError("not retried")
        with patch('time.sleep') as mock_sleep:
            with self.assertRaises(TypeError):
                func()
        self.assertEqual(count, 1)
        self.assertEqual(mock_sleep.call_count, 0)

    def test_invalid_max_attempts(self):
        with self.assertRaises(ValueError):
            retry(max_attempts=0)
        with self.assertRaises(ValueError):
            retry(max_attempts=-1)

if __name__ == '__main__':
    unittest.main()
