import sys

def rolling_hash(s: str, window_size: int, base: int = 131, mod: int = 10**9+7) -> list[int]:
    if not s or window_size <= 0 or window_size > len(s):
        return []
    n = len(s)
    pow_base = pow(base, window_size - 1, mod)
    hashes = []
    h = 0
    for i in range(window_size):
        h = (h * base + ord(s[i])) % mod
    hashes.append(h)
    for i in range(1, n - window_size + 1):
        h = ((h - ord(s[i-1]) * pow_base) * base + ord(s[i+window_size-1])) % mod
        hashes.append(h)
    return hashes
