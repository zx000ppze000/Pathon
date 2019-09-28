# -*- coding: utf-8 -*-
"""
Created on Tue Sep 18 00:56:02 2018

@author: zhangx
"""
for i in range(5):
 a = int(input("the input number is"))
 if ((a%7 == 0) and (a%2 == 0)):
    print("it can be divided by 7 and 2")
    a=None
 elif(a%7 == 0):
    print("it can be divided by 7")
    a=None
 elif(a%2 == 0):
    print("it can be divided by 2")
    a=None
 else:
    print("it neither can be divided by 7 or 2")
    a=None