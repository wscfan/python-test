# -*- coding: utf-8 -*-
import os

L = [x for x in os.listdir('.') if os.path.isdir(x)]
print(L)
