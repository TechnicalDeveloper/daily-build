# Memoization Decorator

Implement a memoization decorator `memoize` that caches the return values of a function based on its arguments. The decorator should use `functools.wraps` to preserve the original function's metadata. It must handle functions with any combination of positional and keyword arguments, provided all arguments are hashable.

**Signature:** `def memoize(func):`

**Edge Cases:**
- Recursive functions (e.g., Fibonacci) – the cache should prevent redundant calls and speed up computation.
- Functions with no arguments – should still cache the result.
- Functions with keyword arguments – the cache key must incorporate kwargs uniquely.
- Functions with mutable default arguments – not required to normalize, but note that calls with different argument forms (positional vs keyword) may produce different cache keys.
