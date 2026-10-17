import test from "node:test";
import assert from "node:assert";
import { CircularBuffer } from "./solution";

test("basic operations", () => {
  const buf = new CircularBuffer<number>(3);
  assert.strictEqual(buf.isEmpty(), true);
  buf.enqueue(1);
  buf.enqueue(2);
  buf.enqueue(3);
  assert.strictEqual(buf.isFull(), true);
  assert.strictEqual(buf.size(), 3);
  assert.strictEqual(buf.peek(), 1);
  assert.strictEqual(buf.dequeue(), 1);
  assert.strictEqual(buf.dequeue(), 2);
  assert.strictEqual(buf.dequeue(), 3);
  assert.strictEqual(buf.isEmpty(), true);
  assert.strictEqual(buf.dequeue(), undefined);
  assert.strictEqual(buf.peek(), undefined);
});

test("overwrite on full buffer", () => {
  const buf = new CircularBuffer<string>(2);
  buf.enqueue("a");
  buf.enqueue("b");
  assert.strictEqual(buf.isFull(), true);
  buf.enqueue("c"); // overwrites "a"
  assert.strictEqual(buf.size(), 2);
  assert.strictEqual(buf.peek(), "b");
  assert.strictEqual(buf.dequeue(), "b");
  assert.strictEqual(buf.dequeue(), "c");
  assert.strictEqual(buf.isEmpty(), true);
});

test("empty buffer edge cases", () => {
  const buf = new CircularBuffer<number>(1);
  assert.strictEqual(buf.isEmpty(), true);
  assert.strictEqual(buf.dequeue(), undefined);
  assert.strictEqual(buf.peek(), undefined);
  buf.enqueue(42);
  assert.strictEqual(buf.dequeue(), 42);
  assert.strictEqual(buf.dequeue(), undefined);
});

test("capacity zero throws error", () => {
  assert.throws(() => new CircularBuffer<number>(0), /positive integer/);
  assert.throws(() => new CircularBuffer<number>(-1), /positive integer/);
});
