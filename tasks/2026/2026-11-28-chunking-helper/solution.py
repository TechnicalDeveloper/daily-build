def chunk(iterable, size):
    if size <= 0:
        raise ValueError("size must be positive")
    current_chunk = []
    for item in iterable:
        current_chunk.append(item)
        if len(current_chunk) == size:
            yield current_chunk
            current_chunk = []
    if current_chunk:
        yield current_chunk
