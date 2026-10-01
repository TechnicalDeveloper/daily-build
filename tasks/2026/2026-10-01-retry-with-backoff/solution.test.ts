import test from "node:test";
import assert from "node:assert";
import { retryWithBackoff } from "./solution";

test("succeeds on first attempt", async () => {
  const result = await retryWithBackoff(async () => "success");
  assert.strictEqual(result, "success");
});

test("succeeds after one retry", async () => {
  let attempts = 0;
  const fn = async () => {
    attempts++;
    if (attempts === 1) throw new Error("fail");
    return "ok";
  };
  const result = await retryWithBackoff(fn, { maxRetries: 1 });
  assert.strictEqual(result, "ok");
  assert.strictEqual(attempts, 2);
});

test("throws after all retries exhausted", async () => {
  let attempts = 0;
  const fn = async () => {
    attempts++;
    throw new Error("always fail");
  };
  await assert.rejects(
    async () => retryWithBackoff(fn, { maxRetries: 2 }),
    { message: "always fail" }
  );
  assert.strictEqual(attempts, 3); // initial + 2 retries
});

test("does not retry when maxRetries is 0", async () => {
  let attempts = 0;
  const fn = async () => {
    attempts++;
    throw new Error("fail");
  };
  await assert.rejects(
    async () => retryWithBackoff(fn, { maxRetries: 0 }),
    { message: "fail" }
  );
  assert.strictEqual(attempts, 1);
});
