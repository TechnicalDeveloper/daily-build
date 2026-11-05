# Simple State Machine

Implement a simple state machine class `StateMachine` that manages transitions between states.

## Signature

```python
class StateMachine:
    def __init__(self, initial_state: str, transitions: dict):
        """
        initial_state: The starting state (a string).
        transitions: A dictionary mapping (current_state, event) -> next_state.
        """
        ...

    def send(self, event: str) -> str:
        """
        Process an event. If the event is valid for the current state, transition to the next state.
        Returns the new state (or the current state if the transition is invalid).
        """
        ...

    def current_state(self) -> str:
        ...
```

## Edge Cases
- Attempting an invalid transition (event not defined for current state) : should return the current state unchanged.
- Empty transitions dict: only the initial state exists; any event returns the initial state.
- Transition to the same state should be handled correctly if defined within transitions.
