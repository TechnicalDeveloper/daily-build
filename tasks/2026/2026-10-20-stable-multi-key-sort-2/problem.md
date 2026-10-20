# Stable Multi-Key Sorting

## Problem: Stable Multi-Key Sort

Implement a function `stable_sort_by_keys(items, keys)` that performs a **stable** sort of `items` using multiple key functions, where the first key has the highest priority, the second key next, and so on.

**Signature:**
```python
def stable_sort_by_keys(items: list, keys: list) -> list:
    """Return a new list sorted stably by the given keys in priority order."""
```

**Edge cases to respect:**
1. If `items` is empty, return an empty list.
2. If `keys` is empty, the result should be a copy of `items` in the same order.
3. For items that compare equal under all keys, their original relative order must be preserved (stable sort).

**Example:**
```python
items = [(1, 'b'), (2, 'a'), (1, 'a')]
keys = [lambda x: x[0], lambda x: x[1]]
result = stable_sort_by_keys(items, keys)
# result == [(1, 'a'), (1, 'b'), (2, 'a')]
# sorted by first element, then second; stable because (1,'b') came before (2,'a') originally
```
