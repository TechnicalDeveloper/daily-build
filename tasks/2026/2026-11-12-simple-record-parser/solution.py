def parse_records(text):
    records = []
    current = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            if current is not None:
                records.append(current)
                current = None
            continue
        if line.startswith('#'):
            continue
        if current is None:
            current = {}
        if ':' not in line:
            raise ValueError('Invalid line (missing colon): ' + repr(raw_line))
        key, value = line.split(':', 1)
        key = key.strip()
        if not key:
            raise ValueError('Invalid line (empty key): ' + repr(raw_line))
        current[key] = value.strip()
    if current is not None:
        records.append(current)
    return records
