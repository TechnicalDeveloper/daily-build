import threading
import time

def debounce(wait):
    def decorator(fn):
        timer = None
        lock = threading.Lock()
        def debounced(*args, **kwargs):
            nonlocal timer
            def call_fn():
                with lock:
                    fn(*args, **kwargs)
            with lock:
                if timer:
                    timer.cancel()
                timer = threading.Timer(wait, call_fn)
                timer.start()
        def cancel():
            nonlocal timer
            with lock:
                if timer:
                    timer.cancel()
                    timer = None
        debounced.cancel = cancel
        return debounced
    return decorator
