# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 01:14:12 2018

@author: zhangx
"""
n = 10
for i in range(n):
    line=" "
    for j in range(n-i):
        line +=" "
    for k in range(i+1):
        line+=str(k)
    for l in range(i):
        line+=str(i-l-1)
    print(line)