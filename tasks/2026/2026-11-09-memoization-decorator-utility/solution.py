import time
from collections import OrderedDict
from functools import wraps

def memoize(maxsize=128, ttl=None):
    """
    Memoization decorator with LRU eviction and optional TTL.
    """
    def decorator(func):
        cache = OrderedDict()
        hits = 0
        misses = 0

        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal hits, misses
            # Build a key from args and kwargs. Must be hashable.
            try:
                # We create a tuple of (args, tuple of sorted kwargs items) for immutability.
                key = (args, tuple(sorted(kwargs.items())))
                hash(key)  # Force hash check
            except TypeError:
                raise TypeError("Arguments must be hashable")

            # If maxsize is 0, no caching
            if maxsize == 0:
                return func(*args, **kwargs)

            now = time.time()
            # Check if key in cache and TTL not expired
            if key in cache:
                value, timestamp = cache[key]
                if ttl is None or (now - timestamp) < ttl:
                    hits += 1
                    # Move to end (most recently used)
                    cache.move_to_end(key)
                    return value
                else:
                    # Expired, remove it
                    del cache[key]

            # Compute the value
            misses += 1
            result = func(*args, **kwargs)
            # Store with current timestamp
            cache[key] = (result, now)
            # Evict oldest if over maxsize
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result

        # Attach cache info for testing
        wrapper.cache_info = lambda: (hits, misses, maxsize, len(cache))
        wrapper.cache_clear = lambda: cache.clear()
        wrapper.cache = cache  # Expose for direct inspection if needed

        return wrapper

    return decorator
