# Debounce Function

Implement a debounce mechanism that delays the execution of a function until after a specified quiet period (in seconds) has elapsed since the last invocation. If the debounced function is called again before the delay expires, the timer is reset and only the most recent call's arguments are used.

**Signature**
```python
def debounce(func, delay):
    """Return a debounced version of `func`.

    The returned callable will wait `delay` seconds after the last call
    before invoking `func` with the arguments of that last call.
    """
```

**Edge cases to consider**
1. Multiple rapid calls within the delay period should only trigger one execution (with the last call's arguments).
2. After a debounced call completes, a new call should start a new debounce period (i.e., the mechanism resets).
3. The debounced function must correctly handle calls with no arguments, positional arguments, and keyword arguments.

Implement the solution using only the Python standard library (e.g., `threading.Timer`).
