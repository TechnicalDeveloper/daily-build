type Resolve<T> = (value: T) => void;
type Reject = (reason?: unknown) => void;

interface Consumer<T> {
  resolve: Resolve<T>;
  reject: Reject;
}

interface Producer<T> {
  item: T;
  resolve: () => void;
  reject: Reject;
}

export class BackpressureQueue<T> {
  private readonly buffer: T[] = [];
  private readonly consumers: Consumer<T>[] = [];
  private readonly producers: Producer<T>[] = [];

  constructor(private readonly capacity: number = 1) {
    if (!Number.isInteger(capacity) || capacity <= 0) {
      throw new RangeError('capacity must be a positive integer');
    }
  }

  push(item: T): Promise<void> {
    return new Promise<void>((resolve, reject) => {
      const consumer = this.consumers.shift();
      if (consumer) {
        consumer.resolve(item);
        resolve();
        return;
      }

      if (this.buffer.length < this.capacity) {
        this.buffer.push(item);
        resolve();
        return;
      }

      this.producers.push({ item, resolve, reject });
    });
  }

  pop(): Promise<T> {
    return new Promise<T>((resolve, reject) => {
      if (this.consumers.length > 0) {
        this.consumers.push({ resolve, reject });
        return;
      }

      if (this.buffer.length > 0) {
        const value = this.buffer.shift()!;
        this.releaseProducer();
        resolve(value);
        return;
      }

      this.consumers.push({ resolve, reject });
    });
  }

  private releaseProducer(): void {
    const producer = this.producers.shift();
    if (!producer) {
      return;
    }

    this.buffer.push(producer.item);
    producer.resolve();
  }
}
