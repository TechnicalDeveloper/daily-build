import test from "node:test";
import assert from "node:assert";
import { RollingHash } from "./solution";

test("RollingHash basic functionality", () => {
  const rh = new RollingHash(3);
  assert.strictEqual(rh.isFull(), false);
  rh.addChar("a");
  assert.strictEqual(rh.isFull(), false);
  rh.addChar("b");
  assert.strictEqual(rh.isFull(), false);
  rh.addChar("c");
  assert.strictEqual(rh.isFull(), true);
  const expected = (97 * 256 * 256 + 98 * 256 + 99) % 1_000_000_007;
  assert.strictEqual(rh.getHash(), expected);
});

test("Sliding window update", () => {
  const rh = new RollingHash(3);
  rh.addChar("a");
  rh.addChar("b");
  rh.addChar("c");
  const h1 = rh.getHash();
  rh.addChar("d");
  const expected = (98 * 256 * 256 + 99 * 256 + 100) % 1_000_000_007;
  assert.strictEqual(rh.getHash(), expected);
});

test("Window size 1", () => {
  const rh = new RollingHash(1);
  rh.addChar("x");
  assert.strictEqual(rh.getHash(), "x".charCodeAt(0));
  rh.addChar("y");
  assert.strictEqual(rh.getHash(), "y".charCodeAt(0));
});

test("Custom base and mod", () => {
  const rh = new RollingHash(2, { base: 10, mod: 100 });
  rh.addChar("a");
  rh.addChar("b");
  assert.strictEqual(rh.getHash(), 68);
  rh.addChar("c");
  assert.strictEqual(rh.getHash(), 79);
});

test("Throws when window not full", () => {
  const rh = new RollingHash(3);
  rh.addChar("a");
  assert.throws(() => rh.getHash(), /Window not full/);
  rh.addChar("b");
  assert.throws(() => rh.getHash(), /Window not full/);
});

test("Reset works", () => {
  const rh = new RollingHash(2);
  rh.addChar("a");
  rh.addChar("b");
  assert.strictEqual(rh.isFull(), true);
  rh.reset();
  assert.strictEqual(rh.isFull(), false);
  assert.throws(() => rh.getHash(), /Window not full/);
});

test("Negative modulo fix", () => {
  const rh = new RollingHash(2, { base: 10, mod: 5 });
  rh.addChar("a");
  rh.addChar("b");
  assert.strictEqual(rh.getHash(), 3);
  rh.addChar("c");
  assert.strictEqual(rh.getHash(), 4);
});
