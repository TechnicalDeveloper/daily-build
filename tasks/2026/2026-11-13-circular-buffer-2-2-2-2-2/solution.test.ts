import { CircularBuffer } from './solution';
import test from 'node:test';
import assert from 'node:assert';

test('push and pop maintain order', () => {
  const buffer = new CircularBuffer<number>(3);
  buffer.push(1);
  buffer.push(2);
  assert.strictEqual(buffer.pop(), 1);
  assert.strictEqual(buffer.pop(), 2);
  assert.strictEqual(buffer.getSize(), 0);
});

test('overwrites oldest when full', () => {
  const buffer = new CircularBuffer<string>(3);
  buffer.push('a');
  buffer.push('b');
  buffer.push('c');
  buffer.push('d');
  assert.strictEqual(buffer.toArray().join(''), 'bcd');
  assert.strictEqual(buffer.pop(), 'b');
  assert.strictEqual(buffer.pop(), 'c');
  assert.strictEqual(buffer.pop(), 'd');
});

test('wraps around indices', () => {
  const buffer = new CircularBuffer<number>(3);
  buffer.push(1);
  buffer.push(2);
  buffer.pop();
  buffer.push(3);
  buffer.push(4);
  assert.deepEqual(buffer.toArray(), [2, 3, 4]);
});

test('throws when popping empty', () => {
  const buffer = new CircularBuffer<number>(2);
  assert.throws(() => buffer.pop(), /empty/i);
  assert.throws(() => buffer.peek(), /empty/i);
});

test('capacity validation', () => {
  assert.throws(() => new CircularBuffer<number>(0), /positive/);
  assert.throws(() => new CircularBuffer<number>(-1), /positive/);
});
