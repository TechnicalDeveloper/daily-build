import test from "node:test";
import assert from "node:assert";
import { PriorityQueue } from "./solution";

test("enqueue and dequeue in order", () => {
  const pq = new PriorityQueue<number>();
  pq.enqueue(3);
  pq.enqueue(1);
  pq.enqueue(2);
  assert.strictEqual(pq.dequeue(), 1);
  assert.strictEqual(pq.dequeue(), 2);
  assert.strictEqual(pq.dequeue(), 3);
});

test("dequeue from empty queue returns undefined", () => {
  const pq = new PriorityQueue<string>();
  assert.strictEqual(pq.dequeue(), undefined);
});

test("peek returns highest priority without removing", () => {
  const pq = new PriorityQueue<number>();
  pq.enqueue(10);
  pq.enqueue(5);
  assert.strictEqual(pq.peek(), 5);
  assert.strictEqual(pq.size(), 2);
});

test("handles items with equal priority", () => {
  const pq = new PriorityQueue<number>();
  pq.enqueue(2);
  pq.enqueue(2);
  pq.enqueue(1);
  assert.strictEqual(pq.dequeue(), 1);
  const next = pq.dequeue();
  assert.ok(next === 2);
  const last = pq.dequeue();
  assert.strictEqual(last, 2);
});
