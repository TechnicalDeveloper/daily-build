class Turnstile:
    def __init__(self):
        self.state = 'locked'

    def get_state(self):
        return self.state

    def process_event(self, event):
        if event == 'coin':
            if self.state == 'locked':
                self.state = 'unlocked'
            # If already unlocked, stay unlocked
        elif event == 'push':
            if self.state == 'unlocked':
                self.state = 'locked'
            # If already locked, stay locked
        else:
            raise ValueError("Invalid event: must be 'coin' or 'push'")
        return self.state
