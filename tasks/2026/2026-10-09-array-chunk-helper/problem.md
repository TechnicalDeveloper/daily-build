# Array Chunk Helper

Implement a generic function `chunk<T>(array: T[], size: number): T[][]` that splits an array into chunks of the specified size.

Edge cases to respect:
- If the array is empty, return an empty array.
- If `size` is less than or equal to 0, throw an error with message `"Size must be a positive integer"`.
- If `size` is larger than the array length, return the whole array as a single chunk.
