# Deep Merge Nested Data

Write a function `deepMerge(target, source)` that deeply merges two objects. The merge should be recursive: if both target and source have a property that is a plain object (not array, null, etc.), merge them recursively. Otherwise, the source value overwrites the target value. Arrays are replaced, not merged. If source property is `undefined`, keep target's value. The function should return a new object and not mutate the original objects.

**Signature:**
```typescript
function deepMerge<T extends Record<string, any>, U extends Record<string, any>>(target: T, source: U): T & U
```

**Edge cases to respect:**
- When a property in source is `undefined`, the target's value should remain unchanged.
- When a property is `null`, it should overwrite the target's value (null is a valid value).
- Arrays are considered atomic values; if source has an array at a key, it replaces the target's value entirely (no array merging).
