# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 17:02:30 2019

@author: zhangx
"""

import requests

target = 'http://unsplash.com/napi/feeds/home'
headers = {'authorization':'Client-ID c94869b36aa272dd62dfaeefed769d4115fb3189a9d1ec88ed457207747be626'}
req = requests.get(url = target,headers = headers, verify=False)
print (req.text)