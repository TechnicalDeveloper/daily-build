export class BackpressureQueue {
  private concurrency: number;
  private running = 0;
  private queue: Array<{
    task: () => Promise<unknown>;
    resolve: (value: unknown) => void;
    reject: (reason?: unknown) => void;
  }> = [];
  private drainResolvers: Array<() => void> = [];

  constructor(concurrency: number) {
    if (concurrency < 1) {
      throw new Error('Concurrency must be at least 1');
    }
    this.concurrency = concurrency;
  }

  get size(): number {
    return this.queue.length;
  }

  get pending(): number {
    return this.running;
  }

  push<T>(task: () => Promise<T>): Promise<T> {
    return new Promise<T>((resolve, reject) => {
      this.queue.push({ task, resolve: resolve as (value: unknown) => void, reject });
      this.processQueue();
    });
  }

  drain(): Promise<void> {
    if (this.running === 0 && this.queue.length === 0) {
      return Promise.resolve();
    }
    return new Promise<void>((resolve) => {
      this.drainResolvers.push(resolve);
    });
  }

  private processQueue(): void {
    while (this.running < this.concurrency && this.queue.length > 0) {
      const item = this.queue.shift()!;
      this.running++;
      Promise.resolve()
        .then(() => item.task())
        .then(
          (result) => item.resolve(result),
          (error) => item.reject(error)
        )
        .finally(() => {
          this.running--;
          this.processQueue();
          if (this.running === 0 && this.queue.length === 0) {
            this.resolveDrain();
          }
        });
    }
  }

  private resolveDrain(): void {
    const resolvers = this.drainResolvers;
    this.drainResolvers = [];
    for (const resolve of resolvers) {
      resolve();
    }
  }
}
