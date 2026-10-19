# Rolling Hash Checksum

Implement a class `RollingHash` that computes a polynomial rolling hash of strings.

## Signature

```python
class RollingHash:
    def __init__(self, base: int, mod: int):
        """Initialize with base and modulus (both positive integers)."""
        pass

    def hash(self, s: str) -> int:
        """Return the rolling hash of the entire string s."""
        pass

    def update(self, prev_hash: int, left_char: str, right_char: str, window_len: int) -> int:
        """Given the hash of a window of length window_len,
        remove left_char from the left end and add right_char to the right end,
        returning the new hash."""
        pass
```

## Requirements
- The hash of an empty string must be `0`.
- For a non‑empty string `s`, compute `h = ( ... ((ord(s[0]) * base + ord(s[1])) * base + ord(s[2]) ) * base + ... ) + ord(s[-1])` all modulo `mod`.
- The `update` method must correctly implement the sliding window formula:
    `new_hash = ((prev_hash - ord(left_char) * base^(L-1)) * base + ord(right_char)) % mod`
  where `L = window_len` and exponentiation uses the stored modulus.
- `mod` may be 1 (in which case all hashes are 0).
- All inputs are valid ASCII characters; no need to handle Unicode surrogates.

## Edge Cases to Respect
- Empty string → hash is 0.
- Window length 1 (base^0 = 1) – update must work correctly.
- Same character for left and right → hash should be unchanged (if the added char equals the removed char).
- Very large hashes (use modular arithmetic correctly to avoid overflow).
