import unittest
import time
from solution import LRUTTLCache


class TestLRUTTLCache(unittest.TestCase):
    def test_get_missing_returns_none(self):
        cache = LRUTTLCache(2)
        self.assertIsNone(cache.get("a"))

    def test_lru_eviction_when_capacity_reached(self):
        cache = LRUTTLCache(2)
        cache.put("a", 1)
        cache.put("b", 2)
        cache.get("a")  # make 'a' most recent
        cache.put("c", 3)  # should evict 'b'
        self.assertIsNone(cache.get("b"))
        self.assertEqual(cache.get("a"), 1)
        self.assertEqual(cache.get("c"), 3)

    def test_ttl_expiration(self):
        cache = LRUTTLCache(3)
        cache.put("a", 1, ttl=0.1)
        self.assertEqual(cache.get("a"), 1)
        time.sleep(0.15)
        self.assertIsNone(cache.get("a"))

    def test_put_update_ttl_and_order(self):
        cache = LRUTTLCache(2)
        cache.put("a", 1, ttl=1.0)
        cache.put("b", 2, ttl=0.1)
        cache.put("a", 10, ttl=0.1)  # update 'a', also refresh TTL
        time.sleep(0.12)
        # 'a' should be expired, 'b' also expired, but 'a' was updated and should be expired now
        self.assertIsNone(cache.get("a"))
        # 'b' should be expired as well
        self.assertIsNone(cache.get("b"))
        # now add new key, should trigger cleanup
        cache.put("c", 3)
        self.assertEqual(cache.get("c"), 3)
        self.assertIsNone(cache.get("a"))
        self.assertIsNone(cache.get("b"))

    def test_evict_expired_before_lru(self):
        cache = LRUTTLCache(2)
        cache.put("a", 1, ttl=0.2)
        cache.put("b", 2, ttl=None)  # never expires
        time.sleep(0.25)  # 'a' expires
        cache.put("c", 3)  # should evict expired 'a', keep 'b'
        self.assertEqual(cache.get("b"), 2)
        self.assertEqual(cache.get("c"), 3)
        self.assertIsNone(cache.get("a"))

    def test_default_ttl_used_when_put_without_ttl(self):
        cache = LRUTTLCache(2, default_ttl=0.1)
        cache.put("x", 1)
        self.assertEqual(cache.get("x"), 1)
        time.sleep(0.15)
        self.assertIsNone(cache.get("x"))

    def test_invalid_capacity_raises(self):
        with self.assertRaises(ValueError):
            LRUTTLCache(0)
        with self.assertRaises(ValueError):
            LRUTTLCache(-1)


if __name__ == '__main__':
    unittest.main()
