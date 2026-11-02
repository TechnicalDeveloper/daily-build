def chunk(iterable, size):
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    it = iter(iterable)
    while True:
        batch = []
        try:
            for _ in range(size):
                batch.append(next(it))
            yield batch
        except StopIteration:
            if batch:
                yield batch
            break
