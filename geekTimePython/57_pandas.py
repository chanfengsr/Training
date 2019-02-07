from pandas import Series, DataFrame
import pandas as pd
import numpy as np
from numpy import nan as NA

obj = Series([4, 5, 6, -7], index=['a', 'b', 'c', 'd'])
print(obj)

data = {'city': ['shanghai', 'shanghai', 'shanghai', 'beijing', 'beijing'],
        'year': [2016, 2017, 2018, 2017, 2018],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame2 = DataFrame(data, columns=['year', 'city', 'pop'])
print(frame2)
print(frame2.year)  # frame2['year']

frame2['cap'] = frame2.city == 'beijing'
print(frame2)

pop = {'beijing': {2008: 1.5, 2009: 2.0},
       'shanghai': {2008: 2.0, 2009: 3.6}
       }

frame3 = DataFrame(pop)
print(frame3)
print(frame3.T)  # 行列转置

data2 = DataFrame([[1., 6.5, 3], [1., NA, NA], [NA, NA, NA]])
data2[3] = NA
print(data2)
print(data2.dropna(axis=1, how='all'))  # 删除全空列
data2.fillna(0)
print(data2.fillna(0, inplace=True))  # data2 本身空值填充 0
print(data2)

data3 = Series(np.random.randn(10),
               index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                      [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
print(data3['b':'c'])
print(data3.unstack())  # 层次化索引
