import unittest
from solution import memoize

class TestMemoize(unittest.TestCase):
    def test_basic_caching(self):
        call_count = 0
        @memoize
        def add(a, b):
            nonlocal call_count
            call_count += 1
            return a + b
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count, 1)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count, 1)

    def test_different_args(self):
        call_count = 0
        @memoize
        def multiply(a, b):
            nonlocal call_count
            call_count += 1
            return a * b
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(call_count, 1)
        self.assertEqual(multiply(4, 5), 20)
        self.assertEqual(call_count, 2)
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(call_count, 2)

    def test_no_args(self):
        call_count = 0
        @memoize
        def constant():
            nonlocal call_count
            call_count += 1
            return 42
        self.assertEqual(constant(), 42)
        self.assertEqual(call_count, 1)
        self.assertEqual(constant(), 42)
        self.assertEqual(call_count, 1)

    def test_recursive_fibonacci(self):
        call_count = 0
        @memoize
        def fib(n):
            nonlocal call_count
            call_count += 1
            if n < 2:
                return n
            return fib(n-1) + fib(n-2)
        self.assertEqual(fib(10), 55)
        self.assertLess(call_count, 20)
        self.assertEqual(call_count, 11)

    def test_keyword_args(self):
        call_count = 0
        @memoize
        def power(base, exp=2):
            nonlocal call_count
            call_count += 1
            return base ** exp
        self.assertEqual(power(3, exp=2), 9)
        self.assertEqual(call_count, 1)
        self.assertEqual(power(3, exp=2), 9)
        self.assertEqual(call_count, 1)
        self.assertEqual(power(3, exp=3), 27)
        self.assertEqual(call_count, 2)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(call_count, 3)
        self.assertEqual(power(3, 2), 9)
        self.assertEqual(call_count, 3)

if __name__ == '__main__':
    unittest.main()
