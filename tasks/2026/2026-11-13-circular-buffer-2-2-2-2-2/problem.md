# Circular Buffer

Implement a generic circular buffer (ring buffer) in TypeScript. The class should be created with a fixed capacity and support the following methods:

- `push(item: T): void` – Adds an item. If the buffer is full, the oldest item is overwritten.
- `pop(): T` – Removes and returns the oldest item. Throws an error if the buffer is empty.
- `peek(): T` – Returns the oldest item without removing it. Throws an error if the buffer is empty.
- `isFull(): boolean` – Returns `true` if the buffer is at capacity.
- `isEmpty(): boolean` – Returns `true` if the buffer has no elements.
- `getSize(): number` – Returns the current number of elements.
- `getCapacity(): number` – Returns the maximum capacity.
- `toArray(): T[]` – Returns an array of the current elements in order (oldest to newest).

Edge cases:
- The buffer must correctly wrap around its internal indices when pushing/popping.
- Pushing to a full buffer overwrites the oldest element.
- Popping or peeking an empty buffer throws an error.
- The constructor must reject non-positive capacity values.
