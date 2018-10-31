# -*- coding: utf-8 -*-
from io import BytesIO

f = BytesIO(b'\x64\xb8\xad\xe6\x96\x87')
print(f.read())
