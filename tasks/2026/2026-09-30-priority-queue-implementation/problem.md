# Priority Queue Implementation

Implement a generic priority queue using a binary heap (min-heap). The priority queue should support the following operations:

```typescript
class PriorityQueue<T> {
  constructor(comparator?: (a: T, b: T) => number);
  enqueue(item: T): void;
  dequeue(): T | undefined;
  peek(): T | undefined;
  size(): number;
  isEmpty(): boolean;
}
```

The `comparator` function should return a negative number if `a` has higher priority than `b`, positive if lower, and zero if equal. If omitted, the default comparator should treat numbers/strings as usual (ascending order).

**Edge cases to respect:**
1. Dequeueing from an empty queue must return `undefined`.
2. Peeking on an empty queue must return `undefined`.
3. Items with equal priority should be handled without errors (order of equal items is not guaranteed).
