# Circular Buffer

Implement a circular buffer (ring buffer) with a fixed capacity.

**Signature:**
```typescript
export class CircularBuffer<T> {
  constructor(capacity: number);
  enqueue(item: T): void;
  dequeue(): T | undefined;
  peek(): T | undefined;
  get length(): number;
  get capacity(): number;
  isEmpty(): boolean;
  isFull(): boolean;
  clear(): void;
  toArray(): T[];
}
```

**Edge cases to respect:**
- Enqueuing to a full buffer should throw an error (not overwrite).
- Dequeuing from an empty buffer should return `undefined` (not throw).
- The buffer must reject `capacity <= 0` in the constructor (throw).
