
class Turnstile:
    def __init__(self):
        self._state = "locked"

    def action(self, action: str) -> None:
        if action not in ("coin", "push"):
            raise ValueError(f"Invalid action: {action}")
        if self._state == "locked":
            if action == "coin":
                self._state = "unlocked"
        else:  # unlocked
            if action == "push":
                self._state = "locked"

    def get_state(self) -> str:
        return self._state
