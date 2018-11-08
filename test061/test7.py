# -*- coding: utf-8 -*-
import psutil

for x in range(10):
    a = psutil.cpu_percent(interval=1, percpu=True)
    print(a)
