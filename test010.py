# -*- coding: utf-8 -*-

d = {'x': 'A', 'y': 'B', 'z': 'C'}
for k, v in d.items():
    print(k, '=', v)

print([k + '=' + v for k, v in d.items()])

L = ['hello', 'world', 'ibm', 'apple']
print([s.lower() for s in L])
