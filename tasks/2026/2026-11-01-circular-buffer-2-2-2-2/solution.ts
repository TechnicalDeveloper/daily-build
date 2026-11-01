export class CircularBuffer<T> {
  private buffer: (T | undefined)[];
  private head: number = 0;
  private tail: number = 0;
  private _length: number = 0;
  private readonly _capacity: number;

  constructor(capacity: number) {
    if (capacity <= 0) {
      throw new Error("Capacity must be greater than 0");
    }
    this._capacity = capacity;
    this.buffer = new Array<T | undefined>(capacity);
  }

  enqueue(item: T): void {
    if (this._length === this._capacity) {
      throw new Error("Buffer is full");
    }
    this.buffer[this.tail] = item;
    this.tail = (this.tail + 1) % this._capacity;
    this._length++;
  }

  dequeue(): T | undefined {
    if (this._length === 0) {
      return undefined;
    }
    const item = this.buffer[this.head];
    this.buffer[this.head] = undefined;
    this.head = (this.head + 1) % this._capacity;
    this._length--;
    return item;
  }

  peek(): T | undefined {
    if (this._length === 0) {
      return undefined;
    }
    return this.buffer[this.head];
  }

  get length(): number {
    return this._length;
  }

  get capacity(): number {
    return this._capacity;
  }

  isEmpty(): boolean {
    return this._length === 0;
  }

  isFull(): boolean {
    return this._length === this._capacity;
  }

  clear(): void {
    this.buffer.fill(undefined);
    this.head = 0;
    this.tail = 0;
    this._length = 0;
  }

  toArray(): T[] {
    const result: T[] = [];
    let index = this.head;
    for (let i = 0; i < this._length; i++) {
      result.push(this.buffer[index] as T);
      index = (index + 1) % this._capacity;
    }
    return result;
  }
}
