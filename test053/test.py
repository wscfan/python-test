# -*- coding: utf-8 -*-
import pickle

d = dict(name='Bob', age=20, score=80)
f = open('dump.txt', 'wb')
pickle.dump(d, f)
f.close()
