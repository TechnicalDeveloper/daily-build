import unittest
from unittest.mock import patch
import time
from solution import retry

class TestRetryBackoff(unittest.TestCase):

    def test_success_on_first_attempt(self):
        @retry(max_retries=3)
        def succeed():
            return 42
        self.assertEqual(succeed(), 42)

    def test_retry_then_success(self):
        attempt_counter = [0]
        @retry(max_retries=3, base_delay=0.01)  # small delay for test speed
        def eventually_succeed():
            attempt_counter[0] += 1
            if attempt_counter[0] < 3:
                raise ValueError('not yet')
            return 'success'
        with patch('time.sleep', return_value=None) as mock_sleep:
            result = eventually_succeed()
        self.assertEqual(result, 'success')
        self.assertEqual(attempt_counter[0], 3)
        self.assertEqual(mock_sleep.call_count, 2)  # two delays before final attempt

    def test_retries_exhausted(self):
        @retry(max_retries=2, base_delay=0.01)
        def always_fail():
            raise RuntimeError('fail')
        with self.assertRaises(RuntimeError):
            always_fail()

    def test_custom_exception_only(self):
        @retry(max_retries=2, base_delay=0.01, exceptions=(ValueError,))
        def raise_custom():
            raise KeyError('not caught')
        with self.assertRaises(KeyError):
            raise_custom()

    def test_zero_max_retries(self):
        @retry(max_retries=0)
        def fail():
            raise ValueError('no retry')
        with self.assertRaises(ValueError):
            fail()

    def test_backoff_delay_increases(self):
        delays = []
        def tracking_sleep(delay):
            delays.append(delay)
        @retry(max_retries=3, base_delay=1, backoff_factor=2)
        def fail_twice():
            raise ValueError('retry')
        with patch('time.sleep', side_effect=tracking_sleep):
            try:
                fail_twice()
            except ValueError:
                pass
        self.assertEqual(delays, [1.0, 2.0, 4.0])

if __name__ == '__main__':
    unittest.main()
