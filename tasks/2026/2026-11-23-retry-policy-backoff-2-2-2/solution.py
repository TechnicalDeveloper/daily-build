import functools
import time


def retry(max_attempts=3, base_delay=0.1, backoff_factor=2, exceptions=(Exception,)):
    """Return a decorator that retries a function with exponential backoff."""
    if max_attempts < 1:
        raise ValueError("max_attempts must be >= 1")
    if base_delay < 0:
        raise ValueError("base_delay must be >= 0")
    if backoff_factor < 1:
        raise ValueError("backoff_factor must be >= 1")
    if not isinstance(exceptions, tuple):
        exceptions = (exceptions,)

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as exc:
                    last_exception = exc
                    if attempt == max_attempts:
                        raise
                    time.sleep(base_delay * (backoff_factor ** (attempt - 1)))
            raise last_exception

        return wrapper

    return decorator
