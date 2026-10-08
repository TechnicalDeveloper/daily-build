import test from 'node:test';
import assert from 'node:assert';
import { BackpressureQueue } from './solution';

test('push and pop in order', async () => {
  const queue = new BackpressureQueue<number>(3);
  await queue.push(1);
  await queue.push(2);
  assert.strictEqual(queue.size(), 2);
  const v1 = await queue.pop();
  assert.strictEqual(v1, 1);
  const v2 = await queue.pop();
  assert.strictEqual(v2, 2);
  assert.strictEqual(queue.size(), 0);
});

test('pop blocks when queue is empty', async () => {
  const queue = new BackpressureQueue<string>(2);
  const popPromise = queue.pop();
  // Give a tick to ensure the promise is pending
  await new Promise(r => setTimeout(r, 0));
  await queue.push('hello');
  const result = await popPromise;
  assert.strictEqual(result, 'hello');
});

test('push blocks when queue is full', async () => {
  const queue = new BackpressureQueue<number>(2);
  await queue.push(1);
  await queue.push(2);
  // The third push should wait
  const pushPromise = queue.push(3);
  await new Promise(r => setTimeout(r, 0));
  assert.strictEqual(queue.size(), 2);
  const item = await queue.pop(); // free space
  await pushPromise;              // now the push should have resolved
  assert.strictEqual(queue.size(), 2); // 2 was popped, 3 pushed: still 2 items (2 and 3? Actually after first pop we have 2, then after push we have 2 and 3? Let's trace: initial [1,2]; pop returns 1, queue becomes [2]; push(3) resolves, queue becomes [2,3]; size =2)
  assert.strictEqual(await queue.pop(), 2);
  assert.strictEqual(await queue.pop(), 3);
});

test('multiple concurrent producers and consumers', async () => {
  const queue = new BackpressureQueue<number>(3);
  const promises: Promise<void>[] = [];
  // Push 5 items (3 will go directly, 2 will wait)
  for (let i = 0; i < 5; i++) {
    promises.push(queue.push(i));
  }
  // Now pop 3 times to unblock the waiting pushes
  const results: number[] = [];
  for (let i = 0; i < 5; i++) {
    results.push(await queue.pop());
  }
  await Promise.all(promises);
  assert.deepStrictEqual(results, [0, 1, 2, 3, 4]);
  assert.strictEqual(queue.size(), 0);
});

test('constructor rejects invalid capacity', () => {
  assert.throws(() => new BackpressureQueue(0), /positive integer/);
  assert.throws(() => new BackpressureQueue(-1), /positive integer/);
  assert.throws(() => new BackpressureQueue(1.5), /positive integer/);
  assert.doesNotThrow(() => new BackpressureQueue(1));
});
