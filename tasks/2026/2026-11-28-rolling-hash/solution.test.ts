import test from "node:test";
import assert from "node:assert";
import { RollingHash } from "./solution";

test("single add sets hash to value", () => {
  const rh = new RollingHash(10, 1000000007);
  rh.add(5);
  assert.strictEqual(rh.getHash(), 5);
  assert.strictEqual(rh.size, 1);
});

test("multiple adds compute polynomial hash", () => {
  const rh = new RollingHash(10, 1000000007);
  rh.add(1);
  rh.add(2);
  rh.add(3);
  // hash = 1*10^2 + 2*10 + 3 = 123
  assert.strictEqual(rh.getHash(), 123);
  assert.strictEqual(rh.size, 3);
});

test("removeLeft subtracts correctly", () => {
  const rh = new RollingHash(10, 1000000007);
  rh.add(1); rh.add(2); rh.add(3);
  rh.removeLeft();
  // remaining [2,3] -> hash = 2*10 + 3 = 23
  assert.strictEqual(rh.getHash(), 23);
  assert.strictEqual(rh.size, 2);
  rh.removeLeft();
  // remaining [3] -> hash = 3
  assert.strictEqual(rh.getHash(), 3);
  assert.strictEqual(rh.size, 1);
});

test("sliding window matches brute force", () => {
  const base = 256;
  const mod = 1000000007;
  const rh = new RollingHash(base, mod);
  const window: number[] = [];
  const bruteForce = (arr: number[]): number => {
    let h = 0;
    for (let i = 0; i < arr.length; i++) {
      h = (h * base + arr[i]) % mod;
    }
    // but our hash is weighted from left, so we need a different brute force:
    // h = sum(arr[i] * base^(len-1-i))
    let bf = 0;
    for (let i = 0; i < arr.length; i++) {
      bf = (bf * base + arr[i]) % mod;
    }
    // Wait, that's same as h? Actually h above is (arr0 * base^2 + arr1 * base + arr2) if len=3.
    // The loop h = (h*base + arr[i]) gives exactly that.
    return bf;
  };

  const data = [7, 2, 9, 4, 1, 8];
  for (let i = 0; i < 3; i++) {
    rh.add(data[i]);
    window.push(data[i]);
  }
  assert.strictEqual(rh.getHash(), bruteForce(window));

  for (let i = 3; i < data.length; i++) {
    rh.removeLeft();
    window.shift();
    rh.add(data[i]);
    window.push(data[i]);
    assert.strictEqual(rh.getHash(), bruteForce(window));
  }
});

test("removing from empty throws", () => {
  const rh = new RollingHash(10, 1000000007);
  assert.throws(() => rh.removeLeft());
});

test("hash always non-negative after operations", () => {
  const rh = new RollingHash(256, 1000000007);
  rh.add(123456789);
  rh.add(987654321);
  rh.removeLeft();
  const h = rh.getHash();
  assert.ok(h >= 0 && h < 1000000007);
});
