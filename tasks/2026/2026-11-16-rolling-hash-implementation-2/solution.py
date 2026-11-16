class RollingHash:
    """Rolling hash for a fixed-size window over a string."""

    def __init__(self, text: str, window_size: int, base: int = 256, mod: int = 10**9 + 7):
        if window_size <= 0:
            raise ValueError("window_size must be positive")
        if window_size > len(text):
            raise ValueError("window_size cannot be larger than text length")
        self.text = text
        self.window_size = window_size
        self.base = base
        self.mod = mod

        # Precompute powers of base modulo mod
        self.power = [1] * (window_size + 1)
        for i in range(1, window_size + 1):
            self.power[i] = (self.power[i - 1] * base) % mod

        # Compute hash for the first window
        self.current_hash = 0
        for i in range(window_size):
            self.current_hash = (self.current_hash * base + ord(text[i])) % mod

        self.start = 0

    def get_hash(self) -> int:
        """Return the current hash value."""
        return self.current_hash

    def roll(self) -> bool:
        """Advance the window by one character. Returns False if at the end."""
        if self.start + self.window_size >= len(self.text):
            return False

        old_char = ord(self.text[self.start])
        new_char = ord(self.text[self.start + self.window_size])

        # Remove leftmost char contribution
        self.current_hash = (self.current_hash - old_char * self.power[self.window_size - 1]) % self.mod
        # Shift and add new char
        self.current_hash = (self.current_hash * self.base + new_char) % self.mod

        self.start += 1
        return True
