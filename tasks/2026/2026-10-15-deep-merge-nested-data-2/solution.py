from copy import deepcopy

def deep_merge(base: dict, override: dict) -> dict:
    '''Recursively merge override into base, returning a new dict.'''
    result = deepcopy(base)  # start with a copy of base
    for key, val in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(val, dict):
            # Both are dicts: merge recursively
            result[key] = deep_merge(result[key], val)
        else:
            # Otherwise, override value replaces (or adds) the key
            result[key] = deepcopy(val) if isinstance(val, (dict, list)) else val
    return result
