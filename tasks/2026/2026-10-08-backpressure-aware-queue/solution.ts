export class BackpressureQueue<T> {
  private capacity: number;
  private buffer: T[] = [];
  private pushResolvers: (() => void)[] = [];
  private popResolvers: ((item: T) => void)[] = [];

  constructor(capacity: number) {
    if (!Number.isInteger(capacity) || capacity <= 0) {
      throw new Error('Capacity must be a positive integer');
    }
    this.capacity = capacity;
  }

  async push(item: T): Promise<void> {
    if (this.buffer.length < this.capacity) {
      this.buffer.push(item);
      // If someone is waiting to pop, resolve the oldest waiter
      if (this.popResolvers.length > 0) {
        const resolve = this.popResolvers.shift()!;
        resolve(this.buffer.shift()!);
      }
      return Promise.resolve();
    }

    // Buffer is full, wait until space becomes available
    return new Promise<void>((resolve) => {
      this.pushResolvers.push(() => {
        this.buffer.push(item);
        // After adding the item, check if a pop waiter can be served
        if (this.popResolvers.length > 0) {
          const popResolve = this.popResolvers.shift()!;
          popResolve(this.buffer.shift()!);
        }
        resolve();
      });
    });
  }

  async pop(): Promise<T> {
    if (this.buffer.length > 0) {
      const item = this.buffer.shift()!;
      // If someone is waiting to push, resolve the oldest waiter
      if (this.pushResolvers.length > 0) {
        const resolve = this.pushResolvers.shift()!;
        resolve();
      }
      return Promise.resolve(item);
    }

    // Buffer is empty, wait until an item becomes available
    return new Promise<T>((resolve) => {
      this.popResolvers.push(resolve);
    });
  }

  size(): number {
    return this.buffer.length;
  }
}
