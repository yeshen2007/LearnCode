"""
p012：生成一年内的所有周一
"""
import pandas as pd

date_range1 = pd.date_range(start='2021-1-1', end='2021-12-31', freq='W-MON')
date_range2 = pd.date_range(start='2021-1-1', periods=52, freq='W-MON')

print(date_range1)
print(date_range2)