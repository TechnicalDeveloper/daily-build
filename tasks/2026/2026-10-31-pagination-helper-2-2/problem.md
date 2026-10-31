# Pagination Helper

Build a generic pagination helper function that takes an array of items, a page number, and a page size, and returns a paginated result object containing the sliced items and metadata.

**Signature**:
```
paginate<T>(items: T[], page: number, pageSize: number): PaginatedResult<T>
```

**Edge cases to handle**:
1. Empty items array should return an empty items array with `totalPages = 1`.
2. Page number less than 1 should be treated as page 1 (clamp to 1).
3. Page number greater than total pages should be clamped to the last page.
4. `pageSize` must be greater than zero; throw an error otherwise.
