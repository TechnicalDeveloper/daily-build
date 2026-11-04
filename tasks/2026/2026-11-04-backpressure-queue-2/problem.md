# Backpressure-Aware Queue

Build a bounded, backpressure-aware async queue. The queue has a maximum capacity. Producers call `enqueue(item)` and get a promise that resolves when the item has been accepted (i.e., there is space in the queue). Consumers call `dequeue()` and get a promise that resolves with the next item when one becomes available.

**Signature**
```typescript
export class BackpressureQueue<T> {
  constructor(maxSize: number);
  enqueue(item: T): Promise<void>;
  dequeue(): Promise<T>;
}
```

**Edge cases to handle**
1. **Full queue**: If the queue is at capacity, `enqueue` must wait (its returned promise does not resolve) until a `dequeue` frees a slot.
2. **Empty queue**: If the queue is empty, `dequeue` must wait until an item is enqueued.
3. **Multiple waiters**: Both `enqueue` and `dequeue` can have many pending callers; they must be served in FIFO order (first-come, first-served).
