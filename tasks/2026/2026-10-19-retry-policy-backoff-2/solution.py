import time
import random

def retry(max_retries=3, base_delay=1, backoff_factor=2, exceptions=(Exception,)):
    def decorator(func):
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    last_exception = e
                    if attempt == max_retries:
                        raise
                    delay = base_delay * (backoff_factor ** attempt)
                    time.sleep(delay)
            # Should never reach here
            raise last_exception
        return wrapper
    return decorator
