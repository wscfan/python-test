# -*- coding: utf-8 -*-
import functools
int2 = functools.partial(int, base=2)
a = int2('1000000')
print(a)
