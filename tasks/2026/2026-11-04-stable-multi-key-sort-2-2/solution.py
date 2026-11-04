def stable_multi_sort(items, keys):
    """Return a stable sorted copy of items, sorted by multiple keys.

    Args:
        items (list): List of items to sort.
        keys (list): List of callables; each callable takes one item and returns a comparable value.

    Returns:
        list: New list sorted by the given keys, stable.
    """
    return sorted(items, key=lambda x: tuple(k(x) for k in keys))
