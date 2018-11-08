# -*- coding: utf-8 -*-
from PIL import Image, ImageFilter

im = Image.open('1.jpg')
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg', 'jpeg')
