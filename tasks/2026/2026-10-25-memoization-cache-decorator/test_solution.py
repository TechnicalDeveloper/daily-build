import unittest
from solution import memoize

class TestMemoize(unittest.TestCase):
    def test_basic_memoization(self):
        call_count = 0
        @memoize(maxsize=100)
        def add(a, b):
            nonlocal call_count
            call_count += 1
            return a + b
        self.assertEqual(add(1,2), 3)
        self.assertEqual(call_count, 1)
        self.assertEqual(add(1,2), 3)
        self.assertEqual(call_count, 1)
        self.assertEqual(add(2,3), 5)
        self.assertEqual(call_count, 2)

    def test_different_args(self):
        @memoize(maxsize=100)
        def mul(x, y):
            return x*y
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(3,2),6)
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(3,2),6)

    def test_cache_eviction(self):
        call_count = 0
        @memoize(maxsize=3)
        def f(x):
            nonlocal call_count
            call_count += 1
            return x
        f(1); f(2); f(3)
        self.assertEqual(call_count, 3)
        f(4)
        self.assertEqual(call_count, 4)
        f(1)
        self.assertEqual(call_count, 5)
        f(2)
        self.assertEqual(call_count, 6)

    def test_exception_not_cached(self):
        call_count = 0
        @memoize(maxsize=100)
        def div(a, b):
            nonlocal call_count
            call_count += 1
            return a / b
        with self.assertRaises(ZeroDivisionError):
            div(1,0)
        self.assertEqual(call_count, 1)
        with self.assertRaises(ZeroDivisionError):
            div(1,0)
        self.assertEqual(call_count, 2)

    def test_default_arguments(self):
        call_count = 0
        @memoize(maxsize=100)
        def power(base, exp=2):
            nonlocal call_count
            call_count += 1
            return base ** exp
        self.assertEqual(power(3), 9)
        self.assertEqual(call_count, 1)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(call_count, 1)
        self.assertEqual(power(3, 3), 27)
        self.assertEqual(call_count, 2)

if __name__ == '__main__':
    unittest.main()
