# LRU Cache with TTL Expiry

## Build an LRU Cache with TTL Expiry

Implement a class `LRUCache` that supports:
- `__init__(self, capacity: int, default_ttl: int = None)` – initializes cache with max capacity and optional default TTL in seconds.
- `get(self, key: str) -> Optional[int]` – returns value if key exists and not expired, else returns None and removes key if expired.
- `put(self, key: str, value: int, ttl: int = None) -> None` – inserts or updates key with given value. If ttl is None, use default_ttl (if default_ttl is None, item never expires). If capacity is exceeded, evict least recently used key (including expired ones).

Edge cases to respect:
- Expired keys should be removed on access and not count towards capacity.
- Updating an existing key should reset its TTL and move it to most recently used.
- When default_ttl is None, items never expire and only LRU eviction applies.
