import test from "node:test";
import assert from "node:assert";
import { debounce } from "./solution";

test("debounce delays invocation", async () => {
  let calls = 0;
  const fn = debounce(() => { calls++; }, 30);
  fn();
  fn();
  fn();
  assert.equal(calls, 0);
  await new Promise(r => setTimeout(r, 50));
  assert.equal(calls, 1);
});

test("debounce passes arguments", async () => {
  let result;
  const fn = debounce((x: number, y: number) => { result = x + y; }, 20);
  fn(2, 3);
  await new Promise(r => setTimeout(r, 40));
  assert.equal(result, 5);
});

test("debounce resets timer on repeated calls", async () => {
  let calls = 0;
  const fn = debounce(() => { calls++; }, 30);
  fn();
  await new Promise(r => setTimeout(r, 10));
  fn();
  await new Promise(r => setTimeout(r, 10));
  fn();
  assert.equal(calls, 0);
  await new Promise(r => setTimeout(r, 50));
  assert.equal(calls, 1);
});

test("debounce does not call before delay", async () => {
  let called = false;
  const fn = debounce(() => { called = true; }, 20);
  fn();
  assert.equal(called, false);
  await new Promise(r => setTimeout(r, 10));
  assert.equal(called, false);
  await new Promise(r => setTimeout(r, 20));
  assert.equal(called, true);
});
