# Chunking Helper Function

# Chunking Helper Function

Build a function `chunk(iterable, size)` that splits an iterable into chunks of the given size. The function should return an iterator (or generator) of lists, each containing up to `size` elements. The last chunk may be smaller if the iterable length is not evenly divisible by `size`.

## Signature
```python
def chunk(iterable, size: int):
    ...
```

## Edge Cases
- If `size` is not a positive integer, raise `ValueError`.
- If the iterable is empty, yield nothing.
- If `size` is larger than the iterable length, yield a single chunk containing all elements.
