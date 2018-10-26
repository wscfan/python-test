# -*- coding: utf-8 -*-

class Student(object):

    def get_score(self):
        return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an interger!')
        if value < 0 or value > 100:
            raise ValueError('score must be between 0 ~ 100!')
        self.__score = value

s = Student()
s.set_score(60)
aa = s.get_score()
print(aa)
s.set_score(9999)
