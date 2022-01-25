"""
p006:转换series数据类型
"""
import pandas as pd

data = pd.Series(['001', '002', '003', '004'], index=list('abcd'))
print(data)

# 转换series数据类型string to int
data1 = data.astype(int)  #int是类型
print(data1)

data2 = data.map(int)   #int是函数
print(data2)


