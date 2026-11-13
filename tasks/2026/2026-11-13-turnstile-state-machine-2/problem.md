# Turnstile State Machine

Implement a simple state machine for a turnstile with two states: **locked** and **unlocked**. The turnstile accepts two events: **coin** and **push**. Transitions are:
- When **locked** and a coin is inserted → transition to **unlocked**.
- When **locked** and a push is attempted → stays **locked**.
- When **unlocked** and a push is made → transition to **locked**.
- When **unlocked** and a coin is inserted → stays **unlocked**.

Create a class `Turnstile` with:
- `__init__()`: initializes the state to `'locked'`.
- `get_state()`: returns the current state.
- `process_event(event)`: processes the given event (`'coin'` or `'push'`), updates the state accordingly, and returns the new state. If the event is not one of the two valid strings, raise a `ValueError`.

Edge cases:
- Invalid event must raise `ValueError`.
- Calling `process_event` multiple times should reflect the sequential state updates.
- The state must remain a string: either `'locked'` or `'unlocked'`.
