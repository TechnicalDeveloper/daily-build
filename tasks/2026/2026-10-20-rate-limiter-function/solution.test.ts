import test from 'node:test';
import assert from 'node:assert';
import { createRateLimiter } from './solution';

test('allows calls up to limit', () => {
  const limiter = createRateLimiter(3, 100);
  assert.strictEqual(limiter.call(), true);
  assert.strictEqual(limiter.call(), true);
  assert.strictEqual(limiter.call(), true);
});

test('blocks calls beyond limit within window', () => {
  const limiter = createRateLimiter(2, 200);
  assert.strictEqual(limiter.call(), true);
  assert.strictEqual(limiter.call(), true);
  assert.strictEqual(limiter.call(), false);
});

test('resets after window expires', async () => {
  const limiter = createRateLimiter(1, 50);
  assert.strictEqual(limiter.call(), true);
  assert.strictEqual(limiter.call(), false);
  // wait for window to expire
  await new Promise(resolve => setTimeout(resolve, 60));
  assert.strictEqual(limiter.call(), true);
});

test('handles multiple windows', async () => {
  const limiter = createRateLimiter(2, 60);
  assert.strictEqual(limiter.call(), true);
  assert.strictEqual(limiter.call(), true);
  assert.strictEqual(limiter.call(), false);
  await new Promise(resolve => setTimeout(resolve, 70));
  assert.strictEqual(limiter.call(), true);
  assert.strictEqual(limiter.call(), true);
  assert.strictEqual(limiter.call(), false);
});

test('throws on invalid parameters', () => {
  assert.throws(() => createRateLimiter(0, 100), /positive/);
  assert.throws(() => createRateLimiter(-1, 100), /positive/);
  assert.throws(() => createRateLimiter(1, 0), /positive/);
  assert.throws(() => createRateLimiter(1, -1), /positive/);
});
