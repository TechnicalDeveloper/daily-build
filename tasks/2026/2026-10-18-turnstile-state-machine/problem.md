# Turnstile State Machine

Implement a simple state machine for a turnstile.

The turnstile has two possible states:
- `'locked'`
- `'unlocked'`

It accepts two actions: `'coin'` and `'push'`.

**Transitions**
- If the turnstile is `locked` and receives a `'coin'`, it transitions to `unlocked`.
- If the turnstile is `locked` and receives a `'push'`, it stays `locked`.
- If the turnstile is `unlocked` and receives a `'push'`, it transitions to `locked`.
- If the turnstile is `unlocked` and receives a `'coin'`, it stays `unlocked`.

**Signature**
- `__init__(self) -> None`
- `action(self, action: str) -> None`
- `get_state(self) -> str`

**Edge cases to respect**
- The initial state must be `'locked'`.
- Passing an invalid action (anything other than `'coin'` or `'push'`) must raise a `ValueError`.
- Multiple actions in sequence should be processed correctly.
