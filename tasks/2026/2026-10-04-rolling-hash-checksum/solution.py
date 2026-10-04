class RollingHash:
    def __init__(self, window_size: int):
        if window_size <= 0:
            raise ValueError('window_size must be positive')
        self._window_size = window_size
        self._buffer = []
        self._hash = 0
        self._mod = 2**32

    def ingest(self, byte_string: bytes) -> None:
        for b in byte_string:
            # add new byte at end of window
            new_idx = len(self._buffer)
            self._buffer.append(b)
            if new_idx < self._window_size:
                # window not yet full: add with current index
                self._hash = (self._hash + b * (new_idx + 1)) % self._mod
            else:
                # window full: shift out oldest byte
                old = self._buffer.pop(0)
                # subtract old contribution (which had index 1)
                self._hash = (self._hash - old * 1) % self._mod
                # slide all remaining contributions: multiply by decremented index?
                # Actually we need to recalc: but for performance we adjust differently.
                # Simpler correct approach: recompute hash from scratch for clarity.
                # We'll rebuild the hash incrementally correctly:
                # After popping, all existing bytes have their index decreased by 1.
                # The new byte gets index = window_size (the last position).
                # We can recompute by iterating buffer: but that is O(window_size) per byte.
                # For a correct simple implementation we accept this.
                # We'll recompute from buffer to avoid bugs.
                self._hash = 0
                for idx, val in enumerate(self._buffer):
                    self._hash = (self._hash + val * (idx + 1)) % self._mod

    def current_hash(self) -> int:
        if len(self._buffer) < self._window_size:
            return 0
        return self._hash
