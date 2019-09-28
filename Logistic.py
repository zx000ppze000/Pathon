# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 15:03:31 2019

@author: zhangx
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn import metrics
import warnings
warnings.filterwarnings('ignore')

kidDataset = pd.read_csv("/Users/zhangx/Desktop/Kid.csv")
kidDataset.head()
kidDataset.drop(columns = ['Obs No.'])
kidDataset.isnull().sum()
kidDataset.Buy.value_counts()
sns.countplot(x = 'Buy', data = kidDataset, palette = 'hls')
plt.show()
# data split with target and features
X = kidDataset[['Income', 'Is Female', 'Is Married', 'Has College', 'Is Professional', 'Is Retired', 'Unemployed', 'Residence Length', 'Dual Income','Minors','Own', 'House','White',
'English', 'Prev Child Mag', 'Prev Parent Mag']]
y = kidDataset['Buy']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)
# model build
logreg = LogisticRegression()
logreg.fit(X_train,y_train)
# prediction
y_pred=logreg.predict(X_test)
# evaluation
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))
# ROC curve
y_pred_proba = logreg.predict_proba(X_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(y_test,  y_pred_proba)
auc = metrics.roc_auc_score(y_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()

# with feature selection
from sklearn.ensemble import ExtraTreesClassifier
data = pd.read_csv("C:/Users/zhangx/Desktop/Kid.csv",na_filter = False)
X = kidDataset[['Income', 'Is Female', 'Is Married', 'Has College', 'Is Professional', 'Is Retired', 'Unemployed', 'Residence Length', 'Dual Income','Minors','Own', 'House','White',
'English', 'Prev Child Mag', 'Prev Parent Mag']] #indepent column
y = kidDataset['Buy']   #target column i.e price range
model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(10).plot(kind='barh')
plt.show()

# build with feature selection
Xf = kidDataset[['Income', 'Is Female', 'Is Married', 'Has College', 'Is Professional', 'Residence Length', 'Dual Income','Minors','Own', 'White']]
yf = kidDataset['Buy']
Xf_train,Xf_test,yf_train,yf_test=train_test_split(Xf,yf,test_size=0.20,random_state=0)
# model build
logreg_f = LogisticRegression()
logreg_f.fit(Xf_train,yf_train)
# prediction
yf_pred=logreg_f.predict(Xf_test)
# evaluation
print("Accuracy:",metrics.accuracy_score(yf_test, yf_pred))
print("Precision:",metrics.precision_score(yf_test, yf_pred))
print("Recall:",metrics.recall_score(yf_test, yf_pred))
# ROC curve
y_pred_proba = logreg_f.predict_proba(Xf_test)[::,1]
fpr, tpr, _ = metrics.roc_curve(yf_test,  y_pred_proba)
auc = metrics.roc_auc_score(yf_test, y_pred_proba)
plt.plot(fpr,tpr,label="data 1, auc="+str(auc))
plt.legend(loc=4)
plt.show()