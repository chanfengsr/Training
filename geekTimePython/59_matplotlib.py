import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# import seaborn as sns

# #绘制简单的曲线
# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()

# # x轴的定义域为 -3.14~3.14，中间间隔100个元素
# x= np.linspace(-np.pi,np.pi,100)
# plt.plot(x,np.sin(x))
# plt.show()

# # 画多条线
# x = np.linspace(-np.pi * 2, np.pi * 2, 100)  # 定义域为： -2pi 到 2pi
# plt.figure(1, dpi=50)  # 创建图表1
# for i in range(1, 5):  # 画四条线
#         plt.plot(x, np.sin(x / i))
# plt.show()

# # 直方图
# plt.figure(1, dpi=50)  # 创建图表1，dpi代表图片精细度，dpi越大文件越大，杂志要300以上
# data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
# plt.hist(data)  # 只要传入数据，直方图就会统计数据出现的次数
# plt.show()

# 散点图
# x = np.arange(1,10)
# y = x
# fig = plt.figure()
# plt.scatter(x,y,c = 'r',marker = 'o')  #c = 'r'表示散点的颜色为红色，marker 表示指定三点多形状为圆形
# plt.show()