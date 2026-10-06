function memoize<Args extends any[], Return>(
  fn: (...args: Args) => Return,
  keyFn: (...args: Args) => string = (...args) => JSON.stringify(args)
): (...args: Args) => Return {
  const cache = new Map<string, Return>();
  return function memoized(...args: Args): Return {
    const key = keyFn(...args);
    if (cache.has(key)) {
      return cache.get(key)!;
    }
    const result = fn(...args);
    cache.set(key, result);
    return result;
  };
}

export { memoize };
