def dice_similarity(s1: str, s2: str) -> float:
    # Handle empty strings: both empty -> 1.0, else if one empty but we need bigrams
    if not s1 and not s2:
        return 1.0
    # If either string has less than 2 characters, no bigrams exist
    if len(s1) < 2 or len(s2) < 2:
        return 0.0

    # Generate bigrams for each string
    bigrams_s1 = {s1[i:i+2] for i in range(len(s1)-1)}
    bigrams_s2 = {s2[i:i+2] for i in range(len(s2)-1)}

    # Compute intersection and sizes
    intersection = len(bigrams_s1 & bigrams_s2)
    size_s1 = len(bigrams_s1)
    size_s2 = len(bigrams_s2)

    # Dice coefficient formula
    return (2.0 * intersection) / (size_s1 + size_s2)
