import test from "node:test";
import assert from "node:assert";
import { PriorityQueue } from "./solution";

test("enqueue and dequeue in priority order", () => {
  const pq = new PriorityQueue<string>();
  pq.enqueue("low", 3);
  pq.enqueue("medium", 2);
  pq.enqueue("high", 1);

  assert.strictEqual(pq.dequeue(), "high");
  assert.strictEqual(pq.dequeue(), "medium");
  assert.strictEqual(pq.dequeue(), "low");
  assert.strictEqual(pq.dequeue(), undefined);
});

test("peek returns top without removing", () => {
  const pq = new PriorityQueue<number>();
  pq.enqueue(10, 5);
  pq.enqueue(20, 3);

  assert.strictEqual(pq.peek(), 20);
  assert.strictEqual(pq.size(), 2);
  assert.strictEqual(pq.isEmpty(), false);
});

test("empty queue returns undefined for dequeue and peek", () => {
  const pq = new PriorityQueue<string>();
  assert.strictEqual(pq.dequeue(), undefined);
  assert.strictEqual(pq.peek(), undefined);
  assert.strictEqual(pq.size(), 0);
  assert.strictEqual(pq.isEmpty(), true);
});

test("stable ordering for equal priorities (FIFO)", () => {
  const pq = new PriorityQueue<string>();
  pq.enqueue("first", 1);
  pq.enqueue("second", 1);
  pq.enqueue("third", 1);

  assert.strictEqual(pq.dequeue(), "first");
  assert.strictEqual(pq.dequeue(), "second");
  assert.strictEqual(pq.dequeue(), "third");
  assert.strictEqual(pq.dequeue(), undefined);
});

test("works with mixed priorities including negatives", () => {
  const pq = new PriorityQueue<number>();
  pq.enqueue(1, -5);
  pq.enqueue(2, 0);
  pq.enqueue(3, -10);

  assert.strictEqual(pq.dequeue(), 3);
  assert.strictEqual(pq.dequeue(), 1);
  assert.strictEqual(pq.dequeue(), 2);
});
