import test from "node:test";
import assert from "node:assert";
import { BackpressureQueue } from "./solution";

test("basic enqueue and dequeue in order", async () => {
  const q = new BackpressureQueue<number>(5);
  await q.enqueue(1);
  await q.enqueue(2);
  assert.strictEqual(await q.dequeue(), 1);
  assert.strictEqual(await q.dequeue(), 2);
});

test("dequeue waits for enqueue", async () => {
  const q = new BackpressureQueue<number>(5);
  const dequeuePromise = q.dequeue();
  // No item yet – should wait
  setTimeout(() => q.enqueue(42), 10);
  assert.strictEqual(await dequeuePromise, 42);
});

test("enqueue waits when full", async () => {
  const q = new BackpressureQueue<number>(2);
  await q.enqueue(1);
  await q.enqueue(2);

  const enqueuePromise = q.enqueue(3); // should wait because queue is full
  const val1 = await q.dequeue();
  assert.strictEqual(val1, 1);
  await enqueuePromise; // now the enqueue resolves

  const val2 = await q.dequeue();
  assert.strictEqual(val2, 2);
  const val3 = await q.dequeue();
  assert.strictEqual(val3, 3);
});

test("multiple producers and consumers served in order", async () => {
  const q = new BackpressureQueue<string>(3);
  // Fill the queue
  await q.enqueue("a");
  await q.enqueue("b");
  await q.enqueue("c");

  // Two producers wait because queue is full
  const enq1 = q.enqueue("d");
  const enq2 = q.enqueue("e");

  // One consumer takes the first item (a), freeing a slot
  assert.strictEqual(await q.dequeue(), "a");
  await enq1; // producer 'd' should now be accepted

  // Next consumer takes b; producer 'e' gets in afterwards
  assert.strictEqual(await q.dequeue(), "b");
  await enq2;

  // Remaining items: c, d, e (in that order)
  assert.strictEqual(await q.dequeue(), "c");
  assert.strictEqual(await q.dequeue(), "d");
  assert.strictEqual(await q.dequeue(), "e");
});
