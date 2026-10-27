import test from "node:test";
import assert from "node:assert";
import { parse } from "./solution";

test("empty string returns empty object", () => {
  assert.deepStrictEqual(parse(""), {});
});

test("single key-value pair", () => {
  assert.deepStrictEqual(parse("foo=bar"), { foo: "bar" });
});

test("multiple lines with comments and blanks", () => {
  const input = `# this is a comment
key1=value1

key2=value2
# another comment`;
  assert.deepStrictEqual(parse(input), { key1: "value1", key2: "value2" });
});

test("duplicate keys: last value wins", () => {
  const input = `a=first\na=second`;
  assert.deepStrictEqual(parse(input), { a: "second" });
});

test("leading/trailing whitespace around key and value", () => {
  const input = `  x =  y  `;
  assert.deepStrictEqual(parse(input), { x: "y" });
});

test("line with key but no value (starts with =)", () => {
  const input = `=onlyvalue`;
  // If key is empty after trimming, it should be ignored per the implementation
  assert.deepStrictEqual(parse(input), {});
});
