from collections import OrderedDict
import time

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.expiry = {}

    def _is_expired(self, key):
        return time.time() > self.expiry.get(key, 0)

    def get(self, key):
        if key not in self.cache:
            return -1
        if self._is_expired(key):
            del self.cache[key]
            del self.expiry[key]
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key, value, ttl: int):
        # Remove any existing key (expired or not) to reset order and expiry
        if key in self.cache:
            del self.cache[key]
            del self.expiry[key]
        # Evict least recently used if at capacity
        while len(self.cache) >= self.capacity:
            oldest_key, _ = self.cache.popitem(last=False)
            del self.expiry[oldest_key]
        self.cache[key] = value
        self.expiry[key] = time.time() + ttl
        self.cache.move_to_end(key)
