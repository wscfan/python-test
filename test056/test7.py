# -*- coding: utf-8 -*-
from datetime import datetime, timedelta, timezone

utc_dt = datetime.utcnow().replace(tzinfo = timezone.utc)
print(utc_dt)

bj_dt = utc_dt.astimezone(timezone(timedelta(hours = 8)))
print(bj_dt)

tokyo_dt = utc_dt.astimezone(timezone(timedelta(hours = 9)))
print(tokyo_dt)
