# Simple State Machine: Door

Implement a simple state machine for a door. The door can be in one of three states: `'OPEN'`, `'CLOSED'`, `'LOCKED'`. The events are: `'open'`, `'close'`, `'lock'`, `'unlock'`. The initial state is `'CLOSED'`.

Allowed transitions:
- `CLOSED` + `open` → `OPEN`
- `OPEN` + `close` → `CLOSED`
- `CLOSED` + `lock` → `LOCKED`
- `LOCKED` + `unlock` → `CLOSED`

Any other combination of (state, event) should raise a `ValueError` (including unrecognized events).

Signature:
```python
class DoorStateMachine:
    def __init__(self): ...
    def process_event(self, event: str) -> str: ...
```

Edge cases to respect:
1. Trying to lock an already locked door must raise `ValueError`.
2. Trying to open a locked door must raise `ValueError`.
3. Using an unknown event (e.g., `'fly'`) must also raise `ValueError`.
