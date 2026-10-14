# Merge Sorted Arrays

Implement a function `mergeSorted` that takes two sorted arrays of numbers (ascending order) and returns a new sorted array containing all elements from both inputs in ascending order. The function should handle empty arrays and duplicate values.

Signature:
```typescript
export function mergeSorted(a: number[], b: number[]): number[]
```

Edge cases to respect:
- Both arrays are empty → returns empty array
- One array is empty, the other has elements → returns the non‑empty array unchanged
- Arrays contain duplicate values → duplicates are preserved in the output (e.g. `[1,2,2]` + `[2,3]` → `[1,2,2,2,3]`)
