"""
p013：生成一天的所有小时
"""

import pandas as pd

date_range1 = pd.date_range(start='2021-10-1', end='2021-10-2', freq='H', closed='left')
date_range2 = pd.date_range(start='2021-10-1', periods=24, freq='H')

print(date_range1)
print(date_range2)