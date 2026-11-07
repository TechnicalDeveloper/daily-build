class BackpressureQueue:
    def __init__(self, maxsize: int):
        if maxsize is None or maxsize < 0:
            self._maxsize = None
        else:
            self._maxsize = maxsize
        self._items = []

    def push(self, item) -> bool:
        if self._maxsize is not None and len(self._items) >= self._maxsize:
            return False
        self._items.append(item)
        return True

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty queue")
        return self._items.pop(0)

    def size(self) -> int:
        return len(self._items)

    def empty(self) -> bool:
        return len(self._items) == 0

    def full(self) -> bool:
        if self._maxsize is None:
            return False
        return len(self._items) >= self._maxsize
