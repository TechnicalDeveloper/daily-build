# Pagination Helper

Implement a function `get_page_info(total_items, page_size, current_page)` that returns a dictionary with pagination metadata.

**Signature:**
```python
def get_page_info(total_items: int, page_size: int, current_page: int) -> dict:
    ...
```

**Returned dictionary keys:**
- `page`: int – the current page number (clamped to valid range)
- `page_size`: int
- `total_items`: int
- `total_pages`: int
- `start_index`: int – zero‑based index of first item on this page (inclusive)
- `end_index`: int – zero‑based index of last item on this page (inclusive, may be equal to total_items-1)
- `has_previous`: bool
- `has_next`: bool

**Edge cases to respect:**
1. If `total_items` is 0, `page` should be 1, `start_index` and `end_index` should be 0, and both `has_previous` and `has_next` are `False`.
2. If `current_page` is less than 1, treat it as page 1.
3. If `current_page` exceeds the last page, treat it as the last page.
4. If `page_size` is 0 or negative, raise a `ValueError` with a clear message.
