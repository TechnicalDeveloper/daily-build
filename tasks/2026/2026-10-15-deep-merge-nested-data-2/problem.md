# Deep Merge of Nested Data

Implement a function `deep_merge(base, override)` that recursively merges two nested dictionaries.

Signature: `def deep_merge(base: dict, override: dict) -> dict`

The function should return a new dictionary that is the result of merging `override` into `base`. When both values are dictionaries, merge recursively. For any other type (including lists), the value from `override` replaces the value from `base`. The original dictionaries should remain unmodified.

Edge cases:
- If `base` and `override` have conflicting types for the same key (e.g., one is dict, the other is int), the `override` value should replace.
- If a key exists only in `override`, it should be added to the result.
- Merging nested dictionaries should work up to arbitrary depth.
