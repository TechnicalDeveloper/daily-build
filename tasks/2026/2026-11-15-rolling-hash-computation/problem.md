# Rolling Hash Computation

Implement a rolling hash function that computes polynomial hashes for all sliding windows of a given string. The function should return an array of hash values (numbers) for each contiguous substring of length `windowSize`.

**Signature**: `export function rollingHash(s: string, windowSize: number): number[]`

**Behavior**:
- Use polynomial rolling hash with base = 31 and modulus = 1_000_000_007.
- For each window starting at index `i` (0-indexed), compute `hash = (char0 * base^(windowSize-1) + char1 * base^(windowSize-2) + ... + charLast) % mod`, where char codes are Unicode code points of the characters.
- Return an array of hashes for all valid windows. If `windowSize` is larger than the string length, return an empty array.

**Edge cases**:
- `windowSize <= 0`: throw an `Error` with message containing `"positive"`.
- Empty or short string yields `[]` when `windowSize > s.length`.
- Single-character windows return the character codes themselves.
