# Backpressure-Aware Async Queue

Implement a bounded, backpressure-aware asynchronous queue in TypeScript.

The queue should support a fixed capacity and allow producers to wait when the queue is full and consumers to wait when the queue is empty.

## Signature

```typescript
export class BoundedQueue<T> {
  constructor(capacity: number);
  enqueue(item: T): Promise<void>;
  dequeue(): Promise<T>;
}
```

- `capacity` must be a positive integer.
- `enqueue` adds an item to the queue. If the queue is full, it returns a promise that resolves when space becomes available.
- `dequeue` removes and returns the oldest item from the queue. If the queue is empty, it returns a promise that resolves when an item becomes available.
- The queue must be first-in-first-out (FIFO).

## Edge Cases

1. **Blocking on full queue**: When the queue is at capacity, any call to `enqueue` must wait until a `dequeue` frees space, without polling.
2. **Blocking on empty queue**: When the queue is empty, any call to `dequeue` must wait until an `enqueue` provides an item.
3. **Multiple waiting producers/consumers**: When multiple producers are waiting due to a full queue, a single `dequeue` must unblock exactly one producer (to maintain order). Similarly, when multiple consumers are waiting due to an empty queue, a single `enqueue` must unblock exactly one consumer.
