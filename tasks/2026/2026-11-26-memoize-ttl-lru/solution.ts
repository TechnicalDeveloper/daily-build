export interface MemoizeOptions<Args extends unknown[] = unknown[]> {
  maxSize?: number;
  ttlMs?: number;
  resolver?: (...args: Args) => string;
}

interface CacheEntry<Result> {
  result: Result;
  expiresAt: number;
}

const objectIds = new WeakMap<object, number>();
let nextObjectId = 1;

function getObjectId(obj: object): number {
  const existing = objectIds.get(obj);
  if (existing !== undefined) return existing;
  const id = nextObjectId++;
  objectIds.set(obj, id);
  return id;
}

function defaultKey(args: unknown[]): string {
  return args.map((arg) => {
    if (arg === null) return 'null';
    switch (typeof arg) {
      case 'string': return `s:${arg}`;
      case 'number': return `n:${Number.isNaN(arg) ? 'NaN' : arg}`;
      case 'boolean': return `b:${arg}`;
      case 'undefined': return 'undefined';
      case 'bigint': return `big:${arg.toString()}`;
      case 'symbol': return `sym:${arg.toString()}`;
      case 'function': return `fn:${getObjectId(arg)}`;
      case 'object': return `obj:${getObjectId(arg)}`;
      default: return 'other';
    }
  }).join('|');
}

export function memoize<Args extends unknown[], Result>(
  fn: (...args: Args) => Result,
  options: MemoizeOptions<Args> = {},
): (...args: Args) => Result {
  const { maxSize = Infinity, ttlMs = 0, resolver } = options;
  const cache = new Map<string, CacheEntry<Result>>();

  const memoized = function (this: unknown, ...args: Args): Result {
    const key = (resolver ? resolver(...args) : defaultKey(args));
    const now = Date.now();
    const entry = cache.get(key);

    if (entry) {
      if (ttlMs > 0 && entry.expiresAt <= now) {
        cache.delete(key);
      } else {
        cache.delete(key);
        cache.set(key, entry);
        return entry.result;
      }
    }

    const result = fn.apply(this, args);
    cache.set(key, { result, expiresAt: ttlMs > 0 ? now + ttlMs : Infinity });

    if (cache.size > maxSize) {
      const oldestKey = cache.keys().next().value as string | undefined;
      if (oldestKey !== undefined) cache.delete(oldestKey);
    }

    return result;
  };

  return memoized;
}
