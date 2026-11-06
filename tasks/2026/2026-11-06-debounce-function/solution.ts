export function debounce<T extends (...args: any[]) => any>(
  fn: T,
  wait: number,
  options?: { leading?: boolean; trailing?: boolean }
): {
  (...args: Parameters<T>): void;
  cancel: () => void;
} {
  const { leading = false, trailing = true } = options ?? {};
  let timer: ReturnType<typeof setTimeout> | null = null;
  let lastArgs: Parameters<T> | null = null;
  let lastThis: any = null;

  const debounced = function (this: any, ...args: Parameters<T>): void {
    lastArgs = args;
    lastThis = this;

    if (timer !== null) {
      clearTimeout(timer);
    }

    if (leading && timer === null) {
      fn.apply(this, args);
    }

    timer = setTimeout(() => {
      if (trailing && lastArgs !== null) {
        fn.apply(lastThis, lastArgs);
      }
      timer = null;
      lastArgs = null;
      lastThis = null;
    }, wait);
  };

  debounced.cancel = function (): void {
    if (timer !== null) {
      clearTimeout(timer);
      timer = null;
    }
    lastArgs = null;
    lastThis = null;
  };

  return debounced;
}
