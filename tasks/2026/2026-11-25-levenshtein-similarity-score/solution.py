def similarity(a: str, b: str) -> float:
    if a == b:
        return 1.0

    if not a or not b:
        return 0.0

    previous = list(range(len(b) + 1))

    for i, char_a in enumerate(a, 1):
        current = [i]
        for j, char_b in enumerate(b, 1):
            deletion = previous[j] + 1
            insertion = current[j - 1] + 1
            substitution = previous[j - 1] + (char_a != char_b)
            current.append(min(deletion, insertion, substitution))
        previous = current

    distance = previous[-1]
    return 1.0 - distance / max(len(a), len(b))
