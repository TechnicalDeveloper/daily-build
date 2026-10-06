def parse_config(text: str) -> dict:
    result = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        # Find first colon
        colon_pos = line.find(':')
        if colon_pos == -1:
            # No colon, skip line
            continue
        key = line[:colon_pos].strip()
        value = line[colon_pos+1:].strip()
        if key == '':
            continue  # no key
        result[key] = value
    return result
