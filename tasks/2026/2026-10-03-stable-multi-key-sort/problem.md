# Stable Sort by Multiple Keys

Implement a generic function `stableSortByKeys<T>(items: T[], sortKeys: SortKey<T>[]): T[]` that performs a **stable** sort on an array of objects by multiple keys. Stability means that items with equal sort keys retain their original relative order.

Define `SortKey<T>` as:
```typescript
type SortKey<T> = {
  key: keyof T;
  direction?: 'asc' | 'desc'; // defaults to 'asc'
};
```

Comparison rules:
- For primitive keys (numbers, strings, booleans), use standard `<` and `>` operators. Strings are compared case-sensitively.
- If a key value is `undefined` or `null`, treat it as **less than** any defined non-null/non-undefined value.
- If two items compare equal on all specified keys, their relative order must be preserved (stable).

Edge cases to respect:
1. Empty array → return `[]`.
2. Empty `sortKeys` array → return a **copy** of the original array (in the same order).
3. Items where a key is missing (`undefined` or `null`) must not cause runtime errors.
