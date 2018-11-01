# -*- coding: utf-8 -*-
import os

cPath = os.path.abspath('.')
print(cPath)
dirPath = os.path.join(cPath, 'testdir')
os.mkdir(dirPath)

