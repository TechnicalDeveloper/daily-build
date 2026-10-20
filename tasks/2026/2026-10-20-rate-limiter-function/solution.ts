export interface RateLimiter {
  call: () => boolean;
}

export function createRateLimiter(maxCalls: number, windowMs: number): RateLimiter {
  if (maxCalls <= 0) {
    throw new Error('maxCalls must be positive');
  }
  if (windowMs <= 0) {
    throw new Error('windowMs must be positive');
  }

  const timestamps: number[] = [];

  return {
    call: (): boolean => {
      const now = Date.now();
      // Remove timestamps outside the window
      while (timestamps.length > 0 && timestamps[0] < now - windowMs) {
        timestamps.shift();
      }
      if (timestamps.length < maxCalls) {
        timestamps.push(now);
        return true;
      }
      return false;
    },
  };
}
