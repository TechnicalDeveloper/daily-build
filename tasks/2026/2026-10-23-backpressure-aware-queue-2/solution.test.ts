import test from 'node:test';
import assert from 'node:assert';
import { BoundedQueue } from './solution';

test('basic enqueue and dequeue', async () => {
  const q = new BoundedQueue<number>(3);
  await q.enqueue(1);
  await q.enqueue(2);
  const v1 = await q.dequeue();
  const v2 = await q.dequeue();
  assert.strictEqual(v1, 1);
  assert.strictEqual(v2, 2);
});

test('dequeue blocks when empty', async () => {
  const q = new BoundedQueue<number>(3);
  const promise = q.dequeue();
  let resolved = false;
  promise.then(() => { resolved = true; });
  await new Promise(r => setTimeout(r, 50));
  assert.strictEqual(resolved, false);
  await q.enqueue(42);
  const val = await promise;
  assert.strictEqual(val, 42);
});

test('enqueue blocks when full', async () => {
  const q = new BoundedQueue<number>(2);
  await q.enqueue(1);
  await q.enqueue(2);
  let resolved = false;
  const promise = q.enqueue(3);
  promise.then(() => { resolved = true; });
  await new Promise(r => setTimeout(r, 50));
  assert.strictEqual(resolved, false);
  const val = await q.dequeue();
  assert.strictEqual(val, 1);
  await promise;
  assert.strictEqual(resolved, true);
  const v1 = await q.dequeue();
  const v2 = await q.dequeue();
  assert.strictEqual(v1, 2);
  assert.strictEqual(v2, 3);
});

test('multiple consumers and producers', async () => {
  const q = new BoundedQueue<number>(2);
  const results: number[] = [];
  const consumer1 = (async () => {
    results.push(await q.dequeue());
  })();
  const consumer2 = (async () => {
    results.push(await q.dequeue());
  })();
  await q.enqueue(10);
  await q.enqueue(20);
  await Promise.all([consumer1, consumer2]);
  assert.deepStrictEqual(results.sort(), [10, 20]);
});

test('FIFO order', async () => {
  const q = new BoundedQueue<number>(5);
  for (let i = 1; i <= 5; i++) {
    await q.enqueue(i);
  }
  for (let i = 1; i <= 5; i++) {
    const v = await q.dequeue();
    assert.strictEqual(v, i);
  }
});
