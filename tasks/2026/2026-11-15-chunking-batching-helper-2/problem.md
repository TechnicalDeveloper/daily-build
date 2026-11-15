# Chunking Helper

Write a function `chunk(sequence, size)` that splits a sequence into chunks of the given size. The function should return a list of lists, where each inner list contains at most `size` elements, preserving the original order. 

**Signature:** `def chunk(sequence, size) -> list[list]`

**Edge cases to handle:**
- If `size` is not a positive integer, raise `ValueError`.
- If `sequence` is empty, return an empty list.
- If `size` is larger than the length of the sequence, return a single chunk containing all elements.
