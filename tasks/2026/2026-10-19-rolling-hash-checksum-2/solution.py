class RollingHash:
    def __init__(self, base: int, mod: int):
        self.base = base
        self.mod = mod

    def hash(self, s: str) -> int:
        h = 0
        for ch in s:
            h = (h * self.base + ord(ch)) % self.mod
        return h

    def update(self, prev_hash: int, left_char: str, right_char: str, window_len: int) -> int:
        # power = base^(window_len - 1) modulo mod
        power = pow(self.base, window_len - 1, self.mod)
        # remove contribution of left_char
        new_hash = (prev_hash - ord(left_char) * power) % self.mod
        # shift left and add right_char
        new_hash = (new_hash * self.base + ord(right_char)) % self.mod
        return new_hash
