# Diff Edit Script

## Problem

Implement a function `diff(seq1: list, seq2: list) -> list[tuple]` that computes an edit script (list of operations) to transform `seq1` into `seq2`. Each operation is one of:
- `('keep', element)` – element present in both sequences at the same relative position.
- `('insert', element)` – element appears only in `seq2`.
- `('delete', element)` – element appears only in `seq1`.

The edit script should be minimal (i.e., obtainable via a longest common subsequence backtrack). Elements are compared using `==`. Preserve the original order of elements from each sequence. When there are multiple minimal scripts, output deletions before insertions (i.e., for completely disjoint sequences, all `delete` operations come before all `insert` operations).

### Signature
```python
def diff(seq1: list, seq2: list) -> list[tuple]:
```

### Edge Cases
- Both sequences empty → return empty list `[]`.
- One sequence empty → all elements from the non-empty sequence are either all `delete` (if seq2 empty) or all `insert` (if seq1 empty).
- Sequences identical → all elements are `('keep', ...)`.
- Sequences with no common elements → all `delete` of seq1 followed by all `insert` of seq2.
