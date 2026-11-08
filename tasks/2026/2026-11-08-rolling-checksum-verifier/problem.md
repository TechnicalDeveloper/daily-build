# Rolling Checksum Verifier

## Rolling Checksum

Implement a simple rolling checksum (like a hash) over a sliding window of bytes.

Define class `RollingChecksum` with:
- `__init__(self, window_size: int)` – initialize with window size (>0).
- `update(self, new_byte: int, old_byte: int = None)` – update the checksum:
  - If `old_byte` is `None`, this is the first byte(s) in the window; accumulate a simple sum.
  - Otherwise, remove the `old_byte` and add the `new_byte` (simulating a slide).
- `digest(self) -> int` – return current checksum (integer).

Rolling logic: start with `checksum=0`. For each byte added, `checksum = (checksum + byte) % 256`. When sliding, `checksum = (checksum - old_byte + new_byte) % 256`.

Edge cases:
1. Window size = 1, sliding repeatedly.
2. Calling `update(new_byte)` (without old_byte) more times than window size before any slide.
3. Large byte values (0-255), ensure modulo 256 works correctly.
