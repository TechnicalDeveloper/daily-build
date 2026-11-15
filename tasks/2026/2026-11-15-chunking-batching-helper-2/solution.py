from typing import List, Any

def chunk(sequence, size: int) -> List[List[Any]]:
    if not isinstance(size, int) or size <= 0:
        raise ValueError("size must be a positive integer")
    result = []
    current = []
    for item in sequence:
        current.append(item)
        if len(current) == size:
            result.append(current)
            current = []
    if current:
        result.append(current)
    return result
