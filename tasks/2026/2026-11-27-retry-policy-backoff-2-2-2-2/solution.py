import time

def retry(max_retries=3, base_delay=0.1, max_delay=1.0, backoff_factor=2, exceptions=Exception, sleep=time.sleep):
    if max_retries < 0:
        raise ValueError("max_retries must be non-negative")
    if base_delay < 0 or max_delay < 0:
        raise ValueError("delays must be non-negative")
    if backoff_factor <= 0:
        raise ValueError("backoff_factor must be positive")
    if not isinstance(exceptions, (type, tuple)):
        raise TypeError("exceptions must be an exception type or tuple of exception types")
    
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while True:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt >= max_retries:
                        raise
                    delay = min(max_delay, base_delay * (backoff_factor ** attempt))
                    sleep(delay)
                    attempt += 1
        return wrapper
    return decorator
