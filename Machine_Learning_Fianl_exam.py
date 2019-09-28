# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 14:38:30 2019
Machine learning Final exam
@author: zhangx
"""
################################################     Q1     ####################################################################################
"""Question 1: Filter all “Normal Experiments” by taking into account only active examples “SDS
Armed = 1”, and then, merge them in a new file named as “merged exp normal.csv”. Write a script
that performs this task and indicate the number of examples of the merged dataset"""
import os
import glob
import pandas

def HEAT_NORMAL_EXPERIMENTS(indir="C:/Users/zhangx/Desktop/Datasets/Normal_Experiments",outfile="C:/Users/zhangx/Desktop/Datasets/Normal_Experiments/merged_exp_normal.csv"):
    os.chdir(indir)
    fileList=glob.glob("*.csv")
    dfList=[]
    for filename in fileList:
        print(filename)
        df=pandas.read_csv(filename)
        df = df[df['Sds_Armed'] == 1]
        dfList.append(df)
    concatDf=pandas.concat(dfList,axis=0)
    concatDf.to_csv(outfile,index=None)
    return concatDf
a = HEAT_NORMAL_EXPERIMENTS()

################################################     Q2     ####################################################################################
""" Filter all “Experiments with Anomalies” by taking into account only active examples
“SDS Armed = 1” similar to the requirements in Questions 1, and then, merge them in a new file named
as “merged exp contains anomalies.csv”. Write a script that performs this task and indicate the
number of examples of the merged dataset"""
def HEAT_EXPERIMENTS_WITH_ANOMALIES(indir="C:/Users/zhangx/Desktop/Datasets/Experiments_with_Anomalies",outfile="C:/Users/zhangx/Desktop/Datasets/Experiments_with_Anomalies/merged_exp_contains_anomalies.csv"):
    os.chdir(indir)
    fileList=glob.glob("*.csv")
    df2List=[]
    for filename in fileList:
        print(filename)
        df2=pandas.read_csv(filename)
        df2 = df2[df2['Sds_Armed'] == 1]
        df2List.append(df2)
    concatDf2=pandas.concat(df2List,axis=0)
    concatDf2.to_csv(outfile,index=None)
    return concatDf2
b = HEAT_EXPERIMENTS_WITH_ANOMALIES()

################################################     Q3     ####################################################################################
"""Since the merged exp contains anomalies.csv contains anomalies, apply any significance test to rank the 
significance of each feature (X1, X2, ..., X8) as being a distinctive feature of anomalies"""
import pandas as pd
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
data = pd.read_csv("C:/Users/zhangx/Desktop/Datasets/Experiments_with_Anomalies/merged_exp_contains_anomalies.csv")
X = data[['X1','X2','X3','X4','X5','X6','X7','X8']]  #independent columns: x1 to x8
y = data[['Anomaly_Tag']]   #target columns: Anomaly_Tag
bestfeatures = SelectKBest(score_func=chi2, k=8)  #apply SelectKBest class to see the rank of 8 features
fit = bestfeatures.fit(X,y)
dfscores = pd.DataFrame(fit.scores_)
dfcolumns = pd.DataFrame(X.columns) 
featureScores = pd.concat([dfcolumns,dfscores],axis=1) #concat two dataframes for better visualization
featureScores.columns = ['Features','Score']  #naming the dataframe columns
print(featureScores.nlargest(8,'Score'))  #print out the scroe of the 8 features

################################################     Q4     ####################################################################################
""" Model the normal process “merged exp normal.csv” using Gaussian distribution.
Assume that the features are independent. Characterize your model using the following cases:
– Consider all features (X1, X2, ..., X8)
– Mark the most important two features (obtained from the significance test in Question 3) 
– The projection of the feature space into the first two components using Principle Component
Analysis (PCA)"""
import pandas as pd
import numpy as np
import math
from sklearn import preprocessing
from sklearn.decomposition import PCA

data = pd.read_csv("C:/Users/zhangx/Desktop/Datasets/Normal_Experiments/merged_exp_normal.csv")
G = data[['X1','X2','X3','X4','X5','X6','X7','X8']]
mu = np.mean(G)
sigma = np.std(G)
print(mu)
print(sigma)
y_sig1 = np.exp(-(G['X1'] - mu[0]) ** 2 /(2* sigma[0]**2 ))/(math.sqrt(2*math.pi)*sigma[0])
y_sig2 = np.exp(-(G['X2'] - mu[1]) ** 2 /(2* sigma[1]**2 ))/(math.sqrt(2*math.pi)*sigma[1])
y_sig3 = np.exp(-(G['X3'] - mu[2]) ** 2 /(2* sigma[2]**2 ))/(math.sqrt(2*math.pi)*sigma[2])
y_sig4 = np.exp(-(G['X4'] - mu[3]) ** 2 /(2* sigma[3]**2 ))/(math.sqrt(2*math.pi)*sigma[3])
y_sig5 = np.exp(-(G['X1'] - mu[4]) ** 2 /(2* sigma[4]**2 ))/(math.sqrt(2*math.pi)*sigma[4])
y_sig6 = np.exp(-(G['X1'] - mu[5]) ** 2 /(2* sigma[5]**2 ))/(math.sqrt(2*math.pi)*sigma[5])
y_sig7 = np.exp(-(G['X1'] - mu[6]) ** 2 /(2* sigma[6]**2 ))/(math.sqrt(2*math.pi)*sigma[6])
y_sig8 = np.exp(-(G['X1'] - mu[7]) ** 2 /(2* sigma[7]**2 ))/(math.sqrt(2*math.pi)*sigma[7])
y_sig = y_sig1*y_sig2*y_sig3*y_sig4*y_sig5*y_sig6*y_sig7*y_sig8
############################## most important 2 features from Q3############################
y_sig_best2 = y_sig3*y_sig4
###################### PCA #################################################################
pca = PCA(n_components=2)
data = pca.fit_transform(G)
sigma_pca = np.std(data)
mu_pca = np.mean(data)
y_sig_pca1 = np.exp(-(data[0] - mu_pca) ** 2 /(2* sigma_pca[0]**2 ))/(math.sqrt(2*math.pi)*sigma_pca[0])
y_sig_pca2 = np.exp(-(data[1] - mu_pca) ** 2 /(2* sigma_pca[1]**2 ))/(math.sqrt(2*math.pi)*sigma_pca[1])
y_sig_pca = y_sig_pca1*y_sig_pca2
################################################     Q5     ####################################################################################
""" Model the same normal process “merged exp normal.csv” using Gaussian distribution
with all requirements in Question 4. However, assume that the features are dependent"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, multivariate_normal

data = pd.read_csv("C:/Users/zhangx/Desktop/Datasets/Normal_Experiments/merged_exp_normal.csv")
G = data[['X1','X2','X3','X4','X5','X6','X7','X8']]

def estimateGaussian(data):
    mu = np.mean(data,axis=0)
    sigma = np.cov(data.T)
    return mu,sigma

def MultivariateGaussianDistribution(data,mu,sigma):
    p = multivariate_normal.pdf(data, mean=mu, cov=sigma)
    return p

mu,sigma = estimateGaussian(G)
MultiGaussian = MultivariateGaussianDistribution(G,mu,sigma)
####################### 2 best features ####################
G_2features = data[['X3','X4']]
mu1,sigma1 = estimateGaussian(G_2features)
MultiGaussian_2best = MultivariateGaussianDistribution(G_2features,mu1,sigma1)
###################### PCA #################################
pca = PCA(n_components=2)
data = pca.fit_transform(G)
mu_pca,sigma_pca = estimateGaussian(data)
MultiGaussian_pca = MultivariateGaussianDistribution(data,mu_pca,sigma_pca)
################################################     Q6     ####################################################################################


################################################     Q8     ####################################################################################
""" Apply one supervised learning approach for classifying the events to normal and anomalies"""
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.svm import OneClassSVM
from sklearn.metrics import accuracy_score

outliers_fraction = 0.01
df = pd.read_csv("C:/Users/zhangx/Desktop/Datasets/Experiments_with_Anomalies/merged_exp_contains_anomalies.csv")
# Take useful feature and standardize them
data = df[['X1','X2','X3','X4','X5','X6','X7','X8']]
min_max_scaler = preprocessing.StandardScaler()
np_scaled = min_max_scaler.fit_transform(data)
# reduce to 2 importants features
pca = PCA(n_components=2)
data = pca.fit_transform(data)
# train one class SVM 
model =  OneClassSVM(nu=0.95 * outliers_fraction) #nu=0.95 * outliers_fraction  + 0.05
data = pd.DataFrame(np_scaled)
model.fit(data)
# add the data to the main
df['principal_feature1'] = data[2]
df['principal_feature2'] = data[3]
df['anomaly'] = pd.Series(model.predict(data))
df['anomaly'] = df['anomaly'].map( {1: 0, -1: 1} )
print(df['anomaly'].value_counts())

fig, ax = plt.subplots(figsize=(10,10))
colors = {0:'blue', 1:'red'}
ax.scatter(df['principal_feature1'], df['principal_feature2'], c=df["anomaly"].apply(lambda x: colors[x]))
plt.show()
accuarcy = accuracy_score(df["Anomaly_Tag"],df["anomaly"])
print(accuarcy)

################################################     Q9     ####################################################################################
""" Apply any clustering based algorithm you learn in the class, i.e., (hard and soft clustering
with K-means, EM, ..., etc.) to decouple the anomaly data from the normal ones. Is there a direct
mapping to the true anomaly tags? discuss your findings"""
import pandas as pd
from matplotlib import pyplot as plt
from sklearn import preprocessing
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

outliers_fraction = 0.01

def getDistanceByPoint(data, model):
    distance = pd.Series()
    for i in range(0,len(data)):
        Xa = np.array(data.loc[i])
        Xb = model.cluster_centers_[model.labels_[i]-1]
        distance.set_value(i, np.linalg.norm(Xa-Xb))
    return distance

df = pd.read_csv("C:/Users/zhangx/Desktop/Datasets/Experiments_with_Anomalies/merged_exp_contains_anomalies.csv")
# Take useful feature and standardize them
data = df[['X1','X2','X3','X4','X5','X6','X7','X8']]
min_max_scaler = preprocessing.StandardScaler()
np_scaled = min_max_scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)
# reduce to 2 importants features
pca = PCA(n_components=2)
data = pca.fit_transform(data)
# standardize these 2 new features
min_max_scaler = preprocessing.StandardScaler()
np_scaled = min_max_scaler.fit_transform(data)
data = pd.DataFrame(np_scaled)
# calculate with different number of centroids to see the loss plot (elbow method)
n_cluster = range(1, 10)
kmeans = [KMeans(n_clusters=i).fit(data) for i in n_cluster]
scores = [kmeans[i].score(data) for i in range(len(kmeans))]
fig, ax = plt.subplots()
ax.plot(n_cluster, scores)
plt.show()
df['cluster'] = kmeans[8].predict(data)
df['principal_feature1'] = data[2]
df['principal_feature2'] = data[3]
# get the distance between each point and its nearest centroid. The biggest distances are considered as anomaly
distance = getDistanceByPoint(data, kmeans[8])
number_of_outliers = int(outliers_fraction*len(distance))
threshold = distance.nlargest(number_of_outliers).min()
# anomaly21 contain the anomaly result of method 2.1 Cluster (0:normal, 1:anomaly) 
df['anomaly'] = (distance >= threshold).astype(int)
# visualisation of anomaly with cluster view
fig, ax = plt.subplots()
colors = {0:'blue', 1:'red'}
ax.scatter(df['principal_feature1'], df['principal_feature2'], c=df["anomaly"].apply(lambda x: colors[x]))
plt.show()
accuarcy = accuracy_score(df["Anomaly_Tag"],df["anomaly"])
print(accuarcy)