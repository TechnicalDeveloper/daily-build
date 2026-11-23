import unittest
from unittest.mock import call, patch

from solution import retry


class RetryPolicyTests(unittest.TestCase):

    @patch("time.sleep")
    def test_success_on_first_attempt_does_not_retry_or_sleep(self, mock_sleep):
        calls = 0

        @retry(max_attempts=3, base_delay=0.1)
        def do_work():
            nonlocal calls
            calls += 1
            return "done"

        self.assertEqual(do_work(), "done")
        self.assertEqual(calls, 1)
        mock_sleep.assert_not_called()

    @patch("time.sleep")
    def test_retries_then_succeeds_with_backoff(self, mock_sleep):
        calls = 0

        @retry(max_attempts=3, base_delay=0.01, backoff_factor=2)
        def flaky():
            nonlocal calls
            calls += 1
            if calls < 3:
                raise ValueError("not yet")
            return "ok"

        self.assertEqual(flaky(), "ok")
        self.assertEqual(calls, 3)
        self.assertEqual(
            mock_sleep.call_args_list,
            [call(0.01), call(0.02)],
        )

    @patch("time.sleep")
    def test_raises_last_exception_after_final_attempt(self, mock_sleep):
        calls = 0

        @retry(max_attempts=3, base_delay=0.01)
        def always_fails():
            nonlocal calls
            calls += 1
            raise RuntimeError("boom")

        with self.assertRaisesRegex(RuntimeError, "boom"):
            always_fails()
        self.assertEqual(calls, 3)
        self.assertEqual(mock_sleep.call_count, 2)

    @patch("time.sleep")
    def test_non_matching_exception_is_not_retried(self, mock_sleep):
        calls = 0

        @retry(max_attempts=5, exceptions=(ValueError,))
        def raises_type_error():
            nonlocal calls
            calls += 1
            raise TypeError("bad type")

        with self.assertRaises(TypeError):
            raises_type_error()
        self.assertEqual(calls, 1)
        mock_sleep.assert_not_called()

    def test_invalid_max_attempts_raises_value_error(self):
        with self.assertRaises(ValueError):
            retry(max_attempts=0)


if __name__ == "__main__":
    unittest.main()
