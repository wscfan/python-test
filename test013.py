# -*- coding: utf-8 -*-

from collections import Iterator
a = isinstance((x for x in range(10)), Iterator)
print(a)
b = isinstance([], Iterator)
print(b)
c = isinstance(iter([]), Iterator)
print(c)
d = isinstance(iter('abc'), Iterator)
print(d)
