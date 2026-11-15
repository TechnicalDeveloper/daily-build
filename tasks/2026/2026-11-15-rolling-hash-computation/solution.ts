export function rollingHash(s: string, windowSize: number): number[] {
  if (windowSize <= 0) {
    throw new Error("windowSize must be positive");
  }
  if (s.length < windowSize) {
    return [];
  }

  const base = 31;
  const mod = 1_000_000_007;
  let hash = 0;
  let highestBase = 1;

  // Compute initial hash and highest power of base for the window size
  for (let i = 0; i < windowSize; i++) {
    hash = (hash * base + s.charCodeAt(i)) % mod;
    if (i > 0) {
      highestBase = (highestBase * base) % mod;
    }
  }

  const results: number[] = [hash];

  for (let i = windowSize; i < s.length; i++) {
    // Remove the leftmost character
    hash = (hash - (s.charCodeAt(i - windowSize) * highestBase) % mod + mod) % mod;
    // Add the new character
    hash = (hash * base + s.charCodeAt(i)) % mod;
    results.push(hash);
  }

  return results;
}
