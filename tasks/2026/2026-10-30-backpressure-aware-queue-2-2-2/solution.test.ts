import test from 'node:test';
import assert from 'node:assert';
import { BackpressureQueue } from './solution';

test('runs tasks with given concurrency', async () => {
  const queue = new BackpressureQueue(2);
  let running = 0;
  let maxRunning = 0;
  const tasks = Array.from({ length: 5 }, (_, i) =>
    queue.push(async () => {
      running++;
      maxRunning = Math.max(maxRunning, running);
      await new Promise((r) => setTimeout(r, 10));
      running--;
      return i;
    })
  );
  const results = await Promise.all(tasks);
  assert.deepStrictEqual(results, [0, 1, 2, 3, 4]);
  assert.ok(maxRunning <= 2, `maxRunning was ${maxRunning}`);
});

test('throws if concurrency is less than 1', () => {
  assert.throws(() => new BackpressureQueue(0), /Concurrency must be at least 1/);
  assert.throws(() => new BackpressureQueue(-1), /Concurrency must be at least 1/);
});

test('drain resolves when all tasks are done', async () => {
  const queue = new BackpressureQueue(1);
  let completed = false;
  queue.push(async () => {
    await new Promise((r) => setTimeout(r, 20));
    completed = true;
  });
  assert.strictEqual(completed, false);
  await queue.drain();
  assert.strictEqual(completed, true);
});

test('drain resolves immediately on empty queue', async () => {
  const queue = new BackpressureQueue(1);
  await queue.drain();
  assert.strictEqual(queue.size, 0);
  assert.strictEqual(queue.pending, 0);
});

test('rejected tasks do not block others and propagate error', async () => {
  const queue = new BackpressureQueue(2);
  const p1 = queue.push(async () => {
    throw new Error('fail');
  });
  const p2 = queue.push(async () => 'ok');
  await assert.rejects(p1, /fail/);
  assert.strictEqual(await p2, 'ok');
});

test('size and pending reflect queue state', async () => {
  const queue = new BackpressureQueue(1);
  let release: () => void = () => {};
  const gate = new Promise<void>((r) => { release = r; });
  const p1 = queue.push(async () => { await gate; });
  const p2 = queue.push(async () => 'second');
  assert.strictEqual(queue.pending, 1);
  assert.strictEqual(queue.size, 1);
  release();
  await p1;
  await p2;
  await queue.drain();
  assert.strictEqual(queue.pending, 0);
  assert.strictEqual(queue.size, 0);
});
