def parse_ini(text: str) -> dict[str, dict[str, str]]:
    result = {}
    current_section = "global"
    for line_num, line in enumerate(text.splitlines(), 1):
        stripped = line.strip()
        if not stripped or stripped.startswith('#') or stripped.startswith(';'):
            continue
        if stripped.startswith('[') and stripped.endswith(']'):
            section = stripped[1:-1].strip()
            if not section:
                raise ValueError(f"Empty section name at line {line_num}")
            current_section = section
            if section not in result:
                result[section] = {}
            continue
        if '=' not in stripped:
            raise ValueError(f"Invalid line at line {line_num}: {stripped}")
        key, value = stripped.split('=', 1)
        key = key.strip()
        value = value.strip()
        if not key:
            raise ValueError(f"Empty key at line {line_num}")
        if current_section not in result:
            result[current_section] = {}
        result[current_section][key] = value
    return result
