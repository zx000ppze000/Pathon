# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 18:15:30 2019

@author: zhangx
"""
from sklearn.datasets import fetch_20newsgroups
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report

def naviebayes():
    '''
    朴素贝叶斯
    '''
    news = fetch_20newsgroups(subset = 'all')
    #进行数据分割
    x_train,x_test,y_train,y_test = train_test_split(news.data,news.target,test_size = 0.25)
    #对数据集进行特征抽取
    tf = TfidfVectorizer()
    #以训练集当中的词进行每篇文章重要性统计【‘a’，‘b’,'c'】
    x_train = tf.fit_transform(x_train)
    print(tf.get_feature_names())
    x_test = tf.transform(x_test)
    #朴素贝叶斯算法
    mlt = MultinomialNB(alpha = 1.0)
    #print(x_train.toarray())
    mlt.fit(x_train,y_train)
    y_predict = mlt.predict(x_test)
    print("预测的文章类别：",y_predict)
    #准确率
    print("准确率为：",mlt.score(x_test,y_test))
    print("每个类别的精确率与召回率：",classification_report(y_test,y_predict,target_names = news.target_names))
    return None

if __name__ =="__main__":
    naviebayes()
    

'''
优点： 分类效率稳定； 对缺失数据不太铭感（常用于文本分类）；分类准确度高，速度快。
缺点： 由于使用样本独立性假设，不是很靠谱； 训练集的好坏决定结果的好坏（太铭感）。
######文本分类用神经网络效果更好#######
'''
