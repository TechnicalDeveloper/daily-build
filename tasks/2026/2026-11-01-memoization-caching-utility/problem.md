# Memoization / Caching Utility

Build a utility that provides a simple in-memory cache with memoization for function results. The utility should be a callable class or function decorator that caches the return value of a function based on its arguments.

**Signature:** Provide a class `Cache` that can be used as a decorator. It should support:
- `__init__(self, max_size=None)` where `max_size` limits the cache entries (None = unlimited).
- `__call__(self, func)` returns a wrapper that caches results.
- The wrapper should also have a `.clear()` method to empty the cache.
- The wrapper should have a `.stats` property returning a dict with `'hits'`, `'misses'`, `'size'`.

**Edge Cases:**
1. Functions with mutable default arguments should cache correctly (use a serialization-friendly argument handling; assume arguments can be hashed via standard Python mechanisms, but handle unhashable args by converting to a string representation).
2. When `max_size` is set, the cache should evict the least recently used (LRU) item once the limit is exceeded.
3. If the same arguments are passed, the cached result should be returned (no re-execution).

Implement with standard library only (use `collections.OrderedDict` for LRU).
