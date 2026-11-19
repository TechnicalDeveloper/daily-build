# Pagination Helper

## Task
Build a TypeScript helper `paginate` that takes an array of items and an options object with `page` (1-based) and `pageSize`, and returns the items for that page along with pagination metadata.

## Signature
```ts
type PageOptions = { page?: number; pageSize?: number };

type Paginated<T> = {
  items: T[];
  totalItems: number;
  totalPages: number;
  currentPage: number;
  pageSize: number;
  hasNext: boolean;
  hasPrev: boolean;
};

declare function paginate<T>(items: T[], options?: PageOptions): Paginated<T>;
```

## Rules
- `page` and `pageSize` default to 1 and 10 respectively.
- If `page` is less than 1, treat it as 1.
- If `page` exceeds the total number of pages, return an empty `items` array but set `currentPage` to the last valid page (or 1 if there are no items).
- If `pageSize` is less than or equal to zero, fall back to the default (10).
- For empty arrays, `totalPages` is 0, `currentPage` is 1, and both `hasNext`/`hasPrev` are `false`.
- The returned object must be safe to use directly in UI rendering.

## Edge Cases
- Empty array
- Page numbers below 1
- Page numbers beyond the last page
- `pageSize` set to 0 or negative
- `pageSize` larger than the total number of items
