import test from "node:test";
import assert from "node:assert";
import { AsyncQueue } from "./solution";

test("basic push and pop (FIFO)", async () => {
  const q = new AsyncQueue<number>(3);
  await q.push(1);
  await q.push(2);
  await q.push(3);
  assert.strictEqual(await q.pop(), 1);
  assert.strictEqual(await q.pop(), 2);
  assert.strictEqual(await q.pop(), 3);
});

test("push blocks when full and pop frees", async () => {
  const q = new AsyncQueue<number>(2);
  await q.push(1);
  await q.push(2);
  const pushPromise = q.push(3);
  const val = await q.pop();
  assert.strictEqual(val, 1);
  await pushPromise;
  assert.strictEqual(await q.pop(), 2);
  assert.strictEqual(await q.pop(), 3);
});

test("pop blocks when empty and push resolves", async () => {
  const q = new AsyncQueue<number>(2);
  const popPromise = q.pop();
  await q.push(10);
  const val = await popPromise;
  assert.strictEqual(val, 10);
});

test("order preserved with interleaved operations", async () => {
  const q = new AsyncQueue<number>(1);
  const results: number[] = [];
  const push1 = q.push(1);
  const push2 = (async () => {
    await q.push(2);
    results.push(99); // should happen after first pop
  })();
  results.push(await q.pop()); // 1
  await push1;
  await push2;
  assert.deepStrictEqual(results, [1, 99]);
  const last = await q.pop();
  assert.strictEqual(last, 2);
});

test("capacity validation", async () => {
  assert.throws(() => new AsyncQueue<number>(0), /positive/);
  assert.throws(() => new AsyncQueue<number>(-1), /positive/);
});
