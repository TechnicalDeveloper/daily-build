def get_page_info(total_items, page_size, current_page):
    if page_size <= 0:
        raise ValueError('page_size must be positive')

    if total_items < 0:
        raise ValueError('total_items cannot be negative')

    if total_items == 0:
        return {
            'page': 1,
            'page_size': page_size,
            'total_items': 0,
            'total_pages': 1,
            'start_index': 0,
            'end_index': 0,
            'has_previous': False,
            'has_next': False
        }

    total_pages = (total_items + page_size - 1) // page_size

    if current_page < 1:
        page = 1
    elif current_page > total_pages:
        page = total_pages
    else:
        page = current_page

    start_index = (page - 1) * page_size
    end_index = min(page * page_size - 1, total_items - 1)

    has_previous = page > 1
    has_next = page < total_pages

    return {
        'page': page,
        'page_size': page_size,
        'total_items': total_items,
        'total_pages': total_pages,
        'start_index': start_index,
        'end_index': end_index,
        'has_previous': has_previous,
        'has_next': has_next
    }
