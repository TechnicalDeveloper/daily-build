import re

def interpolate(template: str, values: dict) -> str:
    def replacement(match):
        key = match.group(1)
        if key not in values:
            raise KeyError(f"Missing key '{key}' in values dictionary")
        return str(values[key])
    pattern = r'\{([^{}]+)\}'
    return re.sub(pattern, replacement, template)
