# Diff and Patch for Sequences

Implement a diff/merge routine for sequences. Write two functions in `solution.py`:

- `def diff(a, b)` – Return a list of operations that transforms sequence `a` into sequence `b`. Each operation is a tuple `(op, item)`, where `op` is one of `'equal'`, `'delete'`, or `'insert'`.
- `def apply_patch(seq, patch)` – Apply a `patch` returned by `diff` to the original sequence `seq`, and return the resulting list. The patch is applied sequentially from the start of `seq`.

Both functions should accept any iterable sequence (lists, tuples, strings) of comparable items.

Edge cases to respect:
- Empty input sequences (either side of the diff).
- Sequences containing duplicate elements.
- A patch that does not match the original sequence must raise `ValueError`.
