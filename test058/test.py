# -*- coding: utf-8 -*-
import base64

aa = base64.b64encode(b'binary\x00string')
bb = base64.b64decode(b'YmluYXJ5AHN0cmluZw==')
cc = base64.b64encode(b'i\xb7\x1d\xfb\xef\xff')
dd = base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff')
ee = base64.urlsafe_b64decode('abcd--__')
print(aa)
print(bb)
print(cc)
print(dd)
print(ee)
