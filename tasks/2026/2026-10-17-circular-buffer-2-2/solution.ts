export class CircularBuffer<T> {
  private buffer: (T | undefined)[];
  private head: number = 0;
  private tail: number = 0;
  private count: number = 0;
  private capacity: number;

  constructor(capacity: number) {
    if (capacity <= 0) throw new Error("Capacity must be a positive integer");
    this.capacity = capacity;
    this.buffer = new Array<T | undefined>(capacity);
  }

  enqueue(item: T): void {
    if (this.isFull()) {
      this.head = (this.head + 1) % this.capacity;
    } else {
      this.count++;
    }
    this.buffer[this.tail] = item;
    this.tail = (this.tail + 1) % this.capacity;
  }

  dequeue(): T | undefined {
    if (this.isEmpty()) return undefined;
    const item = this.buffer[this.head];
    this.buffer[this.head] = undefined;
    this.head = (this.head + 1) % this.capacity;
    this.count--;
    return item;
  }

  peek(): T | undefined {
    if (this.isEmpty()) return undefined;
    return this.buffer[this.head];
  }

  isEmpty(): boolean {
    return this.count === 0;
  }

  isFull(): boolean {
    return this.count === this.capacity;
  }

  size(): number {
    return this.count;
  }
}
