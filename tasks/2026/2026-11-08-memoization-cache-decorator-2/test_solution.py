from solution import memoize
import unittest

class TestMemoize(unittest.TestCase):
    def test_single_argument_caches(self):
        call_count = 0
        @memoize
        def double(x):
            nonlocal call_count
            call_count += 1
            return x * 2
        self.assertEqual(double(5), 10)
        self.assertEqual(double(5), 10)
        self.assertEqual(call_count, 1)

    def test_multiple_arguments(self):
        call_count = 0
        @memoize
        def add(a, b):
            nonlocal call_count
            call_count += 1
            return a + b
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(call_count, 2)

    def test_no_arguments(self):
        call_count = 0
        @memoize
        def constant():
            nonlocal call_count
            call_count += 1
            return 42
        self.assertEqual(constant(), 42)
        self.assertEqual(constant(), 42)
        self.assertEqual(call_count, 1)

    def test_cache_attribute_exists(self):
        @memoize
        def square(x):
            return x * x
        square(3)
        self.assertTrue(hasattr(square, 'cache'))
        self.assertIsInstance(square.cache, dict)
        self.assertIn((3,), square.cache)
        self.assertEqual(square.cache[(3,)], 9)

    def test_unhashable_arguments_raise_typeerror(self):
        @memoize
        def identity(x):
            return x
        with self.assertRaises(TypeError):
            identity([1, 2, 3])

if __name__ == '__main__':
    unittest.main()
