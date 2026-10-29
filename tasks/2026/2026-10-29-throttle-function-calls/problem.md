# Throttle Function Calls

Implement a `throttle` function that limits how often a given function can be called.

**Signature:**
```python
def throttle(func: Callable, interval: float) -> Callable
```

**Behavior:**
- The returned function can be called any number of times, but `func` will be executed at most once every `interval` seconds.
- The first call triggers `func` immediately.
- Subsequent calls made within `interval` seconds of the last execution are ignored (they have no effect).
- After `interval` seconds have passed since the last execution, the next call will again trigger `func` immediately.
- Arguments and keyword arguments are forwarded to `func`.

**Edge cases to handle:**
1. If multiple calls are made within the same interval, only the first call's arguments are used; later calls are ignored.
2. If a call is made exactly after the interval elapses, it should execute immediately.
3. The throttle should work independently for each throttled function (no shared state).

Solve it by implementing the `throttle` function in `solution.py`.
