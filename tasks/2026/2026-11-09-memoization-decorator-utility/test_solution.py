import unittest
import time
from solution import memoize

class TestMemoize(unittest.TestCase):

    def test_basic_caching(self):
        call_count = 0

        @memoize(maxsize=128)
        def add(a, b):
            nonlocal call_count
            call_count += 1
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count, 1)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count, 1)  # Cached
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(call_count, 2)

    def test_lru_eviction(self):
        call_count = 0

        @memoize(maxsize=2)
        def multiply(a, b):
            nonlocal call_count
            call_count += 1
            return a * b

        multiply(1, 2)  # call 1
        multiply(3, 4)  # call 2
        multiply(5, 6)  # call 3, evicts (1,2)
        self.assertEqual(call_count, 3)
        # (1,2) should be evicted, so recalculates
        self.assertEqual(multiply(1, 2), 2)
        self.assertEqual(call_count, 4)

    def test_ttl_expiration(self):
        call_count = 0

        @memoize(maxsize=128, ttl=0.05)  # 50ms TTL
        def square(x):
            nonlocal call_count
            call_count += 1
            return x * x

        self.assertEqual(square(5), 25)
        self.assertEqual(call_count, 1)
        self.assertEqual(square(5), 25)
        self.assertEqual(call_count, 1)  # Cached
        time.sleep(0.06)
        self.assertEqual(square(5), 25)
        self.assertEqual(call_count, 2)  # Expired, recomputed

    def test_maxsize_zero(self):
        call_count = 0

        @memoize(maxsize=0)
        def identity(x):
            nonlocal call_count
            call_count += 1
            return x

        self.assertEqual(identity(10), 10)
        self.assertEqual(call_count, 1)
        self.assertEqual(identity(10), 10)
        self.assertEqual(call_count, 2)  # No caching

    def test_unhashable_arguments(self):
        @memoize(maxsize=128)
        def func(x):
            return x

        with self.assertRaises(TypeError):
            func([1, 2, 3])

    def test_cache_info(self):
        @memoize(maxsize=3)
        def double(x):
            return x * 2

        double(1)  # miss
        double(2)  # miss
        double(1)  # hit
        hits, misses, maxsize, currsize = double.cache_info()
        self.assertEqual(hits, 1)
        self.assertEqual(misses, 2)
        self.assertEqual(maxsize, 3)
        self.assertEqual(currsize, 2)

    def test_cache_clear(self):
        @memoize(maxsize=128)
        def triple(x):
            return x * 3

        triple(4)
        triple(5)
        self.assertEqual(len(triple.cache), 2)
        triple.cache_clear()
        self.assertEqual(len(triple.cache), 0)

if __name__ == '__main__':
    unittest.main()
