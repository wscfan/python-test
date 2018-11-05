# -*- coding: utf-8 -*-
from datetime import datetime

now = datetime.now()
t = now.timestamp()
print(t)
print(datetime.fromtimestamp(t))
