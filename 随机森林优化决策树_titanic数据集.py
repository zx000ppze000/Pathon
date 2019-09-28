# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 17:16:32 2019

@author: zhangx
"""
import pandas as pd
from sklearn.model_selection import train_test_split,GridSearchCV
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestClassifier
'''
随机森林： n_estimator决策树的数量(一般为120,200,300,500,800,1200)； max_depth每棵树的深度限制(一般为5,8,15,25,30)
'''
def randomforest():
    '''
    随机森林优化决策树
    '''
    #获取数据
    titan = pd.read_csv("http://biostat.mc.vanderbilt.edu/wiki/pub/Main/DataSets/titanic.txt")
    #处理数据,找出特征值和目标值
    x = titan[['pclass','age','sex']]
    y = titan['survived']
    #缺失值处理
    x['age'].fillna(x['age'].mean(), inplace=True)
    # 数据集分为测试集和测试集
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.25)
    #进行处理（特征工程） 特征->类别->one hot 编码
    dic_t = DictVectorizer(sparse = False)
    x_train = dic_t.fit_transform(x_train.to_dict(orient = "records"))
    #print(dic_t.get_feature_names())
    x_test = dic_t.transform(x_test.to_dict(orient = "records"))    
    
    #随机森林进行预测（超参数调优）
    rf = RandomForestClassifier()
    param = {"n_estimators": [120,200,300,500,800,1200],"max_depth":[5,8,15,25,30]}
    #网格搜索与交叉验证
    gc = GridSearchCV(rf,param_grid=param, cv=2)
    gc.fit(x_train,y_train)
    
    print("预测准确率：",gc.score(x_test,y_test))
    print("查看选择的参数模型：",gc.best_params_)
    return None

if __name__ == "__main__":
    randomforest()
    
'''
优点：对于高纬度的数据（大数据）随机森林优势越大（不需要降维）；有极好的准去率；能够评估各个特征在分类问题上的重要性。
'''