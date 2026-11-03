# Debounce Decorator

Implement a `debounce` decorator that delays the execution of a function until after a specified wait time has elapsed since the last invocation. The decorator should be a function `debounce(wait)` that returns a decorator. The resulting wrapped function should have a `.cancel()` method to cancel any pending execution.

**Signature:** `def debounce(wait: float) -> Callable[[Callable], Callable]`

**Edge cases:**
- The function should correctly handle keyword arguments.
- Calling the debounced function again within the wait period should reset the timer, postponing execution.
- Calling `.cancel()` should prevent any pending execution from occurring.
- The debounced function can be called again after `.cancel()` and after the wait period.
