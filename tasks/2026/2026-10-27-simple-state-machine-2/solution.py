class DoorStateMachine:
    def __init__(self):
        self.state = 'CLOSED'
        self.transitions = {
            ('CLOSED', 'open'): 'OPEN',
            ('OPEN', 'close'): 'CLOSED',
            ('CLOSED', 'lock'): 'LOCKED',
            ('LOCKED', 'unlock'): 'CLOSED',
        }

    def process_event(self, event: str) -> str:
        key = (self.state, event)
        if key not in self.transitions:
            raise ValueError(f"Invalid event '{event}' for state '{self.state}'")
        self.state = self.transitions[key]
        return self.state
