# Chunking / Batching Helper

Implement a function `chunk(iterable, size)` that yields successive chunks (lists) of the given `size` from the `iterable`. The last chunk may be smaller than `size` if the iterable length is not evenly divisible.

**Signature:**
```python
def chunk(iterable: Iterable, size: int) -> Generator[List, None, None]:
```

**Edge cases to respect:**
- If `iterable` is empty, yield no chunks.
- If `size` is larger than the number of elements in `iterable`, yield one chunk containing all elements.
- If `size` is not a positive integer (e.g., 0, negative, or non‑int), raise `ValueError` (for non‑positive integers) or `TypeError` (for non‑integer types).
