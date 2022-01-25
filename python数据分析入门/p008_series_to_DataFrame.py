"""
p008:使用pandas将Series变成dataframe
"""

import pandas as pd

grades = {"语文": 80, "数学": 85, "英语": 90, "计算机": 95, "体育": 100}
data = pd.Series(data=grades)

df = data.reset_index()
df.columns = ['course', 'grade']
print(df)