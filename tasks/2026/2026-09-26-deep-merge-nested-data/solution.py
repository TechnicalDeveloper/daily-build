def deep_merge(base: dict, update: dict) -> dict:
    merged = {}
    for key in base.keys() | update.keys():
        if key in base and key in update:
            if isinstance(base[key], dict) and isinstance(update[key], dict):
                merged[key] = deep_merge(base[key], update[key])
            else:
                merged[key] = update[key]
        elif key in base:
            merged[key] = base[key]
        else:
            merged[key] = update[key]
    return merged
