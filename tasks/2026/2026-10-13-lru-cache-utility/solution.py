from collections import OrderedDict
import functools

def lru_cache(maxsize=128):
    """Return a decorator that caches function results with LRU eviction."""
    def decorator(func):
        cache = OrderedDict()
        hits = 0
        misses = 0

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal hits, misses
            if maxsize == 0:
                # No caching
                return func(*args, **kwargs)
            key = (args, tuple(sorted(kwargs.items())))
            try:
                result = cache[key]
                hits += 1
                cache.move_to_end(key)   # mark as most recently used
                return result
            except KeyError:
                misses += 1
                result = func(*args, **kwargs)
                if maxsize is not None and len(cache) >= maxsize:
                    # Evict least recently used (first item)
                    cache.popitem(last=False)
                cache[key] = result
                return result

        def cache_info():
            return dict(hits=hits, misses=misses,
                        currsize=len(cache), maxsize=maxsize)

        def cache_clear():
            nonlocal hits, misses
            cache.clear()
            hits = 0
            misses = 0

        wrapper.cache_info = cache_info
        wrapper.cache_clear = cache_clear
        return wrapper

    return decorator
