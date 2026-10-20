class CircularBuffer:
    def __init__(self, capacity: int):
        if capacity < 1:
            raise ValueError('Capacity must be >= 1')
        self._capacity = capacity
        self._buffer = [None] * capacity
        self._head = 0
        self._tail = 0
        self._size = 0

    def enqueue(self, item: object) -> None:
        self._buffer[self._tail] = item
        self._tail = (self._tail + 1) % self._capacity
        if self._size == self._capacity:
            self._head = (self._head + 1) % self._capacity
        else:
            self._size += 1

    def dequeue(self) -> object:
        if self._size == 0:
            raise IndexError('dequeue from empty buffer')
        item = self._buffer[self._head]
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return item

    def peek(self) -> object:
        if self._size == 0:
            raise IndexError('peek from empty buffer')
        return self._buffer[self._head]

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self._capacity

    def __len__(self) -> int:
        return self._size
