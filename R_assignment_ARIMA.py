
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 03:13:44 2018

@author: zhangx
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 

data_train = pd.read_csv("C:/Users/zhangx/R/Assignment_1 data/train.csv",na_filter = False)
x_train = data_train[['TotRmsAbvGrd']]
y_train = data_train[['LotArea']]
print (x_train)
data_test = pd.read_csv("C:/Users/zhangx/R/Assignment_1 data/test.csv",na_filter = False)
x_test = data_test[['TotRmsAbvGrd']]
y_test = data_test[['LotArea']]
"""
Train the model using training sets
""" 
classifier = KNeighborsClassifier(n_neighbors=5)  
classifier.fit(x_train, y_train) 
#predict
y = classifier.predict(x_test)
#Accuarcy
A_reg = classifier.score(x_test,y_test)
print(A_reg)
#plot
plt.scatter(x_train, y_train, color= 'black', label= 'Initial') # plotting the initial datapoints 
plt.plot(x_test, y, color= 'red', label= 'ARIMA') # plotting the line made by the RBF kernel
## plot title 
plt.title("Area realationship with Room number") 
## function to show plot 
plt.show() 