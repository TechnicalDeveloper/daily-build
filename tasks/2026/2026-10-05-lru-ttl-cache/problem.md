# LRU Cache with TTL Expiry

Implement an LRU cache that supports time-to-live (TTL) expiry for each key.

**Class signature**
```python
class LRUCache:
    def __init__(self, capacity: int):
        ...

    def get(self, key):
        ...

    def put(self, key, value, ttl: int):
        ...
```

**Behavior**
- `get(key)` returns the associated value, or `-1` if the key is not present or has expired.
- `put(key, value, ttl)` inserts or updates the key with the given value. `ttl` is the time-to-live in seconds from the moment of insertion/update. After `ttl` seconds, the key is considered expired and `get` will return `-1`.
- When the cache is at full capacity, the **least recently used** item (regardless of its expiry status) is evicted to make room for the new item.
- Updating an existing key resets its TTL and moves it to the most recently used position.

**Edge cases to respect**
1. Getting an expired key returns `-1` and removes the key from the cache.
2. Updating a key resets its TTL, even if the key was previously expired (but still physically present).
3. Eviction triggers only when the cache is at capacity; it always removes the least recently used item, which may or may not be expired.
