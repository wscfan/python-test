# -*- coding: utf-8 -*-

def not_empty(s):
    return s and s.strip()

n = list(filter(not_empty, ['A', '', 'b', None, 'C', '   ']))
print(n)
