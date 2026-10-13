# LRU Cache Decorator

Implement an LRU (Least Recently Used) cache decorator `lru_cache` that caches the results of a function and discards the least recently used entry when the cache reaches a maximum size.

**Signature:**

def lru_cache(maxsize=128):
    """Return a decorator that caches function results with an LRU policy."""

The returned decorator, when applied to a function, must equip that function with two attributes:
- `cache_info()`: returns a dictionary with keys `hits`, `misses`, `currsize`, and `maxsize`.
- `cache_clear()`: clears the cache and resets hit/miss counters.

**Edge Cases to Respect:**
1. `maxsize=0`: no caching at all – the function is always recomputed.
2. `maxsize=None`: unbounded cache – never evicts.
3. When the cache is full (`len(cache) == maxsize`) and a new key arrives, the least recently used entry must be evicted.
4. The same arguments (positional and keyword) should return the cached result and update the access order (the key becomes most recently used).

Assume all arguments are hashable.
