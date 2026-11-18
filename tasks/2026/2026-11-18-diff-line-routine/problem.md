# Line Diff Routine

Implement a function `diff(a: string[], b: string[])` that computes the differences between two arrays of lines and returns a sequence of operations to transform `a` into `b`. The returned array consists of items with a `type` property: `"keep"` (line present in both), `"delete"` (line only in `a`), or `"insert"` (line only in `b`). The order of operations must respect the original order of lines in both inputs.

Signature: `export function diff(a: string[], b: string[]): DiffOp[]` where `DiffOp` is defined as:
```ts
export type DiffOp =
  | { type: "keep"; line: string }
  | { type: "delete"; line: string }
  | { type: "insert"; line: string };
```

Edge cases to respect:
- When both arrays are empty, return an empty array.
- When one array is empty, all lines from the other array are either inserted or deleted.
- When arrays are identical, return all `"keep"` operations.
- The algorithm should produce a valid transformation; the sequence of `keep`, `delete`, and `insert` operations must correspond to a minimal edit script (no unnecessary changes).
