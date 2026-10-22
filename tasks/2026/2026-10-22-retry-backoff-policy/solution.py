import time
import functools

def retry(max_retries=3, base_delay=1, backoff_factor=2, exceptions=Exception):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt < max_retries:
                        delay = base_delay * (backoff_factor ** attempt)
                        time.sleep(delay)
                    else:
                        raise
            # This should never be reached, but for completeness
            if last_exception:
                raise last_exception
        return wrapper
    return decorator
