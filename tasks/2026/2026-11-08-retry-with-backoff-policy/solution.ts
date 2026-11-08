export type AsyncOperation<T> = () => Promise<T>;

export function retryWithBackoff<T>(
  operation: AsyncOperation<T>,
  maxRetries: number = 3,
  baseDelayMs: number = 100
): Promise<T> {
  return new Promise<T>(async (resolve, reject) => {
    let lastError: unknown;

    for (let attempt = 0; attempt <= maxRetries; attempt++) {
      try {
        const result = await operation();
        resolve(result);
        return;
      } catch (error) {
        lastError = error;
        if (attempt < maxRetries) {
          const delay = baseDelayMs * Math.pow(2, attempt);
          if (delay > 0) {
            await new Promise((r) => setTimeout(r, delay));
          }
        }
      }
    }

    reject(lastError);
  });
}
