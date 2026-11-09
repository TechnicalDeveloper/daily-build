# Memoization Decorator Utility

Implement a memoization decorator that caches the results of a function call based on its arguments. The decorator should handle functions with any number of positional and keyword arguments, and should support a configurable cache size limit (LRU eviction) and a time-to-live (TTL) in seconds.

Signature:
```python
def memoize(maxsize: int = 128, ttl: int = None) -> Callable:
```

Edge cases:
- Unhashable arguments (e.g., lists, dicts) should raise a TypeError.
- If `maxsize` is 0, no caching should occur; every call recomputes.
- If `ttl` is set, entries older than `ttl` seconds should be treated as expired and recomputed.
- Thread safety is not required.

Your implementation must be in a file named `solution.py`.
