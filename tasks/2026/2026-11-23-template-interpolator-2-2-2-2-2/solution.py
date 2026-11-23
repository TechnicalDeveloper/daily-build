def interpolate(template, mapping):
    result = []
    i = 0
    n = len(template)
    while i < n:
        ch = template[i]
        if ch == '{':
            # escaped '{{'
            if i + 1 < n and template[i + 1] == '{':
                result.append('{')
                i += 2
                continue
            # find closing brace
            end = template.find('}', i + 1)
            if end == -1:
                raise ValueError("Unclosed brace in template")
            key = template[i + 1:end]
            if not key:
                raise ValueError("Empty placeholder")
            if key not in mapping:
                raise KeyError(key)
            result.append(str(mapping[key]))
            i = end + 1
        elif ch == '}':
            # escaped '}}'
            if i + 1 < n and template[i + 1] == '}':
                result.append('}')
                i += 2
                continue
            # unescaped single '}' treated as literal
            result.append('}')
            i += 1
        else:
            result.append(ch)
            i += 1
    return ''.join(result)
