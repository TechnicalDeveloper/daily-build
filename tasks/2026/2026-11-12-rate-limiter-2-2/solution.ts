export class RateLimiter {
    private limit: number;
    private windowMs: number;
    private hits: Map<string, number[]>;

    constructor(limit: number, windowMs: number) {
        if (limit <= 0 || windowMs <= 0) {
            throw new RangeError("Limit and windowMs must be positive numbers");
        }
        this.limit = limit;
        this.windowMs = windowMs;
        this.hits = new Map();
    }

    isAllowed(key: string): boolean {
        const now = Date.now();
        const cutoff = now - this.windowMs;
        let timestamps = this.hits.get(key) ?? [];

        // Keep only timestamps within the window
        timestamps = timestamps.filter(t => t > cutoff);
        if (timestamps.length >= this.limit) {
            this.hits.set(key, timestamps);
            return false;
        }
        timestamps.push(now);
        this.hits.set(key, timestamps);
        return true;
    }

    resetKey(key: string): void {
        this.hits.delete(key);
    }

    resetAll(): void {
        this.hits.clear();
    }
}
