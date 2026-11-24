from typing import Any

class CircularBuffer:
    '''Fixed-capacity FIFO buffer that overwrites oldest data when full.'''

    def __init__(self, capacity: int) -> None:
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError('capacity must be a positive integer')
        self.capacity = capacity
        self._buffer = [None] * capacity
        self._head = 0
        self._size = 0

    def append(self, item: Any) -> None:
        if self._size < self.capacity:
            idx = (self._head + self._size) % self.capacity
            self._buffer[idx] = item
            self._size += 1
        else:
            self._buffer[self._head] = item
            self._head = (self._head + 1) % self.capacity

    def pop(self) -> Any:
        if self._size == 0:
            raise IndexError('pop from empty CircularBuffer')
        item = self._buffer[self._head]
        self._buffer[self._head] = None
        self._head = (self._head + 1) % self.capacity
        self._size -= 1
        return item

    def peek(self) -> Any:
        if self._size == 0:
            raise IndexError('peek from empty CircularBuffer')
        return self._buffer[self._head]

    def __len__(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def is_full(self) -> bool:
        return self._size == self.capacity
