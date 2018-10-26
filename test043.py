# -*- coding: utf-8 -*-

class Fib(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

f = Fib()
print(f[0], f[1], f[2], f[3], f[4], f[5], f[6], f[7], f[8], f[9])
