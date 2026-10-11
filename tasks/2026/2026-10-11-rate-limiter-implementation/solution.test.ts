import test from 'node:test';
import assert from 'node:assert';
import { RateLimiter } from './solution';

test('RateLimiter: allows first request', () => {
  const limiter = new RateLimiter(2, 1000);
  assert.strictEqual(limiter.isAllowed('alice'), true);
});

test('RateLimiter: limits when exceeding max requests within window', () => {
  const limiter = new RateLimiter(2, 500);
  limiter.isAllowed('bob');
  limiter.isAllowed('bob');
  assert.strictEqual(limiter.isAllowed('bob'), false);
});

test('RateLimiter: allows requests after window expires', async () => {
  const limiter = new RateLimiter(2, 100);
  limiter.isAllowed('charlie');
  limiter.isAllowed('charlie');
  assert.strictEqual(limiter.isAllowed('charlie'), false);
  // Wait for window to expire
  await new Promise(resolve => setTimeout(resolve, 150));
  assert.strictEqual(limiter.isAllowed('charlie'), true);
});

test('RateLimiter: reset clears all state', () => {
  const limiter = new RateLimiter(1, 1000);
  limiter.isAllowed('dave');
  assert.strictEqual(limiter.isAllowed('dave'), false);
  limiter.reset();
  assert.strictEqual(limiter.isAllowed('dave'), true);
  assert.strictEqual(limiter.isAllowed('dave'), false);
});

test('RateLimiter: independent keys do not interfere', () => {
  const limiter = new RateLimiter(1, 1000);
  limiter.isAllowed('eve');
  limiter.isAllowed('frank');
  assert.strictEqual(limiter.isAllowed('eve'), false);
  assert.strictEqual(limiter.isAllowed('frank'), false);
});
