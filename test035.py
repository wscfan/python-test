# -*- coding: utf-8 -*-

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

aa = hasattr(obj, 'x')
bb = hasattr(obj, 'y')
setattr(obj, 'y', 19)
cc = hasattr(obj, 'y')
dd = getattr(obj, 'y')
ee = obj.y

print(aa, bb, cc, dd, ee)

ff = hasattr(obj, 'power')
gg = getattr(obj, 'power')
hh = gg()

print(ff, gg, hh)

ii = getattr(obj, 'z', 404)
print(ii)
