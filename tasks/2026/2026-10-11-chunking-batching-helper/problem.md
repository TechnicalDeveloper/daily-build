# Chunked Iterable Batching

Implement a chunking/batching helper function that groups elements from an iterable into consecutive fixed-size chunks.

Signature: `def chunked(iterable, size):`

- Takes any iterable (`list`, `tuple`, generator, etc.).
- Yields lists; each list contains at most `size` elements in original order.
- The final chunk may be smaller than `size` if the total number of items is not divisible by `size`.
- Raises `ValueError` if `size <= 0`.

Edge cases to respect:
- `size` is zero or negative: raise `ValueError`.
- Empty iterable: yield nothing.
- Input may be an iterator/generator that should only be consumed as needed (the function is itself a generator).
