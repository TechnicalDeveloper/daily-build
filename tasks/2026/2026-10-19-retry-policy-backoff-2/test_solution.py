import unittest
from unittest.mock import patch
from solution import retry

class TestRetry(unittest.TestCase):
    def test_success_on_first_call(self):
        @retry(max_retries=3, base_delay=0.1)
        def always_succeed():
            return "ok"
        self.assertEqual(always_succeed(), "ok")

    def test_success_after_retries(self):
        call_count = [0]
        @retry(max_retries=3, base_delay=0.01)
        def fail_twice_then_succeed():
            call_count[0] += 1
            if call_count[0] < 3:
                raise ValueError("fail")
            return "success"
        with patch('solution.time.sleep') as mock_sleep:
            result = fail_twice_then_succeed()
        self.assertEqual(result, "success")
        self.assertEqual(call_count[0], 3)

    def test_failure_after_max_retries(self):
        @retry(max_retries=2, base_delay=0.01)
        def always_fail():
            raise RuntimeError("always fail")
        with patch('solution.time.sleep') as mock_sleep:
            with self.assertRaises(RuntimeError):
                always_fail()

    def test_non_retryable_exception(self):
        @retry(max_retries=3, base_delay=0.01, exceptions=(ValueError,))
        def raise_type_error():
            raise TypeError("not retryable")
        with self.assertRaises(TypeError):
            raise_type_error()

    def test_no_retry_with_max_retries_zero(self):
        call_count = [0]
        @retry(max_retries=0, base_delay=0.01)
        def fails_once():
            call_count[0] += 1
            raise ValueError("fail")
        with self.assertRaises(ValueError):
            fails_once()
        self.assertEqual(call_count[0], 1)

if __name__ == '__main__':
    unittest.main()
