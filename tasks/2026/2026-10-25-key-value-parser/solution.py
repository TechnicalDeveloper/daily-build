import re

def parse(text: str) -> dict:
    """Parse a simple key=value text format.

    Each line can be:
    - Blank (ignored)
    - Comment starting with '#' (ignored)
    - Key=value pair, where key is alphanumeric+underscores, value is rest after first '=', trimmed.
      Trailing whitespace is stripped. If no '=', line is ignored.

    Returns a dict with keys in order of appearance.
    """
    result = {}
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith('#'):
            continue
        if '=' not in stripped:
            continue
        # Split on first '='
        key, _, value = stripped.partition('=')
        key = key.strip()
        value = value.strip()
        result[key] = value
    return result
