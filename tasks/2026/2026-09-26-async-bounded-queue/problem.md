# Async Bounded Queue with Backpressure

Implement an async bounded queue that handles backpressure. The queue has a fixed capacity. The `push` method should wait (resolve later) when the queue is full, and the `pop` method should wait when the queue is empty. The queue must preserve FIFO order.

**Signature:**
```typescript
export class AsyncQueue<T> {
  constructor(capacity: number);
  get size(): number;
  get capacity(): number;
  push(item: T): Promise<void>;
  pop(): Promise<T>;
}
```

**Edge cases:**
- Pushing to a full queue blocks until a `pop` frees space.
- Popping from an empty queue blocks until a `push` provides an item.
- Order must be preserved even when pushes and pops overlap (e.g., push 1, push 2, push 3 (blocks), pop -> returns 1).
