# -*- coding: utf-8 -*-
import itertools

for key, group in itertools.groupby('AAABBBCCCAAA'):
    print(key, list(group))
