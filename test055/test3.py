# -*- coding: utf-8 -*-
import re

m1 = re.split(r'\s+', 'a b    c')
print(m1)
m2 = re.split(r'[\s\,]+', 'a,b, c,  d')
print(m2)
