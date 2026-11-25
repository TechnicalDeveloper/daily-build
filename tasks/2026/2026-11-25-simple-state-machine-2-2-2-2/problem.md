# Simple State Machine

Build a small state machine factory.

Signature:

```ts
export function createStateMachine<
  S extends string,
  E extends string
>(config: StateMachineConfig<S, E>): StateMachine<S, E>
```

The config contains an `initial` state, a list of `states`, and a list of `transitions` with `from`, `event`, and `to` fields. The returned machine exposes `getState()`, `transition(event)`, `can(event)`, and `reset()`.

Respect these edge cases:
- `transition` with an event that is not allowed from the current state must throw and leave the state unchanged.
- `can` must return a boolean and must not mutate the state.
- `reset` must return the machine to its `initial` state.

Use `as const` when passing state strings so TypeScript preserves the literal unions.
