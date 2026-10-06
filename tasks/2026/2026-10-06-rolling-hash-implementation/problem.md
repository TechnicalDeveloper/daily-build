# Rolling Hash

Implement a rolling hash function that computes hash values for all fixed-size windows of a string.

## Signature
```python
def rolling_hash(s: str, window_size: int, base: int = 131, mod: int = 10**9+7) -> list[int]:
```

## Rules
- Return a list of hash values for each contiguous substring of length `window_size`.
- Hash is computed using the polynomial rolling hash formula: `h = (h * base + ord(c)) % mod`.
- For rolling update: `h = ((h - ord(s[i-1]) * pow_base) * base + ord(s[i+window_size-1])) % mod`, where `pow_base = base^(window_size-1) % mod`.
- Do not use any external libraries.

## Edge cases
- If `s` is empty, return `[]`.
- If `window_size <= 0`, return `[]`.
- If `window_size > len(s)`, return `[]`.
- If `window_size == len(s)`, return a list with one hash value.
