from collections import OrderedDict

class Cache:
    def __init__(self, max_size=None):
        self.max_size = max_size

    def __call__(self, func):
        return CachedFunction(func, self.max_size)

class CachedFunction:
    def __init__(self, func, max_size=None):
        self.func = func
        self.max_size = max_size
        self.cache = OrderedDict()
        self.hits = 0
        self.misses = 0

    def __call__(self, *args, **kwargs):
        key = self._make_key(args, kwargs)
        if key in self.cache:
            self.hits += 1
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            self.misses += 1
            result = self.func(*args, **kwargs)
            self.cache[key] = result
            if self.max_size is not None and len(self.cache) > self.max_size:
                self.cache.popitem(last=False)
            return result

    def clear(self):
        self.cache.clear()

    @property
    def stats(self):
        return {
            'hits': self.hits,
            'misses': self.misses,
            'size': len(self.cache)
        }

    @staticmethod
    def _make_key(args, kwargs):
        try:
            return (args, tuple(sorted(kwargs.items())))
        except TypeError:
            return str(args) + str(sorted(kwargs.items()))
