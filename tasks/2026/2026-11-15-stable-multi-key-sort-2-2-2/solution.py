def stable_multi_sort(items, keys):
    # Work on a copy to avoid modifying the original
    result = items[:]
    # Sort from least significant key to most significant
    for key in reversed(keys):
        result.sort(key=lambda x: x[key])
    return result
