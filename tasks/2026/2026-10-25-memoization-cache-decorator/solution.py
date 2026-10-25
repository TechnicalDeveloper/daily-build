import inspect
from collections import OrderedDict

def memoize(maxsize=128):
    def decorator(func):
        sig = inspect.signature(func)
        cache = OrderedDict()
        def wrapper(*args, **kwargs):
            bound = sig.bind(*args, **kwargs)
            bound.apply_defaults()
            key = tuple(sorted(bound.arguments.items()))
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            result = func(*args, **kwargs)
            cache[key] = result
            if len(cache) > maxsize:
                cache.popitem(last=False)
            return result
        return wrapper
    return decorator
