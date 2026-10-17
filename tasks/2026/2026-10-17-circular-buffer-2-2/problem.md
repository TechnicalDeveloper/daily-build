# Circular Buffer

Implement a generic circular buffer (ring buffer) with a fixed capacity. The buffer overwrites the oldest element when full.

**Signature:**
```typescript
export class CircularBuffer<T> {
  constructor(capacity: number);
  enqueue(item: T): void;
  dequeue(): T | undefined;
  peek(): T | undefined;
  isEmpty(): boolean;
  isFull(): boolean;
  size(): number;
}
```

**Edge cases to respect:**
- Dequeue or peek on an empty buffer returns `undefined`.
- Enqueue on a full buffer overwrites the oldest element (maintaining size).
- The constructor must throw an error if `capacity` is not a positive integer (e.g., 0 or negative).
