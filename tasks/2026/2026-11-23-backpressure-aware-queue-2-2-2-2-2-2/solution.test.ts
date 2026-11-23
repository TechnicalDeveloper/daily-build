import test from 'node:test';
import assert from 'node:assert';
import { BackpressureQueue } from './solution';

test('push resolves immediately while capacity is available', async () => {
  const queue = new BackpressureQueue<number>(2);

  await queue.push(1);
  await queue.push(2);

  assert.equal(await queue.pop(), 1);
  assert.equal(await queue.pop(), 2);
});

test('push waits while the queue is full and resolves after a pop', async () => {
  const queue = new BackpressureQueue<string>(1);

  await queue.push('a');

  let settled = false;
  const pushed = queue.push('b').then(() => {
    settled = true;
  });

  assert.equal(settled, false);
  assert.equal(await queue.pop(), 'a');

  await pushed;
  assert.equal(settled, true);
  assert.equal(await queue.pop(), 'b');
});

test('waiting consumers are resolved in FIFO order', async () => {
  const queue = new BackpressureQueue<number>(1);
  const received: number[] = [];

  const first = queue.pop().then((value) => received.push(value));
  const second = queue.pop().then((value) => received.push(value));

  await queue.push(1);
  await queue.push(2);
  await Promise.all([first, second]);

  assert.deepEqual(received, [1, 2]);
});

test('waiting producers are released in FIFO order', async () => {
  const queue = new BackpressureQueue<number>(1);
  const released: string[] = [];

  await queue.push(1);

  const first = queue.push(2).then(() => released.push('first'));
  const second = queue.push(3).then(() => released.push('second'));

  assert.equal(await queue.pop(), 1);
  await first;

  assert.equal(await queue.pop(), 2);
  await second;

  assert.equal(await queue.pop(), 3);
  assert.deepEqual(released, ['first', 'second']);
});

test('constructor rejects invalid capacity values', () => {
  assert.throws(() => new BackpressureQueue<number>(0), RangeError);
  assert.throws(() => new BackpressureQueue<number>(-1), RangeError);
  assert.throws(() => new BackpressureQueue<number>(1.5), RangeError);
  assert.throws(() => new BackpressureQueue<number>(NaN), RangeError);
});
