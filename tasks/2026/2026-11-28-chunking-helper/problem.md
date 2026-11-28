# Chunking Helper Function

Implement a function `chunk(iterable, size)` that splits an iterable into chunks of a specified size. The function should be a generator yielding lists.

Signature: `def chunk(iterable, size) -> Iterator[List]`

Edge cases:
- If `size` is less than or equal to 0, raise `ValueError`.
- If the iterable is empty, the generator yields nothing.
- If the iterable length is not a multiple of `size`, the final chunk should contain the remaining items (shorter than `size`).
