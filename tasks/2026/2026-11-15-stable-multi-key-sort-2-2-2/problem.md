# Stable Sort by Multiple Keys

Implement a function `stable_multi_sort(items, keys)` that takes a list of dictionaries (`items`) and a list of key names (`keys`). It should return a new list sorted stably by the given keys, with the first key having the highest priority and the last key the lowest. The sorting must be stable: if two items have equal values for all keys, their relative order in the original list must be preserved.

**Signature:**
```python
def stable_multi_sort(items: list[dict], keys: list[str]) -> list[dict]:
```

**Requirements:**
- The function must not modify the original list.
- Use multiple stable sorts (from the least significant key to the most significant) rather than a single sort with a composite key.
- All dictionaries are assumed to contain every key in the `keys` list.

**Edge cases to handle:**
- Empty list returns an empty list.
- Single item returns that item in a list.
- Items with equal values for all keys must appear in the same order as in the input (stability).
- Sorting by multiple keys where the first key ties but the second key differs.
