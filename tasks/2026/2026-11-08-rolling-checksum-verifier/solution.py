class RollingChecksum:
    def __init__(self, window_size: int):
        if window_size <= 0:
            raise ValueError("window_size must be > 0")
        self.window_size = window_size
        self.buffer = []
        self.checksum = 0

    def update(self, new_byte: int, old_byte: int = None) -> None:
        if old_byte is None:
            self.buffer.append(new_byte)
            self.checksum = (self.checksum + new_byte) % 256
        else:
            self.checksum = (self.checksum - old_byte + new_byte) % 256
            if self.buffer:
                self.buffer.pop(0)
                self.buffer.append(new_byte)

    def digest(self) -> int:
        return self.checksum
