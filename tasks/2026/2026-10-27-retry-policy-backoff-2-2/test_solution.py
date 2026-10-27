import unittest
from unittest.mock import patch, MagicMock
from solution import retry

class TestRetryPolicy(unittest.TestCase):

    def test_success_no_retry(self):
        """Function succeeds on first call."""
        mock_func = MagicMock(return_value=42)
        decorated = retry(max_retries=3)(mock_func)
        result = decorated()
        self.assertEqual(result, 42)
        self.assertEqual(mock_func.call_count, 1)

    def test_retry_then_success(self):
        """Function fails twice then succeeds."""
        mock_func = MagicMock(side_effect=[ValueError, ValueError, 99])
        with patch('solution.time.sleep') as mock_sleep:
            decorated = retry(max_retries=3, base_delay=1)(mock_func)
            result = decorated()
            self.assertEqual(result, 99)
            self.assertEqual(mock_func.call_count, 3)
            # Verify delays: attempt 1 (first failure) delay=1, attempt 2 delay=2
            self.assertEqual(mock_sleep.call_args_list[0][0][0], 1)
            self.assertEqual(mock_sleep.call_args_list[1][0][0], 2)

    def test_max_retries_exceeded(self):
        """Function fails on all attempts, raises last exception."""
        mock_func = MagicMock(side_effect=ValueError("persistent error"))
        with patch('solution.time.sleep') as mock_sleep:
            decorated = retry(max_retries=2, base_delay=0.5)(mock_func)
            with self.assertRaises(ValueError) as cm:
                decorated()
            self.assertEqual(str(cm.exception), "persistent error")
            self.assertEqual(mock_func.call_count, 3)  # initial + 2 retries

    def test_non_retryable_exception_propagates_immediately(self):
        """Exception not in retry list should not be caught."""
        mock_func = MagicMock(side_effect=TypeError("type error"))
        with patch('solution.time.sleep') as mock_sleep:
            # only retry on ValueError
            decorated = retry(max_retries=3, exceptions=(ValueError,))(mock_func)
            with self.assertRaises(TypeError):
                decorated()
            self.assertEqual(mock_func.call_count, 1)
            mock_sleep.assert_not_called()

    def test_max_retries_zero(self):
        """With max_retries=0, function is called once and exception is raised."""
        mock_func = MagicMock(side_effect=RuntimeError("fail"))
        with patch('solution.time.sleep') as mock_sleep:
            decorated = retry(max_retries=0)(mock_func)
            with self.assertRaises(RuntimeError):
                decorated()
            self.assertEqual(mock_func.call_count, 1)
            mock_sleep.assert_not_called()

if __name__ == '__main__':
    unittest.main()
