import functools
import time


def metric(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            start = time.time()
            record = func(*args, **kw)
            print('{} {} executed in {} ms'.format(text, func.__name__, time.time()-start) if not callable(text) else '{} executed in {} ms'.format(func.__name__, time.time()-start))
            return record
        return wrapper
    return decorator(text) if callable(text) else decorator
