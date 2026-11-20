# LRU Cache with TTL Expiry

Implement an LRU (Least Recently Used) cache that supports time-to-live (TTL) expiration for entries.

## Class Signature
```python
class LRUTTLCache:
    def __init__(self, capacity: int, default_ttl: float = None):
        ...
    def get(self, key: str):
        ...
    def put(self, key: str, value, ttl: float = None) -> None:
        ...
```

## Behavior
- **get(key)** returns the value if the key exists and is not expired; otherwise returns `None`. If the key exists but is expired, it is removed from the cache.
- **put(key, value, ttl)** stores the key with the given ttl (in seconds). If `ttl` is not provided, the cache's `default_ttl` is used. If `default_ttl` is `None`, the entry never expires. If `ttl` is provided, entry expires after `ttl` seconds from time of insertion.
- When the cache is full, expired entries are evicted first. If no expired entries exist, the least recently used entry is evicted.
- Updating an existing key refreshes its TTL and marks it as most recently used.

## Edge Cases to Respect
- Capacity must be a positive integer; raise `ValueError` if not.
- A `ttl` of `0` or negative makes the entry immediately expire.
- `get` on a key that has expired should delete it and return `None`.
- If the cache holds expired entries and a new key is added, space should be reclaimed by removing expired entries before considering the LRU eviction.
