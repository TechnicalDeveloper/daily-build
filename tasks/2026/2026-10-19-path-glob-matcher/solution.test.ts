import test from "node:test";
import assert from "node:assert";
import { match } from "./solution";

test("Exact match", () => {
    assert.strictEqual(match("hello.txt", "hello.txt"), true);
    assert.strictEqual(match("hello.txt", "hello.TXT"), false);
});

test("Star wildcard", () => {
    assert.strictEqual(match("*.txt", "readme.txt"), true);
    assert.strictEqual(match("*.txt", "readme.md"), false);
    assert.strictEqual(match("*", ""), true);
    assert.strictEqual(match("*", "anything"), true);
    assert.strictEqual(match("*", "path/with/slash"), false);
});

test("Question mark wildcard", () => {
    assert.strictEqual(match("file?.txt", "file1.txt"), true);
    assert.strictEqual(match("file?.txt", "file.txt"), false);
    assert.strictEqual(match("file?.txt", "file12.txt"), false);
    assert.strictEqual(match("??.txt", "ab.txt"), true);
    assert.strictEqual(match("??.txt", "a.txt"), false);
});

test("Path separators", () => {
    assert.strictEqual(match("a/*", "a/b"), true);
    assert.strictEqual(match("a/*", "a/b/c"), false);
    assert.strictEqual(match("a/*/c", "a/x/c"), true);
    assert.strictEqual(match("a/*/c", "a/x/y/c"), false);
    assert.strictEqual(match("a/b?c", "a/bxc"), true);
});

test("Edge cases", () => {
    assert.strictEqual(match("", ""), true);
    assert.strictEqual(match("", "a"), false);
    assert.strictEqual(match("a/", "a/"), true);
    assert.strictEqual(match("a/", "a"), false);
});
