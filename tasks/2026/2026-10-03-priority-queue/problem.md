# Priority Queue

# Priority Queue

Implement a priority queue that supports inserting items with a priority and retrieving the item with the smallest priority value. If multiple items share the same priority, they must be returned in the order they were inserted (FIFO).

## Class: `PriorityQueue`

### Methods
- `insert(item, priority)`: Insert an item with a given priority (lower number = higher priority).
- `extract_min()`: Remove and return the item with the smallest priority. Raises `IndexError` if queue is empty.
- `is_empty()`: Return `True` if the queue is empty, `False` otherwise.
- `size()`: Return the number of items in the queue.

### Edge Cases
- Calling `extract_min()` on an empty queue must raise `IndexError`.
- Items with equal priority must be returned in FIFO order.
- The queue should handle a large number of inserts and extracts correctly.
