# Rolling Hash Implementation

## Problem

Implement a rolling hash (polynomial hash) for a fixed-size window over a string. This is useful for substring matching algorithms.

### Requirements

Create a class `RollingHash` with the following methods:

- `__init__(self, text: str, window_size: int, base: int = 256, mod: int = 10**9 + 7)`
  - Initialize the rolling hash for the first window of `text` of length `window_size`.
  - Raise `ValueError` if `window_size <= 0` or `window_size > len(text)`.

- `get_hash(self) -> int`
  - Return the current hash value.

- `roll(self) -> bool`
  - Advance the window by one character to the right.
  - Return `True` if the roll was successful, `False` if the window is at the end and no more roll is possible.

### Hash Definition

For a substring `s` of length `w`, the hash is computed as:

`hash(s) = (ord(s[0]) * base^(w-1) + ord(s[1]) * base^(w-2) + ... + ord(s[w-1])) mod mod`

### Edge Cases

- `window_size` must be positive and not exceed the length of `text`.
- Rolling when at the end returns `False` and does not change the internal state.
- The hash values are always non-negative integers.

### Example

```python
rh = RollingHash("abcd", 3)
print(rh.get_hash())  # hash of "abc"
rh.roll()
print(rh.get_hash())  # hash of "bcd"
```
