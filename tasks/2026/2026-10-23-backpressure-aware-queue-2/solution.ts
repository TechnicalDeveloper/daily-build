export class BoundedQueue<T> {
  private capacity: number;
  private items: T[] = [];
  private pendingDequeue: Array<{ resolve: (value: T) => void }> = [];
  private pendingEnqueue: Array<{ item: T; resolve: () => void }> = [];

  constructor(capacity: number) {
    if (capacity <= 0) {
      throw new Error('Capacity must be positive');
    }
    this.capacity = capacity;
  }

  get size(): number {
    return this.items.length;
  }

  async enqueue(item: T): Promise<void> {
    if (this.items.length < this.capacity) {
      this.items.push(item);
      this.processPendingDequeue();
      return;
    }

    // Queue is full: wait for space
    return new Promise<void>((resolve) => {
      this.pendingEnqueue.push({ item, resolve });
    });
  }

  async dequeue(): Promise<T> {
    if (this.items.length > 0) {
      const item = this.items.shift()!;
      this.processPendingEnqueue();
      return item;
    }

    // Queue is empty: wait for an item
    return new Promise<T>((resolve) => {
      this.pendingDequeue.push({ resolve });
    });
  }

  private processPendingDequeue(): void {
    while (this.items.length > 0 && this.pendingDequeue.length > 0) {
      const { resolve } = this.pendingDequeue.shift()!;
      const item = this.items.shift()!;
      resolve(item);
    }
  }

  private processPendingEnqueue(): void {
    while (this.items.length < this.capacity && this.pendingEnqueue.length > 0) {
      const { item, resolve } = this.pendingEnqueue.shift()!;
      this.items.push(item);
      resolve();
      this.processPendingDequeue();
    }
  }
}
