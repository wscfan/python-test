# -*- coding: utf-8 -*-

class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running...')
    def eat(self):
        print('Dog is eating...')

Dog().run()
Dog().eat()
