import test from "node:test";
import assert from "node:assert";
import { CircularBuffer } from "./solution";

test("constructor throws for invalid capacity", () => {
  assert.throws(() => new CircularBuffer(0), /Capacity must be greater than 0/);
  assert.throws(() => new CircularBuffer(-5), /Capacity must be greater than 0/);
});

test("enqueue and dequeue basic operations", () => {
  const buf = new CircularBuffer<number>(3);
  assert.strictEqual(buf.isEmpty(), true);
  buf.enqueue(10);
  buf.enqueue(20);
  buf.enqueue(30);
  assert.strictEqual(buf.isFull(), true);
  assert.strictEqual(buf.length, 3);

  assert.strictEqual(buf.dequeue(), 10);
  assert.strictEqual(buf.dequeue(), 20);
  assert.strictEqual(buf.dequeue(), 30);
  assert.strictEqual(buf.isEmpty(), true);
});

test("enqueue on full buffer throws error", () => {
  const buf = new CircularBuffer<string>(2);
  buf.enqueue("a");
  buf.enqueue("b");
  assert.throws(() => buf.enqueue("c"), /Buffer is full/);
});

test("dequeue and peek on empty buffer return undefined", () => {
  const buf = new CircularBuffer<number>(3);
  assert.strictEqual(buf.dequeue(), undefined);
  assert.strictEqual(buf.peek(), undefined);
});

test("wrap-around behavior", () => {
  const buf = new CircularBuffer<number>(3);
  buf.enqueue(1);
  buf.enqueue(2);
  buf.enqueue(3);
  assert.strictEqual(buf.dequeue(), 1);
  assert.strictEqual(buf.dequeue(), 2);
  buf.enqueue(4);
  buf.enqueue(5);
  assert.deepStrictEqual(buf.toArray(), [3, 4, 5]);
  assert.strictEqual(buf.peek(), 3);
});

test("clear resets buffer", () => {
  const buf = new CircularBuffer<number>(3);
  buf.enqueue(1);
  buf.enqueue(2);
  buf.enqueue(3);
  buf.clear();
  assert.strictEqual(buf.isEmpty(), true);
  assert.strictEqual(buf.length, 0);
  assert.strictEqual(buf.dequeue(), undefined);
  buf.enqueue(100);
  assert.strictEqual(buf.peek(), 100);
});
