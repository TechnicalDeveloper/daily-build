export class AsyncQueue<T> {
  private buffer: T[] = [];
  private readonly cap: number;
  private pendingPushes: { item: T; resolve: () => void; reject: (err: any) => void }[] = [];
  private pendingPops: { resolve: (value: T) => void; reject: (err: any) => void }[] = [];

  constructor(capacity: number) {
    if (capacity <= 0) throw new Error("Capacity must be positive");
    this.cap = capacity;
  }

  get size(): number {
    return this.buffer.length;
  }

  get capacity(): number {
    return this.cap;
  }

  async push(item: T): Promise<void> {
    if (this.pendingPops.length > 0) {
      const pop = this.pendingPops.shift()!;
      pop.resolve(item);
      return;
    }
    if (this.buffer.length < this.cap) {
      this.buffer.push(item);
      return;
    }
    return new Promise<void>((resolve, reject) => {
      this.pendingPushes.push({ item, resolve, reject });
    });
  }

  async pop(): Promise<T> {
    if (this.buffer.length > 0) {
      const item = this.buffer.shift()!;
      if (this.pendingPushes.length > 0) {
        const push = this.pendingPushes.shift()!;
        this.buffer.push(push.item);
        push.resolve();
      }
      return item;
    }
    if (this.pendingPushes.length > 0) {
      const push = this.pendingPushes.shift()!;
      push.resolve();
      return push.item;
    }
    return new Promise<T>((resolve, reject) => {
      this.pendingPops.push({ resolve, reject });
    });
  }
}
