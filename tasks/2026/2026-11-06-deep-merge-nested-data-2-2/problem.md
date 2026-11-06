# Deep Merge of Nested Data Structures

Implement a function `deep_merge(dict1, dict2)` that recursively merges two dictionaries.

For keys present in both arguments:
- If both values are dictionaries, merge them recursively.
- Otherwise, the value from `dict2` overwrites the value from `dict1`.

The function should return a new dictionary; the original dictionaries must not be modified.

**Signature:**
```python
def deep_merge(dict1: dict, dict2: dict) -> dict:
```

**Edge cases to respect:**
- Merging nested dictionaries with overlapping keys (e.g., `{'a': {'b': 1}}` and `{'a': {'c': 2}}`).
- Merging with an empty dictionary (`{}`).
- Merging where a key exists in `dict2` but not in `dict1`, or vice versa.
- Values that are not dictionaries (e.g., integers, strings, lists) – the value from `dict2` should simply overwrite.
