def stable_sort_by_keys(items, keys):
    """Return a new list sorted stably by the given keys in priority order."""
    if not keys:
        return list(items)
    # Create a single key function that returns a tuple of all key results
    def combined_key(item):
        return tuple(key(item) for key in keys)
    return sorted(items, key=combined_key)
