# -*- coding: utf-8 -*-

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'zhangsan'
s.age = 25
# s.score = 99

class childStudent(Student):
    pass

c = childStudent()
c.score = 9999
print(c.score)
