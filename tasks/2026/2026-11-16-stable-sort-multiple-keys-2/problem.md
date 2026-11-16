# Stable Sort by Multiple Keys

Write a function `stable_sort_by_keys(iterable, key_funcs)` that returns a new list sorted stably by multiple keys. `iterable` is any iterable of items. `key_funcs` is a list of callables that each extract a comparison key from an item. Sorting is ascending for each key, applied in order. The sort must be stable, meaning that two items with equal keys (for all keys) maintain their original relative order. If a key function returns `None`, treat that key as smaller than any non-`None` value. Edge cases: empty `iterable` returns empty list; empty `key_funcs` preserves original order; missing keys should be handled by the key functions (they might return `None`); the function should work for arbitrary items as long as the keys are comparable (or `None`).

Signature: `def stable_sort_by_keys(iterable, key_funcs): -> list`
