export class RollingHash {
  private readonly base: number;
  private readonly mod: number;
  private readonly modInverse: number;
  private queue: number[] = [];
  private hashVal: number = 0;
  private sizeVal: number = 0;
  private power: number = 1; // base^0

  constructor(base: number, mod: number) {
    if (base <= 0 || mod <= 0) {
      throw new Error("Base and modulus must be positive");
    }
    if (gcd(base, mod) !== 1) {
      throw new Error("Base and modulus must be coprime");
    }
    this.base = base % mod;
    this.mod = mod;
    this.modInverse = modInverse(this.base, mod);
  }

  get size(): number {
    return this.sizeVal;
  }

  add(value: number): void {
    const v = ((value % this.mod) + this.mod) % this.mod;
    if (this.sizeVal === 0) {
      this.hashVal = v;
      this.queue.push(v);
      this.sizeVal = 1;
      this.power = 1;
    } else {
      this.hashVal = (this.hashVal * this.base + v) % this.mod;
      this.queue.push(v);
      this.sizeVal++;
      this.power = (this.power * this.base) % this.mod;
    }
  }

  removeLeft(): void {
    if (this.sizeVal === 0) {
      throw new Error("Cannot remove from empty rolling hash");
    }
    const leftmost = this.queue.shift()!;
    this.hashVal = (this.hashVal - leftmost * this.power) % this.mod;
    if (this.hashVal < 0) {
      this.hashVal += this.mod;
    }
    this.sizeVal--;
    if (this.sizeVal === 0) {
      this.power = 1;
    } else {
      this.power = (this.power * this.modInverse) % this.mod;
    }
  }

  getHash(): number {
    return this.hashVal;
  }
}

function gcd(a: number, b: number): number {
  while (b !== 0) {
    const t = b;
    b = a % b;
    a = t;
  }
  return a;
}

function modInverse(a: number, mod: number): number {
  let [old_r, r] = [a, mod];
  let [old_s, s] = [1, 0];
  while (r !== 0) {
    const q = Math.floor(old_r / r);
    [old_r, r] = [r, old_r - q * r];
    [old_s, s] = [s, old_s - q * s];
  }
  return ((old_s % mod) + mod) % mod;
}
