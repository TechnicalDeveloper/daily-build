# Pagination Helper Class

Build a `Pagination` class that helps manage paginated access to a list of items.

## Signature

```python
class Pagination:
    def __init__(self, items, page_size=10):
        ...
    def get_page(self, page_number):
        ...
    def total_pages(self):
        ...
    def has_next(self, page_number):
        ...
    def has_previous(self, page_number):
        ...
```

## Edge cases

- `page_size` must be a positive integer; otherwise raise `ValueError`.
- Empty list: total pages is 0, any page request returns an empty list.
- Page numbers are 1-indexed. Requesting page <= 0 raises `ValueError`.
- Requesting a page beyond the last page returns an empty list, not an error.
