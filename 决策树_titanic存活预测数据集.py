# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 15:54:16 2019

@author: zhangx
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.tree import DecisionTreeClassifier, export_graphviz

def decisiontree():
    '''
    决策树对坦坦尼克号生存预测
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
    #print(x_train)
   
    #决策树进行预测
    dec = DecisionTreeClassifier(max_depth = 8)
    dec.fit(x_train,y_train)
    #预测准确率
    print("预测准确率：",dec.score(x_test,y_test))
    #决策树显示导出
    export_graphviz(dec,out_file="./tree.dot",feature_names=['age', 'pclass=1st', 'pclass=2nd', 'pclass=3rd', 'sex=female', 'sex=male'])
    '''
    显示decision tree需要下载graphviz吧tree.dot转换为png （$dot -Tpng tree.dot -o tree.png）
    '''
    '''
    改进：随机森林或剪枝
    '''
    
    return None

if __name__ == "__main__":
    decisiontree()
    
'''
优点：树可视；企业重要决策，好的分析能力，在决策过程应用较多；需要很少的数据准备，不需要归一化
缺点：不能很好的推广数据的过于复杂的树（overfitting）
'''