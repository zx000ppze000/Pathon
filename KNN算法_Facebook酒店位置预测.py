# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 17:17:20 2019

@author: zhangx
"""
# KNN算法: 欧式距离 -- sqrt((a1-b1)^2+(a2-b2)^2+(a3-b3)2）....
# 需要做标准化处理
"""
 # normalize data(标准化)    fit_transform(X)    sklearn.preprocessing import standerScaler
 # estimator 估计器, 代指某个算法： K_nearest, decision tree, logistic regression, etc
 # 1.调用 fit (x_train,y_train)
 # 2. 输入与测试集的数据  -- y_predict = predict(x_test); 预测的准确率：score(x_test,y_test)
 """
 # 数据集： facebook 定位酒店推荐
 # 特征值：x,y坐标，定位准确性，时间; 目标值：入住的id位置,（1.可以缩小x,y； 2.时间戳进行（年月日周时分秒...），可以做新的特征；3.几千~几万数据量太大，少于指定签到人数的位置删除）
 
 from sklearn.neighbors import kNeighborsClassifier
 from sklearn.model_selection import train_test_split
 from sklearn.preprocessing import StandardScaler
 def knncls():
     """
     K-近邻预测用户签到位置
     """
     # 读取数据
     data = pd.read_csv("/Users/zhangx/Desktop/FBlocation.csv")
     print(data.head(10))
     #处理数据
     # 1.缩小数据,查询数字筛选
     data = data.query("x > 1.0 & x < 1.25 & y > 2.5 & y < 2.75")
     # 处理时间数据
     time_value = pd.to_datatime(data['time'], unit = 's')
     print(time_value)
     # 把日期格式转换成 字典格式
     time_value = pd.DatatimeIndex(time_value)
     # 构造一些特征
     data['day'] = time_value.day
     data['hour'] = time_value.hour
     data['weekday'] = time_value.weekday
     # 时间戳特征删除
     data.drop(['time'],axis = 1) #axis = 1 是列在pandas里，在sklearn中列为 axis = 0
     data.drop(['Row_id'],axis = 1)
     print(data)
     # 把签到数量少于n个的位置目标删除
     place_count = data.groupby('place_id').count()
     tf = place_count[place_count.row_id>3].reset_index()
     data = data[data['place_id'].isin(tf.place_id)]
     #取出数据当中的特征值和目标值
     y = data['place_id']
     x = data.drop(['place_id'],axis=1)
     #进行数据分割
     x_train,y_train,x_test,y_test = train_test_split(x,y,test_size = 0.25)
     #特征工程（标准化）
     std = StandarScaler()
     #对测试集的特征值进行标准化
     x_train = std.fit_transform(x_train)
     x_test = std.transform(x_test)
     #惊喜算法流程
     knn = KNeighborsClassifier(n_neighbors=5)
     #fit 模型
     knn.fit(x_train,y_train)
     #得出预测结果
     y_predict = knn.predict(x_test)
     print("目标的预测签到位置"，y_predict)
     #得出准确率
     print("预测的准确率"，knn.score(x_test,y_test))
     
     
 if __name__ =="__main__":
     knncls()
     
     
"""
k值取很小：容易受异常点影响
k值取很大：容易受k值数量（类别）波动
优点：简单，无需训练（不是迭代提高准确率），无需估计参数
缺点：分类时计算量大，必须指定k值（k的选择不当则分类精度不能保证）
"""