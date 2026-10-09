# Simple State Machine

Build a simple deterministic finite state machine. It should maintain a current state and allow transitions defined as `(state, event) -> next_state`.

Signature:

```python
class StateMachine:
    def __init__(self, initial_state: str): ...
    def add_transition(self, state: str, event: str, next_state: str) -> None: ...
    def send(self, event: str) -> str: ...
```

The `send` method should process an event, update the current state, and return the new state. If the event is not valid from the current state, raise `ValueError`.

Edge cases to respect:
- Sending an event that has no transition from the current state must raise a `ValueError`.
- The same event may have different next states depending on the current state.
- Adding a transition for the same `(state, event)` pair replaces the old transition.
