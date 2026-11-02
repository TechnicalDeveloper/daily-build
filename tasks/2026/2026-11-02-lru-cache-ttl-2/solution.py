from collections import OrderedDict
import time
from typing import Optional

class LRUCache:
    def __init__(self, capacity: int, default_ttl: int = None):
        self.capacity = capacity
        self.default_ttl = default_ttl
        self.cache = OrderedDict()  # key -> (value, expiry_time)

    def _is_expired(self, expiry: Optional[float]) -> bool:
        if expiry is None:
            return False
        return time.time() > expiry

    def get(self, key: str) -> Optional[int]:
        if key not in self.cache:
            return None
        value, expiry = self.cache[key]
        if self._is_expired(expiry):
            del self.cache[key]
            return None
        self.cache.move_to_end(key)
        return value

    def put(self, key: str, value: int, ttl: int = None) -> None:
        if ttl is None:
            ttl = self.default_ttl
        expiry = None if ttl is None else time.time() + ttl
        if key in self.cache:
            # Update existing key
            self.cache[key] = (value, expiry)
            self.cache.move_to_end(key)
            return
        # Evict if at capacity (include expired items)
        if len(self.cache) >= self.capacity:
            # Remove first expired entry if any, else LRU
            for k, (_, e) in list(self.cache.items()):
                if self._is_expired(e):
                    del self.cache[k]
                    break
            else:
                # No expired item, evict LRU (first item)
                self.cache.popitem(last=False)
        self.cache[key] = (value, expiry)
