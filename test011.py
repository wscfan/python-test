# -*- coding: utf-8 -*-

g = (x * x for x in range(10))

print(next(g))
print('--------------')
for n in g:
    print (n)
