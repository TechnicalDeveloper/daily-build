import unittest
import time
from solution import debounce

class TestDebounce(unittest.TestCase):
    def test_calls_after_wait(self):
        calls = []
        def record(x):
            calls.append(x)
        debounced = debounce(0.1)(record)
        debounced(1)
        debounced(2)
        debounced(3)
        time.sleep(0.2)
        self.assertEqual(calls, [3])

    def test_cancel(self):
        calls = []
        def record(x):
            calls.append(x)
        debounced = debounce(0.1)(record)
        debounced(1)
        debounced.cancel()
        time.sleep(0.2)
        self.assertEqual(calls, [])

    def test_with_kwargs(self):
        calls = []
        def record(**kw):
            calls.append(kw)
        debounced = debounce(0.1)(record)
        debounced(x=1)
        debounced(x=2)
        time.sleep(0.2)
        self.assertEqual(calls, [{'x': 2}])

    def test_multiple_debounce_instances(self):
        calls_a = []
        calls_b = []
        def record_a(x):
            calls_a.append(x)
        def record_b(x):
            calls_b.append(x)
        debounced_a = debounce(0.1)(record_a)
        debounced_b = debounce(0.1)(record_b)
        debounced_a(1)
        debounced_b(2)
        time.sleep(0.2)
        self.assertEqual(calls_a, [1])
        self.assertEqual(calls_b, [2])

    def test_reset_after_cancel(self):
        calls = []
        def record(x):
            calls.append(x)
        debounced = debounce(0.1)(record)
        debounced(1)
        debounced.cancel()
        debounced(2)
        time.sleep(0.2)
        self.assertEqual(calls, [2])

if __name__ == '__main__':
    unittest.main()
