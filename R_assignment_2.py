# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 03:35:00 2018

@author: zhangx
"""

import tensorflow as tf
import pandas as pd
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, LSTM
from sklearn.model_selection import train_test_split

#Choose and splite the data to train and test
data_train = pd.read_csv("C:/Users/zhangx/Desktop/EPL 2000-2018.csv",na_filter = False)
print(data_train)
X = data_train[['FTHG','FTAG','HH','HST','HC','AST','AC']]
y = data_train[['H','A','D']]
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,test_size=0.2, random_state = 42)

X_train = X_train/255.0
X_test = X_test/255.0

print(X_train.shape)
#define modle recurrent model
model = Sequential()
#add layers
#model.add(LSTM(128, input_shape=(X_train.shape[1:]), activation='relu', return_sequences=True))

model.add(Dense(units=64, input_dim=7))
model.add(Activation("relu"))

model.add(Dense(units=32))
model.add(Activation("relu"))

model.add(Dense(units=10))
model.add(Activation("relu"))

model.add(Dense(units=3))
model.add(Activation("relu"))

opt = tf.keras.optimizers.Adam(lr=0.001, decay=1e-16)
model.compile(loss='mse', optimizer=opt, metrics=['accuracy'])
model.fit(X_train, y_train, epochs=100, batch_size=32,validation_data=(X_test, y_test))
classes = model.predict(X_test, batch_size=128)

plt.plot(range(len(classes)), y_test, color= 'black') # plotting the initial datapoints 
plt.plot(range(len(classes)), classes, color= 'red') # plotting the line made by the RBF kernel
## plot title 
plt.title("sales predict graph with test") 
## function to show plot 
plt.show() 