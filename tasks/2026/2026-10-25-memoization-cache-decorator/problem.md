# Memoization Cache Decorator

Implement a memoization decorator `memoize` that caches results of a function based on its arguments. The decorator should accept an optional `maxsize` parameter (default 128) specifying the maximum number of cached results. When the cache exceeds this limit, the oldest entry (least recently used) should be evicted.

**Signature:**
```python
def memoize(maxsize=128):
    ...
```

**Edge cases:**
- Function calls with default arguments must be treated identically to calls where those defaults are provided explicitly.
- If the wrapped function raises an exception, the exception should not be cached; subsequent calls with the same arguments should raise the exception again.
- The cache must work for functions with positional and keyword arguments, including keyword-only arguments.
- Assume all arguments are hashable (no need to handle unhashable types).
