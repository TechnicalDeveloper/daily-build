from functools import lru_cache

def glob_match(pattern: str, path: str) -> bool:
    p = pattern
    s = path

    @lru_cache(maxsize=None)
    def match(i, j):
        if i == len(p):
            return j == len(s)
        if p[i] == '*':
            if match(i + 1, j):
                return True
            if j < len(s) and s[j] != '/':
                return match(i, j + 1)
            return False
        if j < len(s):
            if p[i] == '?' and s[j] != '/':
                return match(i + 1, j + 1)
            if p[i] == s[j]:
                return match(i + 1, j + 1)
        return False

    return match(0, 0)
