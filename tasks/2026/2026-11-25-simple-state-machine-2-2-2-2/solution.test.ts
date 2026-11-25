import test from "node:test";
import assert from "node:assert";
import { createStateMachine } from "./solution";

test("follows the defined cycle", () => {
  const machine = createStateMachine({
    initial: "red",
    states: ["red", "green", "yellow"],
    transitions: [
      { from: "red", event: "next", to: "green" },
      { from: "green", event: "next", to: "yellow" },
      { from: "yellow", event: "next", to: "red" },
    ],
  } as const);

  assert.equal(machine.getState(), "red");
  assert.equal(machine.can("next"), true);
  assert.equal(machine.transition("next"), "green");
  assert.equal(machine.getState(), "green");
  assert.equal(machine.transition("next"), "yellow");
  assert.equal(machine.transition("next"), "red");
});

test("rejects events that are not allowed from the current state", () => {
  const door = createStateMachine({
    initial: "closed",
    states: ["closed", "open"],
    transitions: [
      { from: "closed", event: "open", to: "open" },
      { from: "open", event: "close", to: "closed" },
    ],
  } as const);

  assert.equal(door.can("close"), false);
  assert.throws(() => door.transition("close"), /Cannot transition/);
  assert.equal(door.getState(), "closed");
});

test("can checks without mutating state", () => {
  const machine = createStateMachine({
    initial: "idle",
    states: ["idle", "running"],
    transitions: [{ from: "idle", event: "start", to: "running" }],
  } as const);

  assert.equal(machine.can("start"), true);
  assert.equal(machine.getState(), "idle");
});

test("reset returns to the initial state", () => {
  const machine = createStateMachine({
    initial: "off",
    states: ["off", "on"],
    transitions: [{ from: "off", event: "toggle", to: "on" }],
  } as const);

  machine.transition("toggle");
  assert.equal(machine.getState(), "on");

  machine.reset();
  assert.equal(machine.getState(), "off");
});

test("rejects invalid configuration", () => {
  assert.throws(
    () =>
      createStateMachine({
        initial: "missing",
        states: ["idle"],
        transitions: [],
      } as unknown as Parameters<typeof createStateMachine>[0]),
    /not listed/
  );
});
