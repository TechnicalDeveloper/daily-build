import time

def throttle(func, interval):
    last_call_time = -interval  # ensures first call executes immediately
    def wrapper(*args, **kwargs):
        nonlocal last_call_time
        now = time.time()
        if now - last_call_time >= interval:
            last_call_time = now
            return func(*args, **kwargs)
    return wrapper
