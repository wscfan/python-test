# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone

tz_utc_8 = timezone(timedelta(hours = 8))
now = datetime.now()
print(now)
dt = now.replace(tzinfo = tz_utc_8)
print(dt)
