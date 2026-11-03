# Rolling Window Hashes

# Rolling window hashes

Implement `window_hashes(text: str, window_size: int, base: int = 257, modulus: int = 1_000_000_007) -> list[int]`.

For every contiguous window of length `window_size` in `text`, compute the polynomial hash using Horner's rule:

`h = (((ord(text[i]) * base + ord(text[i+1])) * base + ... ) % modulus)`

Return the hashes in left-to-right order. Use a rolling update so the function runs in O(len(text)) time after the first window.

Respect these edge cases:
- `window_size <= 0` must raise `ValueError`.
- `modulus <= 0` must raise `ValueError`.
- If `window_size > len(text)` (including empty `text`) return `[]`.
