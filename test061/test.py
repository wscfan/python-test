# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('1.jpg')
w, h = im.size
print('image size: %s * %s' % (w, h))

im.thumbnail((w // 2, h // 2))
im.save('thumbnail.jpg', 'jpeg')
