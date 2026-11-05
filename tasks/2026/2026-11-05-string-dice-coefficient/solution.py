def dice_coefficient(s1: str, s2: str) -> float:
    """Return the Sørensen–Dice coefficient between two strings."""
    # Handle edge cases for short strings
    if len(s1) < 2 and len(s2) < 2:
        return 1.0 if s1 == s2 else 0.0
    if len(s1) < 2 or len(s2) < 2:
        return 0.0

    # Generate bigram sets
    bigrams1 = {s1[i:i+2] for i in range(len(s1)-1)}
    bigrams2 = {s2[i:i+2] for i in range(len(s2)-1)}

    intersection_size = len(bigrams1 & bigrams2)
    return 2.0 * intersection_size / (len(bigrams1) + len(bigrams2))
