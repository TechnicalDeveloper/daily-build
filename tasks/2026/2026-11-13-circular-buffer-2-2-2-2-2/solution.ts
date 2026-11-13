export class CircularBuffer<T> {
  private buffer: Array<T | undefined>;
  private capacity: number;
  private head: number; // index of the oldest element
  private size: number;

  constructor(capacity: number) {
    if (capacity <= 0) {
      throw new Error('Capacity must be a positive integer');
    }
    this.capacity = capacity;
    this.buffer = new Array<T | undefined>(capacity);
    this.head = 0;
    this.size = 0;
  }

  push(item: T): void {
    if (this.isFull()) {
      // Overwrite the oldest element
      this.head = (this.head + 1) % this.capacity;
      this.size--;
    }
    const tail = (this.head + this.size) % this.capacity;
    this.buffer[tail] = item;
    this.size++;
  }

  pop(): T {
    if (this.isEmpty()) {
      throw new Error('Buffer is empty');
    }
    const value = this.buffer[this.head] as T;
    this.buffer[this.head] = undefined;
    this.head = (this.head + 1) % this.capacity;
    this.size--;
    return value;
  }

  peek(): T {
    if (this.isEmpty()) {
      throw new Error('Buffer is empty');
    }
    return this.buffer[this.head] as T;
  }

  isFull(): boolean {
    return this.size === this.capacity;
  }

  isEmpty(): boolean {
    return this.size === 0;
  }

  getSize(): number {
    return this.size;
  }

  getCapacity(): number {
    return this.capacity;
  }

  toArray(): T[] {
    const result: T[] = [];
    for (let i = 0; i < this.size; i++) {
      const index = (this.head + i) % this.capacity;
      result.push(this.buffer[index] as T);
    }
    return result;
  }
}
