# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 01:28:56 2018

@author: zhangx
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data_train = pd.read_csv("C:/Users/zhangx/Desktop/EPL 2000-2018.csv",na_filter = False)
print(data_train)
x = data_train[['HTHG','HTAG','HH']]
#y = data_train[['HH','HA','HD']]
y = data_train[['H','A','D']]
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,test_size=0.2, random_state = 42)
"""
Train the model using training sets
"""
Lin_reg = linear_model.LinearRegression()
Lin_reg.fit(x_train,y_train)
#predict
Y = Lin_reg.predict(x_test)
#Accuarcy
#A_reg = Lin_reg.score(x_test,y_test)
#print('Accuarcy',A_reg)

score=r2_score(y_test,Y)
print('score:',score)
#plot
plt.scatter(x_test,Y,label='predict')
plt.scatter(x_test,y_test,label='test')
## plot title 
plt.title("Area realationship with Room number") 
## function to show plot 
plt.show() 