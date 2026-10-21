# Array Chunking Helper

Implement a generic `chunk` function that splits an array into batches of a given size.

**Signature:**
```typescript
export function chunk<T>(arr: T[], size: number): T[][]
```

**Edge cases to handle:**
- An empty array should return an empty array.
- If `size` is less than or equal to 0, throw an error with a descriptive message.
- If `size` is greater than or equal to the length of the array, return a single chunk containing all elements.
