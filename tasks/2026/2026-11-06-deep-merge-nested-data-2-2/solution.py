def deep_merge(dict1, dict2):
    result = dict1.copy()
    for key, val2 in dict2.items():
        if key in result and isinstance(result[key], dict) and isinstance(val2, dict):
            result[key] = deep_merge(result[key], val2)
        else:
            result[key] = val2
    return result
