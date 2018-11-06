# -*- coding: utf-8 -*-
from datetime import datetime, timedelta

now = datetime.now()
print(now)
print(now + timedelta(hours = 10))
print(now - timedelta(days = 1))
print(now + timedelta(days = 2, hours = 12))

