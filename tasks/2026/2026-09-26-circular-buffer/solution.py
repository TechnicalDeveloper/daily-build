class CircularBuffer:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0  # write position
        self.tail = 0  # read position
        self.count = 0

    def put(self, item):
        self.buffer[self.head] = item
        self.head = (self.head + 1) % self.capacity
        if self.count == self.capacity:
            # Overwrite: move tail forward as well to keep track of oldest
            self.tail = (self.tail + 1) % self.capacity
        else:
            self.count += 1

    def get(self):
        if self.count == 0:
            raise IndexError("Buffer is empty")
        item = self.buffer[self.tail]
        self.buffer[self.tail] = None  # optional cleanup
        self.tail = (self.tail + 1) % self.capacity
        self.count -= 1
        return item

    def is_empty(self) -> bool:
        return self.count == 0

    def is_full(self) -> bool:
        return self.count == self.capacity
