class CircularBuffer:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0  # index of oldest element
        self.size = 0  # current number of elements

    def append(self, item):
        if self.size == self.capacity:
            # overwrite oldest, advance head
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.capacity
        else:
            insertion = (self.head + self.size) % self.capacity
            self.buffer[insertion] = item
            self.size += 1

    def get(self):
        if self.size == 0:
            raise IndexError("get from empty buffer")
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.size == 0:
            raise IndexError("peek from empty buffer")
        return self.buffer[self.head]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def __len__(self):
        return self.size
