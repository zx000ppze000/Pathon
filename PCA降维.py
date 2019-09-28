# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 18:58:10 2019

@author: zhangx
"""
# 用户-产品分类
import pandas as pd
import sklearn.decomposition 
import PCA
# 读取数据
prior = pd.read_csv("/Users/zhangx/Desktop/instacart/order_products_prior.csv")
products = pd.read_csv("/Users/zhangx/Desktop/instacart/products.csv")
orders = pd.read_csv("/Users/zhangx/Desktop/instacart/orders.csv")
aisles = pd.read_csv("/Users/zhangx/Desktop/instacart/aisles.csv")
#合并4个表为一张表
_mg = pd.merge(prior,products,on['product_id','product_id'])
_mg = pd.merge(_mg,orders,on['order_id','order_id'])
mt = pd.merge(_mg,aisles,on['aisles_id','aisles_id'])
#查看
mt.head(10)#前10
# 交叉表
cross = pd.crosstab(mt['user_id'],mt['aisle'])
cross.head()
#降维 PCA
pca = PCA(n_components=0.9)
data = pca.fit.transform(cross)
data.shape