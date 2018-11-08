# -*- coding: utf-8 -*-
import requests

r = requests.get('https://www.douban.com/')
print(r.status_code)
print(r.text)
