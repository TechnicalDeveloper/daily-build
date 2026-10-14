import unittest
import time
from solution import debounce

class TestDebounce(unittest.TestCase):
    def test_single_call(self):
        calls = []
        def f(x):
            calls.append(x)
        d = debounce(f, 0.1)
        d(1)
        time.sleep(0.2)
        self.assertEqual(calls, [1])

    def test_multiple_calls_reset(self):
        calls = []
        def f(x):
            calls.append(x)
        d = debounce(f, 0.1)
        d(1)
        d(2)
        d(3)
        time.sleep(0.2)
        self.assertEqual(calls, [3])

    def test_call_after_timeout(self):
        calls = []
        def f(x):
            calls.append(x)
        d = debounce(f, 0.1)
        d(1)
        time.sleep(0.2)
        d(2)
        time.sleep(0.2)
        self.assertEqual(calls, [1, 2])

    def test_no_args(self):
        calls = []
        def f():
            calls.append('called')
        d = debounce(f, 0.1)
        d()
        time.sleep(0.2)
        self.assertEqual(calls, ['called'])

    def test_call_with_kwargs(self):
        calls = []
        def f(**kwargs):
            calls.append(kwargs)
        d = debounce(f, 0.1)
        d(a=1, b=2)
        time.sleep(0.2)
        self.assertEqual(calls, [{'a': 1, 'b': 2}])

if __name__ == '__main__':
    unittest.main()
