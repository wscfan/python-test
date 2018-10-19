# -*- coding: utf-8 -*-

def is_palindrome(n):
    a = list(str(n))
    if a == list(reversed(a)):
        return True
    else: 
        return False

output = filter(is_palindrome, range(1, 1000))
print(list(output))
