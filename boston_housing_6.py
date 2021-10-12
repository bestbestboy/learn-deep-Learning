# 访问已有的数据综合

# 数据集可视化
# 加载本地数据集
# 输出显示测试集数据数和训练集数据数
import tensorflow as tf
boston_housing = tf.keras.datasets.boston_housing
(train_x,train_y),(test_x,test_y) = boston_housing.load_data()
# print("Training set:",len(train_x))
# print("Testing set:",len(test_x))

# 改变数据集划分比例
(train_x,train_y),(test_x,test_y) = boston_housing.load_data(test_split=0)  #全改成训练集
# print("Training set:",len(train_x))
# print("Testing set:",len(test_x))

#访问数据集中的数据
type(train_x)
type(train_y)
print("Dim of train_x:",train_x.ndim)   #维数，秩
print("Shape of train_x:",train_x.shape)  #形状
print("Dim of train_y:",train_y.ndim)
print("Shape of train_y:",train_y.shape)

#访问前5行数据
print(train_x[0:5])
#输出第6列数据
print(train_x[:,5])
#输出train_y所有数据
print(train_y)


#数据集可视化
#房间数与房价的关系
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

boston_housing = tf.keras.datasets.boston_housing
(train_x,train_y),(_,_) = boston_housing.load_data(test_split=0)

#画图
plt.figure(figsize=(5,5))   
plt.scatter(train_x[:,5],train_y)
plt.xlabel("RM")
plt.ylabel("Price($1000's)")
plt.title("5. RM-Price")
plt.show()

