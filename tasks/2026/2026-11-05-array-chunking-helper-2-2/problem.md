# Array Chunking Helper

Implement a function `chunk` that splits an array into groups of the specified size.

**Signature:**
```typescript
function chunk<T>(array: T[], size: number): T[][]
```

**Edge cases to respect:**
1. If `array` is empty, return `[]`.
2. If `size` is less than 1, throw a `RangeError` with a descriptive message.
3. If `size` is greater than or equal to the array length, return a single chunk containing all elements.
