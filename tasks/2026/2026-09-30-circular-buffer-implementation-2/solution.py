from typing import Any

class CircularBuffer:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.count = 0

    def enqueue(self, item: Any) -> None:
        if self.is_full():
            self.head = (self.head + 1) % self.capacity
        else:
            self.count += 1
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity

    def dequeue(self) -> Any:
        if self.is_empty():
            raise IndexError("dequeue from empty buffer")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return item

    def peek(self) -> Any:
        if self.is_empty():
            raise IndexError("peek from empty buffer")
        return self.buffer[self.head]

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity

    def size(self) -> int:
        return self.count
