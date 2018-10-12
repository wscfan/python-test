# -*- coding: utf-8 -*-

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('wangsong', 30)
person('wangsong', 18, address='shanghai', job='web')
person('wangsong', 22, **{'city': 'shanghai', 'job': 'php'})
