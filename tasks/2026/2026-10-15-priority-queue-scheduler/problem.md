# Priority Queue / Scheduler

Implement a generic priority queue (min-heap) that supports scheduling tasks with priorities. Lower numeric priority values correspond to higher urgency (i.e., dequeue returns the item with the lowest priority number). If two items have the same priority, they must be dequeued in FIFO order (stable).

**Signature:**

```typescript
class PriorityQueue<T> {
  constructor()
  enqueue(item: T, priority: number): void
  dequeue(): T | undefined
  peek(): T | undefined
  size(): number
  isEmpty(): boolean
}
```

**Edge cases to respect:**
1. Dequeuing from an empty queue returns `undefined` (no error thrown).
2. Peeking an empty queue returns `undefined`.
3. Items with equal priority are dequeued in insertion order (stable).
4. Priorities can be any integer (including negative and zero).
