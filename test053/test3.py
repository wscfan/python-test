# -*- coding: utf-8 -*-
import json

d = dict(name = 'Bob', age = 20, score = 88)
s = json.dumps(d)
print(s)

j = json.loads(s)
print(j)
