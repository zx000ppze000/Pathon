# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 16:50:46 2019

@author: zhangx
"""
import pandas as pd
data = pd.read_csv("C:/Users/zhangx/Desktop/EPL 2000-2018.csv")
test_data=data.iloc[:,0:10]
import matplotlib.pyplot as plt
plt.rcParams['axes.unicode_minus']=False
plt.figure(1,figsize=(10,10))
p=data.boxplot(return_type='both')
x = p['fliers'][0].get_xdata()
y = p['fliers'][0].get_ydata()
y.sort()
for i in range(len(x)):
    if i>0:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.05 -0.8/(y[i]-y[i-1]),y[i]))
    else:
        plt.annotate(y[i],xy=(x[i],y[i]),xytext=(x[i]+0.08,y[i]))
plt.show()