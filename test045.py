# -*- coding: utf-8 -*-

class Student(object):
    
    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

s = Student()
print(s.name)
print(s.score)
