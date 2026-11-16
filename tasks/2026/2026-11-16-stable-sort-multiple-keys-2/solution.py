def stable_sort_by_keys(iterable, key_funcs):
    """
    Sort iterable by multiple keys, stably.

    Parameters:
        iterable: any iterable of items to sort.
        key_funcs: list of callables that extract a sort key from each item.
    Returns:
        A new list of items sorted stably by the given keys.

    The sort is ascending for all keys. None keys sort before non-None keys.
    Stability means that items which compare equal (i.e., all keys equal) retain their original order.
    """
    def composite_key(item):
        # For each key function, compute the key and wrap (is_not_none, key) so that
        # None sorts before any other value.
        return tuple((k is not None, k) for k in (kf(item) for kf in key_funcs))
    
    return sorted(iterable, key=composite_key)
