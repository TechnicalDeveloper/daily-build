# Deep Merge of Nested Dictionaries

Implement a function `deep_merge(base: dict, update: dict) -> dict` that deeply merges two dictionaries. The merge is recursive: for any key that exists in both dictionaries, if both values are dicts, merge them recursively; otherwise, the value from `update` overwrites the one from `base`. Keys present only in `update` are added to the result. The original dictionaries should not be mutated.

Edge cases:
- When `update` has a key whose value is a dict but `base` has a non-dict value, the dict from `update` overwrites.
- When `update` has a key with value `None`, it overwrites the base value (including possible dict).
- Empty dicts are handled correctly: merging with an empty dict returns the other dict.
