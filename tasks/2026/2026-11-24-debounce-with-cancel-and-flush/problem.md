# Debounce Function

Implement a generic `debounce` function.

Signature:

```ts
export type Debounced<A extends unknown[], R> = {
  (...args: A): void;
  cancel(): void;
  flush(): R | undefined;
};

export function debounce<A extends unknown[], R>(
  fn: (...args: A) => R,
  waitMs: number
): Debounced<A, R>;
```

The returned function should schedule a single invocation of `fn` that fires `waitMs` milliseconds after the **last** call in a burst. If multiple calls occur before the delay elapses, reset the timer and keep the arguments from the most recent call.

Add two methods to the returned function:
- `cancel()`: discards any pending invocation and saved arguments.
- `flush()`: if a call is pending, invokes `fn` immediately with the saved arguments and clears the pending state; otherwise does nothing.

Edge cases to respect:
- Multiple rapid calls produce exactly one invocation, using the last call's arguments.
- `cancel()` prevents the scheduled invocation and any later duplicate call.
- `flush()` invokes the pending call once and does not cause another invocation when the timer would have expired.
- A debounced function can be reused for separate bursts after the previous burst completes.
