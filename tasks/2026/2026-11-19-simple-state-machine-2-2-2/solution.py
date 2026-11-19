class InvalidTransition(Exception):
    pass


class StateMachine:
    def __init__(self, initial_state, transitions):
        self._state = initial_state
        self._transitions = dict(transitions)

    @property
    def state(self):
        return self._state

    def send(self, event):
        key = (self._state, event)
        if key not in self._transitions:
            raise InvalidTransition(
                f'Event {event!r} is not valid from state {self._state!r}'
            )
        self._state = self._transitions[key]
        return self._state
