# Backpressure-Aware Async Queue

Build an async queue that supports backpressure by limiting the number of concurrent tasks and providing a way to wait until the queue is drained.

## Signature
```ts
export class BackpressureQueue {
  constructor(concurrency: number);
  push<T>(task: () => Promise<T>): Promise<T>;
  drain(): Promise<void>;
  get size(): number;
  get pending(): number;
}
```
- `concurrency`: maximum number of tasks running at once (must be >= 1).
- `push`: schedules `task` and returns a promise that resolves/rejects with the task's result.
- `drain`: returns a promise that resolves when all queued and running tasks have settled.
- `size`: number of tasks waiting (not yet started).
- `pending`: number of tasks currently running.

## Edge cases
- If `concurrency` is less than 1, throw an `Error` in the constructor.
- When `push` is called while at capacity, the task waits until a slot opens.
- `drain` called when queue is empty resolves immediately.
- Tasks that reject must not prevent other tasks from running; their rejections propagate to the caller.
