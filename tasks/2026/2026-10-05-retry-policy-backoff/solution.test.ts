import test from "node:test";
import assert from "node:assert";
import { retryWithBackoff } from "./solution";

test("succeeds on first try", async () => {
  let callCount = 0;
  const result = await retryWithBackoff(async () => {
    callCount++;
    return "ok";
  });
  assert.strictEqual(result, "ok");
  assert.strictEqual(callCount, 1);
});

test("succeeds after two retries", async () => {
  let attempts = 0;
  const fn = async () => {
    attempts++;
    if (attempts <= 2) throw new Error("fail");
    return "success";
  };
  const result = await retryWithBackoff(fn, { maxRetries: 3, baseDelay: 10 });
  assert.strictEqual(result, "success");
  assert.strictEqual(attempts, 3);
});

test("fails after max retries", async () => {
  const err = new Error("always fail");
  const fn = async () => {
    throw err;
  };
  await assert.rejects(
    retryWithBackoff(fn, { maxRetries: 2, baseDelay: 10 }),
    (e) => e === err
  );
});

test("default options cause correct number of attempts", async () => {
  let calls = 0;
  const fn = async () => {
    calls++;
    throw new Error("x");
  };
  await assert.rejects(
    retryWithBackoff(fn),
    (e) => (e as Error).message === "x"
  );
  assert.strictEqual(calls, 4); // 1 initial + 3 retries
});
