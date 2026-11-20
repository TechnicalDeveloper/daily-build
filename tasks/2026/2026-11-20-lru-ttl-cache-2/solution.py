import time
from collections import OrderedDict


class LRUTTLCache:
    def __init__(self, capacity: int, default_ttl: float = None):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.default_ttl = default_ttl
        self.cache = OrderedDict()  # key -> (value, expiration)

    def _is_expired(self, key):
        """Return True if key is absent or expired."""
        if key not in self.cache:
            return True
        _, exp = self.cache[key]
        if exp is None:
            return False
        return time.time() > exp

    def _remove_expired(self):
        """Delete all expired entries from the cache."""
        for key in list(self.cache.keys()):
            if self._is_expired(key):
                del self.cache[key]

    def get(self, key):
        if self._is_expired(key):
            # remove the key if it exists but is expired
            if key in self.cache:
                del self.cache[key]
            return None
        value, _ = self.cache[key]
        # mark as most recently used
        self.cache.move_to_end(key)
        return value

    def put(self, key, value, ttl: float = None):
        if ttl is None:
            ttl = self.default_ttl
        if ttl is None:
            expiration = None
        else:
            expiration = time.time() + ttl

        if key in self.cache:
            # update existing key
            self.cache[key] = (value, expiration)
            self.cache.move_to_end(key)
        else:
            # new key
            if len(self.cache) >= self.capacity:
                # free space: evict expired first, then LRU if needed
                self._remove_expired()
                if len(self.cache) >= self.capacity:
                    self.cache.popitem(last=False)  # remove oldest (LRU)
            self.cache[key] = (value, expiration)
