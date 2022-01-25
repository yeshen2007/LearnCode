"""
p011：生成一个月的所有天
"""
import pandas as pd

date_range1 = pd.date_range(start='2021-10-1', end='2021-10-31')
date_range2 = pd.date_range(start='2021-10-1', periods=20)
print(date_range1)
print(date_range2)