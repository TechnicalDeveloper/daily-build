export interface RollingHashOptions {
  base?: number;
  mod?: number;
}

export class RollingHash {
  private base: number;
  private mod: number;
  private windowSize: number;
  private hash: number;
  private power: number;
  private window: string[];

  constructor(windowSize: number, options?: RollingHashOptions) {
    if (windowSize <= 0) {
      throw new Error("Window size must be positive");
    }
    this.windowSize = windowSize;
    this.base = options?.base ?? 256;
    this.mod = options?.mod ?? 1_000_000_007;
    this.hash = 0;
    this.power = 1;
    for (let i = 1; i < windowSize; i++) {
      this.power = (this.power * this.base) % this.mod;
    }
    this.window = [];
  }

  addChar(c: string): void {
    if (this.window.length === this.windowSize) {
      // remove the oldest character
      const oldest = this.window.shift()!;
      this.hash = (this.hash - oldest.charCodeAt(0) * this.power) % this.mod;
      if (this.hash < 0) {
        this.hash += this.mod;
      }
      // now shift the polynomial and add the new character
      this.hash = (this.hash * this.base + c.charCodeAt(0)) % this.mod;
      this.window.push(c);
    } else {
      this.window.push(c);
      this.hash = (this.hash * this.base + c.charCodeAt(0)) % this.mod;
    }
  }

  getHash(): number {
    if (this.window.length < this.windowSize) {
      throw new Error("Window not full");
    }
    return this.hash;
  }

  isFull(): boolean {
    return this.window.length === this.windowSize;
  }

  reset(): void {
    this.hash = 0;
    this.window = [];
  }
}
