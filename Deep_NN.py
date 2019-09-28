import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import datasets,linear_model,metrics, neural_network
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
from sklearn.metrics.pairwise import cosine_similarity

from  tensorflow.keras.models import Sequential
from  tensorflow.keras.layers import Dense, Dropout, Activation
import  tensorflow.keras.optimizers as optimizers

data = pd.read_csv("C:/Users/zhangx/Desktop/EPL 2000-2018.csv")
print(data.columns.tolist())
print(data.shape)

x = data[['HTHG','HTAG','HH','HST','HC','AST','AC']]
y = data[['H','A','D']]

x_train, x_test, y_train, y_test = train_test_split(x, y)


#
#
# # create model
model = Sequential()
model.add(Dense(units=60, activation='relu', input_dim=7))                   #input layer
model.add(Dense(60, activation='relu'))             
model.add(Dropout(0.5))                        #Hidden layer 1  
model.add(Dense(60, activation='relu'))       
model.add(Dropout(0.5))                              #Hidden layer 2
model.add(Dense(3, activation='softmax'))                                   #output layer
sgd = optimizers.SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)     #Leaning rate is 0.01, decay is 10^-6
model.compile(loss='categorical_crossentropy',
              optimizer=sgd,
              metrics=['accuracy'])
# train
history = model.fit(x_train, y_train, validation_split=0.1, epochs=100, batch_size=100) #with 100 epochs training, each batch 
# predict                                                                               #set to 500 data point
print(history.history)
y_predict = model.predict(x_test)

#
value = y_test.values

match = 0
second_match = 0
third_match = 0
for i in range(len(y_predict)):
    list_test = value[i].tolist()
    max_index_test = list_test.index(max(list_test))

    list_predict = y_predict[i].tolist()
    list_predict_s = sorted(list_predict)

    max_index_predict = list_predict.index(max(list_predict))
    sec_index_predict = list_predict.index(list_predict_s[-2])
    third_index_predict = list_predict.index(list_predict_s[-3])
    # print(type(value[i]),type(y_predict[i]))
    if max_index_test==max_index_predict:
        match=match+1
    if max_index_test == sec_index_predict:
        second_match = second_match + 1
    if max_index_test == third_index_predict:
        third_match = third_match + 1
    print(value[i])
    print(y_predict[i])
#
print(match,second_match,third_match,len(y_predict))
print("acc:",match/len(y_predict))
print("acc-3:",(match+second_match+third_match)/len(y_predict))
print("RMSE:",np.sqrt(metrics.mean_squared_error(y_test, y_predict)))
print("MAE:",metrics.mean_absolute_error(y_test, y_predict))

plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Test'], loc='upper left')
plt.show()