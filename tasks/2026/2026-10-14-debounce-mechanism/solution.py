import threading

def debounce(func, delay):
    timer = None
    def debounced(*args, **kwargs):
        nonlocal timer
        if timer is not None:
            timer.cancel()
        def call_func():
            func(*args, **kwargs)
        timer = threading.Timer(delay, call_func)
        timer.start()
    return debounced
