# LRU Cache with TTL Expiry

Build an LRU (Least Recently Used) cache that supports a time-to-live (TTL) per entry. The cache should evict the least recently used entry when it exceeds capacity. Entries that have expired should be treated as not found and removed from the cache upon access.

**Signature**:
```typescript
class LRUCache<K, V> {
  constructor(capacity: number, defaultTTL: number);
  get(key: K): V | undefined;
  set(key: K, value: V, ttl?: number): void;
  delete(key: K): boolean;
  get size(): number;
}
```

**Edge Cases**:
- If an entry's TTL has passed, `get()` returns `undefined` and the entry is removed.
- When the cache is full and a new entry is added, the least recently used entry (by usage order) is evicted, regardless of expiration.
- Updating an existing entry resets its TTL either to the provided `ttl` argument or to the cache's `defaultTTL`.
