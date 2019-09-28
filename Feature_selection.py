# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 14:24:06 2019

@author: zhangx
"""
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import ExtraTreesClassifier
import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/zhangx/Desktop/EPL 2000-2018.csv",na_filter = False)
X = data.iloc[:,0:15]     #independent columns
y = data.iloc[:,16:19]    #target column i.e price range
model = ExtraTreesClassifier()
model.fit(X,y)
print(model.feature_importances_) #use inbuilt class feature_importances of tree based classifiers
#plot graph of feature importances for better visualization
feat_importances = pd.Series(model.feature_importances_, index=X.columns)
feat_importances.nlargest(7).plot(kind='barh')
plt.show()


"""
import pandas as pd
import numpy as np
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
data = pd.read_csv("C:/Users/zhangx/Desktop/EPL 2000-2018.csv",na_filter = False)
X = data.iloc[:,0:15]  #independent columns
y = data.iloc[:,16:19]    #target column i.e price range
#apply SelectKBest class to extract top 10 best features
bestfeatures = SelectKBest(score_func=chi2, k=10)
fit = bestfeatures.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns)
#concat two dataframes for better visualization 
featureScores = pd.concat([dfcolumns,dfscores],axis=1)
featureScores.columns = ['Specs','Score']  #naming the dataframe columns
print(featureScores.nlargest(10,'Score'))  #print 10 best features