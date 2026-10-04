# Rolling Hash Checksum

Implement a simple rolling hash (also known as a checksum) for a sliding window over a byte string. The hash is defined as the sum of (byte_value * (i + 1)) mod 2^32 for each byte in the window, where i is the index within the window (0-based). Write a class `RollingHash` that supports:

```python
class RollingHash:
    def __init__(self, window_size: int):
        """Initialize with window size > 0."""

    def ingest(self, byte_string: bytes) -> None:
        """Feed bytes; after at least window_size bytes, hashes can be computed."""

    def current_hash(self) -> int:
        """Return the rolling hash of the most recent window_size bytes (or 0 if fewer than window_size bytes ingested)."""
```

Edge cases:
- Window size 1: hash of a single byte is its value * 1 mod 2^32.
- If the byte string is shorter than window_size, `current_hash()` returns 0.
- When exactly window_size bytes have been ingested, the hash uses indices 0..window_size-1.
