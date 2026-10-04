# Pagination Helper

Build a pagination helper function that calculates the slice indices and metadata for a page of items given the total count, current page number, and items per page.

## Signature
```python
def paginate(total: int, page: int, per_page: int = 10) -> dict
```
The function returns a dictionary with keys:
- `page` (int): the current page number (clamped to valid range)
- `per_page` (int): number of items per page
- `total` (int): total number of items
- `total_pages` (int): total number of pages (0 if total is 0)
- `start` (int): zero‑based index of the first item on this page (inclusive)
- `end` (int): zero‑based index of the last item on this page (exclusive)
- `has_prev` (bool): whether a previous page exists
- `has_next` (bool): whether a next page exists

## Edge cases to respect
1. **Page < 1** – clamp to page 1.
2. **Page > total pages** – clamp to the last valid page.
3. **Total = 0** – return a valid page object with `total_pages = 0`, `start = 0`, `end = 0`, and both `has_prev` and `has_next` as `False`.
4. **`per_page` ≤ 0** – raise a `ValueError`.
