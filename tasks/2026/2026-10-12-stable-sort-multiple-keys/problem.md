# Stable Sort by Multiple Keys

Implement a function `stable_multi_sort` that performs a stable sort on a list of dictionaries by multiple keys. The function must return a new sorted list without modifying the original.

Signature:
```python
def stable_multi_sort(items: list[dict], keys: list, reverse: bool = False) -> list[dict]:
```

- `items`: a list of dictionaries to sort.
- `keys`: a list where each element is either a string (dictionary key) or a callable that accepts a dictionary and returns a value. The sort order is determined by the keys in the order they appear (primary key first, then secondary, etc.).
- `reverse`: if `True`, the entire sort order is reversed. Default is `False`.
- The sort must be stable: dictionaries that compare equal according to the keys must retain their original relative order.
- If a dictionary is missing a key specified by a string, treat its value as `None`. Callables should be applied to each dictionary.

**Edge cases to respect:**
1. Empty list returns an empty list.
2. Missing keys, or actual `None` values, sort before any non-`None` value.
3. Multiple dictionaries with identical key values must preserve their original order.
4. Keys can contain a mix of strings and callables.
