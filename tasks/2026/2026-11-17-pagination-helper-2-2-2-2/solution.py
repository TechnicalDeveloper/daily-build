from math import ceil

class Pagination:
    def __init__(self, items, page_size=10):
        if page_size <= 0:
            raise ValueError("page_size must be positive")
        self.items = list(items)
        self.page_size = page_size

    def total_pages(self):
        if not self.items:
            return 0
        return ceil(len(self.items) / self.page_size)

    def get_page(self, page_number):
        if page_number < 1:
            raise ValueError("page_number must be >= 1")
        total = self.total_pages()
        if total == 0 or page_number > total:
            return []
        start = (page_number - 1) * self.page_size
        end = min(start + self.page_size, len(self.items))
        return self.items[start:end]

    def has_next(self, page_number):
        return page_number < self.total_pages()

    def has_previous(self, page_number):
        return page_number > 1
