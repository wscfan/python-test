# -*- coding: utf-8 -*-
import re
from datetime import datetime, timezone, timedelta

def to_timestamp(dt_str, tz_str):
    reg_str = r'^UTC([\+-]\d{1,2}):\d{1,2}$'
    tz = int(re.match(reg_str, tz_str).group(1))
    utc_dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S').replace(tzinfo=timezone(timedelta(hours=tz)))
    return utc_dt.timestamp()

print(to_timestamp('2018-11-6 16:29:30', 'UTC+7:00'))
