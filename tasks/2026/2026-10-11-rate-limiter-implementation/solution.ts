export class RateLimiter {
  private maxRequests: number;
  private windowMs: number;
  private timestamps: Map<string, number[]>;

  constructor(maxRequests: number, windowMs: number) {
    if (maxRequests <= 0 || windowMs <= 0) {
      throw new Error('maxRequests and windowMs must be positive integers');
    }
    this.maxRequests = maxRequests;
    this.windowMs = windowMs;
    this.timestamps = new Map();
  }

  isAllowed(key: string): boolean {
    const now = Date.now();

    if (!this.timestamps.has(key)) {
      this.timestamps.set(key, []);
    }

    const stamps = this.timestamps.get(key)!;

    // Remove timestamps outside the current window
    while (stamps.length > 0 && stamps[0] <= now - this.windowMs) {
      stamps.shift();
    }

    if (stamps.length >= this.maxRequests) {
      return false;
    }

    stamps.push(now);
    return true;
  }

  reset(): void {
    this.timestamps.clear();
  }
}
