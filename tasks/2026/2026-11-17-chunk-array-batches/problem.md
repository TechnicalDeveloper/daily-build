# Chunk Array into Batches

Build a helper that splits a given array into fixed-size chunks. Export a `chunk` function with the following signature:

```ts
export function chunk<T>(items: readonly T[], size: number): T[][]
```

Return a new array of arrays, each with at most `size` items. Do not mutate the input array.

Edge cases to respect:
- If the input array is empty, return `[]`.
- If `size` is not a positive integer, throw a `RangeError`.
- If `size` is larger than the array length, return one chunk containing all items.
