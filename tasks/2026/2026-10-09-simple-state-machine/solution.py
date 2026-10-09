class StateMachine:
    def __init__(self, initial_state: str):
        self.state = initial_state
        self.transitions = {}

    def add_transition(self, state: str, event: str, next_state: str) -> None:
        self.transitions[(state, event)] = next_state

    def send(self, event: str) -> str:
        key = (self.state, event)
        if key not in self.transitions:
            raise ValueError(f'No transition for event {event!r} from state {self.state!r}')
        self.state = self.transitions[key]
        return self.state
