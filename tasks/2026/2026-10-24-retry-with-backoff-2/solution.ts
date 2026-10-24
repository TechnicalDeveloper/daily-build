export async function retry<T>(
  fn: () => Promise<T>,
  options: { maxRetries: number; baseDelay: number }
): Promise<T> {
  const { maxRetries, baseDelay } = options;

  async function attempt(remaining: number): Promise<T> {
    try {
      return await fn();
    } catch (err) {
      if (remaining <= 0) {
        throw err;
      }
      const delay = baseDelay * Math.pow(2, maxRetries - remaining);
      if (delay > 0) {
        await new Promise((resolve) => setTimeout(resolve, delay));
      }
      return attempt(remaining - 1);
    }
  }

  return attempt(maxRetries);
}
