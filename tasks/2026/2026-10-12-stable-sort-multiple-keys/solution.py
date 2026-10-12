def stable_multi_sort(items, keys, reverse=False):
    """Return a new list of dicts sorted by multiple keys, stable.

    Missing keys are treated as None, and None sorts before any other value.
    """
    def key_function(d):
        comparisons = []
        for k in keys:
            value = k(d) if callable(k) else d.get(k)
            if value is None:
                comparisons.append((0, None))
            else:
                comparisons.append((1, value))
        return tuple(comparisons)

    return sorted(items, key=key_function, reverse=reverse)
