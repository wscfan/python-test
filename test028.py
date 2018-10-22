# -*- coding: utf-8 -*-
import time, functools

def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, end - start))
        return result
    return wrapper

@metric
def test(x, y):
    time.sleep(0.1234)
    return x + y

print(test(12, 34))
