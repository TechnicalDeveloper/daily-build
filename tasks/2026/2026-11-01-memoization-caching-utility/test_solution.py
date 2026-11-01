import unittest
from solution import Cache

class TestCache(unittest.TestCase):

    def test_basic_caching(self):
        call_count = 0

        @Cache()
        def add(a, b):
            nonlocal call_count
            call_count += 1
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count, 1)
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count, 1)  # Cached, not re-executed
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(call_count, 2)

    def test_lru_eviction(self):
        call_count = 0

        @Cache(max_size=2)
        def multiply(a, b):
            nonlocal call_count
            call_count += 1
            return a * b

        multiply(1, 2)  # miss, cache size 1
        multiply(3, 4)  # miss, cache size 2
        multiply(1, 2)  # hit, now (1,2) is recently used
        multiply(5, 6)  # miss, evict (3,4), cache (1,2) and (5,6)
        multiply(3, 4)  # miss, evict (1,2), cache (5,6) and (3,4)
        self.assertEqual(call_count, 4)

    def test_stats(self):
        call_count = 0

        @Cache()
        def square(x):
            nonlocal call_count
            call_count += 1
            return x * x

        self.assertEqual(square(2), 4)
        self.assertEqual(square(2), 4)
        self.assertEqual(square(3), 9)
        stats = square.stats
        self.assertEqual(stats['hits'], 1)
        self.assertEqual(stats['misses'], 2)
        self.assertEqual(stats['size'], 2)

    def test_clear_cache(self):
        call_count = 0

        @Cache()
        def double(x):
            nonlocal call_count
            call_count += 1
            return x * 2

        double(1)
        double(2)
        self.assertEqual(call_count, 2)
        double.clear()
        double(1)
        self.assertEqual(call_count, 3)  # Re-executed after clear
        self.assertEqual(double.stats['size'], 1)

if __name__ == '__main__':
    unittest.main()
