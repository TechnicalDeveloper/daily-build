import unittest
from unittest.mock import patch
from solution import LRUCacheWithTTL

class TestLRUCacheWithTTL(unittest.TestCase):

    def setUp(self):
        self.time_patcher = patch('time.time', return_value=1000)
        self.mock_time = self.time_patcher.start()

    def tearDown(self):
        self.time_patcher.stop()

    def test_basic_get_put(self):
        cache = LRUCacheWithTTL(2, 10)
        cache.put('a', 1)
        cache.put('b', 2)
        self.assertEqual(cache.get('a'), 1)
        self.assertEqual(cache.get('b'), 2)

    def test_expiry(self):
        cache = LRUCacheWithTTL(2, 10)
        cache.put('a', 1)
        self.assertEqual(cache.get('a'), 1)
        self.mock_time.return_value = 1011  # past TTL
        self.assertEqual(cache.get('a'), -1)

    def test_capacity_eviction(self):
        cache = LRUCacheWithTTL(2, 10)
        cache.put('a', 1)
        cache.put('b', 2)
        cache.put('c', 3)  # should evict 'a' (least recently used)
        self.assertEqual(cache.get('a'), -1)
        self.assertEqual(cache.get('b'), 2)
        self.assertEqual(cache.get('c'), 3)

    def test_update_resets_ttl(self):
        cache = LRUCacheWithTTL(2, 10)
        cache.put('a', 1)
        self.mock_time.return_value = 1005
        cache.put('a', 2, ttl=20)  # new expiry = 1005+20 = 1025
        self.mock_time.return_value = 1015  # old expiry 1010 passed, new expiry 1025 not passed
        self.assertEqual(cache.get('a'), 2)

if __name__ == '__main__':
    unittest.main()
