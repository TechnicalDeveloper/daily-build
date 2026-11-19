def stable_sort_by_keys(items, key_funcs):
    result = list(items)
    for key_func in reversed(key_funcs):
        result = sorted(result, key=key_func)
    return result
