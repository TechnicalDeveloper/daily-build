import time
import functools

def rate_limiter(max_calls: int, time_window: float):
    """
    Returns a decorator that limits the decorated function to `max_calls`
    invocations per sliding `time_window` (in seconds).
    Raises RuntimeError if the limit is exceeded.
    """
    def decorator(func):
        calls = []

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.monotonic()
            # Remove timestamps outside the window
            while calls and now - calls[0] > time_window:
                calls.pop(0)
            if len(calls) >= max_calls:
                raise RuntimeError("Rate limit exceeded")
            calls.append(now)
            return func(*args, **kwargs)

        return wrapper

    return decorator
