# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 18:14:16 2019

@author: zhangx
"""

'''
保存模型，下次使用不用再训练
'''
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression, SGDRegressor,Ridge
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error
from sklearn.externals import joblib

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
    #保存训练好的模型
    joblib.dump(lr,"/Users/zhangx/Pathon/test.pkl")
    #正规方程预测测试集房子价格
    y_lr_predict = std_y.inverse_transform(lr.predict(x_test))
    print("正规方程测试集里每个房子的预测价格：",y_lr_predict)
    print("正规方程均方误差：",mean_squared_error(std_y.inverse_transform(y_test),y_lr_predict))
    
    return None

def usesavedmodel():
    '''
    用保存好的模型
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
    #调取保存好的模型
    model = joblib.load("/Users/zhangx/Pathon/test.pkl")
    y_predict = std_y.inverse_transform(model.predict(x_test))
    print("保存的模型预测结果：",y_predict)    
    return None
if __name__ == "__main__":
    #myLinear()
    usesavedmodel()