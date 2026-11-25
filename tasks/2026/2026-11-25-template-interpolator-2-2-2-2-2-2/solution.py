def interpolate(template: str, mapping: dict) -> str:
    result = []
    i = 0
    n = len(template)
    while i < n:
        ch = template[i]
        if ch == '{':
            # Check for escaped brace
            if i + 1 < n and template[i+1] == '{':
                result.append('{')
                i += 2
                continue
            # Find closing brace
            j = template.find('}', i+1)
            if j == -1:
                raise ValueError("Unclosed brace")
            key = template[i+1:j]
            if key not in mapping:
                raise KeyError(key)
            result.append(str(mapping[key]))
            i = j + 1
        elif ch == '}':
            if i + 1 < n and template[i+1] == '}':
                result.append('}')
                i += 2
            else:
                raise ValueError("Unmatched closing brace")
        else:
            result.append(ch)
            i += 1
    return ''.join(result)
