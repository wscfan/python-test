# -*- coding: utf-8 -*-
import os

L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(L)
