import time
import functools
import random

def retry(max_retries=3, base_delay=1, max_delay=60, backoff_factor=2, exceptions=(Exception,)):
    """Decorator that retries a function with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == max_retries:
                        raise
                    # Calculate backoff with full jitter (random between 0 and delay)
                    delay = min(base_delay * (backoff_factor ** attempt), max_delay)
                    time.sleep(delay)
                except Exception as e:
                    # Non-retryable exceptions are re-raised immediately
                    raise
            # Should never reach here, but for completeness
            raise last_exception
        return wrapper
    return decorator
