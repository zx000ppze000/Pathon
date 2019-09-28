# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 16:58:03 2019

@author: zhangx
"""
#分类数据集

from sklearn.datasets import load_iris,fetch_20newsgroups
from sklearn.model_selection import train_test_split

li = load_iris()
#print("获取特征值")
#print(li.data)
#print("目标值")
#print(li.target)
#print(li.DESCR)

"""
#注意返回值，训练集  train   x_train,y_train           策士集  test    x_test,y_test
x_train,x_test,y_train,y_test = train_test_split(li.data, li.target, test_size = 0.25)

print("训练集特征值和目标值",x_train,y_train)
print("测试集特征值和目标值",x_test,y_test)
"""

# 获取新闻数据集
news = fetch_20newsgroups(subset = 'all')

print(news.data)
print(news.target)


#回归数据集 用相同方法获取，数据特征为持续性的