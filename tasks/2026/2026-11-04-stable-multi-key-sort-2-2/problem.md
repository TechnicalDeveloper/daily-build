# Stable Sort by Multiple Keys

Implement a function `stable_multi_sort(items, keys)` that returns a new list containing all items from `items` sorted in ascending order by multiple keys. The sort must be stable, meaning items with equal keys preserve their original relative order. The `keys` parameter is a list of callables; each callable takes one item and returns a comparable value. Sorting is performed by the first key first, then by the second key (to break ties), and so on.

**Signature:**
```python
def stable_multi_sort(items: list, keys: list) -> list:
```

**Edge cases to respect:**
1. Empty list: returns an empty list.
2. Single key: behaves like `sorted(items, key=keys[0])`.
3. All items have identical keys for all key functions: the result must preserve the original order of `items`.
4. Keys that produce non‑comparable types (e.g., mixing integers and strings) – the function may let Python raise `TypeError` (no special handling required).
