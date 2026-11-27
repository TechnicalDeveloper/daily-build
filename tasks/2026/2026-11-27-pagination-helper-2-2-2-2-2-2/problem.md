# Pagination Helper

Build a typed helper function `paginate` that computes pagination metadata from a page number, page size, and total number of items. The function must return an object containing the effective page, page size, total items, total pages, booleans for next/previous pages, and the zero-based start/end indices (end exclusive) to slice an array. Handle edge cases:

- Page numbers less than 1 should be treated as 1.
- Page sizes less than 1 should be treated as 1.
- If the requested page exceeds the last page, clamp it to the last page.
- If there are no items, total pages is 0, the page is set to 1, and both navigation flags are false.

Signature:
```ts
interface PaginationParams {
  page?: number;
  pageSize?: number;
  totalItems: number;
}
interface PaginationResult {
  page: number;
  pageSize: number;
  totalItems: number;
  totalPages: number;
  hasNextPage: boolean;
  hasPreviousPage: boolean;
  startIndex: number;
  endIndex: number; // exclusive
}
function paginate(params: PaginationParams): PaginationResult;
```
