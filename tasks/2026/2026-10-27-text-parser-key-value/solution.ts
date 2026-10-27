export function parse(text: string): Record<string, string> {
  const result: Record<string, string> = {};
  const lines = text.split('\n');
  for (const line of lines) {
    const trimmed = line.trim();
    if (trimmed === '' || trimmed.startsWith('#')) {
      continue;
    }
    const eqIndex = trimmed.indexOf('=');
    if (eqIndex === -1) {
      // Ignore lines without '=' (optional: could throw, but spec says nothing)
      continue;
    }
    const key = trimmed.slice(0, eqIndex).trim();
    const value = trimmed.slice(eqIndex + 1).trim();
    if (key !== '') {
      result[key] = value;
    }
  }
  return result;
}
