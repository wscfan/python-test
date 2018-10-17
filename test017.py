# -*- coding: utf-8 -*-

def is_odd(n):
    return n % 2 == 1

n = list(filter(is_odd, [1, 2, 4, 5, 6, 8, 10, 15]))
print(n)
