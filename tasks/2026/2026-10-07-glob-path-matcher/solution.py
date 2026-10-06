def matches(pattern: str, path: str) -> bool:
    p, s = 0, 0
    star = -1
    match = 0
    while s < len(path):
        if p < len(pattern) and (pattern[p] == '?' or pattern[p] == path[s]):
            p += 1
            s += 1
        elif p < len(pattern) and pattern[p] == '*':
            star = p
            match = s
            p += 1
        elif star != -1:
            p = star + 1
            match += 1
            s = match
        else:
            return False
    while p < len(pattern) and pattern[p] == '*':
        p += 1
    return p == len(pattern)
