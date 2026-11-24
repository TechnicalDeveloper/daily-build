export type Debounced<A extends unknown[], R> = {
  (...args: A): void;
  cancel(): void;
  flush(): R | undefined;
};

export function debounce<A extends unknown[], R>(
  fn: (...args: A) => R,
  waitMs: number
): Debounced<A, R> {
  let timer: ReturnType<typeof setTimeout> | undefined;
  let pendingArgs: A | undefined;

  const debounced = (...args: A): void => {
    pendingArgs = args;

    if (timer !== undefined) {
      clearTimeout(timer);
    }

    timer = setTimeout(() => {
      timer = undefined;

      if (pendingArgs === undefined) {
        return;
      }

      const argsToInvoke = pendingArgs;
      pendingArgs = undefined;
      fn(...argsToInvoke);
    }, waitMs);
  };

  debounced.cancel = (): void => {
    if (timer !== undefined) {
      clearTimeout(timer);
      timer = undefined;
    }

    pendingArgs = undefined;
  };

  debounced.flush = (): R | undefined => {
    if (timer === undefined || pendingArgs === undefined) {
      return undefined;
    }

    clearTimeout(timer);
    timer = undefined;

    const argsToInvoke = pendingArgs;
    pendingArgs = undefined;

    return fn(...argsToInvoke);
  };

  return debounced;
}
