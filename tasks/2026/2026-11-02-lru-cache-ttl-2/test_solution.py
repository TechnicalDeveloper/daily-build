import unittest
import time
from solution import LRUCache

class TestLRUCache(unittest.TestCase):
    def test_basic_get_put(self):
        cache = LRUCache(2, default_ttl=10)
        cache.put('a', 1)
        cache.put('b', 2)
        self.assertEqual(cache.get('a'), 1)
        self.assertEqual(cache.get('b'), 2)
        self.assertIsNone(cache.get('c'))

    def test_lru_eviction(self):
        cache = LRUCache(2, default_ttl=None)
        cache.put('a', 1)
        cache.put('b', 2)
        cache.get('a')  # a becomes most recent
        cache.put('c', 3)  # should evict 'b'
        self.assertIsNone(cache.get('b'))
        self.assertEqual(cache.get('a'), 1)
        self.assertEqual(cache.get('c'), 3)

    def test_ttl_expiry(self):
        cache = LRUCache(2, default_ttl=0.1)
        cache.put('x', 100)
        cache.put('y', 200)
        self.assertEqual(cache.get('x'), 100)
        time.sleep(0.15)
        self.assertIsNone(cache.get('x'))
        self.assertIsNone(cache.get('y'))

    def test_put_updates_ttl(self):
        cache = LRUCache(2, default_ttl=0.1)
        cache.put('k', 10)
        time.sleep(0.05)
        cache.put('k', 20)  # reset TTL
        time.sleep(0.08)  # within original expiry but past if not updated
        self.assertEqual(cache.get('k'), 20)

    def test_capacity_with_expired_items(self):
        cache = LRUCache(2, default_ttl=0.1)
        cache.put('a', 1)
        time.sleep(0.15)
        cache.put('b', 2)  # 'a' is expired but still present
        # Now cache has 'a'(expired) and 'b'. Next put should evict expired 'a' not LRU.
        cache.put('c', 3)
        self.assertIsNone(cache.get('a'))  # already removed
        self.assertEqual(cache.get('b'), 2)
        self.assertEqual(cache.get('c'), 3)

    def test_no_ttl_no_expiry(self):
        cache = LRUCache(2, default_ttl=None)
        cache.put('p', 1)
        cache.put('q', 2)
        time.sleep(0.1)
        self.assertEqual(cache.get('p'), 1)

if __name__ == '__main__':
    unittest.main()
