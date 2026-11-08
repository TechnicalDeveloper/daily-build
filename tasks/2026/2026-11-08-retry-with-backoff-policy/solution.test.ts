import test from "node:test";
import assert from "node:assert";
import { retryWithBackoff } from "./solution";

test("succeeds on first attempt", async () => {
  const result = await retryWithBackoff(async () => "ok", 3, 10);
  assert.strictEqual(result, "ok");
});

test("retries and eventually succeeds", async () => {
  let attempts = 0;
  const result = await retryWithBackoff(async () => {
    attempts++;
    if (attempts < 3) throw new Error("fail");
    return "success";
  }, 4, 5);
  assert.strictEqual(result, "success");
  assert.strictEqual(attempts, 3);
});

test("rejects after maxRetries failures", async () => {
  let attempts = 0;
  await assert.rejects(
    retryWithBackoff(async () => {
      attempts++;
      throw new Error("always fail");
    }, 2, 1),
    /always fail/
  );
  assert.strictEqual(attempts, 3); // 1 initial + 2 retries
});

test("maxRetries = 0 does not retry", async () => {
  let attempts = 0;
  await assert.rejects(
    retryWithBackoff(async () => {
      attempts++;
      throw new Error("no retry");
    }, 0, 100),
    /no retry/
  );
  assert.strictEqual(attempts, 1);
});

test("baseDelayMs = 0 retries immediately", async () => {
  let attempts = 0;
  const result = await retryWithBackoff(async () => {
    attempts++;
    if (attempts < 2) throw new Error("try again");
    return "immediate";
  }, 2, 0);
  assert.strictEqual(result, "immediate");
  assert.strictEqual(attempts, 2);
});

test("handles undefined success value", async () => {
  const result = await retryWithBackoff(async () => undefined, 1, 5);
  assert.strictEqual(result, undefined);
});
