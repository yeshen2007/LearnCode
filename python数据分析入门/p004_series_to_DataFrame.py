"""
p004:使用pandas将Series变成dataframe,输出到命令行
"""

import pandas as pd

grades = {"语文": 80, "数学": 85, "英语": 90, "计算机": 95, "体育": 100}
data = pd.Series(data=grades)

# 将Series变成dataframe
df = pd.DataFrame(data, columns=["grade"])
print(df)