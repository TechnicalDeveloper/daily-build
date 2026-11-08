# Memoization Cache Decorator

## Problem

Build a decorator `@memoize` that caches the return values of a deterministic function based on its arguments. The cache should be stored on the function object (e.g., `func.cache`) as a dictionary mapping argument tuples to results.

### Signature
```python
def memoize(func):
    ...
```

The decorator should:
- Return a wrapper function that computes the result if the arguments are not in the cache, otherwise return the cached value.
- Expose the cache as a dict on the wrapper via attribute `.cache`.
- Only handle positional arguments (ignore keyword arguments — optional bonus, but not required).

### Edge Cases to Respect
1. **Multiple arguments**: Function takes two or more arguments; cache key must be based on all of them.
2. **Mutable arguments not allowed**: When arguments are unhashable (e.g., lists), the cache will raise a TypeError; the wrapper should let that error propagate (no special handling).
3. **Empty arguments**: The function takes no arguments; cache key should be an empty tuple.
4. **Side effect counting**: The original function can be instrumented (e.g., with a counter) to verify that the wrapper calls the original only once for identical arguments.
