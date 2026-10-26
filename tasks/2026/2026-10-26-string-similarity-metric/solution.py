def get_ngrams(s: str, n: int) -> set:
    """Return set of all character n-grams of string s.
    If n <= 0 or len(s) < n, returns an empty set."""
    if n <= 0 or len(s) < n:
        return set()
    return {s[i:i+n] for i in range(len(s)-n+1)}


def string_similarity(s1: str, s2: str, n: int = 3) -> float:
    """Compute Jaccard similarity between two strings using character n-grams."""
    set1 = get_ngrams(s1, n)
    set2 = get_ngrams(s2, n)

    # Both strings have no n-grams (e.g., too short or empty)
    if not set1 and not set2:
        return 1.0 if s1 == s2 else 0.0

    # One has n-grams, the other does not -> disjoint
    if not set1 or not set2:
        return 0.0

    intersection = set1 & set2
    union = set1 | set2
    return len(intersection) / len(union)
