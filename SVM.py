# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 02:56:30 2018

@author: zhangx
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

data_train = pd.read_csv("C:/Users/zhangx/Desktop/EPL 2000-2018.csv",na_filter = False)
x = data_train[['FTHG','FTAG','HH','HST','HC','AST','AC']]
y = data_train[['H','A','D']]
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,test_size=0.2, random_state = 42)
"""
Train the model using training sets
"""
svr = SVR(kernel= 'rbf', C= 1e3, gamma= 0.1)
svr_poly = SVR(kernel= 'poly', C= 1e3, degree= 2)
svr.fit(x_train,y_train)
svr_poly.fit(x_train,y_train)
#predict
y = svr.predict(x_test)
y_poly = svr_poly.predict(x_test)
#Accuarcy
A_reg = svr.score(x_test,y_test)
print(A_reg)
#plot
plt.scatter(x_train, y_train, color= 'black', label= 'Initial') # plotting the initial datapoints 
plt.plot(x_test, y, color= 'red', label= 'RBF model') # plotting the line made by the RBF kernel
plt.plot(x_test,y_poly, color= 'blue', label= 'Polynomial model') # plotting the line made by polynomial kernel
## plot title 
plt.title("Area realationship with Room number") 
## function to show plot 
plt.show() 