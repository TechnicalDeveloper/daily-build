class PriorityQueue<T> {
  private heap: Array<{ item: T; priority: number; seq: number }> = [];
  private seq = 0;

  enqueue(item: T, priority: number): void {
    const node = { item, priority, seq: this.seq++ };
    this.heap.push(node);
    this.bubbleUp(this.heap.length - 1);
  }

  dequeue(): T | undefined {
    if (this.heap.length === 0) return undefined;
    const min = this.heap[0];
    const last = this.heap.pop()!;
    if (this.heap.length > 0) {
      this.heap[0] = last;
      this.sinkDown(0);
    }
    return min.item;
  }

  peek(): T | undefined {
    return this.heap.length > 0 ? this.heap[0].item : undefined;
  }

  size(): number {
    return this.heap.length;
  }

  isEmpty(): boolean {
    return this.heap.length === 0;
  }

  private bubbleUp(index: number): void {
    while (index > 0) {
      const parent = (index - 1) >> 1;
      if (this.lessThan(this.heap[index], this.heap[parent])) {
        this.swap(index, parent);
        index = parent;
      } else {
        break;
      }
    }
  }

  private sinkDown(index: number): void {
    const size = this.heap.length;
    while (true) {
      let smallest = index;
      const left = 2 * index + 1;
      const right = 2 * index + 2;
      if (left < size && this.lessThan(this.heap[left], this.heap[smallest])) {
        smallest = left;
      }
      if (right < size && this.lessThan(this.heap[right], this.heap[smallest])) {
        smallest = right;
      }
      if (smallest !== index) {
        this.swap(index, smallest);
        index = smallest;
      } else {
        break;
      }
    }
  }

  private lessThan(
    a: { priority: number; seq: number },
    b: { priority: number; seq: number }
  ): boolean {
    if (a.priority !== b.priority) return a.priority < b.priority;
    return a.seq < b.seq;
  }

  private swap(i: number, j: number): void {
    [this.heap[i], this.heap[j]] = [this.heap[j], this.heap[i]];
  }
}

export { PriorityQueue };
