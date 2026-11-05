class StateMachine:
    def __init__(self, initial_state: str, transitions: dict):
        self._state = initial_state
        self._transitions = transitions

    def send(self, event: str) -> str:
        key = (self._state, event)
        if key in self._transitions:
            self._state = self._transitions[key]
        return self._state

    def current_state(self) -> str:
        return self._state
