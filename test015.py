# -*- coding: utf-8 -*-
from functools import reduce

def add(x, y):
    return x * 10 + y

print(reduce(add, [1, 3, 5, 7, 9]))
