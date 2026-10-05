import unittest
import time
from solution import LRUCache

class TestLRUCache(unittest.TestCase):

    def test_get_missing(self):
        cache = LRUCache(2)
        self.assertEqual(cache.get('x'), -1)

    def test_get_expired(self):
        cache = LRUCache(2)
        cache.put('a', 1, 0.1)  # TTL = 0.1 seconds
        time.sleep(0.15)
        self.assertEqual(cache.get('a'), -1)

    def test_lru_eviction(self):
        cache = LRUCache(2)
        cache.put('a', 1, 100)
        cache.put('b', 2, 100)
        cache.get('a')          # 'a' becomes most recent
        cache.put('c', 3, 100)  # evicts 'b' (least recently used)
        self.assertEqual(cache.get('a'), 1)
        self.assertEqual(cache.get('b'), -1)
        self.assertEqual(cache.get('c'), 3)

    def test_update_resets_ttl(self):
        cache = LRUCache(2)
        cache.put('x', 10, 0.1)
        time.sleep(0.05)
        cache.put('x', 20, 100)  # update before expiry
        time.sleep(0.1)          # original TTL would have expired, but updated TTL still valid
        self.assertEqual(cache.get('x'), 20)

    def test_capacity_one(self):
        cache = LRUCache(1)
        cache.put('a', 1, 100)
        cache.put('b', 2, 100)  # evicts 'a'
        self.assertEqual(cache.get('a'), -1)
        self.assertEqual(cache.get('b'), 2)

if __name__ == '__main__':
    unittest.main()
