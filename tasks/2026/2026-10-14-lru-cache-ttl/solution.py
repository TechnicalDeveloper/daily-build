from collections import OrderedDict
import time

class LRUCacheWithTTL:
    def __init__(self, capacity: int, default_ttl: int):
        self.capacity = capacity
        self.default_ttl = default_ttl
        self.cache = OrderedDict()  # key -> (value, expiry_time)

    def get(self, key):
        if key not in self.cache:
            return -1
        value, expiry = self.cache[key]
        if time.time() > expiry:
            del self.cache[key]
            return -1
        self.cache.move_to_end(key)
        return value

    def put(self, key, value, ttl=None):
        if ttl is None:
            ttl = self.default_ttl
        expiry = time.time() + ttl
        if key in self.cache:
            self.cache[key] = (value, expiry)
            self.cache.move_to_end(key)
            return
        if len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)
        self.cache[key] = (value, expiry)
