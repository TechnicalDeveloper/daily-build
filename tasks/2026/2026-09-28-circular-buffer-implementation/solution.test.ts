import test from "node:test";
import assert from "node:assert";
import { CircularBuffer } from "./solution";

test("push and pop basics", () => {
  const buf = new CircularBuffer<number>(3);
  buf.push(1);
  buf.push(2);
  assert.strictEqual(buf.size(), 2);
  assert.strictEqual(buf.pop(), 1);
  assert.strictEqual(buf.pop(), 2);
  assert.strictEqual(buf.pop(), undefined);
  assert.strictEqual(buf.size(), 0);
});

test("overwrite behavior when full", () => {
  const buf = new CircularBuffer<number>(3);
  buf.push(1);
  buf.push(2);
  buf.push(3);
  assert.strictEqual(buf.isFull(), true);
  buf.push(4); // overwrites 1
  assert.strictEqual(buf.size(), 3);
  assert.strictEqual(buf.pop(), 2);
  assert.strictEqual(buf.pop(), 3);
  assert.strictEqual(buf.pop(), 4);
  assert.strictEqual(buf.pop(), undefined);
});

test("pop from empty returns undefined", () => {
  const buf = new CircularBuffer<string>(2);
  assert.strictEqual(buf.pop(), undefined);
});

test("isEmpty and isFull", () => {
  const buf = new CircularBuffer<number>(2);
  assert.strictEqual(buf.isEmpty(), true);
  assert.strictEqual(buf.isFull(), false);
  buf.push(10);
  assert.strictEqual(buf.isEmpty(), false);
  buf.push(20);
  assert.strictEqual(buf.isFull(), true);
  buf.pop();
  assert.strictEqual(buf.isFull(), false);
  assert.strictEqual(buf.isEmpty(), false);
});
