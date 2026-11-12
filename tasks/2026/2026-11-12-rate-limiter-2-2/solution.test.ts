import test from "node:test";
import assert from "node:assert";
import { RateLimiter } from "./solution";

test("allows up to limit requests within a window", () => {
    const limiter = new RateLimiter(3, 1000);
    assert.strictEqual(limiter.isAllowed("a"), true);
    assert.strictEqual(limiter.isAllowed("a"), true);
    assert.strictEqual(limiter.isAllowed("a"), true);
    assert.strictEqual(limiter.isAllowed("a"), false);
});

test("resets after the time window expires", async () => {
    const limiter = new RateLimiter(2, 50);
    assert.strictEqual(limiter.isAllowed("a"), true);
    assert.strictEqual(limiter.isAllowed("a"), true);
    assert.strictEqual(limiter.isAllowed("a"), false);

    await new Promise(resolve => setTimeout(resolve, 60)); // wait > 50ms
    assert.strictEqual(limiter.isAllowed("a"), true);
});

test("tracks keys independently", () => {
    const limiter = new RateLimiter(1, 1000);
    assert.strictEqual(limiter.isAllowed("user1"), true);
    assert.strictEqual(limiter.isAllowed("user2"), true);
    assert.strictEqual(limiter.isAllowed("user1"), false);
    assert.strictEqual(limiter.isAllowed("user2"), false);
});

test("throws on invalid constructor arguments", () => {
    assert.throws(() => new RateLimiter(0, 1000), RangeError);
    assert.throws(() => new RateLimiter(3, 0), RangeError);
});

test("resetKey allows new requests immediately", () => {
    const limiter = new RateLimiter(1, 1000);
    assert.strictEqual(limiter.isAllowed("a"), true);
    assert.strictEqual(limiter.isAllowed("a"), false);
    limiter.resetKey("a");
    assert.strictEqual(limiter.isAllowed("a"), true);
});
