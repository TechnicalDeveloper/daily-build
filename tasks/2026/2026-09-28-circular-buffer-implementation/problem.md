# Circular Buffer

Implement a circular buffer (ring buffer) with a fixed capacity.

When the buffer is full and a new item is pushed, the oldest item is overwritten.

### Signature
```typescript
class CircularBuffer<T> {
  constructor(capacity: number);
  push(item: T): void;
  pop(): T | undefined;
  size(): number;
  isEmpty(): boolean;
  isFull(): boolean;
}
```

### Edge Cases
- Popping from an empty buffer returns `undefined`.
- Pushing to a full buffer overwrites the oldest element; `size()` remains equal to capacity.
- The buffer must handle elements of any type (generic).
