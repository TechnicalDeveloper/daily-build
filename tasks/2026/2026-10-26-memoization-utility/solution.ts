export function memoize<T extends (...args: any[]) => any>(fn: T): T {
  const cache = new Map<string, any>();

  function generateKey(args: IArguments | any[]): string {
    const serialized = Array.from(args).map(arg => {
      if (arg === undefined) return '__undef__';
      if (arg === null) return '__null__';
      if (typeof arg === 'object') {
        // Use JSON.stringify with sorted keys for deep equality
        return JSON.stringify(arg, (_, value) => {
          if (typeof value === 'function') throw new Error('Cannot memoize functions');
          return value;
        });
      }
      return String(arg);
    }).join('::');
    return serialized;
  }

  const memoized = function (this: any, ...args: any[]) {
    const key = generateKey(args);
    if (cache.has(key)) {
      return cache.get(key);
    }
    const result = fn.apply(this, args);
    cache.set(key, result);
    return result;
  } as unknown as T;

  return memoized;
}
