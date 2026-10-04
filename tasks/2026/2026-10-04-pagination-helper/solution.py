def paginate(total: int, page: int, per_page: int = 10) -> dict:
    if per_page <= 0:
        raise ValueError('per_page must be positive')
    if total < 0:
        raise ValueError('total cannot be negative')

    page = max(1, page)
    total_pages = max(1, (total + per_page - 1) // per_page) if total > 0 else 0
    if page > total_pages and total_pages > 0:
        page = total_pages

    start = (page - 1) * per_page
    end = min(start + per_page, total)

    return {
        'page': page,
        'per_page': per_page,
        'total': total,
        'total_pages': total_pages,
        'start': start,
        'end': end,
        'has_prev': page > 1,
        'has_next': page < total_pages,
    }
