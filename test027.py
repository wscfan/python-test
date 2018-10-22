# -*- coding: utf-8 -*-
import functools

def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('test')
def aa():
    print('2018.10.22')

aa()

print(aa.__name__)
