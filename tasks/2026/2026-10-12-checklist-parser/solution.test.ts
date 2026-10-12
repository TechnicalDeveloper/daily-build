import test from "node:test";
import assert from "node:assert";
import { parseChecklist, Task } from "./solution";

test("parses simple unchecked task", () => {
  const result = parseChecklist("- [ ] Buy milk");
  assert.deepStrictEqual(result, [{ description: "Buy milk", completed: false }]);
});

test("parses simple checked task", () => {
  const result = parseChecklist("- [x] Wash dishes");
  assert.deepStrictEqual(result, [{ description: "Wash dishes", completed: true }]);
});

test("handles multiple tasks, ignoring invalid lines", () => {
  const input = `- [ ] Task A\n- [x] Task B\ninvalid line\n- [ ] Task C\n  - [x] Task D with leading spaces\n`;
  const expected: Task[] = [
    { description: "Task A", completed: false },
    { description: "Task B", completed: true },
    { description: "Task C", completed: false },
    { description: "Task D with leading spaces", completed: true },
  ];
  const result = parseChecklist(input);
  assert.deepStrictEqual(result, expected);
});

test("returns empty array for empty input", () => {
  const result = parseChecklist("");
  assert.deepStrictEqual(result, []);
});

test("ignores lines with missing spaces", () => {
  const input = "-[ ] no space\n- [ ]space after bracket?\n- [x] valid";
  const result = parseChecklist(input);
  assert.deepStrictEqual(result, [
    { description: "valid", completed: true },
  ]);
});
