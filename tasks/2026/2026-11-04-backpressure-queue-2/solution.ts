export class BackpressureQueue<T> {
  private readonly maxSize: number;
  private items: T[] = [];
  private waitingDequeue: Array<(value: T) => void> = [];
  private waitingEnqueue: Array<{ resolve: (value: void) => void; item: T }> = [];

  constructor(maxSize: number) {
    if (maxSize <= 0) {
      throw new Error("maxSize must be a positive integer");
    }
    this.maxSize = maxSize;
  }

  enqueue(item: T): Promise<void> {
    return new Promise<void>((resolve) => {
      // If there is a consumer already waiting, hand off directly
      if (this.waitingDequeue.length > 0) {
        const dequeueResolve = this.waitingDequeue.shift()!;
        dequeueResolve(item);
        resolve();
        return;
      }

      // If there is room, store the item
      if (this.items.length < this.maxSize) {
        this.items.push(item);
        resolve();
        return;
      }

      // Queue is full, wait until a slot becomes available
      this.waitingEnqueue.push({ resolve, item });
    });
  }

  dequeue(): Promise<T> {
    return new Promise<T>((resolve) => {
      // If there are items, take the oldest
      if (this.items.length > 0) {
        const value = this.items.shift()!;

        // After removing an item, if there is a waiting producer, let it in immediately
        if (this.waitingEnqueue.length > 0) {
          const enqueueEntry = this.waitingEnqueue.shift()!;
          this.items.push(enqueueEntry.item);
          enqueueEntry.resolve();
        }

        resolve(value);
        return;
      }

      // No items, wait for a producer
      this.waitingDequeue.push(resolve);
    });
  }
}
