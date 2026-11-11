def paginate(items: list, page: int, per_page: int = 10) -> list:
    if page < 1:
        raise ValueError("page must be >= 1")
    if per_page <= 0:
        raise ValueError("per_page must be > 0")
    start = (page - 1) * per_page
    end = start + per_page
    return items[start:end]

def page_count(total_items: int, per_page: int) -> int:
    if per_page <= 0:
        raise ValueError("per_page must be > 0")
    return (total_items + per_page - 1) // per_page
