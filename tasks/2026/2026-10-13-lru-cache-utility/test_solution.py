import unittest
from solution import lru_cache

class TestLRUCache(unittest.TestCase):

    def test_basic_caching(self):
        call_count = 0

        @lru_cache(maxsize=5)
        def add(a, b):
            nonlocal call_count
            call_count += 1
            return a + b

        self.assertEqual(add(1, 2), 3)
        self.assertEqual(call_count, 1)
        self.assertEqual(add(1, 2), 3)   # cached
        self.assertEqual(call_count, 1)

    def test_maxsize_eviction(self):
        call_count = 0

        @lru_cache(maxsize=2)
        def square(x):
            nonlocal call_count
            call_count += 1
            return x * x

        square(1)   # miss, count=1
        square(2)   # miss, count=2
        square(3)   # miss, count=3, evicts key 1
        self.assertEqual(call_count, 3)
        # 1 was evicted, so we recompute
        square(1)   # miss, count=4
        self.assertEqual(call_count, 4)
        # 2 is still in cache (most recent order: 3,1 after above call? Actually after square(1) it becomes most recent, so order is 3 then 1)
        square(3)   # hit, count still 4
        self.assertEqual(call_count, 4)

    def test_cache_info(self):
        @lru_cache(maxsize=3)
        def mul(a, b):
            return a * b

        info = mul.cache_info()
        self.assertEqual(info['hits'], 0)
        self.assertEqual(info['misses'], 0)
        self.assertEqual(info['currsize'], 0)
        self.assertEqual(info['maxsize'], 3)

        mul(2, 3)   # miss
        mul(2, 3)   # hit
        mul(4, 5)   # miss
        info = mul.cache_info()
        self.assertEqual(info['hits'], 1)
        self.assertEqual(info['misses'], 2)
        self.assertEqual(info['currsize'], 2)

    def test_cache_clear(self):
        @lru_cache(maxsize=3)
        def inc(x):
            return x + 1

        inc(1)
        inc(2)
        inc(1)   # hit
        self.assertEqual(inc.cache_info()['hits'], 1)
        inc.cache_clear()
        info = inc.cache_info()
        self.assertEqual(info['hits'], 0)
        self.assertEqual(info['misses'], 0)
        self.assertEqual(info['currsize'], 0)

    def test_no_args(self):
        call_count = 0

        @lru_cache(maxsize=2)
        def const():
            nonlocal call_count
            call_count += 1
            return 42

        self.assertEqual(const(), 42)
        self.assertEqual(call_count, 1)
        self.assertEqual(const(), 42)   # cached
        self.assertEqual(call_count, 1)

    def test_maxsize_zero(self):
        call_count = 0

        @lru_cache(maxsize=0)
        def double(x):
            nonlocal call_count
            call_count += 1
            return x * 2

        self.assertEqual(double(5), 10)
        self.assertEqual(call_count, 1)
        self.assertEqual(double(5), 10)
        self.assertEqual(call_count, 2)   # no caching
        self.assertEqual(double.cache_info()['hits'], 0)

    def test_maxsize_none(self):
        call_count = 0

        @lru_cache(maxsize=None)
        def identity(x):
            nonlocal call_count
            call_count += 1
            return x

        for i in range(100):
            identity(i)
        self.assertEqual(call_count, 100)
        # All calls now cached
        for i in range(100):
            identity(i)
        self.assertEqual(call_count, 100)
        self.assertEqual(identity.cache_info()['currsize'], 100)
        self.assertEqual(identity.cache_info()['hits'], 100)

if __name__ == '__main__':
    unittest.main()
