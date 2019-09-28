# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 00:52:00 2018

@author: zhangx
"""

import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from sklearn.model_selection import train_test_split

#Choose and splite the data to train and test
data_train = pd.read_csv("C:/Users/zhangx/R/Assignment_1 data/train.csv",na_filter = False)
X = data_train[['TotRmsAbvGrd','MSSubClass','LotArea','OverallQual','OverallCond','BsmtFinSF1','GrLivArea']]
y = data_train[['SalePrice']]
X_train,X_test,y_train,y_test = train_test_split(X,y,train_size=0.8,test_size=0.2, random_state = 42)

print(X_train.shape)

model = Sequential()

model.add(Conv4D(256, (3, 3), input_shape=X_train.shape[1:]))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Conv2D(256, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))

model.add(Flatten())  # this converts our 3D feature maps to 1D feature vectors

model.add(Dense(64))

model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(X_train, y_train, batch_size=32, epochs=3, validation_split=0.3)

classes = model.predict(X_test, batch_size=128)

plt.plot(range(len(classes)), y_test, color= 'black') # plotting the initial datapoints 
plt.plot(range(len(classes)), classes, color= 'red') # plotting the line made by the RBF kernel
## plot title 
plt.title("sales predict graph with test") 
## function to show plot 
plt.show() 