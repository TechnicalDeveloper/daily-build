export function parseDuration(input: string): number {
  const clean = input.replace(/\s+/g, '').toLowerCase();
  if (!clean) throw new Error('Invalid duration: empty string');
  const pattern = /(\d+)([dhms])/g;
  let total = 0;
  let match: RegExpExecArray | null;
  let lastIndex = 0;
  while ((match = pattern.exec(clean)) !== null) {
    const value = parseInt(match[1], 10);
    const unit = match[2] as 'd' | 'h' | 'm' | 's';
    const multipliers: Record<string, number> = {
      d: 86400000,
      h: 3600000,
      m: 60000,
      s: 1000,
    };
    total += value * multipliers[unit];
    lastIndex = pattern.lastIndex;
  }
  if (lastIndex !== clean.length) {
    throw new Error(`Invalid duration: unexpected characters in "${input}"`);
  }
  return total;
}

export function formatDuration(ms: number): string {
  if (ms < 0) throw new Error('Invalid duration: negative milliseconds');
  if (ms === 0) return '0ms';
  const units = [
    { name: 'd', ms: 86400000 },
    { name: 'h', ms: 3600000 },
    { name: 'm', ms: 60000 },
    { name: 's', ms: 1000 },
    { name: 'ms', ms: 1 },
  ] as const;
  const parts: string[] = [];
  for (const unit of units) {
    const count = Math.floor(ms / unit.ms);
    if (count > 0) {
      parts.push(`${count}${unit.name}`);
      ms -= count * unit.ms;
    }
  }
  return parts.join(' ');
}

export function addDuration(date: Date, duration: string): Date {
  const ms = parseDuration(duration);
  return new Date(date.getTime() + ms);
}
