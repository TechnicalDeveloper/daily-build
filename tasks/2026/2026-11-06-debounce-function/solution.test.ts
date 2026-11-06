import test from "node:test";
import assert from "node:assert";
import { debounce } from "./solution";

test("basic trailing debounce calls only after wait", async () => {
  const calls: number[] = [];
  const fn = (n: number) => calls.push(n);
  const debounced = debounce(fn, 50);

  debounced(1);
  debounced(2);
  debounced(3);

  // No call should have been made yet
  assert.strictEqual(calls.length, 0);

  await new Promise((resolve) => setTimeout(resolve, 100));

  assert.strictEqual(calls.length, 1);
  assert.strictEqual(calls[0], 3);
});

test("leading debounce invokes immediately and then waits", async () => {
  const calls: number[] = [];
  const fn = (n: number) => calls.push(n);
  const debounced = debounce(fn, 50, { leading: true, trailing: true });

  debounced(1); // should invoke immediately
  assert.strictEqual(calls.length, 1);
  assert.strictEqual(calls[0], 1);

  debounced(2); // should not invoke yet (resets timer)
  assert.strictEqual(calls.length, 1);

  await new Promise((resolve) => setTimeout(resolve, 100));

  // trailing call should happen with the last argument
  assert.strictEqual(calls.length, 2);
  assert.strictEqual(calls[1], 2);
});

test("cancel prevents pending invocation", async () => {
  const calls: number[] = [];
  const fn = (n: number) => calls.push(n);
  const debounced = debounce(fn, 50);

  debounced(10);
  debounced.cancel();

  await new Promise((resolve) => setTimeout(resolve, 100));

  assert.strictEqual(calls.length, 0);
});

test("this context is preserved", async () => {
  const obj = {
    value: 42,
    method: function (this: { value: number }) {
      return this.value;
    },
  };

  const results: number[] = [];
  const debounced = debounce(function (this: { value: number }) {
    results.push(this.value);
  }, 50);

  debounced.call(obj);
  await new Promise((resolve) => setTimeout(resolve, 100));

  assert.strictEqual(results.length, 1);
  assert.strictEqual(results[0], 42);
});
