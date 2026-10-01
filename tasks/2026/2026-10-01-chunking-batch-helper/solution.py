from typing import Iterable, List, Generator

def chunk(iterable: Iterable, size: int) -> Generator[List, None, None]:
    if not isinstance(size, int):
        raise TypeError(f"size must be an int, not {type(size).__name__}")
    if size <= 0:
        raise ValueError("size must be a positive integer")

    it = iter(iterable)
    while True:
        batch = []
        for _ in range(size):
            try:
                batch.append(next(it))
            except StopIteration:
                if batch:
                    yield batch
                return
        yield batch
