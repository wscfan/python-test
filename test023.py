# -*- coding: utf-8 -*-

def createCounter():
    num = 0
    def counter():
        nonlocal num
        num = num + 1
        return num
    return counter

counterA = createCounter()
print(counterA())
print(counterA())
print(counterA())
print(counterA())
print(counterA())
print(counterA())
print(counterA())
