# -*- coding: utf-8 -*-
import requests
r = requests.get('https://douban.com/search', params={'q': 'python', 'cat': '1001'})
print(r.url)
print(r.encoding)
print(r.content)
