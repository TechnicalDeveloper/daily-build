# Simple State Machine

Build a minimal finite-state machine with a state and a transition table.

Signature:
- `InvalidTransition(Exception)`
- `StateMachine(initial_state: str, transitions: dict[tuple[str, str], str])`
- `StateMachine.state -> str`
- `StateMachine.send(event: str) -> str`

Details:
- `transitions` maps `(state, event)` pairs to the next state.
- `state` is a read-only property returning the current state.
- `send` fires `event`; if `(current_state, event)` is in the table, it sets the new state and returns it.
- If `(current_state, event)` is not in the table, raise `InvalidTransition` and do not change the current state.

Edge cases:
- The current state must remain unchanged when an event is invalid.
- After a valid event, `send` must return the newly entered state.
- Mutating the original `transitions` dict after constructing the machine must not affect the machine.
