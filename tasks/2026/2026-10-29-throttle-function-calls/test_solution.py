import unittest
from unittest.mock import patch, MagicMock
from solution import throttle

class TestThrottle(unittest.TestCase):
    def test_first_call_executes_immediately(self):
        func = MagicMock()
        throttled = throttle(func, 1.0)
        with patch('solution.time.time') as mock_time:
            mock_time.return_value = 0.0
            throttled("first")
            func.assert_called_once_with("first")

    def test_second_call_within_interval_ignored(self):
        func = MagicMock()
        throttled = throttle(func, 5.0)
        with patch('solution.time.time') as mock_time:
            mock_time.return_value = 0.0
            throttled("a")
            self.assertEqual(func.call_count, 1)
            mock_time.return_value = 2.0
            throttled("b")
            self.assertEqual(func.call_count, 1)
            func.assert_called_once_with("a")

    def test_call_after_interval_executes(self):
        func = MagicMock()
        throttled = throttle(func, 3.0)
        with patch('solution.time.time') as mock_time:
            mock_time.return_value = 0.0
            throttled("first")
            self.assertEqual(func.call_count, 1)
            mock_time.return_value = 4.0
            throttled("second")
            self.assertEqual(func.call_count, 2)
            func.assert_any_call("first")
            func.assert_any_call("second")

    def test_multiple_functions_independent(self):
        func1 = MagicMock()
        func2 = MagicMock()
        throttled1 = throttle(func1, 2.0)
        throttled2 = throttle(func2, 2.0)
        with patch('solution.time.time') as mock_time:
            mock_time.return_value = 0.0
            throttled1("a")
            throttled2("b")
            self.assertEqual(func1.call_count, 1)
            self.assertEqual(func2.call_count, 1)
            mock_time.return_value = 1.0
            throttled1("c")
            throttled2("d")
            self.assertEqual(func1.call_count, 1)
            self.assertEqual(func2.call_count, 1)
            mock_time.return_value = 2.1
            throttled1("e")
            throttled2("f")
            self.assertEqual(func1.call_count, 2)
            self.assertEqual(func2.call_count, 2)

    def test_keyword_arguments(self):
        func = MagicMock()
        throttled = throttle(func, 0.5)
        with patch('solution.time.time') as mock_time:
            mock_time.return_value = 0.0
            throttled(x=1, y=2)
            func.assert_called_with(x=1, y=2)

if __name__ == '__main__':
    unittest.main()
