class CircularBuffer:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError('Capacity must be positive')
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.size = 0

    def append(self, item):
        if self.size < self.capacity:
            self.buffer[(self.head + self.size) % self.capacity] = item
            self.size += 1
        else:
            self.buffer[self.head] = item
            self.head = (self.head + 1) % self.capacity

    def pop(self):
        if self.is_empty():
            raise IndexError('pop from empty circular buffer')
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError('peek from empty circular buffer')
        return self.buffer[self.head]

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.capacity

    def __len__(self):
        return self.size
