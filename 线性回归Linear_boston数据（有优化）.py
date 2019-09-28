# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 14:31:37 2019

@author: zhangx
"""

from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor,Ridge
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

def myLinear():
    '''
    线性回归直接预测房子价格
    '''
    #获取数据
    lb = load_boston()
    #分个数据集到训练和测试
    x_train, x_test, y_train, y_test = train_test_split(lb.data,lb.target,test_size=0.25)
    #进行标准化处理(?) 目标值要不要处理？--需要（训练值太小，目标值也需要变小）
    #实例化两个标准化api
    std_x = StandardScaler()
    x_train = std_x.fit_transform(x_train)
    x_test = std_x.transform(x_test)
    #目标值
    std_y = StandardScaler()
    y_train = std_y.fit_transform(y_train.reshape(-1,1))
    y_test = std_y.transform(y_test.reshape(-1,1))    
    #预测
    #正规方程求解
    lr = LinearRegression()
    lr.fit(x_train,y_train)
    print(lr.coef_)
    #正规方程预测测试集房子价格
    y_lr_predict = std_y.inverse_transform(lr.predict(x_test))
    print("正规方程测试集里每个房子的预测价格：",y_lr_predict)
    print("正规方程均方误差：",mean_squared_error(std_y.inverse_transform(y_test),y_lr_predict))
    #梯度下降进行房价预测
    sgd = SGDRegressor()
    sgd.fit(x_train,y_train)
    print(sgd.coef_)
    #预测房子价格
    y_sgd_predict = std_y.inverse_transform(sgd.predict(x_test))
    #print("梯度下降测试集里每个房子的预测价格：",y_sgd_predict)
    print("梯度下降均方误差：",mean_squared_error(std_y.inverse_transform(y_test),y_sgd_predict))
    
    #岭回归(正则化处理overfiting)
    rd = Ridge() #0~1，1~10之间的一个值，可以用网格搜索做
    param = {"alpha": [0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1,2,3,4,5,6,7,8,9,10]}
    #网格搜索与交叉验证
    gc = GridSearchCV(rd,param_grid=param, cv=5)
    gc.fit(x_train,y_train)
    #rd.fit(x_train,y_train)
    #print(rd.coef_)
    #预测
    y_rd_predict = std_y.inverse_transform(gc.predict(x_test))
    print("岭回归均方误差：",mean_squared_error(std_y.inverse_transform(y_test),y_rd_predict))
    print("查看选择的参数模型：",gc.best_params_)
    return None

if __name__ == "__main__":
    myLinear()