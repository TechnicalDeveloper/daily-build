import test from "node:test";
import assert from "node:assert";
import { debounce } from "./solution";

const sleep = (ms: number): Promise<void> =>
  new Promise((resolve) => setTimeout(resolve, ms));

test("delays execution until the wait time has passed", async () => {
  let calls = 0;

  const debounced = debounce(() => {
    calls++;
  }, 20);

  debounced();

  assert.equal(calls, 0);

  await sleep(30);

  assert.equal(calls, 1);
});

test("collapses a burst into one call with the last arguments", async () => {
  const received: string[] = [];

  const debounced = debounce((value: string) => {
    received.push(value);
  }, 20);

  debounced("a");
  debounced("b");
  debounced("c");

  assert.deepEqual(received, []);

  await sleep(30);

  assert.deepEqual(received, ["c"]);
});

test("cancel discards a pending invocation", async () => {
  let calls = 0;

  const debounced = debounce(() => {
    calls++;
  }, 20);

  debounced();
  debounced.cancel();

  await sleep(30);

  assert.equal(calls, 0);
});

test("flush invokes a pending call immediately without a later duplicate", async () => {
  let calls = 0;

  const debounced = debounce(() => {
    calls++;
  }, 20);

  debounced();
  debounced.flush();

  assert.equal(calls, 1);

  await sleep(30);

  assert.equal(calls, 1);
});

test("a completed debounce can start a new burst", async () => {
  let calls = 0;

  const debounced = debounce(() => {
    calls++;
  }, 20);

  debounced();

  await sleep(30);

  assert.equal(calls, 1);

  debounced();

  assert.equal(calls, 1);

  await sleep(30);

  assert.equal(calls, 2);
});
