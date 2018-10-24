# -*- coding: utf-8 -*-

class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

bart = Student('wangsong', 21)
bart.print_score()
print(bart.get_name())
print(bart.get_score())
