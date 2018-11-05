# -*- coding: utf-8 -*-
import re

m = re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
if m:
    print('success')
else:
    print('faile')
