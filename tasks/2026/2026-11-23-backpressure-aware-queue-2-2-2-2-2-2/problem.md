# Backpressure-Aware Async Queue

Build a bounded asynchronous queue that applies backpressure to producers. The class should allow consumers to wait for values and producers to wait for free capacity.

Signature:

```ts
export class BackpressureQueue<T> {
  constructor(capacity?: number);
  push(item: T): Promise<void>;
  pop(): Promise<T>;
}
```

`push(item)` must resolve only once the item has been accepted into the queue or handed directly to a waiting consumer. If the queue is full, the returned promise must stay pending until a consumer frees a slot. `pop()` must resolve with the next available item, or wait until one is pushed.

Edge cases to respect:
- Waiting consumers and waiting producers must be served in FIFO order.
- Multiple pending `pop()` calls must each eventually receive a distinct item in call order.
- Multiple pending `push()` calls on a full queue must be released one per free slot, in call order.
- The constructor must reject zero, negative, and non-integer capacities with a `RangeError`.
