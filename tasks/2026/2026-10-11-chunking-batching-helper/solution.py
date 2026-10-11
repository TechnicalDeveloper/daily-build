def chunked(iterable, size):
    if size <= 0:
        raise ValueError("size must be positive")
    chunk = []
    for item in iterable:
        chunk.append(item)
        if len(chunk) == size:
            yield chunk
            chunk = []
    if chunk:
        yield chunk
