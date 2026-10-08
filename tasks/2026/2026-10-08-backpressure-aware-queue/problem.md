# Backpressure-Aware Queue

Implement a bounded asynchronous queue that respects backpressure. The queue should block a producer when full and block a consumer when empty, using promises.

## Signature
```typescript
class BackpressureQueue<T> {
  constructor(capacity: number);
  async push(item: T): Promise<void>; // resolves when space becomes available
  async pop(): Promise<T>;            // resolves when an item is available
  size(): number;                     // current number of items
}
```

## Edge Cases
- Pushing to a full queue causes the promise to wait until a consumer pops an item.
- Popping from an empty queue causes the promise to wait until a producer pushes an item.
- Multiple concurrent pushes and pops must not lose data or violate FIFO order.
- Capacity must be a positive integer.
