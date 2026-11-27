import unittest
from solution import retry

class TestRetry(unittest.TestCase):
    def test_retry_success_after_failures(self):
        calls = []
        def flaky_func():
            calls.append(1)
            if len(calls) < 3:
                raise ValueError("temporary error")
            return "ok"
        
        captured = []
        fake_sleep = lambda delay: captured.append(delay)
        
        decorated = retry(max_retries=3, base_delay=0.1, backoff_factor=2, max_delay=10, sleep=fake_sleep)(flaky_func)
        result = decorated()
        self.assertEqual(result, "ok")
        self.assertEqual(len(calls), 3)
        self.assertEqual(captured, [0.1, 0.2])
    
    def test_max_retries_zero_no_retry(self):
        calls = []
        def always_fail():
            calls.append(1)
            raise RuntimeError("fail")
        captured = []
        fake_sleep = lambda delay: captured.append(delay)
        decorated = retry(max_retries=0, sleep=fake_sleep)(always_fail)
        with self.assertRaises(RuntimeError):
            decorated()
        self.assertEqual(len(calls), 1)
        self.assertEqual(captured, [])
    
    def test_exhausts_retries_raises_last_exception(self):
        calls = []
        def always_fail():
            calls.append(1)
            raise ValueError("fail")
        captured = []
        fake_sleep = lambda delay: captured.append(delay)
        decorated = retry(max_retries=2, base_delay=0.1, backoff_factor=2, max_delay=10, sleep=fake_sleep)(always_fail)
        with self.assertRaises(ValueError):
            decorated()
        self.assertEqual(len(calls), 3)
        self.assertEqual(captured, [0.1, 0.2])
    
    def test_custom_exceptions_only(self):
        def raises_type_error():
            raise TypeError("type error")
        captured = []
        fake_sleep = lambda delay: captured.append(delay)
        decorated = retry(max_retries=2, exceptions=ValueError, sleep=fake_sleep)(raises_type_error)
        with self.assertRaises(TypeError):
            decorated()
        self.assertEqual(len(captured), 0)
    
    def test_max_delay_cap(self):
        calls = []
        def always_fail():
            calls.append(1)
            raise Exception("fail")
        captured = []
        fake_sleep = lambda delay: captured.append(delay)
        decorated = retry(max_retries=3, base_delay=1, backoff_factor=2, max_delay=3, sleep=fake_sleep)(always_fail)
        with self.assertRaises(Exception):
            decorated()
        self.assertEqual(captured, [1, 2, 3])
