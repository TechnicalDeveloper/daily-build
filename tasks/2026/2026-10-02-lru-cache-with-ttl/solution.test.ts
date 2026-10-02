import test from "node:test";
import assert from "node:assert";
import { LRUCache } from "./solution";

test("LRU eviction on capacity", () => {
  const cache = new LRUCache<string, number>(2, 100000);
  cache.set("a", 1);
  cache.set("b", 2);
  assert.strictEqual(cache.get("a"), 1);
  cache.set("c", 3);
  assert.strictEqual(cache.get("b"), undefined);
  assert.strictEqual(cache.size, 2);
});

test("TTL expiry", async () => {
  const cache = new LRUCache<string, number>(2, 50);
  cache.set("x", 42);
  assert.strictEqual(cache.get("x"), 42);
  await new Promise((resolve) => setTimeout(resolve, 60));
  assert.strictEqual(cache.get("x"), undefined);
  assert.strictEqual(cache.size, 0);
});

test("Update resets TTL", async () => {
  const cache = new LRUCache<string, number>(2, 50);
  cache.set("y", 1);
  await new Promise((resolve) => setTimeout(resolve, 30));
  cache.set("y", 2);
  await new Promise((resolve) => setTimeout(resolve, 30));
  assert.strictEqual(cache.get("y"), 2);
  await new Promise((resolve) => setTimeout(resolve, 30));
  assert.strictEqual(cache.get("y"), undefined);
});

test("delete removes entry", () => {
  const cache = new LRUCache<string, number>(2, 1000);
  cache.set("a", 1);
  assert.strictEqual(cache.delete("a"), true);
  assert.strictEqual(cache.get("a"), undefined);
  assert.strictEqual(cache.size, 0);
  assert.strictEqual(cache.delete("nonexistent"), false);
});

test("expired entries are removed on get and size decreases", async () => {
  const cache = new LRUCache<string, number>(5, 30);
  cache.set("k", 10);
  await new Promise((resolve) => setTimeout(resolve, 40));
  cache.get("k");
  assert.strictEqual(cache.size, 0);
});
