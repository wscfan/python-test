# -*- coding: utf-8 -*-

with open('./test.txt', 'r') as f:
    for line in f.readlines():
        print(line.strip())
