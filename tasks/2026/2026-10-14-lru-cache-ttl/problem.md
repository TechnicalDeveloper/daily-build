# LRU Cache with TTL Expiry

Build a least-recently-used (LRU) cache with time-to-live (TTL) expiry. The cache has a fixed capacity; when full, the least recently used item is evicted. Items become stale after their TTL and must not be returned on `get`. 

**Signature:**
```python
class LRUCacheWithTTL:
    def __init__(self, capacity: int, default_ttl: int):
    def get(self, key: int) -> int:  # returns -1 if missing or expired
    def put(self, key: int, value: int, ttl: Optional[int] = None) -> None:
```

**Edge cases to respect:**
1. An expired key must return `-1` from `get`, even if it has not been evicted.
2. When the cache is full, `put` must evict the least recently used item (by order of access, not insertion).
3. Updating an existing key with a new `ttl` resets its expiry; the key becomes the most recently used.
