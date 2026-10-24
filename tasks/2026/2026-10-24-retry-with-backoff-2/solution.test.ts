import test from "node:test";
import assert from "node:assert";
import { retry } from "./solution";

test("succeeds on first attempt", async () => {
  let callCount = 0;
  const fn = async () => {
    callCount++;
    return "success";
  };
  const result = await retry(fn, { maxRetries: 3, baseDelay: 10 });
  assert.strictEqual(result, "success");
  assert.strictEqual(callCount, 1);
});

test("retries and eventually succeeds", async () => {
  let callCount = 0;
  const fn = async () => {
    callCount++;
    if (callCount < 3) throw new Error("fail");
    return "ok";
  };
  const result = await retry(fn, { maxRetries: 3, baseDelay: 1 });
  assert.strictEqual(result, "ok");
  assert.strictEqual(callCount, 3);
});

test("fails after exhausting retries", async () => {
  const fn = async () => {
    throw new Error("permanent failure");
  };
  await assert.rejects(
    retry(fn, { maxRetries: 2, baseDelay: 1 }),
    /permanent failure/
  );
});

test("zero retries calls fn once and rejects on failure", async () => {
  let callCount = 0;
  const fn = async () => {
    callCount++;
    throw new Error("no retry");
  };
  await assert.rejects(
    retry(fn, { maxRetries: 0, baseDelay: 100 }),
    /no retry/
  );
  assert.strictEqual(callCount, 1);
});

test("handles synchronous throw", async () => {
  let callCount = 0;
  const fn = () => {
    callCount++;
    throw new Error("sync error");
  };
  await assert.rejects(
    retry(fn, { maxRetries: 1, baseDelay: 1 }),
    /sync error/
  );
  assert.strictEqual(callCount, 2);
});
