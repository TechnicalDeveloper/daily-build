import test from "node:test";
import assert from "node:assert";
import { vString, vNumber, vBoolean, vArray, vObject, vOptional, vNullable, vAnd, vOr, type Validator } from "./solution";

test("string validator", () => {
  const str = vString();
  assert.deepStrictEqual(str("hello"), { success: true, value: "hello" });
  assert.deepStrictEqual(str(42), { success: false, errors: ["expected a string"] });
});

test("number validator rejects NaN", () => {
  const num = vNumber();
  assert.deepStrictEqual(num(123), { success: true, value: 123 });
  assert.deepStrictEqual(num(NaN), { success: false, errors: ["expected a number"] });
  assert.deepStrictEqual(num("1"), { success: false, errors: ["expected a number"] });
});

test("object validator validates shape and reports key errors", () => {
  const obj = vObject({ name: vString(), age: vNumber() });
  const good = { name: "Alice", age: 30 };
  assert.deepStrictEqual(obj(good), { success: true, value: good });
  const bad = { name: 1, age: NaN };
  const result = obj(bad);
  assert.strictEqual(result.success, false);
  if (!result.success) {
    assert.deepStrictEqual(result.errors, ["name: expected a string", "age: expected a number"]);
  }
});

test("array validator validates each element", () => {
  const arr = vArray(vNumber());
  assert.deepStrictEqual(arr([1, 2, 3]), { success: true, value: [1, 2, 3] });
  const result = arr([1, "x", 3]);
  assert.strictEqual(result.success, false);
  if (!result.success) {
    assert.deepStrictEqual(result.errors, ["[1]: expected a number"]);
  }
});

test("optional and nullable validators", () => {
  const opt = vOptional(vString());
  assert.deepStrictEqual(opt(undefined), { success: true, value: undefined });
  assert.deepStrictEqual(opt("abc"), { success: true, value: "abc" });
  assert.deepStrictEqual(opt(null), { success: false, errors: ["expected a string"] });

  const nul = vNullable(vString());
  assert.deepStrictEqual(nul(null), { success: true, value: null });
  assert.deepStrictEqual(nul("abc"), { success: true, value: "abc" });
  assert.deepStrictEqual(nul(undefined), { success: false, errors: ["expected a string"] });
});

test("and / or combinators", () => {
  const even: Validator<number> = (value) => {
    if (typeof value === "number" && value % 2 === 0) {
      return { success: true, value };
    }
    return { success: false, errors: ["expected even number"] };
  };
  const evenNumber = vAnd(vNumber(), even);
  assert.deepStrictEqual(evenNumber(4), { success: true, value: 4 });
  const notEven = evenNumber(3);
  assert.strictEqual(notEven.success, false);

  const stringOrNumber = vOr(vString(), vNumber());
  assert.deepStrictEqual(stringOrNumber("x"), { success: true, value: "x" });
  assert.deepStrictEqual(stringOrNumber(1), { success: true, value: 1 });
  const bad = stringOrNumber(true);
  assert.strictEqual(bad.success, false);
});
