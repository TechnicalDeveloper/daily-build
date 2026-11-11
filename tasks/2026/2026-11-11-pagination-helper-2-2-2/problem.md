# Pagination Helper

Implement a small pagination helper.

### Functions

def paginate(items: list, page: int, per_page: int = 10) -> list:
    Return the slice of `items` for the given `page` (1-indexed). If `page` is out of range, return an empty list.

def page_count(total_items: int, per_page: int) -> int:
    Return the total number of pages needed to display `total_items` with `per_page` items per page.

Edge cases:
- `page < 1` or `per_page <= 0` must raise `ValueError`.
- `total_items` may be 0, then `page_count` should return 0.
- `page` may point beyond the last page; `paginate` should return an empty list.
