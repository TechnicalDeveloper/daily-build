from typing import List


def window_hashes(text: str, window_size: int, base: int = 257, modulus: int = 1_000_000_007) -> List[int]:
    if window_size <= 0:
        raise ValueError('window_size must be positive')
    if modulus <= 0:
        raise ValueError('modulus must be positive')
    n = len(text)
    if window_size > n:
        return []
    highest = pow(base, window_size - 1, modulus)
    current = 0
    for ch in text[:window_size]:
        current = (current * base + ord(ch)) % modulus
    result = [current]
    for i in range(window_size, n):
        outgoing = ord(text[i - window_size])
        incoming = ord(text[i])
        current = ((current - outgoing * highest) * base + incoming) % modulus
        result.append(current)
    return result
