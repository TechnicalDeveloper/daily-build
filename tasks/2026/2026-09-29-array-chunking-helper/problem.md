# Array Chunking Helper

Create a helper function that splits an array into chunks (batches) of a given size.

**Signature**
```typescript
function chunk<T>(array: T[], size: number): T[][]
```

**Behavior**
- Returns an array of chunks (each chunk is an array of up to `size` elements).
- The last chunk may be smaller if the array length is not evenly divisible.
- If `size` is not a positive integer (> 0), throw an error.
- If the input array is empty, return an empty array.

**Edge cases to respect**
1. Empty input array → `[]`
2. `size` greater than the array length → a single chunk containing the whole array
3. `size` ≤ 0 → throws an error
