# Stable Sort by Multiple Keys

Implement `stable_sort_by_keys(items, key_funcs)`.

It must return a new list containing all elements of `items` sorted by multiple keys. The keys are applied in priority order: `key_funcs[0]` is the primary key, `key_funcs[1]` is the secondary key, and so on. Each element's sort key is computed by calling the corresponding key function on the element. The sort must be **stable**: elements that compare equal under every key function must keep their original relative order from `items`.

The input list must not be mutated. If `key_funcs` is empty, return a copy of `items`.

Edge cases to respect:
- Empty input list: returns `[]` (a new empty list).
- All key values equal: original order is preserved.
- Primary keys equal: secondary key decides the order.
